def saisieNotes(dictio):

    for i in range(len(dictio)):
        #print(dictio[i]["nom"])
        note = int(input("Quelle note souhaitez-vous attribuer pour " + dictio[i]["prenom"] +" " + dictio[i]["nom"] +" ?"))
        dictio[i]["note"] = note
        #print(dictio)
    return dictio

def meilleur(dictionnaire):
    max = 0
    liste_max = []
    
    for i in range(len(dictionnaire)):
        if (max < dictionnaire[i]["note"]) : 
            liste_max = [str(dictionnaire[i]["prenom"]) + " " + str(dictionnaire[i]["nom"])]
            max = dictionnaire[i]["note"]
        
        elif (max == dictionnaire[i]["note"]):
            nom = str(dictionnaire[i]["prenom"]) + " " + str(dictionnaire[i]["nom"])
            liste_max.append(nom)
    
    return max, liste_max

def progPrincipal():
    d=[{"nom":"ebel","prenom":"franck"},{"nom":"spriet","prenom":"hugues"},{"nom":"burel","prenom":"romain"},{"nom":"de montalivet","prenom":"paul"}]
    l1=saisieNotes(d)
    print(l1)
    resu = meilleur(l1)
    print("la meilleur note est : ",resu[0]," et appartient à ")
    for i in range(len(resu[1])):
        print(resu[1][i])
    return
progPrincipal()