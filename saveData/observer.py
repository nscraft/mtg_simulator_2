import get_data


class saveDataObserver:
    """
    This class is an observer concerned with changes to data files.
    """

    def __init__(self, singleton_mtg_sim):
        self.singleton_mtg_sim = singleton_mtg_sim

    def notify(self, save_dat_file: str):
        """
        This method will be called by the subject when the state of the subject changes
        """
        data_files_of_concern = ['players.json',
                                 'decks.json',
                                 'cards.json',
                                 ]
        assert save_dat_file in data_files_of_concern, "Invalid data file."
        print(f"Observer Notified: Data file {save_dat_file} has been updated.")
        self.get_state()

    def get_state(self):
        self.singleton_mtg_sim.set_data()
