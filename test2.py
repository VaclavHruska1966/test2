import random

pole = []



body = 0
body = int(body)
    
for x in range (random.randint(1, 15)):
    print("kolo číslo",x+1)
    
    
    for i in range(random.randint(1,10)):
        pole.append(random.randint(1, 10))
    print(pole)

    delka = int(len(pole))

    odpoved = input("Uhodnete kolik prvků je v poli?   :")
    odpoved = int(odpoved)
    
    if delka == odpoved:
        body = body +1
        print("správně přičítá se vám bod", body)
    else:
        body = body-1
        print("špatně odečítá se vám bod", )