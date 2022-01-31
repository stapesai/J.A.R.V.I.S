def Append_Keywords():
    # Importing necessary files...
    import Reply_Bot
    bot_msg = Reply_Bot.bot_msg
    bot_user_input = Reply_Bot.bot_user_input
    
    if bot_msg==['No Such Keyword found in directory']:
        # If the keyword is not found in directory then appending keyword in bot_data.csv
        # By r+ mode in temp file....
        bot_data_open2 = open('bot_new_keywords_data.txt','a')
        new_keyword = str(bot_user_input.lower())
        print('New Keyword is : ',new_keyword)
        # Removing Emoji
        # new_keyword_unicode = new_keyword.encode('ascii','ignore')
        import re
        emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
        new_keyword_unicode = emoji_pattern.sub(r'', new_keyword)
        print('Keyword after removing emoji : ', new_keyword_unicode)
        bot_data_open2.write(new_keyword_unicode+'\n')
        print('Message appended : ', new_keyword)
        bot_data_open2.close()
    return 'Keywords are appended'