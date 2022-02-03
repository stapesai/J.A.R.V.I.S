# Importing Modules...
import csv
import youtube_dl       # install using guide video in youtube-dl


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
global urls
urls = []
def ReadCSV(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # edit the video name to remove any special characters
            row[0] = row[0].replace(': ', '')
            row[0] = row[0].replace('||', 'II')

            # edit the video url to paste master.m3u8
            video_link_initial = row[1]
            j=''
            for i in  range(75):
                j+=video_link_initial[i]

            video_link_final = j + 'master.m3u8'
            row[1] = video_link_final
            
            urls.append(row)

ReadCSV('videos.csv')

# main function
def main():
    for task in urls:
        video_name = task[0] + '.mp4'
        video_link = task[1]
        video_path = task[2]
        print('New Video: ' + video_name)
        print('New Video Link: ' + video_link)
        print('New Video Path: ' + video_path)
        print('Downloading...')
        VideoDownloader(video_link, video_name, video_path)



main()