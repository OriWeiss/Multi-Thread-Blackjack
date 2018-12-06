class player():
	def __init__(self,name):
		self.bust = False
		self.cards = []
		self.hasHit = True
		self.name = name
	def getCards(self):
		return self.cards
	def resetCards(self):
		self.cards=[]

