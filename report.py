import argparse
from src.model.games import GameCollection, Game

if __name__ == "__main__":
    # Configura il parser per gestire gli argomenti da riga di comando
    parser = argparse.ArgumentParser(description='Chess games Report')
    parser.add_argument('--user', type=str, default="", help='The user for whom the report is to be created')
    parser.add_argument('--num-games', type=int, default=-1, help='Number of recent games to select')
    parser.add_argument('--time-control', type=str, default="", help='The desired chess game time control (daily, rapid, blitz, bullet, etc.)')
    args = parser.parse_args()

    pgn_file_name = args.user + ".pgn"
    num_games = args.num_games if args.num_games >= 0 else None
    time_control = args.time_control if args.time_control != "" else None
    game_collection = GameCollection(pgn_file_name, num_games, time_control)

    # Apre il file REPORT.md in modalità scrittura
    with open("REPORT.md", "w") as report_file:
        report_file.write(f"# Chess games Report for the latest {args.num_games} {args.user}'s games.\n\n")
        report_file.write( "| Game | Date and Time | Opening | Result |\n")
        report_file.write( "|------|---------------|---------|--------|\n")
        for game in game_collection:
            for game in game_collection:
                if game.result == "1-1":
                    report_file.write(f"| [{game.white_player} ({game.white_elo}) vs {game.black_player} ({game.black_elo})]({game.link}) | {game.start_time.strftime("%Y%m%d %H:%M")} | [{game.opening_name} - {game.opening_variation}]({game.opening_url}) | ![Draw](img/draw.png) |\n")
                elif (game.white_player == args.user and game.result == "1-0") or (game.black_player == args.user and game.result == "0-1"):
                    report_file.write(f"| [{game.white_player} ({game.white_elo}) vs {game.black_player} ({game.black_elo})]({game.link}) | {game.start_time.strftime("%Y%m%d %H:%M")} | [{game.opening_name} - {game.opening_variation}]({game.opening_url}) | ![Win](img/win.png) |\n")
                else:
                    report_file.write(f"| [{game.white_player} ({game.white_elo}) vs {game.black_player} ({game.black_elo})]({game.link}) | {game.start_time.strftime("%Y%m%d %H:%M")} | [{game.opening_name} - {game.opening_variation}]({game.opening_url}) | ![Lose](img/lose.png) |\n")
