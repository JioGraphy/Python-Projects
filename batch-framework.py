import os
import logging
import time

class BatchFramework:
    def __init__(self, input_dir, output_dir, log_file):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.log_file = log_file

    def setup(self):
        self.setup_logging()
        self.create_output_directory()

    def setup_logging(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def create_output_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def process(self):
        raise NotImplementedError("Subclasses must implement the 'process' method.")

    def run(self):
        try:
            self.setup()
            self.process()
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_directory = "input_data"
    output_directory = "output_data"
    log_file = "batch.log"

    class MyBatchProcess(BatchFramework):
        def process(self):
            logging.info("Batch process started.")
            # Your batch processing logic goes here.
            time.sleep(5)
            logging.info("Batch process completed.")

    batch = MyBatchProcess(input_directory, output_directory, log_file)
    batch.run()
