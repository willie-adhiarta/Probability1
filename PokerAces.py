# Sample Space
cards = 52

# Outcomes
aces = 4

# Divide possbile outcomes by the sample set
ace_probability = aces / cards

# Print probability rounder to two decimal places
print(round(ace_probability, 2))

# Ace Probability Percent Code
ace_probability_percent = ace_probability * 100

# Print probability percent rounded to one decimal place
print(str(round(ace_probability_percent, 0)) + '%')