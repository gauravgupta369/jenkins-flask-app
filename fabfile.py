from fabric import Connection
import os

from dotenv import load_dotenv
load_dotenv()


ip = os.getenv("ip")
port = os.getenv("port")
username  = os.getenv("BACKEND_AUTH_USR")
password = os.getenv("BACKEND_AUTH_PSW")

conn = Connection(
    "{username}@{ip}:{port}".format(
        username=username,
        ip=ip,
        port=port,
    ),
    connect_kwargs={"password": password},
)

conn.open()
print(conn.is_connected)

with conn.cd("/var/www/html"):
    conn.run("ls -a")


conn.close()