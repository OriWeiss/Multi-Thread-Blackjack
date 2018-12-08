
from player import *
import threading
from deck import *

def isWinner(players):
    playersPlaying = 0
    playersHit = 0
    for i in range(len(players)):
        if(players[i].playing == True):
            playersPlaying +=1
        if(players[i].hasHit == True):
            playersHit+=1
    if(playersPlaying == 1): #if only one player is playing he is the winner
        return True
    if(playersHit ==0): #if no one hit there needs to be a winner and is to be calculated
        return True
    return False # no one has won

# def calculateWinner(players):
# 	winner = player("Temp")
# 	for i in range(len(players)):
# 		if(players[i].bust & (winner.totalCards < players[i].totalCards)):
# 			winner = players[i]
# 	return winner



def totals(cards):
    total = 0

    for i in range(len(cards)):
        if(cards[i] == 1):
            total = total + 11
            cards[i] = 11
            if (total > 21):
                total = total - 10
                cards[i] = 1
        else:
            total = total + cards[i]

    return total



def strategy(player,deck,dealerFaceCard):
    if(totals(player.cards)>= 17):
        player.hasHit = False

    elif(totals(player.cards)== 16):
        if(2<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = False

    elif(totals(player.cards)== 15):
        if(2<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = True

    elif(totals(player.cards)== 14):
        if(2<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = True

    elif(totals(player.cards)== 13):
        if(2<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = True

    elif(totals(player.cards)== 12):
        if(4<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = True

    elif(totals(player.cards)== 11):
        player.cards.append(deck.flipCard())
        player.hasHit = True

    elif(totals(player.cards)== 10):
        player.cards.append(deck.flipCard())
        player.hasHit = True

    elif(totals(player.cards)== 9):
        if(3<=dealerFaceCard<=6):
            player.hasHit = False
        else:
            player.cards.append(deck.flipCard())
            player.hasHit = True

    elif(totals(player.cards)== 8):
        player.cards.append(deck.flipCard())
        player.hasHit = True
    elif(totals(player.cards) < 8):
        player.cards.append(deck.flipCard())
        player.hasHit = True

    if(totals(player.cards) > 21): #check if player has busted
        player.bust = True

def dealerStrategy(dealer,decks,highestCards):
    dealer.bust = False
    while((totals(dealer.cards) < highestCards) ):
        dealer.cards.append(decks.flipCard())
        dealer.hasHit = True
        if(totals(dealer.cards) > 21):
            dealer.bust = True
    #print("Inside dealer strategy for ",dealer.name)


def largestPlayer(players):
    winner  = player("temp")
    for i in range(len(players)):
       
        if(players[i].bust != True):
            total = totals(players[i].cards)    

            if(total > totals(winner.cards)):
                winner = players[i]
            total = 0
    return winner

def calculateWinner(players,dealer):
    winner  = player("temp")
    for i in range(len(players)):
        cards = ""
        for j in range(len(players[i].cards)):
            cards = str(players[i].cards[j]) + " "+ cards
        if(players[i].bust != True):
            total = totals(players[i].cards)
            print(players[i].name, " has total ", total, " with cards ", cards)

            if(total > totals(winner.cards)):
                winner = players[i]
            total = 0
        else:
            print(players[i].name , " busted")
            print(cards)
    if(dealer.bust == False):
        cards =""
        for j in range(len(dealer.cards)):
            cards = str(dealer.cards[j]) + " "+ cards   
        print(dealer.name, " has total ", totals(dealer.cards), " with cards ", cards)
        if(totals(winner.cards) < totals(dealer.cards)):
            winner = dealer 
    else:
        print(dealer.name, " busted")
    return winner

def run(player,deck,dealerFaceCard):
    while(not((player.hasHit==False) or (player.bust == True))):
        strategy(player,deck,dealerFaceCard)
    #print("In strategy for ", player.name)
        

