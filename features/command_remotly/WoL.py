def WoL(mac,ip,port_input = 8080, interface_input = None):
    from wakeonlan import send_magic_packet as wol
    wol(mac, ip_address=str(ip), port=port_input, interface=interface_input)

# for pc
WoL(mac='B4-2E-99-EE-B6-15',ip='192.168.1.2')

# for laptop
# WoL(mac='E8-6F-38-CE-46-DB',ip='192.168.1.51')      # wifi