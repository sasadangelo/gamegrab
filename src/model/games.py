from datetime import datetime, timezone
import chess.pgn

class Game:
    def __init__(self, game):
        self.game = game
        self.white_player = self.game.headers["White"]
        self.black_player = self.game.headers["Black"]
        self.result = self.game.headers["Result"]
        self.link = self.game.headers["Link"]
        self.start_time = self.convert_to_local_time(self.game.headers["Date"], self.game.headers["StartTime"])
        self.end_time = self.convert_to_local_time(self.game.headers["EndDate"], self.game.headers["EndTime"])

    def convert_to_local_time(self, date_str, time_str):
        # Combina data e ora in un unico formato datetime
        date_time_str = f"{date_str}T{time_str}"
        # Converte la stringa in un oggetto datetime
        date_time_utc = datetime.strptime(date_time_str, "%Y.%m.%dT%H:%M:%S")
        # Aggiunge il timezone UTC alla data e ora
        date_time_utc = date_time_utc.replace(tzinfo=timezone.utc)
        # Converte il timezone in quello locale
        date_time_local = date_time_utc.astimezone()
        return date_time_local

class GameCollection:
    def __init__(self, pgn_file, num_games=100):
        self.games = self.load_games(pgn_file, num_games)

    def load_games(self, pgn_file, num_games=100):
        games = []
        with open(pgn_file) as pgn:
            while True:
                game = chess.pgn.read_game(pgn)
                if game is None:
                    break
                games.append(Game(game))
                if len(games) > num_games:
                    break
        return games

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.games):
            game = self.games[self.index]
            self.index += 1
            return game
        raise StopIteration