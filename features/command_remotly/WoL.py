def WoL(mac,ip,port_input = 8080, interface_input = None):
    from wakeonlan import send_magic_packet as wol
    wol(mac, ip_address=str(ip), port=port_input, interface=interface_input)
    print("WoL sent to " + str(mac) + " at " + str(ip))
    return

if __name__ == "__main__":
    import time
    for i in range(50):
        WoL(mac='80:9f:9b:38:6c:7c',ip='192.168.1.16')      # tv
        time.sleep(2x)