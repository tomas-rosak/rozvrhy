import random
import os


def rozpoznani_tridy(tridy, trida, vyuka):
    if trida == "6A":
        for i in tridy:
            i.append(vyuka)
            break   
    elif trida == "6B":
        index = 0
        for i in tridy:
            if index == 1:
                i.append(vyuka)
                break  
            index +=1 
    elif trida == "6C":
        index = 0
        for i in tridy:
            if index == 2:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "7A":
        index = 0
        for i in tridy:
            if index == 3:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "7B":
        index = 0
        for i in tridy:
            if index == 4:
                i.append(vyuka)
                break  
            index +=1  
    elif trida == "7C":
        index = 0
        for i in tridy:
            if index == 5:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "8A":
        index = 0
        for i in tridy:
            if index == 6:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "8B":
        index = 0
        for i in tridy:
            if index == 7:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "8C":
        index = 0
        for i in tridy:
            if index == 8:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "9A":
        index = 0
        for i in tridy:
            if index == 9:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "9B":
        index = 0
        for i in tridy:
            if index == 10:
                i.append(vyuka)
                break  
            index +=1   
    elif trida == "9C":
        index = 0
        for i in tridy:
            if index == 11:
                i.append(vyuka)
                break  
            index +=1   
    return tridy
    

def vytvoreni_rozvrhu():
    jmena = ["adlerova","bavlnkova","gregorova","haisova","haskova","hofirkova",
             "jaskova","kottek","kralova","miksova", "motyckova","satinska","scerbejova",
             "smyckova","spickova","stibor","svaniga","szmekova", "ticha","trnkova","videnska",
             "vokrojova","vorisek","weissova"]
            
    rozvrhy = []        
    for i in jmena:  
        try:
            with open("/home/tom/skola_rozvrh/pocet_ucitele/"+i, "r") as rozvrh:
                rozvrh = rozvrh.read()
                rozvrhy.append(rozvrh)
        except:
            pass

    tridy = [["6A"], ["6B"], ["6C"], ["7A"], ["7B"], ["7C"], ["8A"], ["8B"], ["8C"], ["9A"], ["9B"], ["9C"]]
               
    index = 0
    predmety_ucitel = []
    ucitele_rozvrh = []
    for i in rozvrhy:
        i = i.split("\n")
        predmety_ucitel = []
        index = 0
        for j in i:
            if index == 0 or index % 3 == 0:
                try:
                    predmet = j + " " + i[index + 1]
                    predmety_ucitel.append(predmet)
                except:
                    continue
            index += 1 
        ucitele_rozvrh.append(predmety_ucitel)    

    index = 0
    for i in ucitele_rozvrh:
        index = 0
        for j in i:
            j = j.split(" ")
            trida = j[0]
            prace = j[1] + " " + j[2]
            opakovani = j[3][0]
            for j in range(int(opakovani)):
                tridy = rozpoznani_tridy(tridy, trida, prace)
        index += 1
 
    rozvrh1 = []
    for i in tridy:
        trida = i[0]
        vyuka = i[1:]
        komplet = [trida, vyuka]
        rozvrh1.append(komplet)
        
    return rozvrh1


def promichani(seznam_hodin, tridy):
    
    prazdny_rozvrh = []
    for i in range(len(tridy)):
        trida = tridy[i]
        dny = []
        for j in range(5):
            den = []
            for h in range(7):
                hodina = []
                den.append(hodina)
            dny.append(den)
        prazdny_rozvrh.append([trida, dny])
                                                               # prazdny_rozvrh[0][1][0][0]  1. kompletni trida, 2. nazev tridy/cely hodiny, 3. jednotlivy den 4. hodina
    index = 0
    for i in seznam_hodin:
        for hodiny in i[1:]:
            for predmet in hodiny:
                pokracovat = True
                ucitel = ""
                for pismeno in predmet[4:]:
                    if pismeno != ",":
                        ucitel += pismeno
                while pokracovat:
                    den = random.randint(0, 4)
                    hodina = random.randint(0, 6)  
                    if prazdny_rozvrh[index][1][den][hodina] == []:
                        for index1 in range(5):
                            if prazdny_rozvrh[index1][1][den][hodina] != ucitel:    
                                prazdny_rozvrh[index][1][den][hodina] = (predmet)
                                pokracovat = False
           
        index += 1
    return prazdny_rozvrh
    

         
            
    
                
          
def main():
    tridy = ["6A", "6B", "6C", "7A", "7B", "7C", "8A", "8B", "8C", "9A", "9B", "9C"]
    print("Zpracovávání dat...")
    seznam_hodin = vytvoreni_rozvrhu()
    print("Vytváření rozvrhu...")
    rozvrh = promichani(seznam_hodin, tridy)
    print(rozvrh)

    
    
    
main()  


