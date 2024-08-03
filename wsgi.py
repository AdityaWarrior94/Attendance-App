import sys
import os

# Add your project directory to the sys.path
project_home = '/home/AdiRajputBinary95/mysite'
if project_home not in sys.path:
    sys.path.append(project_home)

# Activate your virtual environment
activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import your Flask app
from app import app as application
