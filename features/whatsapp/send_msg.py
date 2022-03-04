def send_msg(phone_no: str, message: str, file_name: str = 'WhatsappMsg_DB.log'):
    try:
        import webbrowser
        webbrowser.open("https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + message)
        from time import sleep
        sleep(6)
        from pyautogui import click, hotkey, press
        click(x=1113, y=1029)
        sleep(1)
        press("enter")
        sleep(3)
        hotkey("ctrl", "w")
        
        # appending to database
        try:
            with open(file_name, 'a') as data:
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