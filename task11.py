
# import json
# # import pprint
# def final(text):
#     return " ".json(text.split())

# def movie_analys():
#     list=open("movie details.json","r")

#     language=json.load(list)
#     # print(lang)
#     list1=[]
#     # dict={}
#     for i in language:
#         # g=i["Original Language:"]

        
#         if i["Genre:"] not in list1:
#             list1.append(i["Genre:"])
#     dict={}
#     list2=[]
#     for g in list1:
#         i=0
#         count=0
#         while i<len(language):
#             if g==language[i]["Genre:"]:
#                 count+=1
#             i+=1
#         dict.update({g:count})
#     # print(dict) 
#     list2.append(dict) 
#     # print(list2)
#     # l=(list2.strip())

#     with open("comedy drama.json","w") as f:
#         json.dump(list2,f,indent=4)




#     # print(list1)
# movie_analys()    



# from task5 import*
# get=get_movie_details(scrapped)
# print(get)


# # def analyse_movie_gener(movies):
# #     gener_list=[]
# #     for movie in movies:
# #         json_2_dic=json.loads(movies)
# #         gener=json_2_dic["Genre:"]
# #         for i in gener:
# #             if i not in gener_list:
# #                 gener_list.append(i)
# #         analyse_gener={gener_type:0 for gener_type in gener_list}
# #         for gener_type in gener_list:
# #             for movie in movies:
# #                 json_2_dic=json.loads(movie)
# #                 if gener_type in json_2_dic["Genre:"]:
# #                     analyse_gener[gener_type]+=1
# # gener_analysis=analyse_movie_gener(movies_details)
# # print(gener_analysis)




# import json
# import pprint
# def final(text):
#     return " ".json(text.split())

# def director_analyse():
#     list=open("movie details.json")
#     language=json.load(list)
#     # print(lang)
#     list1=[]
#     # dict={}
#     for i in language:
#         # g=i["Original Language:"]

        
#         if i["Genre:"] not in list1:
#             # print(list1)
#             list1.append(i["Genre:"])
#     dict={}
#     list2=[]
#     for g in list1:
#         i=0
#         count=0
#         while i<len(language):
#             if g==final(language[i]["Genre:"]):
#                 count+=1
#             i+=1
#         dict[g]=count
#     # print(dict) 
#     pprint.pprint(dict)   


#     with open("task11.json","w") as f:
#         json.dump(dict,f,indent=4)




#     # print(list1)
# director_analyse()    





import json
# import pprint
def final(text):
    return " ".join(text.split())

def director_analyse():
    list=open("task5.json")
    l=json.load(list)
    # print(lang)
    list1=[]
    # dict={}
    for i in l:
        # g=i["Original Language:"]
        f=final(i["Genre:"])
        temp=f.split(",")
        # print(temp)
        for j in temp:
            if j not in list1:
                list1.append(j)
    # print(list1)            


        
    # if final(i["Genre:"]) not in list1:
        
        # #     # print(list1)
        # list1.append(final(i["Genre:"]))
    dict={}
    for j in list1:
        i=0
        count=0
        while i<len(l):
            if j in final(l[i]["Genre:"]).split(","):
                count+=1
            i+=1
        dict[j]=count
    # print(dict) 
    # pprint.pprint(dict)   


                                                          
    with open("task11.json","w") as f:
        json.dump(dict,f,indent=4)



    # print(list1)
director_analyse()    

