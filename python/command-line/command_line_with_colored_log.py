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


# paths
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)

# Custom log levels.
logging.TRACE = 5
logging.SUCCESS = 60
logging.NONE = 100
LOG_LEVELS = {'success': logging.SUCCESS, 'crit': logging.CRITICAL, 'error': logging.ERROR, 'warn': logging.WARNING, 'info': logging.INFO, 'debug': logging.DEBUG, 'trace': logging.TRACE, 'none': logging.NONE, 'all': logging.TRACE}


def get_logger(log_level=logging.NONE, colored=True):
    """Logger settings."""

    # add custom levels
    def add_log_level(name: str):
        level = getattr(logging, name.upper())
        logging.addLevelName(level, name.upper())
        def f(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws) 
        setattr(logging.getLoggerClass(), name.lower(), f)

    add_log_level('TRACE')
    add_log_level('SUCCESS')

    class ColoredFormatter(logging.Formatter):
        def __init__(self, fmt, colored):
            super().__init__()

            # ANSI ECMA-48 color codes (semicolon-separated):
            # bold=1, half-bright=2, underscore=4, doubly-underlined=21, normal-intensity=22
            # foreground:30+color, background:40+color
            # colors: black=0, red=1, green=2, brown=3, blue=4, magenta=5, cyan=6, white=7
            no_change = lambda s: s
            red = lambda s: f'\x1b[31m{s}\x1b[0m'
            bold_red = lambda s: f'\x1b[1;31m{s}\x1b[0m'
            bold_green = lambda s: f'\x1b[1;32m{s}\x1b[0m'
            yellow = lambda s: f'\x1b[33m{s}\x1b[0m'
            gray = lambda s: f'\x1b[2;37m{s}\x1b[0m'
            cyan = lambda s: f'\x1b[36m{s}\x1b[0m'

            self.fmt = fmt
            colors = {logging.TRACE: cyan, logging.DEBUG: gray, logging.INFO: no_change, logging.WARNING: yellow, logging.ERROR: red, logging.CRITICAL: bold_red, logging.SUCCESS: bold_green}
            self.formats = {k: v(fmt) for k, v in colors.items()} if colored else {}

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
    parser.add_argument('--log-level', choices=LOG_LEVELS.keys(), default='info', help='log level')
    parser.add_argument('--no-color', action='store_true', help='disables log coloring')
    return parser


def main(args):
    """Entry point of the program. """

    # get logger
    logger = get_logger(LOG_LEVELS[args.log_level], not args.no_color)

    # main logic
    logger.trace('trace log')
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')
    logger.success('success log')


if __name__ == '__main__':
    main(get_parser().parse_args())
