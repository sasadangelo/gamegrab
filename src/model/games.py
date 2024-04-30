from datetime import datetime, timezone
import chess.pgn
import enum

class TimeControlType(enum.Enum):
    UNKNOW = 0
    UNLIMITED = 1
    STANDARD = 2
    RAPID = 3
    BLITZ = 4
    BULLET = 5

class Game:
    def __init__(self, game):
        self.game = game
        self.white_player = self.game.headers["White"]
        self.black_player = self.game.headers["Black"]
        self.result = self.game.headers["Result"]
        self.link = self.game.headers["Link"]
        self.white_elo = self.game.headers["WhiteElo"]
        self.black_elo = self.game.headers["BlackElo"]
        self.start_time = self.__convert_to_local_time(self.game.headers["Date"], self.game.headers["StartTime"])
        self.end_time = self.__convert_to_local_time(self.game.headers["EndDate"], self.game.headers["EndTime"])
        self.time_control = self.__parse_time_control(self.game.headers["TimeControl"])
        self.opening_code = self.game.headers["ECO"]
        self.opening_url = self.game.headers["ECOUrl"]

    def __convert_to_local_time(self, date_str, time_str):
        # Combina data e ora in un unico formato datetime
        date_time_str = f"{date_str}T{time_str}"
        # Converte la stringa in un oggetto datetime
        date_time_utc = datetime.strptime(date_time_str, "%Y.%m.%dT%H:%M:%S")
        # Aggiunge il timezone UTC alla data e ora
        date_time_utc = date_time_utc.replace(tzinfo=timezone.utc)
        # Converte il timezone in quello locale
        date_time_local = date_time_utc.astimezone()
        return date_time_local

    def __parse_time_control(self, str):
        if (str == "600"):
            return TimeControlType.RAPID
        elif (str=="1/86400"):
            return TimeControlType.STANDARD

        self.black_player = self.game.headers["TimeControl"]

class GameCollection:
    def __init__(self, pgn_file, num_games=None, time_control=None):
        self.games = self.load_games(pgn_file, num_games, time_control)

    def load_games(self, pgn_file, num_games=None, time_control=None):
        games = []
        with open(pgn_file) as pgn:
            while True:
                chess_game = chess.pgn.read_game(pgn)
                if chess_game is None:
                    break
                game = Game(chess_game)
                if (time_control is None) or \
                    (time_control=="rapid" and game.time_control == TimeControlType.RAPID) or \
                    (time_control=="standard" and game.time_control == TimeControlType.STANDARD):
                    games.append(game)
                if num_games and len(games) > num_games:
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