import os
from get_data import get_data
from saveData.observer import saveDataObserver
from UI import consol_ui


class MTGSim:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MTGSim, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensure __init__ is only called once
            self.data = {}
            self.observers = []
            self.initialized = True
            print("~~Welcome to MTG_Sim!~~")

    def set_data(self):
        print("Updating data...")
        # find all json files in the data directory
        data_files = [file for file in os.listdir('data') if file.endswith('.json')]
        if not data_files:
            print("No data files found.")
        else:
            # for each file, update self.configuration with the contents of the file
            for file in data_files:
                self.data.update(get_data(file.split('.')[0]))

    def _add_observer(self):
        observer = saveDataObserver(self)
        self.observers.append(observer)

    def _start_ui(self):
        ui = consol_ui.ConsoleUI(self)
        ui.main_console_menu()

    def run(self):
        self.set_data()
        self._add_observer()
        self._start_ui()


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.run()
