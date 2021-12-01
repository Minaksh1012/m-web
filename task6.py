
# import json


# def language_analys():
#     list=open("task5.json")
#     language=json.load(list)
#     # print(language)
#     list1=[]
#     for i in language:
#         # g=i["Original Language:"]
#         # print(i)

        
#         if i["Original Language:"] not in list1:
#             # print(list1)
#             list1.append(i["Original Language:"])
#     dict={}
#     list2=[]
#     for g in list1:
#         i=0
#         count=0
#         while i<len(language):
#             if g==language[i]["Original Language:"]:
#                 count+=1
#             i+=1
#         dict.update({g:count})
#     # print(dict) 
#     list2.append(dict) 
#     print(list2)

#     with open("task6.json","w") as f:
#         json.dump(list2,f,indent=4)




#     # print(list1)
# language_analys()    

import json


def language_analys():
    list=open("task5.json")
    language=json.load(list)
    # print(language)
    list1=[]
    for i in language:
        # g=i["Original Language:"]
        # print(g)

        
        if i["Original Language:"] not in list1:
            # print(list1)
            list1.append(i["Original Language:"])
            # print(list1)
    dict={}
    list2=[]
    for g in list1:
        i=0
        count=0
        while i<len(language):
            if g==language[i]["Original Language:"]:
                count+=1
            i+=1

        dict.update({g:count})
    # print(dict) 
    list2.append(dict) 
    # print(list2)

    with open("task6.json","w") as f:
        json.dump(list2,f,indent=4)




    # print(list1)
language_analys()    

