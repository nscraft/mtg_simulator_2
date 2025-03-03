class Card:
    """
    cards have the following attributes:
    deck_slot: int | None
    card_name: str
    color_identity: str (W, U, B, R, G)
    mana_cost: str (2W, 1UU, 3BB, etc.)
    cmc: int (converted mana cost)
    card_super_types: str (creature, sorcery, instant, enchantment, artifact, land)
    card_sub_types: str (human, elf, goblin, etc.)
    card_text: str
    card_power: int | None
    card_toughness: int | None
    card_loyalty: int | None
    card_score: int (A score based on the card's utility in the game)
    """
    def __init__(self, deck_slot, card_name, color_identity, mana_cost, cmc, card_super_types, card_sub_types, card_text,
                 card_power, card_toughness, card_loyalty, card_score):
        self.deck_slot = deck_slot
        self.card_name = card_name
        self.color_identity = color_identity
        self.mana_cost = mana_cost
        self.cmc = cmc
        self.card_super_types = card_super_types
        self.card_sub_types = card_sub_types
        self.card_text = card_text
        self.card_power = card_power
        self.card_toughness = card_toughness
        self.card_loyalty = card_loyalty
        self.card_score = card_score


