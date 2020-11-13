# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
cards = 52

# Calculate the probability of drawing a heart or or an ace
hearts = 13
aces = 4
ace_of_hearts = 1
heart_or_ace = event_probability(hearts, cards) + event_probability(aces, cards) - event_probability(ace_of_hearts, cards)

# Calculate the probability of drawing a red card or a face card
red_cards = 26
face_cards = 12
red_face_cards = 6
red_or_face_cards = event_probability(red_cards, cards) + event_probability(face_cards, cards) - event_probability(red_face_cards, cards)

# Print probability percent rounded to one decimal place
print(round(heart_or_ace, 1))
print(round(red_or_face_cards, 1))