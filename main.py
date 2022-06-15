def fonc1(mot):
    i=0
    for letter in mot:
        i += 1
    return i

def fonc2(mot):
    for letter in mot:
        if letter == 'a':
            return True
        return False
def verif12(mot):
    if fonc1(mot) < 1:
        return False
    if fonc2(mot) == True:
        return False
    return True

sort = verif12("slut")
if sort == True:
    print (" tt est ok")
else:
    print("tt est ko")



