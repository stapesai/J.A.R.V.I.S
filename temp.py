def extract_msg(text : str):
        output = {'number': '', 'message': ''}
        if 'send a message to' in text:
            print('send a message to')
            text.replace('send','fsgsdgsdf')

        text.replace('inform','')
        
        extracted_data=text.split('that')
        print('data is',extracted_data)

        R_name=extracted_data[0].lower()
        msg = extracted_data[1]
        output.update({'message': str(msg)})
        # finding name in contact list
        import csv
        contacts_data_open = open('contacts_data.csv','r')
        contacts_data = csv.reader(contacts_data_open)
        list_contacts_data = list(contacts_data)
        for temp in list_contacts_data:
            print('loop1')
            import ast
            names = ast.literal_eval(temp[0])
            num=temp[1]
            for temp2 in names:
                print('loop2')
                print(R_name)
                if R_name == temp2:
                    print('loop3')
                    output.update({'number': '+91' + str(num)})
                    contacts_data_open.close()
                    return output
                else:
                    print('loop4')
        print(output)

extract_msg('send a message to ayush bansal that i am fine')