#Snake and ladders game because why not

import random


boardRow = ["1","2","3","4","5","6","7","8","9","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30",
            "31","32","33","34","35","36","37","38","39","40",
            "41","42","43","44","45","46","47","48","49","50",
            "51","52","53","54","55","56","57","58","59","60",
            "61","62","63","64","65","66","67","68","69","70",
            "71","72","73","74","75","76","77","78","79","80",
            "81","82","83","84","85","86","87","88","89","90",
            "91","92","92","94","95","96","97","98","99","100",]

#Prints Board with placehold numbers 
def board():
    i = 0
    while i<=99:
        print (" | "+ boardRow[i]+" | ",boardRow[i+1]+" | ",boardRow[i+2]+" | ",boardRow[i+3]+" | ",boardRow[i+4]+" | ",boardRow[i+5]+" | ",boardRow[i+6]+" | ",boardRow[i+7]+" | ",boardRow[i+8]+" | ",boardRow[i+9]+" | ")
        i+=10

# Generates random locations for the snakes
def genSnakes():
    global s1s,s2s,s3s,s4s #head of the snakes
    global s1e,s2e,s3e,s4e #tail of the snakes

    s1s = random.randint(0,101)
    s1e = random.randint(0,s1s)

    
    s2s = random.randint(0,101)
    s2e = random.randint(0,s2s)

    
    s3s = random.randint(0,101)
    s3e = random.randint(0,s3s)

    
    s4s = random.randint(0,101)
    s4e = random.randint(0,s4s)

#Gets letter of player name 
def playerName():
    global lst

    lst = []
    num = numPlayer
    for i in range(0,num):
        name =  str("Player "+i+" please enter a letter: "+input())

        lst.append(name)

    print (lst)

    



        

def playGame():
    board()

    print ("Welcome to Walmart Snakes and Ladders!")
    numPlayer = input("Please enter how many players from 1-4: ")
    if numPlayer == "1" or numPlayer == "2 "or numPlayer == "3" or numPlayer == "4":

        genSnakes()

        playerName()
        print(lst)

    
    
playGame()
