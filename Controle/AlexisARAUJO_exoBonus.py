def mot_crypte(M):
    dictio = {}
    for i in M:
        if i in dictio:
            dictio[i][0] +=1
        else : 
            dictio[i] = [1]
    #print(dictio)

    for lettre in dictio:
        #print(dictio[lettre][0])
        if(dictio[lettre][0] %2 == 0):
            calcul = dictio[lettre][0]//2
            dictio[lettre].append(calcul)
        else : 
            calcul = dictio[lettre][0] * 2
            dictio[lettre].append(calcul)
    
    return dictio

M = str(input("Veuillez entrer un mot en majuscule"))
print(mot_crypte(M))