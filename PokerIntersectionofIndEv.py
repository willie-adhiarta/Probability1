# Sample Space for the first draw
cards = 52

# Outcomes for the first draw
aces = 4

# Probability for the first draw
first_ace_probability = aces / cards

# Sample Space for the second draw
cards = cards - 1

# Outcomes of the second draw
aces = aces - 1

# Probability of two consecutive independent aces
second_ace_probability = aces / cards

# Determine river flush probability
both_aces_probability = first_ace_probability * second_ace_probability * 100
print(both_aces_probability)