import random
from socket import socket

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

input("Do you and to play a game of Blackjack? Type 'y' or 'n': ")
def drawCard():
    return  random.choice(cards)

def calculateScore(hand):
    score= sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score= sum(hand)
    return score

playerHand= [drawCard(), drawCard()]
dealerHand= [drawCard(), drawCard()]

print(f"Your cards: {playerHand}, current score: {calculateScore(playerHand)}")
print(f"Dealer's first card: {dealerHand[0]}")

while calculateScore(playerHand) < 21:
    action = input("Type 'hit' to draw another card, or 'stand' to pass: ")
    if action == "hit":
        playerHand.append(drawCard())
        print(f"Your cards: {playerHand}, current score: {calculateScore(playerHand)}")
    else:
        break

while calculateScore(dealerHand) < 17:
    dealerHand.append(drawCard())

playerScore= calculateScore(playerHand)
dealerSocre= calculateScore(dealerHand)

print(f"Your final hand: {playerHand}, final score: {playerScore}")
print(f"Dealer's final hand: {dealerHand}, final score: {dealerSocre}")

if playerScore > 21:
    print("You went over. You lose!")
elif dealerSocre > 21 or playerScore > dealerSocre:
    print("You win!")
elif playerScore < dealerSocre:
    print("Dealer wins!")
else:
    print("It's a draw!")