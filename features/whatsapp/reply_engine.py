def Reply_Engine(msg_input, file, centiment='happy'):

    # CSV Synthesize...
    import csv
    bot_data_open = open(file)
    bot_data_reader = csv.reader(bot_data_open)
    list_bot_data = list(bot_data_reader)

    # Main Code...
    # print('--'*50)
    print('User said : ',msg_input)

    # reply if could not understand the user input
    if msg_input == 'Seems like you are not speaking or i can not understand you':
        return 'Seems like you are not speaking or i can not understand you'

    # bot_msg=['No Such Keyword found in directory']

    for data in list_bot_data:

        # keywords
        all_keyword = data[0]           # data = ["['break','end','Bye','GoodBye']", "['Good Bye Sir have a nice day']"]
        # Converting str all_keywords to list all_keywords
        import ast
        lst_bot_keyword = ast.literal_eval(all_keyword)
        # print('All Keywords are',lst_bot_keyword)

        # replies
        all_reply = data[1]
        # Converting str all_replies to list all_replies
        import ast
        lst_bot_reply = ast.literal_eval(all_reply)
        # print('All Replies are',lst_bot_reply)

        # Checking if msg_input is in lst_all_keywords
        for temp_keyword in lst_bot_keyword:
            # print('temp keyword is : ',temp_keyword.lower())

            # user msg is split into words
            try:
                lst_user_msg = msg_input.split()
            except:
                lst_user_msg = ['hello']
            
            for msg in lst_user_msg:
                if temp_keyword.lower() == msg.lower():
                    import emoji
                    # print('Match found')
                    # Randomly selecting a reply from all_replies
                    import random
                    bot_msg = random.choice(lst_bot_reply)
                    # print('Bot_reply is : ',emoji.emojize(bot_msg, use_aliases=True))
                    return emoji.emojize(bot_msg, use_aliases=True)

    # If no match found
    bot_msg = 'No Such Keyword found in directory'
    # print('Bot_reply is : ',bot_msg)
    return bot_msg