import csv

import log
from ambigqa import dev_light_and_train_light
from cmdc import cmdc


def save_to_dataset(new_data_for_dataset):
    """
    Save new data to dataset
    """

    log.part_log(f"Initiate saving {len(new_data_for_dataset)} number(s) of dialogues... ")
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

    new_data_for_dataset = []

    file_addresses = {}
    file_addresses["ambigqa"] = [
        "./Training_data/dev_light.json",
        "./Training_data/train_light.json"
    ]
    file_addresses["cmdc"] = [
        "./Training_data/movie_lines.txt",
    ]

    # ? ambigqa
    for file_address in file_addresses["ambigqa"]:
        new_data_for_dataset.extend(dev_light_and_train_light(file_address))


    # ? C.M.D.C
    for file_address in file_addresses["cmdc"]:
        new_data_for_dataset.extend(cmdc(file_address))

    # ? Save data to dataset
    save_to_dataset(new_data_for_dataset)


if __name__ == "__main__":
    main()
