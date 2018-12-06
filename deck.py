#code for the deck of cards

from random import randint
class card():
	def __init__(self, number):
		self.number = number


class Deck():
	def __init__(self):
		self.deck = []
		self.amountOfCardsLeft = 52
		#add cards to deck
		for i in range(13):
			if(i+1 >= 10 ):
				self.deck.append(10)
			else:
				self.deck.append(i+1)
		for i in range(13):
			if(i+1 >= 10 ):
				self.deck.append(10)
			else:
				self.deck.append(i+1)
		for i in range(13):
			if(i+1 >= 10 ):
				self.deck.append(10)
			else:
				self.deck.append(i+1)
		for i in range(13):
			if(i+1 >= 10 ):
				self.deck.append(10)
			else:
				self.deck.append(i+1)
		#shuffle deck		
		for i in range(1000):
			randomRon = randint(0,51)
			randomRandy = randint(0,51)
			temp = self.deck[randomRon] 
			self.deck[randomRon] = self.deck[randomRandy]
			self.deck[randomRandy] = temp

	def flipCard(self):
		randomCard = self.deck.pop() #pick a card from the back of the deck	
		self.amountOfCardsLeft = self.amountOfCardsLeft - 1
		return randomCard
	
	def resetDeck(self):
		self.deck = Deck().deck
		self.amountOfCardsLeft = 52

	def printDeck(self):
		for i in range(len(self.deck)):
			print ("Position: " ,i," number:",self.deck[i])



# deck = Deck()
# card = deck.flipCard()
# print (card)
# deck.printDeck()
#deck.resetDeck()
#deck.printDeck()"""