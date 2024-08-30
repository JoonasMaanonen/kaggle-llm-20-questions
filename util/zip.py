import tarfile


def extract_tar_gz(file_path: str, extract_path: str) -> None:
    """Open a .tar.gz file and extract it to a given path."""
    with tarfile.open(file_path, "r") as tar:
        tar.extractall(path=extract_path)
