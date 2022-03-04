def send_msg(phone_no: str, message: str):
    try:
        import webbrowser
        webbrowser.open("https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + message)
        from time import sleep
        sleep(8)
        from pyautogui import click, hotkey, position, press
        WIDTH, HEIGHT = position()
        click(x=WIDTH / 2, y=HEIGHT / 2)
        sleep(1)
        press("enter")
        sleep(3)
        hotkey("ctrl", "w")
        
        # appending to database
        try:
            with open('logs\WhatsappMsg_DB.txt', 'a') as data:
                import datetime
                data.write('Time Stamp :  ' + str(datetime.datetime.now()) + '\n')
                data.write('Phone Number: ' + phone_no + '\n')
                data.write('Message: ' + message + '\n')
                data.write('--------------------------------' + '\n')
        except Exception as e:
            print('Error Appending to database with error : ',e)
        
        return True
    except Exception as e:
        print(e)
        return False