
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
    ace = False
    for i in range(len(cards)):
        if(cards[i] == 1):
            ace = True
            total = total + 11
        else:
            total = total + cards[i]
    if(ace == True & total > 21):
        total = total - 10
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
        if(2<=dealerFaceCard<=9):
            player.hasHit = False
        else:
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

def dealerStrategy(player,deck,highestCards):
    while(totals(player) < highestCards):
        player.cards.append(deck.flipCard())
        player.hasHit = True
        if(totals(player) > 21):
            player.bust = True


def largestPlayer(players):
    winner  = player("temp")
    for i in range(len(players)):
       
        if(players[i].bust != True):
            total = totals(players[i].cards)    

            if(total > totals(winner.cards)):
                winner = players[i]
            total = 0
    return winner


def run(player,deck,dealerFaceCard):
    while(not((player.hasHit==False) or (player.bust == True))):
        strategy(player,deck,dealerFaceCard)
        

