import argparse
from src.model.games import GameCollection, Game

if __name__ == "__main__":
    # Configura il parser per gestire gli argomenti da riga di comando
    parser = argparse.ArgumentParser(description='Chess games Report')
    parser.add_argument('--num-games', type=int, default=-1, help='Number of recent games to select')
    args = parser.parse_args()

    if args.num_games < 0:
        game_collection = GameCollection("sasadangelo.pgn", None)
    else:
        game_collection = GameCollection("sasadangelo.pgn", args.num_games)

    # Apre il file REPORT.md in modalità scrittura
    with open("REPORT.md", "w") as report_file:
        report_file.write(f"# Chess games Report for the latest {args.num_games} sasadangelo games.\n\n")
        report_file.write( "|------|--------|\n")
        report_file.write( "| Game | Result |\n")
        report_file.write( "|------|--------|\n")
        for game in game_collection:
            for game in game_collection:
                report_file.write(f"| [{game.white_player} vs {game.black_player}]({game.link}) | {game.result} |\n")
