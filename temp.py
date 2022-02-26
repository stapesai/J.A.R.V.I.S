def check_for_new_call():
    import sys
    sys.path.append('features//whatsapp')
    from features.whatsapp.main_call import check_incoming_call
    if check_incoming_call() == True:
        print('Sir There is a new call')

check_for_new_call()