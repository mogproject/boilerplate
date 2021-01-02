#!/bin/bash

RM=/bin/rm
TIMEOUT=gtimeout

SCRIPT_DIR=$( cd "$( dirname "$0" )" && pwd -P )
PROJECT_ROOT=$( dirname "${SCRIPT_DIR}" )

echo "$PROJECT_ROOT"

