import csv

import log
from ambigqa import dev_light_and_train_light_and_train, nqopen_dev
from cmdc import movie_lines
from udc import dialogueText


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

    # ? ambigqa
    new_data_for_dataset.extend(dev_light_and_train_light_and_train("./Training_data/dev_light.json"))
    new_data_for_dataset.extend(dev_light_and_train_light_and_train("./Training_data/train_light.json"))
    new_data_for_dataset.extend(dev_light_and_train_light_and_train("./Training_data/train.json"))
    new_data_for_dataset.extend(nqopen_dev("./Training_data/nqopen-dev.json"))
    new_data_for_dataset.extend(nqopen_dev("./Training_data/nqopen-test.json"))
    new_data_for_dataset.extend(nqopen_dev("./Training_data/nqopen-train.json"))


    # ? C.M.D.C
    new_data_for_dataset.extend(movie_lines("./Training_data/movie_lines.txt"))


    # ? Ubuntu-dialogue-corpus
    new_data_for_dataset.extend(dialogueText("./Training_data/dialogueText.csv"))


    # ? Save data to dataset
    save_to_dataset(new_data_for_dataset)


if __name__ == "__main__":
    main()
