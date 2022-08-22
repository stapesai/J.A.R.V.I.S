# function to download video
def VideoDownloader(url_input, video_name, video_path):
    import youtube_dl
    ydl_opts = {
        'nopart': True,
        'format': 'bestvideo+bestaudio/best', # download best quality of video and audio available
        'outtmpl': video_path+'/'+video_name # output file name
    }
    url = str(url_input)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) # download video from url input and save it in the same directory as the script


# function to read csv file and append the title and url to a list
urls = []
def ReadCSV(file_name):
    import csv
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # edit the video name to remove any special characters
            row[0] = row[0].replace(': ', '')
            row[0] = row[0].replace('||', 'II')
            row[0] = row[0].strip()

            # if pw_check == 'y':
            if '.mp4' in row[1]:
                # edit the video url to paste master.m3u8
                video_link_initial = row[1]
                j=''
                for i in  range(75):
                    j+=video_link_initial[i]

                video_link_final = j + 'master.m3u8'
                row[1] = video_link_final
            urls.append(row)
    csv_file.close() # close the csv file


# check connection to client
def check_client():
    import sys
    sys.path.insert(0, 'G:\\Jarvis NvMe Drive\\J.A.R.V.I.S\\features')
    import command_remotly.command_server as command_server
    command_server.check_connection_to_client()


# shuting down the computer after download
def shut_down(n):
    if shut_check == 'y':
        # showing user that the computer will shut down in n seconds
        import time
        print(f'Shutting down in {n} sec...') # computer will shut down in 5 min after download.
        time.sleep(n)

        # shut down the remote computer
        try:
            import sys
            sys.path.insert(0, 'V:\\J.A.R.V.I.S\\features')
            import command_remotly.command_server as command_server
            command_server.send_command('shutdown')
            time.sleep(2)
            if command_server.reply == 'shutting down sir':
                print('NAS is shutting down...')
            time.sleep(5)
            
        except:
            print('Error: Shutting down the computer failed.')

        # shut down the main computer
        import os
        os.system('shutdown -s -t 0')

# main function
if __name__ == '__main__':
    # ask user if he want to shut down the computer after download
    shut_check = input('Do you want to shut down the computer after download? (y/n) : ')
    if shut_check == 'y':
        check_client()

    # ask user the name of the csv file
    csv_file_name = str(input('Enter the csv file name: ')) + str('.csv')
    ReadCSV(csv_file_name)

    from plyer import notification
    for task in urls:
        if 'master.m3u8' in task[1]:               # for pw protected videos
            video_name = task[0] + '.mp4'
        else:
            video_name = task[0]
        video_link = task[1]
        video_path = task[2]
        print('-'*500) # print a line

        # check if the video is already downloaded
        import os
        if os.path.isfile(video_path+'/'+video_name):
            print(f'{video_name} is already downloaded.')
        else:
            # giving information about the new video
            print('New Video: ' + video_name)
            print('New Video Link: ' + video_link)
            print('New Video Path: ' + video_path)
            print('Downloading...')
            print('-'*500) # print a line
            
            # notification.notify(title = 'New Video : {}'.format(video_name))


            # download the video
            VideoDownloader(video_link, video_name, video_path)
    print('All videos downloaded!')
    
    # shuting down the computer after download
    shut_down(300)