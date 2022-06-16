"""
Functions for processing 'ambigqa' datasets
"""

import json

from colorama import Fore, Style, init

import log

init(autoreset=True)


def next_training_data(original_file_address):
    """
    returning next training data in original file
    """

    with open(original_file_address, "r", encoding='utf-8-sig') as file:
        while True:
            element = file.readline()
            if not element:
                return False
            yield json.loads(element)


def dev_light():
    """
    Read data and save them in `dataset` file in needed format
    File: Training_data/dev_light.json
    """

    new_data_for_dataset = []
    original_file_address = "./Training_data/dev_light.json"
    for data in next_training_data(original_file_address):
        for index, datum in enumerate(data):
            try:
                # * Log
                if (index+1) % 100 == 1:
                    log.part_log(f"Data {index+1} - {index+100 if (len(data) > (index+100)) else len(data)}... ")

                for item in datum["annotations"]:
                    if not "answer" in item:
                        for pair in item['qaPairs']:
                            for answer in pair["answer"]:
                                if "|" in pair["question"]:
                                    question = pair["question"].split("|")[0]
                                else:
                                    question = pair["question"]
                                new_data_for_dataset.append([question, answer])
                    else:
                        if "|" in datum["question"]:
                            question = datum["question"].split("|")[0]
                        else:
                            question = datum["question"]

                        for answer in item["answer"]:
                            new_data_for_dataset.append([question, answer])

                # * Log
                if ((index+1) % 100 == 0) or (len(data) == (index+1)):
                    log.part_log("Done", end=True)
            except Exception as error:
                log.error_log(f"In datum #{index+1} we have error")
                log.error_logfile(f"Running 'dev_light - Datum #{index}'", str(error))

    print()
    log.log(f"Got {len(new_data_for_dataset)} Q&As from ambigqa.dev_light")
    print()

    return new_data_for_dataset