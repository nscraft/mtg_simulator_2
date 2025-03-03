class Orchestrate:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def run(self):
        self.logger.info("Orchestration started")
        self.logger.info("Orchestration completed")