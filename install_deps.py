#!/usr/bin/python
import sys
import subprocess
from security import safe_command

if sys.version_info[:2] < (2, 7):
    safe_command.run(subprocess.call, 'pip install unittest2 --use-mirrors', shell=True)
