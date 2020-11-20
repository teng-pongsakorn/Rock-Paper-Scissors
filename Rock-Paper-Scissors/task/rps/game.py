# Write your code here
import random


class Game:

    SCORE_WIN = 100
    SCORE_DRAW = 50
    START_SCORE = 350

    PLAYER_LOST_MESSAGE = "Sorry, but the computer chose {}"
    PLAYER_WIN_MESSAGE = "Well done. The computer chose {} and failed"
    PLAYER_DRAW_MESSAGE = "There is a draw ({})"
    INVALID_MESSAGE = "Invalid input"

    GET_USERNAME = "Enter your name: > "
    GREETING = "Hello, {}"

    FULL_CHOICES = ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper',
                    'air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock']
    DEFAULT_CHOICES = ['scissors', 'paper', 'rock']

    RATING_FILE = 'rating.txt'

    GAME_START_MESSAGE = "Okay, let's start"

    RATING_MESSAGE = "Your rating: {}"

    EXIT_MESSAGE = 'Bye!'

    @staticmethod
    def play():

        who = input(Game.GET_USERNAME)
        print(Game.GREETING.format(who))

        scores = Game.get_score_dict()
        rating = scores.get(who, Game.START_SCORE)

        game_options = input("> ")
        if game_options == '':
            game_options = Game.DEFAULT_CHOICES
        else:
            game_options = game_options.split(',')

        winning_dict = Game.get_winning_dict(Game.FULL_CHOICES)

        print(Game.GAME_START_MESSAGE)
        exit_game = False

        while not exit_game:
            player_input = input("> ")
            if player_input in game_options:
                computer_input = random.choice(game_options)
                player_result = Game.get_game_result(player_input, computer_input, winning_dict)
                if player_result == 'Draw':
                    rating += Game.SCORE_DRAW
                    print(Game.PLAYER_DRAW_MESSAGE.format(computer_input))
                elif player_result == 'Win':
                    rating += Game.SCORE_WIN
                    print(Game.PLAYER_WIN_MESSAGE.format(computer_input))
                else:
                    print(Game.PLAYER_LOST_MESSAGE.format(computer_input))
            elif player_input == '!exit':
                print(Game.EXIT_MESSAGE)
                scores[who] = rating
                Game.save_score_dict(scores)
                exit_game = True
            elif player_input == '!rating':
                print(Game.RATING_MESSAGE.format(rating))
            else:
                print(Game.INVALID_MESSAGE)


    @staticmethod
    def get_score_dict():
        scores = dict()
        with open(Game.RATING_FILE, 'a+') as f:
            for line in f:
                name, rating = line.split()
                scores[name] = int(rating)
        return scores

    @staticmethod
    def save_score_dict(scores):
        with open(Game.RATING_FILE, 'w') as f:
            for k, v in scores.items():
                print(k, v, sep=' ', file=f, flush=True)

    @staticmethod
    def get_rating(user):
        with open(Game.RATING_FILE, 'a+') as f:
            for line in f:
                name, rating = line.split()
                if name == user:
                    return int(rating)
        return 0

    @staticmethod
    def get_winning_dict(game_options):
        result = {}
        n = len(game_options)
        k = n // 2
        for i, option in enumerate(game_options):
            winning = []
            for j in range(1, k+1):
                winning.append(game_options[(i+j)%n])
            result[option] = set(winning)
        return result

    @staticmethod
    def get_game_result(player, computer, winning_dict):
        if player == computer:
            return 'Draw'
        elif computer in winning_dict[player]:
            return 'Win'
        return 'Lose'


if __name__ == '__main__':
    Game.play()
