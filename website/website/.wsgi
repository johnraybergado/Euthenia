#!/usr/bin/python3
import sys, os
import logging
logging.basicConfig(stream=sys.stderr)

PROJECT_DIR = '/var/www/Euthenia/website'

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
with open(activate_this) as f:
	code = compile(f.read(), activate_this, 'exec')
	exec(code)
sys.path.append(PROJECT_DIR)

from website import app as application