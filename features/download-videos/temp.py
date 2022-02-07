def check_client():
    import sys
    sys.path.insert(0, 'V:\\J.A.R.V.I.S\\features')
    import command_remotly.command_server as command_server
    command_server.check_connection_to_client()

check_client()