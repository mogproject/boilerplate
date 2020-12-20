#!/usr/bin/env python3
"""
Create a project from a template.
"""

__author__ = 'Yosuke Mizutani'
__version__ = '0.0.1'
__license__ = 'Apache License, Version 2.0'

# imports standard libraries
import argparse
import yaml
import pathlib
import os
import shutil
from jinja2 import Environment, FileSystemLoader


def get_parser():
    """Argument parser."""

    parser = argparse.ArgumentParser(description='Create a project from a template.')
    parser.add_argument('--log-level', choices=['crit', 'error', 'warn', 'info', 'debug', 'none'], default='info', help='log level')
    parser.add_argument('-t', '--template', required=True, help='template name', metavar='TEMPLATE_NAME')
    parser.add_argument('-c', '--config', required=True, help='path to the configuration file', metavar='CONFIG_PATH')
    parser.add_argument('target', help='target directory', metavar='TARGET_DIRECTORY')
    return parser


def main(args):
    """Entry point of the program. """

    # Load config
    conf = yaml.safe_load(open(args.config))

    # Check template
    template_dir = pathlib.Path(args.template)
    assert template_dir.is_dir()
    env = Environment(loader=FileSystemLoader(str(template_dir)), trim_blocks=True, lstrip_blocks=True)

    # Create target directory
    target_dir = pathlib.Path(args.target)
    if not target_dir.exists():
        print(f'Creating: {target_dir}/')
        target_dir.mkdir(parents=True, exist_ok=True)

    # Copy files
    for root, dirs, files in os.walk(template_dir, topdown=True):
        for dir in dirs:
            p = target_dir.joinpath(dir)
            if not p.exists():
                # create directory
                print(f'Creating: {p}/')
                p.mkdir(parents=False, exist_ok=True)
        for file in files:
            p = target_dir.joinpath(file)

            if file.endswith('.j2'):
                # convert jinja2 template
                p = p.with_suffix('')
                print(f'Generating: {file} -> {p}')
                with open(p, 'w') as f:
                    f.write(env.get_template(file).render(conf))
            else:
                # copy file
                print(f'Copying: {file} -> {p}')
                shutil.copyfile(file, p)


if __name__ == '__main__':
    main(get_parser().parse_args())
