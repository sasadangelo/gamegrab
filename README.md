# Game Grab

This tool download your games from Chess.com and create statistics.

# How to use it

Here the instructions to create the statistics of your games:

1. Download the code with the command:
```
git clone https://github.com/sasadangelo/gamegrab
cd gamegrab
```

2. Create a virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
```

2. Grab your games from Chess.com:
```
python3 gamegrab.py --num-games=100 --time-class=rapid --outfile=sasadangelo.pgn sasadangelo
```

this command download the recent 100 rapid games of the Chess.com sasadangelo user.

ChessBase also has good tools for looking at performance--see the Dossier and Prepare Against features.
