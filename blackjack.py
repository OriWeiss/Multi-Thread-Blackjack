#Author: Ori Weiss, Connor Stephens
#Date 12/5/18

#strategy: imagine a blackjack game where the dealer and players all play simultaneuously. Each player is its own thread as well as the dealer
#TODO finish up the logic for the player strategies as well as calculate the winner

#code for the threads and game process

from deck import *
from tools import *
#from tools import MyThread






#initiate list of players
player =[(player("Dealer")),(player("Jimmy")),(player("Bobby"))]
deck = Deck() 
jobs = []



#Take user input
#run a for loop for the amount of times to play
#after each game,reset the cards

#handout cards to each player
for i in range(len(player)):
	player[i].cards.append(deck.flipCard()) #same as hitting
	player[i].cards.append(deck.flipCard())

dealerFaceCard = player[0].cards[0]
print("Dealer face card is a " , dealerFaceCard)



for i in range(len(player)):
	jobs.append(threading.Thread(target = run(player[i],deck,dealerFaceCard)))
	jobs[i].start()
	

#join threads
for j in range(len(jobs)):
	jobs[j].join()



#calculate who the winner is
calculateWinner(player)

