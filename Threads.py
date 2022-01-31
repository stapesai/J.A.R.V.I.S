from cProfile import run
from  threading import Thread
class Whatsapp(Thread):
    def Whatsapp():
        import features.whatsapp.main as whatsapp_main
        whatsapp_main.Whatsapp_Automate()
while True:
    Whatsapp_thread = Whatsapp()
    Whatsapp_thread.start()