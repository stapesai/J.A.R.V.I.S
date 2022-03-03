def extract_msg(text):
    out = {'name': '', 'msg': ''}
    out = text.replace('send msg to', '')
    return out


print(extract_msg('send message to ayush bansal that i am fine'))