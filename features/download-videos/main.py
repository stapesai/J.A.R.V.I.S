# Importing Modules...
import csv
import youtube_dl       # install using guide video in youtube-dl
from multiprocessing import Process

global shut_check # just to avoid the error
shut_check = input('Do you want to shut down the computer after download? (y/n) : ')

global pw_check # just to avoid the error
pw_check = input('Do you want to download videos from pw? (y/n) : ')

# function to download video
def VideoDownloader(url_input, video_name, video_path):
    ydl_opts = {
        'nopart': True,
        'format': 'bestvideo+bestaudio/best', # download best quality of video and audio available
        'outtmpl': video_path+'/'+video_name # output file name
    }
    url = str(url_input)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) # download video from url input and save it in the same directory as the script


# function to read csv file and append the title and url to a list
global urls # just to avoid the error
urls = []
def ReadCSV(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # edit the video name to remove any special characters
            row[0] = row[0].replace(': ', '')
            row[0] = row[0].replace('||', 'II')

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

csv_file_name = str(input('Enter the csv file name: ')) + str('.csv')
ReadCSV(csv_file_name)
#ReadCSV('videos.csv')

# main function
def main():
    for task in urls:
        video_name = task[0] + '.mp4'
        video_link = task[1]
        video_path = task[2]
        print('-'*500) # print a line
        print('New Video: ' + video_name)
        print('New Video Link: ' + video_link)
        print('New Video Path: ' + video_path)
        print('Downloading...')
        print('-'*500) # print a line
        
        VideoDownloader(video_link, video_name, video_path)
    
    # shuting down the computer after download
    if shut_check == 'y':
        print('All videos downloaded!')
        import time
        print('Shutting down in 5 min...') # Showing the user that the computer will shut down in 5 min after download
        time.sleep(300)
        import os
        os.system('shutdown -s -t 0')

# calling main function
main()
print('All videos downloaded!')

# using multiprocessing to download videos in parallel
# if __name__ == '__main__':
#     process_list = []
#     for task in urls:
#         video_name = task[0] + '.mp4'
#         video_link = task[1]
#         video_path = task[2]
#         process = Process(target=VideoDownloader, args=(video_link, video_name, video_path))
#         process_list.append(process)
#         process.start()
#     for process in process_list:
#         process.join()
# code completed..... :) :) :)