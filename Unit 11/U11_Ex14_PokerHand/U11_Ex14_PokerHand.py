# U11_Ex14_PokerHand.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 7 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Uses Deck and Card classes to "deal" a five-card hand of cards to a Graphwin
#
# Algorithm (pseudocode)
#   main():
#       create GraphWin and set coordinates
#       create Deck object, shuffle, and cut
#       deal five cards from top of deck (every other card, like a real hand with two players)
#       draw each card to window, overlapping (because of their large size)
#       wait for mouse click to close window

from Chapter11.U11_Ex14_PokerHand.Card import *


class PokerHand:
    def __init__(self):
        self.hand = []
        self.xHigh = ''
        self.isPair = False
        self.isTwoPair = False
        self.isThreeOfAKind = False
        self.isStraight = False
        self.isFlush = False
        self.isFullHouse = False
        self.isFourOfAKind = False
        self.isStraightFlush = False
        self.isRoyalFlush = False
        self.theHand = ''

    def add_card(self, card):
        self.hand.append(card)

    def update(self):
        self._x_high()
        self._is_pair()
        self._is_two_pair()
        self._is_three_of_a_kind()
        self._is_straight()
        self._is_flush()
        self._is_full_house()
        self._is_four_of_a_kind()
        self._is_straight_flush()
        self._is_royal_flush()
        self.the_hand()

    def the_hand(self):
        if self.isRoyalFlush:
            self.theHand = 'Royal Flush'
        elif self.isStraightFlush:
            self.theHand = 'Straight Flush, {} high'.format(self.xHigh)
        elif self. isFourOfAKind:
            self.theHand = 'Four of a Kind, {} high'.format(self.xHigh)
        elif self.isFullHouse:
            self.theHand = 'Full House, {} high'.format(self.xHigh)
        elif self.isFlush:
            self.theHand = 'Flush, {} high'.format(self.xHigh)
        elif self.isStraight:
            self.theHand = 'Straight, {} high'.format(self.xHigh)
        elif self.isThreeOfAKind:
            self.theHand = 'Three of a Kind, {} high'.format(self.xHigh)
        elif self.isTwoPair:
            self.theHand = 'Two Pair, {} high'.format(self.xHigh)
        elif self.isPair:
            self.theHand = 'Pair, {} high'.format(self.xHigh)
        else:
            self.theHand = '{} high'.format(self.xHigh)

    def sort(self, keyFunc):
        self.hand.sort(key=eval(keyFunc))

    def _is_flush(self):
        _suit = self.hand[0].getSuit()
        self.isFlush = all(card.getSuit() == _suit for card in self.hand)

    def _is_straight(self):
        self.hand.sort(key=Card.getRank)
        _isStraight = True
        if self.hand[-1].getRank() == 14 and self.hand[0].getRank() == 2:
            _previousRank = 1
            for card in self.hand[:-1]:
                if not card.getRank() == _previousRank + 1:
                    _isStraight = False
                    break
                _previousRank = card.getRank()
        else:
            _previousRank = self.hand[0].getRank()
            for card in self.hand[1:]:
                if not card.getRank() == _previousRank + 1:
                    _isStraight = False
                    break
                _previousRank = card.getRank()
        self.isStraight = _isStraight

    def _is_straight_flush(self):
        self.isStraightFlush = self.isStraight and self.isFlush

    def _is_royal_flush(self):
        self.isRoyalFlush = self.isFlush and self.isStraight and self.hand[0].getRank() == 10

    def _is_four_of_a_kind(self):
        self.isFourOfAKind = self._in_a_row(4, 0) or self._in_a_row(4, 1)

    def _is_full_house(self):
        self.isFullHouse = self._in_a_row(3, 0) and self._in_a_row(2, 3) or \
                           self._in_a_row(2, 0) and self._in_a_row(3, 2)

    def _is_three_of_a_kind(self):
        self.isThreeOfAKind = self._in_a_row(3, 0) or \
                              self._in_a_row(3, 1) or \
                              self._in_a_row(3, 2)

    def _is_two_pair(self):
        self.isTwoPair = self._in_a_row(2, 0) and self._in_a_row(2, 2) or \
                         self._in_a_row(2, 0) and self._in_a_row(2, 3) or \
                         self._in_a_row(2, 1) and self._in_a_row(2, 3)

    def _is_pair(self):
        self.isPair = self._in_a_row(2, 0) or \
                      self._in_a_row(2, 1) or \
                      self._in_a_row(2, 2) or \
                      self._in_a_row(2, 3)

    def _in_a_row(self, num, start):
        i = start + 1
        while i < start + num:
            if not self.hand[i].getRank() == self.hand[start].getRank():
                return False
            i += 1
        return True

    def _x_high(self):
        self.xHigh = self.hand[-1].getRankName()


def main():
    win = GraphWin("Five Cards", 1200, 800)
    win.setCoords(0, 0, 10, 10)
    deck = Deck()
    deck.shuffle()
    deck.cut()
    i = 0
    pokerHand = PokerHand()

    while i < 5:
        card = deck.getDeck()[i*2]
        pokerHand.add_card(card)
        i += 1

    pokerHand.sort("Card.getSuit")
    pokerHand.sort("Card.getRank")


    # r = 10
    i = 0
    for card in pokerHand.hand:
        # card.setSuit(0)
        # card.setRank(r)
        # r += 1
        card.draw(win, Point(i + 3, 5))
        i += 1

    pokerHand.update()
    print(pokerHand.theHand)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
