import abobus
inp = input("encrypt - 0 or decrypt - 1   ")
if inp == '0':
    while True :
        cypher = input("Wordswithoutspaces ") 
        if cypher != "":
            break
    while True :
        key = input("key ")
        if key != "":
            break
    
    print(abobus.encrypt(cypher, key))
elif inp == "1":
    while True :
        cypher = input("Cypher ") 
        if cypher != "":
            break
    while True :
        key = input("Key ")
        if key != "":
            break
    # howmanyspaces = int(input("how many spaces   "))
    # helo = dict()
    # for i in range(howmanyspaces):
    #     helo[i] = int(input("space "+ str(i) + "   "))
    # helo = list(helo.values()) 
    # print("hello")
    print(abobus.decrypt(cypher, key))