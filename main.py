import csv

import log
from ambigqa import dev_light_and_train_light


def save_to_dataset(new_data_for_dataset):
    """
    Save new data to dataset
    """

    log.part_log(f"Initiate saving {len(new_data_for_dataset)} number(s) of Q&As... ")
    try:
        with open("./dataset", "a") as dataset:
            writer = csv.writer(dataset)
            writer.writerows(new_data_for_dataset)

        log.part_log(f"Done", end=True)
        log.log(f"Total number of data in dataset: {len(open('./dataset').readlines())}")
    except Exception as error:
        log.error_log()
        log.error_logfile(f"Running save_to_dataset function", str(error))


def main():
    """
    Main function of program
    """

    # new_data_for_dataset = dev_light()
    # save_to_dataset(new_data_for_dataset)

    ambigqa_file_addresses = [
        "./Training_data/dev_light.json",
        "./Training_data/train_light.json"
    ]

    new_data_for_dataset = []
    for file_address in ambigqa_file_addresses:
        new_data_for_dataset.extend(dev_light_and_train_light(file_address))
    save_to_dataset(new_data_for_dataset)







if __name__ == "__main__":
    main()
