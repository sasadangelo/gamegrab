import argparse
from src.model.games import GameCollection, Game

if __name__ == "__main__":
    # Configura il parser per gestire gli argomenti da riga di comando
    parser = argparse.ArgumentParser(description='Chess games Report')
    parser.add_argument('--user', type=str, default="", help='The user for whom the report is to be created')
    parser.add_argument('--num-games', type=int, default=-1, help='Number of recent games to select')
    args = parser.parse_args()

    pgn_file_name = args.user + ".pgn"
    if args.num_games < 0:
        game_collection = GameCollection(pgn_file_name, None)
    else:
        game_collection = GameCollection(pgn_file_name, args.num_games)

    # Apre il file REPORT.md in modalità scrittura
    with open("REPORT.md", "w") as report_file:
        report_file.write(f"# Chess games Report for the latest {args.num_games} {args.user}'s games.\n\n")
        report_file.write( "|------|--------|\n")
        report_file.write( "| Game | Result |\n")
        report_file.write( "|------|--------|\n")
        for game in game_collection:
            for game in game_collection:
                if game.result == "1-1":
                    report_file.write(f"| [{game.white_player} vs {game.black_player}]({game.link}) | ![Draw](img/draw.png) |\n")
                elif (game.white_player == args.user and game.result == "1-0") or (game.black_player == args.user and game.result == "0-1"):
                    report_file.write(f"| [{game.white_player} vs {game.black_player}]({game.link}) | ![Win](img/win.png) |\n")
                else:
                    report_file.write(f"| [{game.white_player} vs {game.black_player}]({game.link}) | ![Lose](img/lose.png) |\n")
