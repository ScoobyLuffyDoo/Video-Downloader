from turtle import down
import urllib.request
import threading
import time
# https://1movieshd.com/watch-tv/free-the-troop-hd-35496.5204686
Download_Links = {
                #   '013':''
}
threadList =[]

def download_video(Episode_number,dwn_link):
    file_name =f'Firends With Better Lives Episode {Episode_number}.mp4'
    urllib.request.urlretrieve(dwn_link, file_name)
    print(f'{file_name} : Downloaded Complete')

for number,link in Download_Links.items():
    thread= threading.Thread(target=download_video,args=(number,link,))   
    print(f'Episode : {number} Added')
    threadList.append(thread)
for thread in threadList:
    thread.start()
    print('downloading started')
for thread in threadList:
    thread.join()    
print("done")