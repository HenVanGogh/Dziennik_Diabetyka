#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List, Dict
import random as rm


def filling_the_list_of_jokes_to_choose(joke_list: Dict[str, bool]) -> List[str]:
    jokes_to_random_choice: List[str] = []
    for joke_as_key in joke_list.keys():
        if joke_list[joke_as_key] is True:
            jokes_to_random_choice.append(joke_as_key)
    return jokes_to_random_choice


def dict_with_jokes_as_string(jokes_dct: Dict[str, bool]) -> str:
    dict_as_string = ""
    for key in jokes_dct:
        dict_as_string += key + "\n" + str(jokes_dct[key]) + "\n"
    return dict_as_string


def say_a_joke() -> str:
    file_with_jokes_to_read = open("file_with_jokes.txt", "r", encoding="utf-8")
    jokes = {}
    was_joke_ended = False
    temp_joke = ""
    for line in file_with_jokes_to_read:
        if was_joke_ended:
            if line.strip() == "True":
                jokes[temp_joke] = True
            else:
                jokes[temp_joke] = False
            temp_joke = ""
            was_joke_ended = False
        else:
            if line.strip()[-1] == ';':
                temp_joke += line.strip()
                was_joke_ended = True
            else:
                temp_joke += line.strip() + "\n"

    file_with_jokes_to_read.close()

    jokes_to_choose: List[str] = filling_the_list_of_jokes_to_choose(jokes)
    if len(jokes_to_choose) == 0:
        for joke in jokes.keys():
            jokes[joke] = True
        jokes_to_choose = filling_the_list_of_jokes_to_choose(jokes)
    the_chosen_joke: str = rm.choice(jokes_to_choose)
    jokes[the_chosen_joke] = False
    file_with_jokes_to_write = open("file_with_jokes.txt", "w", encoding="utf-8")
    file_with_jokes_to_write.write(dict_with_jokes_as_string(jokes))
    file_with_jokes_to_write.close()
    return the_chosen_joke[:-1]
