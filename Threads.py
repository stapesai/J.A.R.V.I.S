import threading

def Whatsapp():
    import features.whatsapp.main as test
    test.hello('hello')


Whatsapp_thread = threading.Thread(target=Whatsapp, args=())
Whatsapp_thread.start()
Whatsapp_thread.join()