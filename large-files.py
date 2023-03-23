# Example CLI for finding large files from a starting path
import os
import argparse
from operator import itemgetter


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", help="Filepath to use. e.g. /home/me/", type=str)
    parser.add_argument("--size_limit", "-s", default=20, type=int, nargs="?",
                        help="Minimum file size limit to apply in MB. e.g. 50. Default: 20")
    parser.add_argument("--file_suffix", default="", type=str, nargs='?',
                        help="Optional: specify file type. e.g. '.mp3'")
    args = parser.parse_args()
    return args


def size_MB(bytecount):
    size_in_MB = int(bytecount/1024**2)
    return size_in_MB


def path_walker(start_dir, size_limit, f_suffix):
    # Capture the data in a dictionary, paths as keys.
    # Only "save" large files, greater than 20MB by default (argparse setting)
    file_metadata = {}
    for root, directories, files in os.walk(start_dir):
        for _file in files:
            if _file.lower().endswith(f_suffix):
                full_path = os.path.join(root, _file)
                size_bytes = os.path.getsize(full_path)
                size = size_MB(size_bytes)
                if size >= size_limit:
                    file_metadata[full_path] = size
    return file_metadata


def main():
    args = get_args()
    start_dir = args.path
    size_limit = args.size_limit
    f_suffix = args.file_suffix
    file_metadata = path_walker(start_dir, size_limit, f_suffix)

    # Decide on how many to show (could add to args via argparse)
    items_shown = 0
    items2show = 20

    # Just because, use itemgetter instead of lambda
    for path, size in sorted(file_metadata.items(), key=itemgetter(1), reverse=True):
        if items_shown >= items2show:
            break
        print(f"Size: {size} MB\tPath: {path}")
        items_shown += 1


if __name__ == '__main__':
    main()
