
import json
import pprint
def final(text):
    return " ".join(text.split())

def director_analyse():
    list=open("task5.json")
    a=json.load(list)
    # print(lang)
    list1=[]
    # dict={}
    for i in a:
        # g=i["Original Language:"]

        
        if i["Director:"] not in list1:
            # print(list1)
            list1.append(i["Director:"])
    dict={}
    list2=[]
    for g in list1:
        i=0
        count=0
        while i<len(a):
            if g==final(a[i]["Director:"]):
                count+=1
            i+=1
        dict[g]=count
    # print(dict) 
    # pprint.pprint(dict)   


                                                          
    with open("task7.json","w") as f:
        json.dump(dict,f,indent=4)




    # print(list1)
director_analyse()    
