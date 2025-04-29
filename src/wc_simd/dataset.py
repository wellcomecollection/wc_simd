import requests
import os
from tqdm import tqdm


def download_file(url, dest_folder="."):
    """Download a file from a URL into a destination folder with a progress bar."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    local_filename = os.path.join(dest_folder, url.split('/')[-1])

    # Stream download to handle large files
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        # Setup progress bar
        with tqdm(
            total=total_size, unit='iB', unit_scale=True, desc=os.path.basename(local_filename)
        ) as bar, open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))

    print(f"Downloaded: {local_filename}")
    return local_filename


def main():
    urls = [
        "https://data.wellcomecollection.org/catalogue/v2/works.json.gz",
        "https://data.wellcomecollection.org/catalogue/v2/images.json.gz",
        "https://developers.wellcomecollection.org/redocusaurus/plugin-redoc-0.yaml"]

    dest_folder = "./data/imports"
    for url in urls:
        download_file(url, dest_folder)


if __name__ == "__main__":
    main()
