#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0
"""Script which reads multiple huge files.
"""

import argparse
import multiprocessing


def stress(i):
    with open(f"file-{i}", "rb") as f:
        f.read()
    return


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-n", type=int, default=4,
                        help="number of files")
    args = parser.parse_args()

    pool = multiprocessing.Pool()
    pool.map(stress, range(args.n))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
