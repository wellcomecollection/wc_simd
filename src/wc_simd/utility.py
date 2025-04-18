import os


def spark_path(relative_path: str):
    # Compute the absolute path of your file
    absolute_path = os.path.abspath(relative_path)

    # Prepend with the "file://" scheme
    # Note: use three slashes (file:///)
    local_path = "file://" + absolute_path

    return local_path
