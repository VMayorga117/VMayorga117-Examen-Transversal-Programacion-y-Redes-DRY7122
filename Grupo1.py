from ncclient import manager

conn = manager.connect(
    host="192.168.56.103",
    port=830,
    username="cisco",
    password="cisco",
    hostkey_verify=False
)
print(conn.connected)
