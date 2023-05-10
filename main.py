import random
import time
nballu= int(input("combien d'allumettes ?"))

def jeubien(nballu):
    '''truc'''
    start = int(input("qui commence ? \n 0 : toi \n 1 : la machine"))
    win = False
    while nballu !=0 :
        allu= '|'*nballu
        print (allu)
        if start == 0 :
            #choix du joueur
            playerChoice = int(input("choississez 1,2 ou 3 allumettes"))
            while playerChoice > 3 or playerChoice < 1 or playerChoice > nballu:
                playerChoice = int(input("nombre incorrect, veuillez ne pas tricher"))
            nballu -= playerChoice
            allu = "|"*nballu
            print(allu)
            print("il reste " + str(nballu) + ' allumettes')
            if nballu ==0 :
                win = True
        start = 0
        #choix de l'ordinateur
        time.sleep(2)
        if nballu !=0 :
            IAChoice = Choose(nballu)
            nballu -= IAChoice
            allu = "|"*nballu
            print(allu)
            print("il reste " + str(nballu) + " allumettes")

        #victoire ou defaite
    if win ==True:
        print(" bien joué !")
    if win ==False:
        print("game over")

def Choose (nballu) :
    '''action !! '''
    if (nballu -1) % 4 ==0 :
        return 1
    if (nballu -2) % 4 ==0 :
        return 2
    if (nballu -3) % 4 ==0 :
        return 3
    else :
         if nballu >=3 :
                return random.randint(1,3)
         else :
                return random.randint(1,nballu)


jeubien(nballu)
