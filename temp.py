def check_for_new_call():
    import sys
    sys.path.append('features//whatsapp')
    import features.whatsapp.main_call as call
    if call.check_incoming_call() == True:
        print('Sir There is a new call')

check_for_new_call()
