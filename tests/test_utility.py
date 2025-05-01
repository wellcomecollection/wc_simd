from wc_simd.utility import spark_path


def test_relative_path_to_spark_path():
    """This test only works on MacOS and Linux"""
    p = spark_path("../data/imports")
    print(p)
    assert p.startswith("file:///")
