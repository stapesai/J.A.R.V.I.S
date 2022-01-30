def Randomised_Bot_Reply(input):
    import Reply_Bot
    print('Reply Came To randomise : ',Reply_Bot.Bot_Reply())

    # Randomising Bot Reply
    import ast
    import random
    str_bot_reply = str(input)
    list_bot_reply = ast.literal_eval(str_bot_reply)
    print('List in bot reply to use : ',list_bot_reply)
    random_reply = random.choice(list_bot_reply)
    print('Random reply choosed : ',random_reply)
    return random_reply
    
#Randomised_Bot_Voice_Reply()