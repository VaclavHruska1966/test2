import random

pole = []



body = 1
body = int(body)
    
for x in range (random.randint(1, 15)):
    print("kolo číslo",x+1)
    
    
    for i in range(random.randint(1,10)):
        pole.append(random.randint(1, 10))
    print(pole)

    delka = int(len(pole))

    odpoved = input("Uhodnete kolik prvků je v poli?   :")
    odpoved = int(odpoved)
    if body >0:
        if delka == odpoved:
            print("body vám zůstávají", )
        else:
            body = body-1
            print("špatně odečítá se vám bod", )
    else:
        print("skončils ty noobe")
        break
        
print("přežil jsi do konce")
print(" ")
znovu = input("chcete hrát znovu? [ano] nebo [ne]")
