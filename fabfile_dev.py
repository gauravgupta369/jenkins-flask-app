# import os

# from dotenv import load_dotenv
from fabric import Connection
from config import SERVERS

# load_dotenv()

# IP = os.getenv("ip")
# PORT = os.getenv("port")
# USER = os.getenv("BACKEND_AUTH_USR")
# PASS = os.getenv("BACKEND_AUTH_PSW")

# CONN = Connection(
#     "{username}@{ip}:{port}".format(
#         username=USER,
#         ip=IP,
#         port=PORT,
#     ),
#     connect_kwargs={"password": PASS},
# )

PEM_FILE = 'backend.pem'

DEV_SERVERS = SERVERS['dev']
for dev_server in DEV_SERVERS:
    CONN = Connection(inline_ssh_env=PEM_FILE, host=dev_server['host'], user=dev_server['user'], \
        connect_kwargs={"key_filename": PEM_FILE})

    CONN.open()

    print(CONN.is_connected)

    with CONN.cd("/var/www/html"):
        CONN.run("ls -a")

    CONN.close()
