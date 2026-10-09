#!/bin/bash
set -e

root=$(cd "$(dirname "$0")/.." && pwd)
python3 "${root}/build.py"
