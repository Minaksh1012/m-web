import requests
from bs4 import BeautifulSoup
import json





def scrape_top_list():
    TopMovie_url= "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"

    TopRatedMoviesApi=requests.get(TopMovie_url)

    htmlcontent=TopRatedMoviesApi.content
    # print(htmlcontent)


    soup=BeautifulSoup(htmlcontent,"html.parser")

    tableTag=soup.find("table",class_="table")
    td=tableTag.find_all("tr")
#    
    top_movie=[]
    for i in td[1:]:    
        
        movieRank=i.find("td",class_="bold")
        # print(movieRank)
        # for rank in movieRank:
        # r=movieRank.pop()
        # print(r)
        rank=((movieRank).text.strip())
        # print(rank)
        s=rank[:-1]

    
        # print(s)

        

        movieRating=i.find("span",class_="tMeterScore")
        # for rating in movieRating:
        #     a=(" ".join(movieRating.text.split()))
        #     a.strip()
        a=(movieRating.text.strip())
  
        movieName=i.find("a", class_="unstyled articleLink")
        # for name in movieName:
        b=(movieName.text.strip())
        n=b[:-7]
        # print(n)

        year=b[len(b)-5:len(b)-1]
            # b.strip()
        # print(b)
        
        
        reviewsNo=i.find("td",class_="right hidden-xs")
        # for reviews in reviewsNo:
        reviews=(reviewsNo.text.strip())
            

        Movie_url=i.find("a",class_="unstyled articleLink")['href']

        Movie_link="https://www.rottentomatoes.com"+Movie_url
       
        allDetails={"movieRank":s ,"movieYear":year , "movieRating":a , "movieName":n , "reviewsNo":reviews , "movie_link":Movie_link}

        top_movie.append(allDetails.copy())
        # print(top_movie)
    
    with open("task1.json","w") as movieDataFile:
        json.dump(top_movie,movieDataFile,indent=5)
    return top_movie

movies=scrape_top_list()



