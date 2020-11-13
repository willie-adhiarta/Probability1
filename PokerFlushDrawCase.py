# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
cards = 52
hole_cards = 2
turn_community_cards = 4
cards = cards - (hole_cards + turn_community_cards)

# Outcomes
diamonds = 13
diamonds_drawn = 4

# In poker, cards that complete a draw are known as 'outs'
outs = diamonds - diamonds_drawn

# Determine river flush probability
river_flush_probability = event_probability(outs, cards)
print(river_flush_probability)