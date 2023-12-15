import random

#activity 1 / 2
def make_card(rank, suit):
    if rank < 2 or rank > 14:
        return "Invalid Rank"
    if suit != "Clubs" and suit != "Diamonds" and suit != "Hearts" and suit != "Spades":
        return "Invalid Suit"
    rank = str(rank)
    if rank == "11":
        face = "Jack"
        name = face + " of " + suit
    elif rank == "12":
        face="Queen"
        name = face + " of " + suit
    elif rank == "13":
        face="King"
        name = face + " of " + suit
    elif rank == "14":
        face="Ace"
        name = face + " of " + suit
    else:
        name = rank + " of " + suit

    if suit == "Hearts" or suit == "Diamonds":
        if len(rank) == 1:
            short = " " + rank + suit[0]
            shorthand = "\033[31m" + short + "\033[37m"
        elif rank == "10":
            short = rank + suit[0]
            shorthand = "\033[31m" + short + "\033[37m"
        elif int(rank) > 10:
            short = " " + face[0] + suit[0]
            shorthand = "\033[31m" + short + "\033[37m"
    elif suit == "Clubs" or suit == "Spades":
        if len(rank) == 1:
            short = " " + rank + suit[0]
            shorthand = "\033[34m" + short + "\033[37m"
        elif rank == "10":
            short = rank + suit[0]
            shorthand = "\033[34m" + short + "\033[37m"
        elif int(rank) > 10:
            short = " " + face[0] + suit[0]
            shorthand = "\033[34m" + short + "\033[37m"
    return rank, suit, name, shorthand

def make_deck():
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    deck = []
    i = 0
    while i < 52:
        for suit in suits:
            for rank in range(2, 15):
                deck.append(make_card(rank, suit))
                i +=1
    # print(len(deck))
    return deck

def shuffle(deck):
    length = len(deck)
    i =0
    while i >= 0 and i < length-1:
        j = random.randrange(i, length)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        i +=1
    return deck

def draw(deck, hand):
    if len(deck) > 0:
        card = deck.pop()
        hand.append(card)
        return card
    else:
        return None

def deal_one_hand(deck, num):
    hand = []
    for i in range(num):
        hand.append(draw(deck,[hand]))
    return hand

#def main():
#     # card = make_card(8, "Clubs")
#     # card1 = make_card(12, "Diamonds")
#     # card2 = make_card(3, "Clubs")
#     # card3 = make_card(6, "Spades")
#     # card4 = make_card(10, "Clubs")
#     # card5 = make_card(13, "Clubs")
#     # card6 = make_card(9, "Hearts")
#     # print(card[3], card1[3], card2[3],card3[3],card4[3],card5[3],card6[3])
# print(make_deck())

#     #activity 4
#     a_list = [i for i in range(1, 53)]
#     # print(a_list)
#     # random.seed(3)
#     # print(shuffle(a_list))
    
#     print(deal_one_hands(a_list, 10))


# main()