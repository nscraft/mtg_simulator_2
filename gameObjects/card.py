class Card:
    """
    cards have the following attributes:
    card_name: str
    color_identity: str (W, U, B, R, G)
    mana_cost: str (2W, 1UB, XR, etc.)
    cmc: int (converted mana cost)
    card_super_types: list[str] (creature, sorcery, instant, enchantment, artifact, land)
    card_sub_types: str (human, elf, goblin, etc.)
    card_text: str
    effects: [] (list of effects inferred from card text and corresponding to the card's abilities)
    card_power: int | None
    card_toughness: int | None
    card_loyalty: int | None
    card_score: int (A score based on the card's utility in the game)
    """

    def __init__(self, card_name: str, color_identity: str, mana_cost: str, cmc: int, card_super_types: list[str],
                 card_sub_types: list[str] | None, card_text: str, effects: list | None, card_power: int | None,
                 card_toughness: int | None, card_loyalty: int | None, card_score: int | 0):
        self.card_name = card_name
        self.color_identity = color_identity
        self.mana_cost = mana_cost
        self.cmc = cmc
        self.card_super_types = card_super_types
        self.card_sub_types = card_sub_types
        self.card_text = card_text
        self.effects = effects
        self.card_power = card_power
        self.card_toughness = card_toughness
        self.card_loyalty = card_loyalty
        self.card_score = card_score
