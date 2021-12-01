# from task12 import*
# import json
# from bs4 import BeautifulSoup
# cast=main_fun(url)
# print(cast)



# def scrape_movie_details(Movie_url):
#     moviedetails={}
#     page=requests.get(Movie_url)
#     # print(page)
#     soup=BeautifulSoup(page.text,"html.parser")
#     # print(soup)
#     # title_div=soup.find(div,class_="scoreboard_title").h1.get.text()
#     # print(title_div)
#     moviedetails["name"]=soup.find("h1").text
#     # print(moviedetails)
#     main=soup.find("ul",class_="content-meta info")
#     # print(main)
#     all=main.find_all("li",class_="meta-row clearfix")
#     # print(all)
#     for i in all:
#         # print(i)
#         # moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value")).text).split())
#         moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
#         print(moviedetails)
# scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")        




# a="p"
# c="v"
# total=(a+c)
# print(total)



# a=9
# b=7
# c=6
# print(9)
# print(7)

# a=5+8
# b="5"+"8"
# print(b)
# v="a"+"b"+"s"
# print(v)

# a=36
# b=32
# c=31
# a=a+b+c
# b=a-(b+c)
# c=a-(b+c)
# a=a-(b+c)
# print(a,b,c)




from bs4 import BeautifulSoup
import json
import requests
# import task12
from Task12 import main_fun
a=[]
def scrape_movie_details(url):
    cast=(main_fun(url))
    # print(cast)
    moviedetails={}
    link=requests.get(url)
    # print(link)
    soup=BeautifulSoup(link.text,"html.parser")
    

    # b["cast"]=cast
    # print(cast)
    moviedetails["name"]=soup.find("h1").text
    # print(moviedetails)
    main=soup.find("ul",class_="content-meta info")
    # print(main)
    all=main.find_all("li",class_="meta-row clearfix")
    # print(all)
    for i in all:
        # print(i)
        # moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value")).text).split())
        moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())

    moviedetails["cast"]=cast

    
        # print(moviedetails)
    with open("task13.json","w") as f:
        json.dump(moviedetails,f,indent=2)

    
    return moviedetails
    # moviedetails["cast"]=cast
    # print(cast)
    
        
cast=scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")