def WoL(mac,ip,port_input = 8080, interface_input = None):
    from wakeonlan import send_magic_packet as wol
    wol(mac, ip_address=str(ip), port=port_input, interface=interface_input)
    print("WoL sent to " + str(mac) + " at " + str(ip))
    return

# WoL(mac='b4:60:77:03:1a:66',ip='192.168.1.16')      # tv