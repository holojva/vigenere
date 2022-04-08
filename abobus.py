def vig_square() :
    bukvy = list("abcdefghijklmnopqrstuvwxyz")
    apple = []
    for i in range(len(bukvy)) :
        apple.append(bukvy[i:] + bukvy[:i])
    return apple
def encrypt(cypher, key) :
    
    spaces = []
    
    # for i in range(len(cypher)) :
    #     # print(cypher[i])
    #     if cypher[i] == " " :
    #         spaces.append(i)
    # print(spaces)
    cypher = cypher.lower()
    # # print(cypher)
    cypher2 = cypher.split()
    # print(cypher)
    cypher2 = "".join(cypher2)
    # print(cypher)
    keykey = []
    lens = len(cypher2) // len(key)
    for i in range(lens) :
        keykey.append(key)
    keykey.append(key[:len(cypher2) % len(key)])
    keykey = "".join(keykey)
    
    # letters = {"a": 0, "b": 1, "c": 2, "d": 3,"e": 4, "f": 5,"g": 6, "h": 7,"i": 8, "j": 9, "k": 0, "l": 1, "m": 2, "n": 3,"o": 4, "f": 5,"g": 6, "h": 7,"i": 8, "j": 9,}
    bukvy = list("abcdefghijklmnopqrstuvwxyz")
    letters = dict()
    for i in range(len(bukvy)) :
        letters[bukvy[i]] = i
    # print(letters)
    apple = vig_square()
    # print(i)
    cypherunkey = list(cypher)
    keykey = str(keykey)
    # apple это квадкат видженера
    # keykey это ключ
    # cypher это то что нужно шифровать
    # letters это словарь с буквами
    # attackatdawn
    # LEMONLEMONLE
    # LXFOPVEFRNHR
    # print(keykey, cypher)
    otvet = []
    app = 0
    other = '''1234567890!@#$%^&*()!<>?:'{}".,|\/'''
    for i in range(len(cypher)) :
        if cypher[i] in bukvy :
            otvet.append(apple[letters[keykey[i-app]]][letters[cypher[i]]])
        else:
            otvet.append(cypher[i])
            app += 1
    otvet2 = "".join(otvet)
    return otvet2
# cypher
def decrypt(otvet2, key) :
    # attackatdawn
    # LEMONLEMONLE
    # LXFOPVEFRNHR
    spaces = []
    apple = vig_square()
    bukvy = list("abcdefghijklmnopqrstuvwxyz")
    letters = dict()
    for i in range(len(bukvy)) :
        letters[bukvy[i]] = i
    text = []
    numbers = dict()
    for i in range(len(bukvy)) :
        numbers[i] = bukvy[i]
    # print("hello")
    # print("hello")
    # print("hello")
    answer = []
    keykey = []
    lens = len(otvet2) // len(key)
    for i in range(lens) :
        keykey.append(key)
    keykey.append(key[:len(otvet2) % len(key)])
    keykey = "".join(keykey)
    # print("important")
    # print(keykey)
    # print("important")
    app = 0
    for i in range(len(keykey)) :
        if otvet2[i] in bukvy :
            # print(i)
            mystring = apple[letters[keykey[i-app]]]
            answer.append(numbers[mystring.index(otvet2[i])])
        else:
            answer.append(str(otvet2[i]))
            app += 1
        # letters[otvet[i]]
        # print(key[i])
        # text.append()
    
    # answer# = "".join(answer)
    # cypherunkey = answer
    # for i in spaces :
    #     cypherunkey.insert(i, " ")
    # print("hello")
    # print("".join(cypherunkey))
    return "".join(answer)

# encrypt(cypher, key)
# decrypt(encrypt(cypher, key)[0], encrypt(cypher, key)[1], encrypt(cypher, key)[2])