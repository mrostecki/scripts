#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0
"""Script which creates multiple files with random data.
"""

import argparse
import multiprocessing
import os


def write_random(i, size):
    size_cur = 0
    with open(f"file-{i}", "wb") as f:
        while size_cur < size:
            size_cur += f.write(os.urandom(64 * 1024))  # 64KB chunks


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-n", type=int, default=4,
                        help="number of files")
    parser.add_argument("-s", type=int, default=1024,
                        help="size (MB)")
    args = parser.parse_args()

    size = args.s * 1024 * 1024

    pool = multiprocessing.Pool()
    seq = [(i, size) for i in range(args.n)]
    pool.starmap(write_random, seq)
    pool.close()
    pool.join()

    os.sync()


if __name__ == "__main__":
    main()
