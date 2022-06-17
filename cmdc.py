"""
Functions for processing 'Cornell Movie-Dialog Corpus' datasets
"""

import codecs
import json

import log


def next_training_data(file_address):
    """
    returning next training data in original file
    """

    with codecs.open(file_address, 'r', encoding='utf-8', errors='replace') as file:
        while True:
            row = file.readline()
            if not row:
                return False
            yield row


def remove_unneeded_char(sentence):
    """
    Remove unnecessary characters from sentence
    """

    unneeded_characters = ['+', '$', '"', '<u>']
    new_sentence = sentence
    for char in sentence:
        if char in unneeded_characters:
            new_sentence = new_sentence.replace(char, "")
    return new_sentence.strip()


def movie_lines(file_address):
    """
    Read data and save them in `dataset` file in needed format
    Files: ./Training_data/movie_lines.txt
    (File is reversed)
    """

    new_data_for_dataset = []
    file_address_size = len(open(file_address).readlines())

    first_person = ""
    for index, data in enumerate(next_training_data(file_address)):
        try:
            # * Log
            if (index+1) % 1000 == 1:
                log.part_log(f"Rows {index+1} - {index+1000 if (file_address_size > (index+1000)) else file_address_size}... ")

            if index % 2 == 0:
                first_person = remove_unneeded_char(' '.join(data.split()[8:]))
            else:
                new_data_for_dataset.append([first_person, remove_unneeded_char(' '.join(data.split()[8:]))])

            # * Log
            if ((index+1) % 1000 == 0) or (file_address_size == (index+1)):
                log.part_log('Done', end=True)
        except Exception as error:
            log.error_log(f'In row #{index+1} we have error')
            log.error_logfile(f"Running 'movie_lines ({file_address}) - Row #{index}'", str(error))

    print()
    log.log(f"Got {len(new_data_for_dataset)} dialogues from cmdc.{file_address.split('/')[-1].split('.')[0]}")
    print()

    return new_data_for_dataset
