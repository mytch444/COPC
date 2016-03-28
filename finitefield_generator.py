#Ensuring Correct Input
def ECI(n):
    return 7 * n + 1

#Polyniomialiser of finite field
def PFF(LD, UD): 
    return ((ECI(LD) ^ 13 + ECI(UD) ^ 11) % 26)

#Generate Finite Field
def GFF():
    ff = []

    for LD in range(0,10):
        ff.append([PFF(LD, UD) for UD in range(0, 10)])

    return ff

#Print FF
def PrintFF():
    ff = GFF()
    for col in ff:
        print([chr(97 + n) for n in col])