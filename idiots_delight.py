#activity 2
import cards
import random

def deal_hand():
    # random.seed(74) <----- one of the winning seeds
    hand = []
    deck = cards.make_deck()
    shuffled = cards.shuffle(deck)
    card_group = cards.deal_one_hand(shuffled, 4)
    for card in card_group:
        hand.append(card)
    return shuffled, hand
    # TESTS DONT WORK WHEN SHUFFLED

def discard(hand, num):
    length = len(hand)
    if num == 4:
        for i in range(length-1, length-5,-1):
            hand.pop(i)
    elif num == 2:
        for i in range(length-2, length-4,-1):
            hand.pop(i)
    return hand

def play_round(deck, hand):
    if len(hand) < 4:
        hand = enough_cards(deck, hand)
    print("Hand at start of round (including fill if needed):\n", shorthand(hand))

    discarded = True
    while len(hand) >= 4 and discarded == True:
        length = len(hand)
        discarded = False
        one = hand[0]
        other = hand[length-4]
        last = hand[length-1]
        second = hand[length-3]
        third = hand[length-2]
        if one[0] == last[0] or other[0] == last[0]:
            hand = discard(hand, 4)
            print("Ranks of outer pair of last 4 match - discarding last 4 cards\n", shorthand(hand))
            length = len(hand)
            discarded = True
        elif second[1] == third[1]:
            hand = discard(hand, 2)
            print("Suits of inner pair of last 4 match - discarding inner pair\n", shorthand(hand))
            length = len(hand)
            discarded = True

    if len(deck) > 0:
        # print(hand)
        card = (cards.draw(deck, hand))
        print("Hand at the end of round:\n", shorthand(hand))
    return deck, hand

def shorthand(hand):
    colored = ""
    for card in hand:
        colored += (str(card[3]) + " ")
    return colored

def enough_cards(deck, hand):
    length = len(hand)
    while length < 4:
        card = (cards.draw(deck, hand))
        length+=1
    return hand
    
def main():
    deck, hand= deal_hand()
    length = len(deck)
    i = 0
    while length > 0:
        i +=1
        print("\nRound:", i)
        play_round(deck, hand)
        length = len(deck)
    
    length_hand = len(hand)
    if length == 0:
        if length_hand == 0:
            print("\nGame is over! You have 0 cards left in your hand.")
            print("You are a winner!")
        elif length_hand > 0:
            print("\nGame is over! You have", length_hand, "cards left in your hand.")
            print("Better luck next time!")



    """
    winning seeds up to 10,000 seeds:
    [74, 145, 256, 1383, 1455, 1686, 1818, 2015, 2241, 2451, 3364, 3463, 3465, 4045, 4235, 4372, 4609, 4770, 4951, 5220, 6195, 6818, 7025, 7327, 7509, 7672, 8029, 8189, 8701]
    """
if __name__ == "__main__":
    main()