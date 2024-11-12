import numpy as np
deck = []
for rank in RANKS :
    for suit in SUITS:
        card = rank +' of '+ suit
        deck += [card]