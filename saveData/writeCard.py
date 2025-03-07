import json


class WriteCard:
    def __init__(self, singleton_mtg_sim):
        self.data = singleton_mtg_sim.data
        self.observers = singleton_mtg_sim.observers

    def add_card(self, card_name: str, color_identity: str, mana_cost: str, card_super_types: list[str],
                 card_sub_types: list[str] | None, card_text: str, effects: list | None, card_power: int | None,
                 card_toughness: int | None, card_loyalty: int | None, card_score: int | 0):
        new_card = {
            'card_name': card_name,
            'color_identity': color_identity,
            'mana_cost': mana_cost,
            # 'cmc' calculated at cast time
            'card_super_types': card_super_types,
            'card_sub_types': card_sub_types,
            'card_text': card_text,
            'effects': effects,
            'card_power': card_power,
            'card_toughness': card_toughness,
            'card_loyalty': card_loyalty,
            'card_score': card_score
        }
        self.data['card'].append(new_card)
        card_file_content = {
            'cards': self.data['cards']
        }
        with open('data/cards.json', 'w') as f:
            json.dump(card_file_content, f, indent=4)
        for each in self.observers:
            each.notify('cards.json')

    def remove_player(self, player_name):
        for each in self.observers:
            each.notify('cards.json')
        pass

    def update_player(self, player_name, *args):
        for each in self.observers:
            each.notify('cards.json')
        pass
