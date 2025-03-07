import json


class WriteDeck:
    def __init__(self, singleton_mtg_sim):
        self.data = singleton_mtg_sim.data
        self.observers = singleton_mtg_sim.observers

    def add_deck(self, deck_name: str, kind: str, cards: list[str], commander: str | None = None):
        new_deck = {
            'name': deck_name,
            'kind': kind,
            'cards': cards,
            'commander': commander
        }
        self.data['decks'].append(new_deck)
        deck_file_content = {
            'decks': self.data['decks']
        }
        with open('data/decks.json', 'w') as f:
            json.dump(deck_file_content, f, indent=4)
        for each in self.observers:
            each.notify('decks.json')

    def remove_deck(self, deck_name):
        for each in self.observers:
            each.notify('decks.json')
        pass

    def update_deck(self, deck_name, *args):
        for each in self.observers:
            each.notify('decks.json')
        pass
