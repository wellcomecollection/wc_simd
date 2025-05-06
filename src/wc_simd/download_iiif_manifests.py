import requests
import os
from tqdm import tqdm
import pyspark.sql.functions as F
from pyspark.sql import SparkSession


def download_iiif_manifests(
        subset_fraction: float = 0.01, download_dir: str = "."):
    """
    This script is used to extract IIIF manifest URLs from the works table in the database.
    It uses PySpark to process the data and saves the manifests to a specified directory.
    """

    # Create a Spark session
    spark = SparkSession.builder \
        .appName("test_pyspark") \
        .config("spark.driver.memory", "12g") \
        .config("spark.executor.memory", "12g") \
        .config("spark.sql.orc.enableVectorizedReader", "false") \
        .config("spark.sql.parquet.columnarReaderBatchSize", "1024") \
        .config("spark.sql.orc.columnarReaderBatchSize", "1024") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    df_works_item_urls = (
        spark.table("works")
        # 1) explode each item so we have work‐level id + item struct
        .select(
            F.col("id"),
            F.explode(F.col("items")).alias("item")
        )
        # 2) from each item, explode only the locations whose URL matches
        .select(
            F.col("id"),
            F.col("item.id").alias("item_id"),
            F.explode(
                F.expr("filter(item.locations, l -> l.url LIKE '%/presentation/%')")
            ).alias("location")
        )
        # 3) pick out just the fields you want
        .select(
            F.col("id"),
            F.col("item_id"),
            F.col("location.url").alias("url")
        )
    )

    df_works_item_urls_subset = df_works_item_urls.sample(
        withReplacement=False,
        fraction=subset_fraction,
        seed=42
    )

    # Ensure download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Replace conversion to Pandas with Spark local iterator and tqdm
    total = df_works_item_urls_subset.count()
    row_iter = df_works_item_urls_subset.toLocalIterator()
    for row in tqdm(row_iter, total=total, desc="Downloading manifests"):
        url = row['url']
        last_part = url.rstrip('/').rsplit('/', 1)[-1]
        filename = f"{row['id']}_{last_part}.json"
        full_path = os.path.join(download_dir, filename)

        # Skip if file already exists
        if os.path.exists(full_path):
            continue

        # Try downloading up to 3 times
        success = False
        for attempt in range(3):
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                with open(full_path, "w") as f:
                    f.write(resp.text)
                success = True
                break
            except Exception:
                if attempt < 2:  # Don't sleep after the last attempt
                    import time
                    time.sleep(1)  # Wait a bit before retrying

        # If all attempts failed, create an empty JSON file
        if not success:
            with open(full_path, "w") as f:
                f.write("{}")


if __name__ == "__main__":
    import argparse
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Download IIIF manifests.")
    parser.add_argument(
        "--subset_fraction", type=float, default=0.01,
        help="Fraction of rows to sample from the works table.")
    parser.add_argument("--download_dir", type=str, default=".",
                        help="Directory to download manifests.")
    args = parser.parse_args()
    download_iiif_manifests(
        subset_fraction=args.subset_fraction,
        download_dir=args.download_dir)
