from task1 import*
import os 
import json
import requests
from bs4 import BeautifulSoup



url_list=[]
for i in movies:
    url_list.append(i["movie_link"])
def text_file(ulist):
    last=[]
    # time_sleep=random.randint(1,3)
    for i in ulist:
        id=i[33:]
        if os.path.exists(id+".json")==True:
            with open(id+".json","r") as movieDataFile:
                data=movieDataFile.read()
                final=json.loads(data)
            last.append(final)
        else:
            final={}
            # time.sleep(time_sleep)
            LinkData=requests.get(i)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            final["name"]=soup.find("h1").text
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            for i in all:
                final[i.find("div",class_="meta-label subtle").text.replace("\n","")]=(i.find("div",class_="meta-value")).text.replace("\n","")
            with open(id+".json","w") as file:
                json.dump(final,file,indent=2)
            last.append(final)
    # return last
text_file(url_list[:10])

