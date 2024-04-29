import argparse
from src.model.games import GameCollection, Game

if __name__ == "__main__":
    # Configura il parser per gestire gli argomenti da riga di comando
    parser = argparse.ArgumentParser(description='Chess games Report')
    parser.add_argument('--num-games', type=int, default=100, help='Number of recent games to select')
    args = parser.parse_args()

    game_collection = GameCollection("sasadangelo.pgn", args.num_games)
    for game in game_collection:
        # Apre il file REPORT.md in modalità scrittura
        with open("REPORT.md", "w") as report_file:
            report_file.write(f"# Chess games Report for the latest {args.num_games} sasadangelo games.\n\n")
            for game in game_collection:
                report_file.write(f"* [{game.white_player} vs {game.black_player}]({game.link}) - {game.result}\n")