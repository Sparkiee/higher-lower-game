import random
from art import logo
from art import vs
from data import data

print(logo)
print("Welcome to the Higher or Lower game, you have to decide who has more followers on instagram")
run = True
score = 0

B = random.choice(data)

while run:
    A = B
    B = random.choice(data)
    # print(A['follower_count'])
    # print(B['follower_count'])
    print(f"Your current score is {score}")
    print(f"Personality A: {A['name']}, {A['description']}, from the {A['country']}")
    print(vs)
    print(f"Personality B: {B['name']}, {B['description']}, from the {B['country']}")
    choice = input("Who has more instagram followers? 'A' or 'B': ")
    if choice == "A" and A['follower_count'] > B['follower_count']:
        score += 1
    elif choice == "B" and A['follower_count'] < B['follower_count']:
        score += 1
    else:
        print(f"You lost! Your score is {score}")
        run = False
    # clear screen
    print(logo)
    print("Broccoli")