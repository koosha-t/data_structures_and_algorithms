'''

Write a method to shuffle a list of numbers. 

'''


from random import randint

def shuffle(cards):
	if len(cards) == 1:
		return cards

	else:
		x = randint(0, len(cards) - 1)
		picked_card = cards[x]
		cards[x] =  cards[0]
		return [picked_card] + shuffle(cards[1:])



### Test:

def shuffle_cards(cards):
	while True:
		cards = shuffle(cards)
		yield cards



