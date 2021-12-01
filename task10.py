# import json

# with open("task5.json","r") as f:
#     data1=json.load(f)

# def language_and_directores(movies_list):
#     DirectoresDict={}
#     for movies in movies_list:
#         for Director in movies:
#             if Director=="Director:":
#                 DirectoresDict[movies[Director]]={}
#     for i in range(len(movies_list)):
#         for Director in DirectoresDict:
#             if Director in movies_list[i][ "Director:"]:
#                 for language in movies_list[i]:
#                     if language=="Original Language:":
#                         a=movies_list[i]["Original Language:"]
#                         DirectoresDict[Director][a]=0
#     for i in range(len(movies_list)):
#         for Director in DirectoresDict:
#             if Director in movies_list[i][ "Director:"]:
#                 for language in movies_list[i]:
#                     if language=="Original Language:":
#                         for l in DirectoresDict[Director]:
#                             DirectoresDict[Director][l]+=1
#     return DirectoresDict

# Director_language=language_and_directores(data1)
# with open("task10.json","w") as f:
#     json.dump(Director_language,f,indent=4)
# print(Director_language)





import json

with open("task5.json","r") as f:
    data1=json.load(f)

def language_and_directores(movies_list):
    Directoreslist=[]

    for movies in movies_list:
        # print(movies)
        if movies["Director:"] not in Directoreslist:
            Directoreslist.append(movies["Director:"])
            # print(Directoreslist)
    f={}        
    for i in Directoreslist:
        print(i) 
        count={}
        lan=[]
        for director in movies_list:
            if i==director["Director:"]:
                if director["Original Language:"] not in lan:
                   count[director["Original Language:"]]=1
                   lan.append(director["Original Language:"])
                    # print(a)
                    # print(lan)                     
                else:
                    count[director["Original Language:"] ]+=1              
        f[i]=count
        # print(f) 
                        
    with open("task10.json","w") as file:
        json.dump(f,file,indent=4)
    return f

language_and_directores(data1)