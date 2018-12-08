#Author: Ori Weiss, Connor Stephens
#Date 12/5/18

#strategy: imagine a blackjack game where the dealer and players all play simultaneuously. Each player is its own thread as well as the dealer
#TODO finish up the logic for the player strategies as well as calculate the winner

#code for the threads and game process

from deck import *
from tools import *
#from tools import MyThread






#initiate list of players
players =[(player("Jimmy")), (player("Bobby"))]
dealer = player("Dealer")
deck = Deck() 

numOfPlayers = input("How many players should there be? (in addition to the default 2)")
for i in range(int(numOfPlayers)):
	playerName = input("Name of player: ")
	players.append(player(str(playerName)))



#Take user input
rounds = input("How many rounds should we play?: ")
#run a for loop for the amount of times to play
for z in range(int(rounds)):

	jobs = []
#handout cards to each player
	for i in range(len(players)):
		players[i].cards.append(deck.flipCard()) #same as hitting
		players[i].cards.append(deck.flipCard())
	
	dealer.cards.append(deck.flipCard())
	dealer.cards.append(deck.flipCard())
	
	dealerFaceCard =dealer.cards[0]
	print("Dealer face card is a " , dealerFaceCard)



	for i in range(len(players)):
		jobs.append(threading.Thread(target = run(players[i],deck,dealerFaceCard)))
		jobs[i].start()
	

#join threads
	for j in range(len(jobs)):
		jobs[j].join()

	dealerThread = threading.Thread(target = dealerStrategy(dealer,deck,totals(largestPlayer(players).cards)))
	dealerThread.start()
	dealerThread.join()


#calculate who the winner is
	winner = calculateWinner(players,dealer)
	print("The winner is " , winner.name,"\n")

#after each game,reset the cards
	deck.resetDeck()
	#reset all player carc
	for i in range(len(players)):
		players[i].resetCards()
		players[i].hasHit = True
		players[i].bust = False
	
	dealer.resetCards()
