import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://192.168.56.103/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback1",
        "type": "iana-if-type:softwareLoopback",
        "enabled": False,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "1.1.1.1",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

response = requests.put(
    url,
    headers=headers,
    auth=HTTPBasicAuth("cisco", "cisco"),
    json=payload,
    verify=False
)

print("Código de respuesta:", response.status_code)
print("Respuesta:", response.text)
