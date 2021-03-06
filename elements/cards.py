from random import choice, shuffle

CARDS_NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
CARDS_SUITS = {'clovers': 5, 'diamonds': 4, 'hearts': 3, 'pikes': 6}
SUITS_COLORS = {'black': ['clovers', 'pikes'], 'red': ['diamonds', 'hearts']}


class Card:
    """
    Dependencies:
    - Encoding cp850, french cards suites are chr(3)-chr(6)
        To be able to print characters in Windows console:
            pip install win-unicode-console
    """
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def print(self):
        print('{}{}'.format(self.number, chr(CARDS_SUITS[self.suit])))

    def __str__(self):
        return '{} of {}'.format(self.number, self.suit)

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suite


class DeckOfCards:
    """
    French deck of cards is composed by 52 cards 
    """
    def __init__(self):
        self.deck_of_cards = []
        self.__create_deck_of_cards__()
        shuffle(self.deck_of_cards)

    def __create_deck_of_cards__(self):
        for suit in CARDS_SUITS.keys():
            for n in CARDS_NUMBERS:
                self.deck_of_cards.append(Card(n, suit))

    def print(self):
        for card in self.deck_of_cards:
            card.print()

    def __str__(self):
        return str([str(card) for card in self.deck_of_cards])

    def __len__(self):
        return len(self.deck_of_cards)

    def random_card(self):
        card = choice(self.deck_of_cards)
        self.deck_of_cards.remove(card)
        return card

    def next(self):
        while self.deck_of_cards:
            card = self.deck_of_cards.pop()
            yield card
        else:
            print('No cards left in the deck.')
            raise StopIteration
