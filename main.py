from random import *

ans=input("do you want too see anime ?")
animes=["naruto", "jjk", "demonSlayer"]

if ans=="y":
    print("ok\nwatch this:")
    print(animes[randint(0,2)])
else:
    print('byyye!')



