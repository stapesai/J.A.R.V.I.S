def Bot_Reply():
    import Copy_Msg
    global bot_msg
    bot_input=Copy_Msg.message
    print('Bot Input is : ',bot_input)
    if "?"in str(bot_input).lower():
        bot_msg =  "Interesting question, I'll talk to you about that later - Jarvis"
    elif "hi"in str(bot_input).lower():
        bot_msg =  "Hey, a bit busy right now. just drop a bot_input ill talk to you later- Jarvis"
    elif "republic day"in str(bot_input).lower():
        bot_msg =  "Wishing you and your family a very Happy New Year! ✨.May this year bring joy and happiness in your life! - Jarvis "
    elif "good morning"in str(bot_input).lower():
        bot_msg = "Good Morning! Have a great day"
    elif "good night"in str(bot_input).lower():
        bot_msg = "Good Night! Sleep tight"
    else:
        bot_msg =  "Hello! Dear Sir/Madam, Devasheesh is currently unavailable to reply. Do drop your message. - Jarvis"
