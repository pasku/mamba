# -*- coding: utf-8 -*-

import sys
import argparse

from mamba import application_factory


def main():
    arguments = _parse_arguments()
    factory = application_factory.ApplicationFactory(arguments)
    runner = factory.create_runner()

    runner.run()

    if runner.has_failed_examples:
        sys.exit(1)


def _parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--slow', '-s', default=0.075, type=float, help='slow test threshold in seconds (default: %(default)s)')
    parser.add_argument('--enable-coverage', default=False, action='store_true', help='enable code coverage measurement (default: %(default)s)')
    parser.add_argument('--watch', '-w', default=False, action='store_true', help='enable file watching support (default: %(default)s)')
    parser.add_argument('specs', default=['spec'], nargs='*', help='specs or directories with specs to run (default: %(default)s)')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
