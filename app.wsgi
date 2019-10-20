activate_this = '/home/rodrigueskevin2/HackHarvard2019/venv/bin/activate_this.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/HackHarvard2019/")

from HTMLTextAPI import app as application

