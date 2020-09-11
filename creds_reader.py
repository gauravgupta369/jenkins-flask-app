# from creds import HOST_IP

import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('BACKEND_AUTH_USR'))