# -*- coding: utf-8 -*-
"""
    clementina
    ~~~~~~~~~~~~~~~~

    Clementina takes Clementine databases and performs various metadata retrieval operations

    This script requires that `sqlalchemy` and `python-magic` installed within the Python
    environment you are running this script in.

    :copyright: © 2018 by the etakdc.
    :license: BSD, see LICENSE for more details.
"""

import argparse
import sys
from normalize import normalize, bulk_normalize


def main():

    """
        Option menu for the user. Only its executed if is this module is executed as main file.

        Available Options:
        --gcstar:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--normalize',
                        nargs=2,
                        metavar=(
                            'clementine_db',
                            'output_file'
                        ),
                        help='Normalizes a clementine database',
                        )
    parser.add_argument('-b',
                        '--bulk',
                        nargs=2,
                        metavar=(
                            'root_dir',
                            'output_dir'
                        ),
                        help='Bulk normalizes clementine databases',
                        )

    if len(sys.argv) > 1:
        options = parser.parse_args()
        user_options(options)

    else:
        parser.print_help()
        sys.exit(0)


def user_options(options):
    """
    Handles the diverse user options given as argument in the script

    :param options: ArgumentParser Object
    :return:
    """
    if options.normalize is not None:
        normalize_db(options.normalize[0], options.normalize[1])
    elif options.bulk is not None:
        bulk_normalize_db(options.bulk[0], options.bulk[1])


def normalize_db(db_path, out_path):
    normalize(db_path, out_path)


def bulk_normalize_db(root_path, out_path):
    bulk_normalize(root_path, out_path)


if __name__ == '__main__':
    main()
