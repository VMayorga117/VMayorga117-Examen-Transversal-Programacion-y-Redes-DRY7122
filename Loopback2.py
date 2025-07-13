from ncclient import manager

loopback_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>2</name>
        <ip>
          <address>
            <primary>
              <address>2.2.2.2</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

with manager.connect(
    host="192.168.56.103",
    port=830,
    username="cisco",
    password="cisco",
    hostkey_verify=False
) as m:
    m.edit_config(target='running', config=loopback_config)
