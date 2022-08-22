cookie_raw = (open('cookie.txt', 'r')).read()
import ast
cookie = ast.literal_eval(cookie_raw)

no_of_link_in_cookie = len(cookie)
# print('No of link in given cookie : ', no_of_link_in_cookie)


names = list(((open('names.txt', 'r')).read()).split('\n'))
# print('No of names in file : ',len(names))

import traceback
if no_of_link_in_cookie == len(names):
    try:
        # print('No of names and links are same')
        for i in range(no_of_link_in_cookie):
            url = cookie[i]['videoUrl'].replace('mpd', 'm3u8') + cookie[i]['cookie']
            print(url, '    ', names[i])

            # now write the url and name to a text file
            with open('output.txt', 'a') as f:
                f.write(url + '\t' +names[i] + '\n' + '\n')
            f.close()
    
    except Exception():
        traceback.print_exc()

else:
    print('No of names and links are not same')