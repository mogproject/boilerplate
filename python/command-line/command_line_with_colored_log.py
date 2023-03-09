#!/usr/bin/env python3
"""
Program description.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

# imports standard libraries
import sys
import os
import logging
import argparse

# imports extrenal libraries
try:
    pass
except ImportError:
    sys.stderr.writelines([
        'Failed to load modules.',
    ])
    sys.exit(1)


LOG_LEVELS = {'none': 51, 'crit': 50, 'error': 40, 'warn': 30, 'info': 20, 'debug': 10}

# paths
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)


def get_logger(log_level=logging.CRITICAL + 1, colored=True):
    """Logger settings."""

    class ColoredFormatter(logging.Formatter):
        # ANSI ECMA-48 color codes (semicolon-separated):
        # bold=1, half-bright=2, underscore=4, doubly-underlined=21, normal-intensity=22
        # foreground:30+color, background:40+color
        # colors: black=0, red=1, green=2, brown=3, blue=4, magenta=5, cyan=6, white=7
        reset = "\x1b[0m"
        red = '\x1b[31m'
        bold_red = '\x1b[1;31m'
        yellow = '\x1b[33m'
        gray = '\x1b[2;37m'

        def __init__(self, fmt, colored):
            super().__init__()
            self.fmt = fmt
            self.formats = {
                logging.DEBUG: self.gray + fmt + self.reset,
                logging.INFO: fmt,
                logging.WARNING: self.yellow + fmt + self.reset,
                logging.ERROR: self.red + fmt + self.reset,
                logging.CRITICAL: self.bold_red + fmt + self.reset,
            } if colored else {}

        def format(self, record):
            fmt = self.formats.get(record.levelno, self.fmt)
            formatter = logging.Formatter(fmt)
            return formatter.format(record)

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(ColoredFormatter('%(asctime)s [%(levelname)-8s] %(message)s', colored))

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


def get_parser():
    """Argument parser."""

    parser = argparse.ArgumentParser(description='program description')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('--log-level', choices=['crit', 'error', 'warn', 'info', 'debug', 'none'], default='info', help='log level')
    parser.add_argument('--no-color', action='store_true', help='disables log coloring')
    return parser


def main(args):
    """Entry point of the program. """

    # get logger
    logger = get_logger(LOG_LEVELS[args.log_level], not args.no_color)

    # main logic


if __name__ == '__main__':
    main(get_parser().parse_args())
