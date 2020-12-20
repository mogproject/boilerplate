# boilerplate

Templates for various projects.

## Prerequisites

```
$ pip3 install jinja2
```

## Usage

```
usage: create.py [-h] [--log-level {crit,error,warn,info,debug,none}] -t TEMPLATE_NAME -c CONFIG_PATH TARGET_DIRECTORY

Create a project from a template.

positional arguments:
  TARGET_DIRECTORY      target directory

optional arguments:
  -h, --help            show this help message and exit
  --log-level {crit,error,warn,info,debug,none}
                        log level
  -t TEMPLATE_NAME, --template TEMPLATE_NAME
                        template name
  -c CONFIG_PATH, --config CONFIG_PATH
                        path to the configuration file
```

## Example

```
$ ./create.py -t python/command-line -c config/python/command-line.example.yml your_project_path
```
