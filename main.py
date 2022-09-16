from random import *

ans=input("do you want too see anime ?")

animes={
    "action":["naruto","one piece","bleach","dragon ball"],
    "comedy":["gintama","one punch man","le college foufoufou"],
    "drama":["your name","ousamma ranking"]
}

if ans=="y":
    print("what type of anime do you want to see ?\nThe disponible types are: ")
    for x in animes:
        print(x)
    typeofanimes=input("your choice : ")
    print("ok\nwatch this:")
    print(animes[typeofanimes][randint(0,len(animes[typeofanimes])-1)])
else:
    print('byyye!')
    
    
    


