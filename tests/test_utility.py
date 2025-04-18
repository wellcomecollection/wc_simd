from wc_simd.utility import spark_path


def test_relative_path_to_spark_path():
    """This test only works on MacOS and Linux"""
    spark_path = spark_path("../data/imports")
    print(spark_path)
    assert spark_path.startswith("file:///")
