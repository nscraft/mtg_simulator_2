class Deck:
    def __init__(self, deck_name: str, kind: str, cards: list[str], commander: str | None = None):
        self.name = deck_name
        self.kind = kind  # 'commander' or 'standard'
        self.cards = cards  # list of card names
        self.num_cards = len(self.cards)
        assert self.num_cards > -1, 'Deck is empty'
        if kind == 'commander':
            assert commander is not None, 'Commander deck must have a commander'
            self.commander = commander
