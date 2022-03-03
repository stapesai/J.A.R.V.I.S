import features.whatsapp.main_call as call
import multiprocessing as mp
import datetime

# reply function
def reply(text): 

    if 'jarvis' == text:
        return('Yes sir')

    elif 'hello how are you' in text:
        return('hello sir, I am fine.')
    
    elif 'what is your name' in text:
        return('My name is Jarvis')
    
    elif 'what are you doing' in text:
        return('I am waiting for your command sir')
    
    elif 'what time is it' in text:
        return('Current time is {}'.format(datetime.datetime.now().strftime("%H:%M:%S")))

    elif 'hello' in text:
        return('Hello sir')

    elif 'how are you' in text:
        return('I am fine sir')

    elif 'your name' in text:
        return('My name is jarvis')

    elif 'your age' in text:
        return('My software is still in development mode')

    elif 'your job' in text or 'your profession' in text or 'what do you do' in text or 'who are you' in text:
        return('I am a virtual assistant')

    elif 'your favourite colour' in text:
        return('My favourite colour is blue')

    elif 'your favourite song' in text:
        return('My favourite song is Iron Man Songs')

    elif 'could not understand what you said' in text:
        return('Could not understand what you said')
    
    # Features
    # 1. attending to calls
    elif 'attend my call' in text or 'respond to my call' in text or 'is there any call' in text or 'is there any new call' in text or 'respond to call' in text or 'respond to incoming call' in text or 'respond to my call' in text:

        if call.check_incoming_call() == True:
            calling_process = mp.Process(target=call.__main__)

            if calling_process.is_alive() == False:
                calling_process.start()
                return('ok sir, now i am taking your call')
            
            elif calling_process.is_alive() == True:
                return('sir, i am already talking to your call')
        
        else:
            return('no sir, there is no new call')

    # 2. send whatsapp message
    elif 'send whatsapp message' in text or 'send message' in text or 'inform' in text:
        import tools.pywhatkit as pywhatkit

        '''
        Type:
             jarvis send a message to ayush bansal that i am fine
             jarvis inform ayush bansal that i am fine           
             jarvis inform kshitij that i am fine
             jarvis 
        '''

        def extract_msg(text):
           # out = {'number': '', 'message': ''}
            out=text.replace('jarvis send a msg to','')
            out=text.replace('jarvis inform','')
            out=text.replace('jarvis tell','')
            extracted_data=out.split('that','')
            global msg
            global R_name
            msg=extracted_data[1]
            R_name=extracted_data[0].lower()
            #finding name in csv file
            # CSV Synthesize...

            import csv

            contacts_data_open = open('contacts_data.csv','r')
            contacts_data = csv.reader(contacts_data_open)
            list_contacts_data = list(contacts_data)

            for temp in list_contacts_data:
                
                import ast
                names = ast.literal_eval(temp[0])
                global num
                num=temp[1]
                for temp2 in names:
                    if R_name == temp2:
                        print('found')
                        print(num)
                    else:
                        print('not found')

           

            
            # code to extract number and message from text
            # NOTE : out is dict and it contains number and message as key and value are to be appended in the out dict. find number using csv or json.

            return extracted_data
        
        out = extract_msg(text)
        crt_hr = datetime.datetime.now().strftime("%H")
        crt_min = datetime.datetime.now().strftime("%M")

        pywhatkit.sendwhatmsg(  phone_no = num, 
                                message = out['message'], 
                                time_hour = crt_hr, 
                                time_min = crt_min+1, 
                                tab_close=True
                                )
        
        return('sir, now i have sent your message')

    else:
        return('This is not programmed yet.')