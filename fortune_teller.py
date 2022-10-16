#%%

# Card Parameters
suits = ['swords', 'cups', 'coins', 'wands', 'major']
suits_map = {
    's': 'swords',
    'u': 'cups',
    'c': 'coins',
    'w': 'wands',
    'm': 'major'
}
minor_suits = suits[:4]
minor_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
minor_values = [str(value) for value in minor_values]
major_values = [str(value) for value in range(0, 22)]


class Card:

    def __init__(self, suit, value):

        # Check if suit valid
        if suit in suits:
            self.suit = suit
        else:
            raise ValueError(
                f'ERROR: {suit} is not an acceptable suit for a card')

        # Check if value valid
        if (suit == 'major') & (value in major_values):
            self.value = value
        elif value in minor_values:
            self.value = value
        else:
            raise ValueError(
                f'ERROR: {value} is not an acceptable value for a card')

    def __repr__(self):
        return f'{self.value} {self.suit}'

    def legal(self, card):
        '''To legally play the card you need the have the same suit and an adjacent value'''
        if self.suit == card.suit:
            if card_value_index(self) + 1 == card_value_index(card):
                return True

            elif card_value_index(self) - 1 == card_value_index(card):
                return True
            else:
                return False
        else:
            return False


class Board:

    def __init__(self):
        self.columns = [[] for column in range(11)]
        self.foundations = {
            'majors_low': None,
            'majors_high': None,
            'swords': swords[0],
            'cups': cups[0],
            'coins': coins[0],
            'wands': wands[0]
        }


def parse_column(column):
    column = reversed(column.split())
    parsed_column = []
    for card in column:

        # everything but the last character is the value
        value = str(card[:-1]).upper()
        suit = str(card[-1]).lower()
        # the last character is the suit
        try:
            suit = suits_map[suit]
        except KeyError:
            print(f'ERROR: {suit} is not a valid suit: {suits_map}')
            return None

        try:
            card = Card(suit=suit, value=value)
        except ValueError as e:
            print(e)
            return None

        parsed_column.append(card)

    return parsed_column


def card_value_index(card):
    if card.suit in minor_suits:
        return minor_values.index(card.value)

    else:
        return major_values.index(card.value)


majors = [Card(suit='major', value=value) for value in major_values]
swords = [Card(suit='swords', value=value) for value in minor_values]
cups = [Card(suit='cups', value=value) for value in minor_values]
coins = [Card(suit='coins', value=value) for value in minor_values]
wands = [Card(suit='wands', value=value) for value in minor_values]

# All the cards in the deck
deck = swords[1:] + cups[1:] + coins[1:] + wands[1:] + majors


def cli():
    board = Board()
    print('''>>> For this cli enter the card by typing the value then the suit
next to eachother. For example 2 of cups is represented as \'2u\' and King
of swords as \'ks\'.''')
    for board_column_num, board_column in enumerate(board.columns):

        column_parsed_flag = False
        while column_parsed_flag is False:
            column = input(
                '''>>> Please enter the column from top to bottom with a single 
space between each card:''')

            # TODO: if the user gets an error the cli with ask to confirm a blank column
            column_parsed = parse_column(column)
            column_confirm = input(
                f'''>>> Is this column correct?: {column_parsed}
>>>You can reenter the column if it's incorrect [y/N]''').lower()

            # Confirmed
            if column_confirm == 'y':
                column_parsed_flag = True
                board.columns[board_column_num] = column_parsed
                print(board.columns)

            # Not confirmed, reenter the column
            else:
                column_parsed_flag = False

    print(
        '''The board is now complete and we'll start calculating the first solution'''
    )


# %%
if __name__ == '__main__':
    cli()

# %%
