""" Printing logs with custom format """

from datetime import datetime

from colorama import Fore, Style, init

init(autoreset=True)
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


def log(log_text):
    """ Just print log_text """
    print(Fore.YELLOW + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S: "), end="")
    print(log_text)


def error_log(error_text=False):
    """ Printing errors with red color """
    print(Fore.MAGENTA + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S: "), end="")
    if error_text:
        print(Fore.RED + Style.BRIGHT + f"Error: {error_text}")
    else:
        print(Fore.RED + Style.BRIGHT + "Error")

def part_log(log_text, end = False, error = False):
    """ Printing logs which has two parts for printing in program """
    # if log_text == "Done":
    #     log_text = u'\u2714'
    # elif log_text == "Error":
    #     log_text = u'\u2717'

    if end is True:
        if error is True:
            print(Fore.RED + Style.BRIGHT + log_text)
        else:
            print(Fore.GREEN + Style.BRIGHT + log_text)
    else:
        print(Fore.YELLOW + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S: "), end="")
        print(log_text , end="")


def error_logfile(error_address, log_text):
    """ Saving error logs in file """
    with open("error.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"ERROR IN: {error_address}\nERROR TEXT: {log_text}\n{'='*50}\n\n")
