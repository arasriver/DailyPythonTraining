import random
score_p1 = 0
score_p2 = 0


def game(name,score):
    while True:
        print(f"{name} turn")
        dice = random.randint(1, 6)
        print(f"You rolled {dice}")
        if dice == 1:
            score = 0
            print(f"BAD LUCK! TOTAL SCORE IS {score}")
            return score
        score = dice + score
        if score < 20:
            step = input("Roll again?(y/n): ")
            if step == "n":
                print(f"Your score in this turn is {score}")
                return score
            else:
                continue
        else:
            print(f"YOU WON! you exceeded max point! your score is {score}")
            return score


while True:
    max_point = 20
    if score_p1 < max_point and score_p2 < max_point:
        score_p1 = game("player1", score_p1)
        print(f"current score: player1: {score_p1} player2:{score_p2}")
        score_p2 = game("player2", score_p2)
        print(f"current score: player1: {score_p1} player2:{score_p2}")
    else:
        break

