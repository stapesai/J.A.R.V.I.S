def Randomised_Bot_Reply():
    import Reply_Bot
    print('Reply Came To randomise : ',Reply_Bot.Bot_Reply())

    # Randomising Bot Reply
    import ast
    import random
    str_bot_msg = str(Reply_Bot.bot_msg)
    list_bot_msg = ast.literal_eval(str_bot_msg)
    print('List in bot reply to use : ',list_bot_msg)
    random_reply = random.choice(list_bot_msg)
    print('Random reply choosed : ',random_reply)
    return random_reply
    
#Randomised_Bot_Reply()