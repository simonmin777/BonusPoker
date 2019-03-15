import PokerDeck
# this section is payoff table
PAYOFF_BONUS_POKER = {
    'royal flush': 800,
    'straight flush': 50,
    '4 ace with 2,3,4': 80,
    '4 ace': 80,
    '4 2,3,4 with A,2,3,4': 40,
    '4 2,3,4': 40,
    '4 of a kind (5-k)': 25,
    'full house': 7,
    'flush': 5,
    'straight': 4,
    '3 of a kind': 3,
    '2 pairs': 2,
    'J+ pair': 1,
    'loss': 0,
}
PAYOFF_DOUBLE_BONUS_POKER = {
    'royal flush': 800,
    'straight flush': 50,
    '4 ace with 2,3,4': 160,
    '4 ace': 160,
    '4 2,3,4 with A,2,3,4': 80,
    '4 2,3,4': 80,
    '4 of a kind (5-k)': 50,
    'full house': 9,
    'flush': 6,
    'straight': 5,
    '3 of a kind': 3,
    '2 pairs': 1,
    'J+ pair': 1,
    'loss': 0,
}
PAYOFF_DOUBLE_DOUBLE_BONUS_POKER = {
    'royal flush': 800,
    'straight flush': 50,
    '4 ace with 2,3,4': 400,
    '4 ace': 160,
    '4 2,3,4 with A,2,3,4': 160,
    '4 2,3,4': 80,
    '4 of a kind (5-k)': 50,
    'full house': 6,
    'flush': 5,
    'straight': 4,
    '3 of a kind': 3,
    '2 pairs': 1,
    'J+ pair': 1,
    'loss': 0,
}
PAYOFF_TRIPLE_BONUS_POKER = {
    'royal flush': 800,
    'straight flush': 50,
    '4 ace with 2,3,4': 800,
    '4 ace': 160,
    '4 2,3,4 with A,2,3,4': 400,
    '4 2,3,4': 80,
    '4 of a kind (5-k)': 50,
    'full house': 9,
    'flush': 6,
    'straight': 4,
    '3 of a kind': 2,
    '2 pairs': 1,
    'J+ pair': 1,
    'loss': 0,
}

# initialize 4 different bonus poker payoff
bonus = PokerDeck.BonusPoker(PAYOFF_BONUS_POKER)
bonus2 = PokerDeck.BonusPoker(PAYOFF_BONUS_POKER)
double = PokerDeck.BonusPoker(PAYOFF_DOUBLE_BONUS_POKER)
double2 = PokerDeck.BonusPoker(PAYOFF_DOUBLE_BONUS_POKER)
d_double = PokerDeck.BonusPoker(PAYOFF_DOUBLE_DOUBLE_BONUS_POKER)
d_double2 = PokerDeck.BonusPoker(PAYOFF_DOUBLE_DOUBLE_BONUS_POKER)
triple = PokerDeck.BonusPoker(PAYOFF_TRIPLE_BONUS_POKER)
triple2 = PokerDeck.BonusPoker(PAYOFF_TRIPLE_BONUS_POKER)


def set_hand(game, deck, hand_in, flag_print=False):
    my_deck = PokerDeck.PokerDeck(False)
    my_deck.copy(deck)
    game.hand = []
    for card in hand_in:
        game.hand.append(PokerDeck.PokerCard(card))
    for _ in game.hand:
        my_deck.add_drawn(_.true_value)
    # draw until 5 cards
    num = len(hand_in)
    while num < 5:
        num += 1
        game.hand.append(PokerDeck.PokerCard(my_deck.draw_next()))
    game.pay_hand()
    if flag_print:
        print(game.show_hand())


def run_loop():
    hand1 = [7, 20, 24, 11]
    hand2 = [11, 24]
    hand1_label = 'Hand 1 = '
    for item in hand1:
        hand1_label += str(PokerDeck.PokerCard(item)) + ' '
    print(hand1_label)
    hand2_label = 'Hand 2 = '
    for item in hand2:
        hand2_label += str(PokerDeck.PokerCard(item)) + ' '
    print(hand2_label)
    for i in range(1000):
        deck = PokerDeck.PokerDeck()
        set_hand(bonus, deck, hand1, False)
        set_hand(bonus2, deck, hand2, False)
        set_hand(double, deck, hand1, False)
        set_hand(double2, deck, hand2, False)
        set_hand(d_double, deck, hand1, False)
        set_hand(d_double2, deck, hand2, False)
    bonus.print_chart('Bonus Poker ' + hand1_label)
    bonus2.print_chart('Bonus Poker ' + hand2_label)
    double.print_chart('Double Bonus Poker ' + hand1_label)
    double2.print_chart('Double Bonus Poker ' + hand2_label)
    d_double.print_chart('Double Double Poker ' + hand1_label)
    d_double2.print_chart('Double Double Poker ' + hand2_label)


run_loop()
