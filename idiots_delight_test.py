import cards 
import idiots_delight

def test_deal_hand1():
    #setup
    expected = [('14', 'Spades', 'Ace of Spades', '\x1b[34m AS\x1b[37m'), ('13', 'Spades', 'King of Spades', '\x1b[34m KS\x1b[37m'), ('12', 'Spades', 'Queen of Spades', '\x1b[34m QS\x1b[37m'), ('11', 'Spades', 'Jack of Spades', '\x1b[34m JS\x1b[37m')]

    #invoke
    deck, hand = idiots_delight.deal_hand()
    actual = hand

    #analyze
    assert actual == expected

def test_discard_2():
    #setup
    deck, hand = idiots_delight.deal_hand()
    expected = [('14', 'Spades', 'Ace of Spades', '\x1b[34m AS\x1b[37m'), ('11', 'Spades', 'Jack of Spades', '\x1b[34m JS\x1b[37m')]

    #invoke
    actual = idiots_delight.discard(hand, 2)

    #analyze
    assert actual == expected

def test_discard_4():
    #setup
    deck, hand = idiots_delight.deal_hand()
    expected = []

    #invoke
    actual = idiots_delight.discard(hand, 4)

    #analyze
    assert actual == expected

def test_discard_5():
    #setup
    hand = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'), ('14', 'Spades', 'Ace of Spades', '\x1b[34m AS\x1b[37m'), ('13', 'Spades', 'King of Spades', '\x1b[34m KS\x1b[37m'), ('12', 'Spades', 'Queen of Spades', '\x1b[34m QS\x1b[37m'), ('11', 'Spades', 'Jack of Spades', '\x1b[34m JS\x1b[37m')]
    expected = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m')]

    #invoke
    actual = idiots_delight.discard(hand, 4)

    #analyze
    assert actual == expected

def test_play_round_less_than():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('9', 'Diamonds', '8 of Diamonds', '\x1b[34m 8D\x1b[37m'), ('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m')]
    expected = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('9', 'Diamonds', '8 of Diamonds', '\x1b[34m 8D\x1b[37m'), ('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m'), ('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m'), ('9', 'Spades', '9 of Spades', '\x1b[34m 9S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected

def test_play_round_exact():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('8', 'Diamonds', '8 of Diamonds', '\x1b[34m 8D\x1b[37m'), ('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m'), ('11', 'Spades', '11 of Spades', '\x1b[34m11S\x1b[37m')]
    expected = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('8', 'Diamonds', '8 of Diamonds', '\x1b[34m 8D\x1b[37m'), ('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m'), ('11', 'Spades', '11 of Spades', '\x1b[34m11S\x1b[37m'), ('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected

def test_play_round_discard_4():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('10', 'Spades', '10 of Spades', '\x1b[31m10S\x1b[37m'),('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'), ('10', 'Diamonds', '10 of Diamonds', '\x1b[34m10D\x1b[37m'), ('10', 'Clubs', '10 of Clubs', '\x1b[34m10C\x1b[37m')]
    expected = [('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected

def test_play_round_discard_5():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('14', 'Spades', 'Ace of Spades', '\x1b[34m AS\x1b[37m'),('10', 'Spades', '10 of Spades', '\x1b[31m10S\x1b[37m'),('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'), ('10', 'Diamonds', '10 of Diamonds', '\x1b[34m10D\x1b[37m'), ('10', 'Clubs', '10 of Clubs', '\x1b[34m10C\x1b[37m')]
    expected = [('14', 'Spades', 'Ace of Spades', '\x1b[34m AS\x1b[37m'),('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected

def test_play_round_discard_2():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('11', 'Spades', '11 of Spades', '\x1b[31m JS\x1b[37m'),('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'), ('10', 'Hearts', '10 of Hearts', '\x1b[31m10H\x1b[37m'), ('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m')]
    expected = [('11', 'Spades', '11 of Spades', '\x1b[31m JS\x1b[37m'),('7', 'Clubs', '7 of Clubs', '\x1b[34m 7C\x1b[37m'),('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected

def test_play_round_discard_2_of_5():
    #setup
    deck, hand = idiots_delight.deal_hand()
    hand = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('10', 'Diamonds', '10 of Diamonds', '\x1b[34m10D\x1b[37m'),('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m'), ('3', 'Spades', '3 of Spades', '\x1b[34m 3S\x1b[37m'), ('9', 'Clubs', '9 of Clubs', '\x1b[34m 9C\x1b[37m')]
    expected = [('2', 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m'),('10', 'Diamonds', '10 of Diamonds', '\x1b[34m10D\x1b[37m'), ('9', 'Clubs', '9 of Clubs', '\x1b[34m 9C\x1b[37m'), ('10', 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')]

    #invoke
    actual = idiots_delight.play_round(deck, hand)

    #analyze
    assert actual == expected
