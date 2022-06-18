"""
Functions for processing 'ambigqa' datasets
"""

import json

import log


def next_training_data(file_address):
    """
    returning next training data in original file
    """

    with open(file_address, "r", encoding='utf-8-sig') as file:
        while True:
            element = file.readline()
            if not element:
                return False
            yield json.loads(element)


def dev_light_and_train_light(file_address):
    """
    Read data and save them in `dataset` file in needed format
    Files: ./Training_data/dev_light.json
                          /train_light.json
    """

    new_data_for_dataset = []
    for data in next_training_data(file_address):
        for index, datum in enumerate(data):
            try:
                # * Log
                if (index+1) % 100 == 1:
                    log.part_log(f"Data {index+1} - {index+100 if (len(data) > (index+100)) else len(data)}... ")

                for item in datum['annotations']:
                    if not 'answer' in item:
                        for pair in item['qaPairs']:
                            answer = ""
                            for ans in pair['answer']:
                                if '|' in pair['question']:
                                    question = pair['question'].split('|')[0]
                                else:
                                    question = pair['question']
                                answer += (ans + " - ")
                            answer = answer[:-3]
                            new_data_for_dataset.append([question, answer])
                    else:
                        if '|' in datum['question']:
                            question = datum['question'].split('|')[0]
                        else:
                            question = datum['question']

                        for answer in item['answer']:
                            new_data_for_dataset.append([question, answer])

                # * Log
                if ((index+1) % 100 == 0) or (len(data) == (index+1)):
                    log.part_log('Done', end=True)
            except Exception as error:
                log.error_log(f'In datum #{index+1} we have error')
                log.error_logfile(f"Running 'dev_light_and_train_light ({file_address})' \
                    - Datum #{index}'", str(error))

    print()
    log.log(f"Got {len(new_data_for_dataset)} Q&As from ambigqa.{file_address.split('/')[-1].split('.')[0]}")
    print()

    return new_data_for_dataset


def nqopen_dev(file_address):
    """
    Read data and save them in `dataset` file in needed format
    Files: ./Training_data/nqopen-dev.json
                          /nqopen-test.json
    """

    new_data_for_dataset = []
    for data in next_training_data(file_address):
        for index, datum in enumerate(data):
            try:
                # * Log
                if (index+1) % 100 == 1:
                    log.part_log(f"Data {index+1} - {index+100 if (len(data) > (index+100)) else len(data)}... ")

                question = datum["question"]
                answer = ""
                for ans in datum["answer"]:
                    answer += (ans + " - ")
                answer = answer[:-3]

                new_data_for_dataset.append([question, answer])
                # * Log
                if ((index+1) % 100 == 0) or (len(data) == (index+1)):
                    log.part_log('Done', end=True)
            except Exception as error:
                log.error_log(f'In datum #{index+1} we have error')
                log.error_logfile(f"Running 'nqopen_dev ({file_address})' \
                    - Datum #{index}'", str(error))

    print()
    log.log(f"Got {len(new_data_for_dataset)} Q&As from ambigqa.{file_address.split('/')[-1].split('.')[0]}")
    print()

    return new_data_for_dataset
