from random import choice
from FrenchDeck import FrenchDeck
import collections

def main():
    french_deck = FrenchDeck()
    print(f"French Deck has {len(french_deck)} cards.")

    User = collections.namedtuple('User', ['name', 'age', 'email'])
    user = User('John Doe', 30, 'johndoe@test.com')

    print(f"User name: {user.name}")

    deck = choice(french_deck)
    print(deck)

    for card in french_deck:
        print(card)

if __name__ == "__main__":
    main()