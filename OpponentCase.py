# Sample Space
cards = 52
hole_cards = 2

#Your opponent provided you information... use it!
opponents_hole_cards = 2

turn_community_cards = 4
cards = cards - (hole_cards + opponents_hole_cards + turn_community_cards)

# Outcomes
diamonds = 13
diamonds_drawn = 4

#You can't count the two diamonds that won't help you win
diamonds_non_outs = 2

outs = diamonds - diamonds_drawn - diamonds_non_outs

# Determine win probability
win_probability = outs / cards

# Determine expected value
pot = 60
ev = pot * win_probability

# Print ev and appropriate decision
call_amount = 20
if ev >= 20:
    print(round(ev, 2), 'Call')
else:
    print(round(ev, 2), 'Fold')