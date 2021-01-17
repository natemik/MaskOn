import random

last_chosen = 0

msgs = [
    "Thanks for wearing a mask!",
    "Thanks for setting a good example by wearing a mask!",
    "Thank you for keeping our community safe by wearing a mask!",
    "Thank you for not being a conspiracy theorist!",
    "You look real cool wearing that mask 😘.",
    "Looking great in that fantastic mask!",
    "Great job helping to reduce the spread of disease!",
    "Making the smart choice by wearing a mask!",
]
random.shuffle(msgs)


def get_callout():
    if last_chosen < len(msgs):
        last_chosen += 1
        return msgs[last_chosen-1]
    else:
        last_chosen = 0
        random.shuffle(msgs)
        return get_callout()