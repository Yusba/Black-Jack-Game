import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return (0)

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw🙃"
    elif computer_score == 0:
        return "Lose,opponent has BlackJack 😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > 21:
        return "You went over.You lose 😭"
    elif computer_score > 21:
        return "opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😄"
    else:
        return "You lose 😣"


def play_game():
    print(logo)

    users_card = []
    computers_card = []
    is_game_over = False

    for _ in range(2):
        users_card.append(deal_card())
        computers_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(users_card)
        computer_score = calculate_score(computers_card)
        print(f'Your cards: {users_card}, current score: {user_score}')
        print(
            f'Computer cards: {computers_card}, current score: {computer_score}'
        )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                'Type "y" to get another card, type "n" to pass :')
        if user_should_deal == "y":
            users_card.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_card.append(deal_card())
        computer_score = calculate_score(computers_card)

    print(
        f"Your final hand is {users_card} and your final score is {user_score}"
    )
    print(
        f"Computer final hand is {computers_card} and computer final score is {computer_score}"
    )
    print(compare(user_score, computer_score))


while input(
        "Do you want to play the game of BlackJack? Type 'y' and 'n':") == "y":
    play_game()

