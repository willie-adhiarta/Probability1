# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
cards = 52

# Calculate the probability of drawing a heart or club
hearts = 13
clubs = 13
hearts_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)

# Calculate the probability of drawing an ace, a king, or a queen
aces = 4
kings = 4
queens = 4
ace_king_or_queen = event_probability(aces, cards) + event_probability(kings, cards) + event_probability(queens, cards)

# Outcomes
print(hearts_or_club)
print(ace_king_or_queen)