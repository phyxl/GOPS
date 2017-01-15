#!python
from random import shuffle
#begin with welcome message and initialize arrays

class Player(object):
    def __init__(self, name, isai):
        self.name = name
        self.isAI = isai
    score = 0
    hand = [0,0,0,0,0,0,0,0,0,0,0,0,0] #each index is a card, 1 through 13
    name = ''
    isAI = False
    def makeBid(self, card):
        if card > 12:
            return -1
        #check if card is available
        if self.hand[card] == 0:
            #the card is available
            #return the bid value
            self.hand[card] += 1
            return card + 1
            
        else:
            #this is an invalid move
            return -1
    def winCard(self, scoreCard):
        self.score += scoreCard
    
def shuffleSuit():
    #generate a list of numbers from 0 to 12
    suit = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    shuffle(suit)
    return suit
    
#just 2 players for now
#whosTurn = 0
NUMPLAYERS = 2

Game = []
for num in range(0,NUMPLAYERS):
    Game.append(Player('Player ' + str(num + 1), False))
Moves = []
for num in range(0, NUMPLAYERS):
    Moves.append(-1)
#there are 13 turns
scoreCards = shuffleSuit()


for card in scoreCards:
    playerNum = 0
    for player in Game:
        print(player.name)
        print(' current available score card is ' + str(card) + '\n')
        print('your avalable cards are: ')
        cardNum = 0
        for hcard in player.hand:
            if hcard == 0:
                print(cardNum + 1)
            cardNum += 1
        move = input('select a card: ') - 1 #for simplicity, haha
        while player.makeBid(move) == -1:
            print('bad selection')
            move = input('select a card: ') #for simplicity, haha
        #should have a valid move now
        Moves[playerNum] = move
        playerNum += 1
    print(max(Moves))
    Game[Moves.index(max(Moves))].winCard(card)
for player in Game:
    print(player.name + ' with a score of ' + str(player.score))
exit()