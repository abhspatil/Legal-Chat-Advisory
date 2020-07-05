from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import Articles,ArticleDescription,References,Keywords,QueryData
from collections import defaultdict

# Create your views here.

def home(req):
    return render(req,'home.html',{})

def setData(req):
    
    num=13
    statement="If any law made against the fundamental rights then such law is made as void."
    Desc=["States about Doctrine of Eclipse and Doctrine of Severability","Valid law will have its enforcement",
                "The State shall not make any law which takes away or abridges the rights conferred by this Part and any law \
                made in contravention of this clause shall, to the extent of the contravention, be void",
                "In this article, unless the context otherwise requires law includes any Ordinance \
                order, bye law, rule, regulation, notification, custom or usages having in the territory \
                of India the force of law laws in force includes laws passed or made by Legislature or \
                other competent authority in the territory of India before the commencement of this \
                Constitution and not previously repealed, notwithstanding that any such law or any \
                part thereof may not be then in operation either at all or in particular areas",
                "Nothing in this article shall apply to any amendment of this Constitution made under \
                    Article 368 Right of Equality"]
    
    links =["https://en.wikipedia.org/wiki/I.C._Golaknath_and_Ors._vs_State_of_Punjab_and_Anrs.",
            "https://en.wikipedia.org/wiki/I.C._Golaknath_and_Ors._vs_State_of_Punjab_and_Anrs.jnjncsc",
            "https://en.wikipedia.org/wiki/I.C._Golaknath_and_Ors._vs_State_of_Punjab_and_Anrs.ndjjdjj292"]
            
    article=Articles(articleNum=num,statement=statement)
    article.save()
    
    art=Articles.objects.get(articleNum=num)
    
    for i in Desc:
        desc=ArticleDescription(articleNum=art,description=i)
        desc.save()
        
    for i in links:
        link=References(articleNum=art,links=i)
        link.save()
        
    keywords=["Law made void","Against fundamental rights","Doctrine of Eclipse","Doctrine of Severability",
                        "Article 13","Kesavananda Bharatia","L C Golaknath"]
                        
    for i in keywords:
        key=Keywords(articleNum=art,keyword=i)
        
    return JsonResponse({"status":"OK"})
    
def getData(req):
    
    key=req.GET["key"]
    key=key.lower()
    
    try:
        keyObj=Keywords.objects.get(keyword=key)
    except Exception as e:
        print(e)
        ##########
        querydata = QueryData.objects.all()
        print("searching in loop : "+key)
        for data in querydata:
            print(data.keywords)
            if key in data.keywords.lower():
                
                js=defaultdict(list)
                
                keylist=data.keywords.split("|||")
                
                js["Article"]=keylist[0]
                js["statement"]=data.statement
                js["description"]=data.description
                
                for x in data.links.split("|||"):
                    js["links"].append(x)
                
                return JsonResponse(js)
                
        
        
        
        
        print("Seraching in hashmap cache : ",len(querydata))
        for data in querydata:
            hm={}
            res=data.keywords.split("|||")
            for y in res:
                for x in y.split():
                    hm[x.lower()]=0 
            
            print(hm)
            inpdata=key.split()
            
            print(inpdata)
            for x in inpdata:
                if x in hm:
                    hm[x]=1
                    
            print(sum(hm.values()))
            if sum(hm.values())>=2:
                js=defaultdict(list)
                
                keylist=data.keywords.split("|||")
                
                js["Article"]=keylist[0]
                js["statement"]=data.statement
                js["description"]=data.description
                
                for x in data.links.split("|||"):
                    js["links"].append(x)
                
                return JsonResponse(js)
        
        
        ######
        keydata= Keywords.objects.all()
        for data in keydata:
            if key in data.keyword.lower():
                print(data.keyword)
                
                js=defaultdict(list)
                
                js["Article"].append(data.articleNum.articleNum)
                
                #print("---))) ",)
                
                js["statement"].append(data.articleNum.statement)
                
                Desc=ArticleDescription.objects.filter(articleNum=data.articleNum)
                for i in range(len(Desc)):
                    js["description"].append(Desc[i].description)
                    
                Links=References.objects.filter(articleNum=data.articleNum)
                for i in range(len(Links)):
                    js["links"].append(Links[i].links)
                
                '''
                Statement=Articles.objects.filter(articleNum=keyObj.articleNum)
                js["statement"].append(Statement.statement)
                '''
                
                print("\n Sending Data from Exception of : ",data.articleNum.articleNum)
                return JsonResponse(js)
                
        
        
        
        return JsonResponse({"Status":"Try again. No data Found"})
        
    js=defaultdict(list)
    
    js["Article"].append(keyObj.articleNum.articleNum)
    
    #print("---))) ",)
    
    js["statement"].append(keyObj.articleNum.statement)
    
    Desc=ArticleDescription.objects.filter(articleNum=keyObj.articleNum)
    for i in range(len(Desc)):
        js["description"].append(Desc[i].description)
        
    Links=References.objects.filter(articleNum=keyObj.articleNum)
    for i in range(len(Links)):
        js["links"].append(Links[i].links)
    
    '''
    Statement=Articles.objects.filter(articleNum=keyObj.articleNum)
    js["statement"].append(Statement.statement)
    '''
    
    print("\n Sending Data of : ",keyObj.articleNum.articleNum)
    return JsonResponse(js)
    

def uploadData(req):
    
    return render(req,'uploadData.html',{})

def submitData(req):
    
    if req.method == "POST":
        
        artNum=int(req.POST['articleNum'])
        statement= req.POST['statement']
        keywords= req.POST['keywords']
        description = req.POST['description']
        references = req.POST['references']
        
        keywords=keywords.lower()
        
        keywords=keywords.split('|||')
        description =description.split('|||')
        references = references.split('|||')
        
        print("\n ------------")
        print("Article ",artNum," Added")
        print("---------------\n")
        
        '''
        print(statement)
        
        for i in keywords:
            print(i)
            
        for i in description:
            print(i)
        
        for i in references:
            print(i)
        '''
            
        article=Articles(articleNum=artNum,statement=statement)
        article.save()
        
        #art=Articles.objects.get(articleNum=artNum)
        #print("------->>>>",art)
        
        
        for i in description:
            desc=ArticleDescription(articleNum=article,description=i)
            desc.save()
        
        for i in references:
            link=References(articleNum=article,links=i)
            link.save()
                
        for i in keywords:
            key=Keywords(articleNum=article,keyword=i)
            key.save()
        
        return JsonResponse({"status":"OK"})
    
    return JsonResponse({"status":"Error"})
    
def QueryDataSubmit(req):
    if req.method=="POST":
        
        artNum=int(req.POST['articleNum'])
        statement= req.POST['statement']
        keywords= req.POST['keywords']
        description = req.POST['description']
        references = req.POST['references']
        
        keywords=keywords.lower()
        
        data = QueryData(statement = statement,keywords=keywords,description=description,links=references)
        data.save()
        
        print("Saved : ", statement)
        
        return JsonResponse({"message" : "success"})
        
    return JsonResponse({"message" : "error"})
        
    
import json
import requests

def mlAPI(req):
    data = req.GET['message']

    data = {"sender":"Patil92","message":data}
    #print(data)
    
    url= "http://15.206.161.203:5005/webhooks/rest/webhook"
    res = requests.post(url, data = json.dumps(data))
    
    try:
        data=res.json()
    
    #print(data)
    
        if len(data)==0:
            return JsonResponse({"message" : "Try again. No data Found"})
        
   
        data=data[0]["text"].replace("'","\"")
        #data=data[0]["text"].replace("\\","\\\\")
    except:
        return JsonResponse({"message" : data[0]["text"],"Article":"1"})
    
    print(data)
    
    if "Article" in data:
        #print(data)
        try:
            data=json.loads(data)
            
            #print(data["Article"])
            
            return JsonResponse({"message" : data,"Article":"1"})
            
        except:
            return JsonResponse({"message" : data,"Article":"1"})
            
    
    else:
        #print(data)
        
        return JsonResponse({"message" : data,"Article":"0"})
        
    
    
    
def toJson(req):
    
    print(req)
    js =json.loads(req.body)
    
    print(js)
    
    #js = eval(js) 
    
    return JsonResponse({"js": ""}) 
    
    
    
        
    
    