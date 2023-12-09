import re


class CubesChallenge:
    cubes_boundaries = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def is_valid_game(self, game: dict):
        for play in game.get('plays', []):
            if any(play.get(color, 0) > self.cubes_boundaries.get(color, 0) for color in play.keys()):
                return False

        return True

    def transform_data(self, line: str):
        game_id, plays = line.split(':')
        game = dict({
            'game_id': int(re.sub(r'[\D\s]', '', game_id)),
            'plays': []
        })
       
        plays_list = plays.strip().split(';')

        for play in plays_list:
            sorted_cubes = play.split(',')
            sorted_cubes_dict = dict()

            for cube in sorted_cubes:
                count, color = cube.strip().split(' ')
                sorted_cubes_dict.update({color: int(count)})

            game['plays'].append(sorted_cubes_dict)

        return game

    def validate(self):
        valid_games_sum = 0
        with open('test_content.txt', 'r') as file:
            for line in file:
                game = self.transform_data(line)
                is_valid = self.is_valid_game(game)
                if is_valid:
                    valid_games_sum += game.get('game_id')
            print(f'Sum of valid game\'s ids: {valid_games_sum}')


# Class instantiation
cc = CubesChallenge()
cc.validate()
