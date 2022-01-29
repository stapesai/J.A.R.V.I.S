# Training bot by txt file...
from csv import writer


train_file = open('bot_training.txt','r')
train_data = train_file.read()
#print(train_data)

for temp in train_data.split('\n \n'):
    #print(temp)
    List = ['','']
    if 'Ayush Bansal David FD' in temp:
        train_keyword = temp.replace('Ayush Bansal David FD: ','')
        print('Train Keyword is : ',train_keyword)
        List[0] = train_keyword

    if 'DEVASHEESH' in temp:
        train_reply = temp.replace('DEVASHEESH: ','')
        print('Train Reply is : ',train_reply)
        List[1] = train_keyword

    print('List is : ',List)

    import csv
    csv_open = open('train_output.csv','a')
    csv_train = writer(csv_open)
    csv_train.writerow(List)
    

train_file.close()