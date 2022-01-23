def Bot_Reply():
    
    # Importing necessary files...
    import Copy_Msg

    # CSV Synthesize...
    import csv
    bot_data_open = open('bot_data_lst.csv')
    bot_data_reader = csv.reader(bot_data_open)
    list_bot_data = list(bot_data_reader)
    #print(list_bot_data)

    print('--'*50)
    global bot_user_input
    bot_user_input=Copy_Msg.message
    print('Bot Input is : ',bot_user_input)

    global bot_msg
    bot_msg=['No Such Keyword found in directory']

    print('Pointer is at 1st position')

    for data in list_bot_data:

        print('Pointer is in 1st for loop')
        #print(data)
        all_keyword = data[0]
        # Converting str all_keywords to list all_keywords
        import ast
        lst_bot_keyword = ast.literal_eval(all_keyword)
        print(type(lst_bot_keyword))
        print('All Keywords are',lst_bot_keyword)
        all_reply = data[1]
        bot_input = (bot_user_input.lower())
        for temp_keyword in lst_bot_keyword:
            print('temp keyword is : ',temp_keyword)

            for bot_keyword in temp_keyword.split():
                print('Comparing :',bot_keyword.lower(),'       with :',bot_user_input.lower())            
                # Bugs can be here...
                if bot_keyword.lower() in bot_input:
                    print('Comparing Successful.....')
                    #global bot_msg          # This statement is not working...
                    bot_msg=all_reply
                    print('Reply to User  is : ',bot_msg)
                    return bot_msg               
                else:
                    print('The Loop has jumped in else statement')      # Error: The Loop is jumping to else...
            #print('Bot msg on Pos-01 : ',bot_msg)
        #print('Pointer is at last position')

    bot_data_open.close()
    print('--'*50)
    
    return bot_msg
    
#Bot_Reply()