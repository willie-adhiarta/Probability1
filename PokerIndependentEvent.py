# Sample Space
cards = 52

# Outcomes
aces = 4

# Divide possbile outcomes by the sample set
ace_probability = aces / cards

# Probability of two consecutive independent aces
two_aces_probability = ace_probability * ace_probability

# Determine river flush probability
two_aces_probability_percent = two_aces_probability * 100
print(round(two_aces_probability_percent, 1))