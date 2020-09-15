from fabric import Connection
import os

import creds

conn = Connection(
    "{username}@{ip}:{port}".format(
        username=creds.USERNAME,
        ip=creds.IP,
        port=creds.PORT,
    ),
    connect_kwargs={"password": creds.PASSWORD},
)

conn.open()
print(conn.is_connected)

with conn.cd("/var/www/html"):
    conn.run("ls -a")


conn.close()