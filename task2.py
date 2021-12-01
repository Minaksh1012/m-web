from task1 import movies
import json
# movies=scrape_top_list()

def group_by_year(movies):
    # print(movies)
    years=[]
    for i in movies: 
        # print(i)
        if i["movieYear"] not in years:
            # print(years)
            years.append(i["movieYear"])
    years.sort()
    # print(years)
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for k in movies:
        year1=k["movieYear"]
        movie_dict[year1].append(k)
    with open("task2.json","w") as F:
        json.dump(movie_dict,F,indent=4)
year=group_by_year(movies)