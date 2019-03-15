""" This is a poker deck, with bonus poker check
    Heart (0-12) Diamond (13-25) Club (26-38) Sword (39-51)
    00 ==> A(H)
"""
import random

G_TABLE_1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
G_TABLE_2 = ['(H)', '(D)', '(C)', '(S)']


class PokerCard:
    def __init__(self, value):
        self.true_value = value
        self.number = value % 13
        self.shade = value // 13

    def __repr__(self):
        return G_TABLE_1[self.number] + G_TABLE_2[self.shade]

    def get_shade(self):
        return self.shade

    def get_number(self):
        return self.number


class PokerDeck:
    def __init__(self, random_flag=True):
        self.deck = [0]*52
        self.index = 0
        self.drawn = []
        for i in range(52):
            self.deck[i] = i
        if random_flag:
            random.shuffle(self.deck)

    def __repr__(self):
        rslt = '['
        for item in self.deck:
            rslt += '%02d ' % item
        rslt += ']'
        return rslt

    def copy(self, deck_b):
        self.index = 0
        self.drawn = []
        for i in range(52):
            self.deck[i] = deck_b.deck[i]

    def add_drawn(self, value):
        self.drawn.append(value)

    def is_in_drawn(self, value):
        for item in self.drawn:
            if item == value:
                return True
        return False

    def draw_next(self):
        rslt = self.deck[self.index]
        self.index += 1
        if not self.is_in_drawn(rslt):
            return rslt
        else:
            return self.draw_next()

    def show_deck(self):
        rslt = ''
        for item in self.deck:
            x = PokerCard(item)
            rslt += '%s ' % x
        return rslt

    def show_drawn(self):
        rslt = ''
        for item in self.drawn:
            x = PokerCard(item)
            rslt += '%s ' % x
        return rslt


class BonusPoker:
    def __init__(self, payoff_table):
        """ define payoff table here """
        self.payoff = payoff_table
        self.counter = {
            'royal flush': 0,
            'straight flush': 0,
            '4 ace with 2,3,4': 0,
            '4 ace': 0,
            '4 2,3,4 with A,2,3,4': 0,
            '4 2,3,4': 0,
            '4 of a kind (5-k)': 0,
            'full house': 0,
            'flush': 0,
            'straight': 0,
            '3 of a kind': 0,
            '2 pairs': 0,
            'J+ pair': 0,
            'loss': 0,
        }
        self.hand = []      # list of PokerCard object
        self.award = 0
        self.last_hand = 'loss'
        self.last_award = 0

    def show_hand(self):
        rslt = '[ '
        for item in self.hand:
            rslt += '%s ' % item
        rslt += '] ==> (%s +%d = %d)' % (self.last_hand, self.last_award, self.award)
        return rslt

    def pay_hand(self):
        """ pay according to payoff table """
        outcome = 'loss'
        if self.is_flush():
            if self.is_straight():
                if self.is_AKQJT():
                    outcome = 'royal flush'
                else:
                    outcome = 'straight flush'
            else:
                outcome = 'flush'
        elif self.is_straight():
            outcome = 'straight'
        else:
            # count cards
            counter = [0] * 13
            for item in self.hand:
                counter[item.number] += 1
            pair = 0
            pair_card = -1
            three = False
            four = False
            bomb = 100
            deuce = 100
            for i in range(13):
                if counter[i] == 1:
                    deuce = i
                elif counter[i] == 2:
                    pair += 1
                    pair_card = i
                elif counter[i] == 3:
                    three = True
                elif counter[i] == 4:
                    four = True
                    bomb = i
            # 4 of a kind
            if four:
                # 4 ace
                if bomb == 0:
                    if deuce < 4:
                        outcome = '4 ace with 2,3,4'
                    else:
                        outcome = '4 ace'
                elif bomb < 4:
                    if deuce < 4:
                        outcome = '4 2,3,4 with A,2,3,4'
                    else:
                        outcome = '4 2,3,4'
                else:
                    outcome = '4 of a kind (5-k)'
            elif three:
                if pair == 1:
                    outcome = 'full house'
                else:
                    outcome = '3 of a kind'
            elif pair == 2:
                outcome = '2 pairs'
            elif pair == 1:
                if pair_card == 0 or pair_card > 9:
                    outcome = 'J+ pair'
        self.last_hand = outcome
        self.last_award = self.payoff[outcome]
        self.award += self.last_award
        self.counter[outcome] += 1
        return outcome

    def is_flush(self):
        shade = self.hand[0].get_shade()
        for item in self.hand:
            if not shade == item.get_shade():
                return False
        return True

    def is_AKQJT(self):
        checker = 0
        for item in self.hand:
            if item.number == 0:
                checker += 10000
            elif item.number == 12:
                checker += 1000
            elif item.number == 11:
                checker += 100
            elif item.number == 10:
                checker += 10
            elif item.number == 9:
                checker += 1
        return checker == 11111

    def is_straight(self):
        if self.is_AKQJT():
            return True
        number = [0, 0, 0, 0, 0]
        for i in range(5):
            number[i] = self.hand[i].number
        number.sort()
        walker = number[0]
        for item in number:
            if walker != item:
                return False
            walker += 1
        return True

    def print_chart(self, header):
        state = [
            'royal flush',
            'straight flush',
            '4 ace with 2,3,4',
            '4 ace',
            '4 2,3,4 with A,2,3,4',
            '4 2,3,4',
            '4 of a kind (5-k)',
            'full house',
            'flush',
            'straight',
            '3 of a kind',
            '2 pairs',
            'J+ pair',
            'loss',
        ]
        print('')
        print(header, 'Award: ', self.award)
        for item in state:
            print('%6d  (%s)' % (self.counter[item], item))

# end of file
