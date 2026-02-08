# Number Guessing Game

A simple, fun command-line number guessing game written in Python 🕹️

You try to guess a secret number within a limited number of attempts.  
Choose your difficulty level and get helpful "too high" / "too low" hints.

## Features

- Three difficulty levels (Easy, Medium, Hard)
- Clear high/low feedback after each guess
- Limited attempts based on difficulty
- Play again option after each game
- Clean terminal formatting and messages

## Difficulty Levels

| Level  | Number Range | Attempts |
|--------|--------------|----------|
| Easy   | 1 – 50       | 10       |
| Medium | 1 – 100      | 7        |
| Hard   | 1 – 200      | 5        |

## How to Play

1. Make sure you have **Python 3** installed
2. Clone this repository:

   ```bash
   git clone https://github.com/Manil-k/number-guessing-game.git
   cd number-guessing-game
   ```

3. Run the game:

   ```bash
   python guess.py
   # or on some systems:
   python3 guess.py
   ```

## Example Gameplay

```
============================================================
          Welcome to Number Guessing Game          
============================================================

Press ENTER to continue...

Enter Difficulty Level → [E]asy, [M]edium, [H]ard  (or Q to quit): m

→ M mode selected
------------------------------------------------------------
The number is between 1 and 100.
You have 7 attempts
------------------------------------------------------------
Enter your guess: 50
Too low! Attempts left: 6
Enter your guess: 75
Too high! Attempts left: 5
Enter your guess: 62
Too low! Attempts left: 4
...
Viola! You guessed it correct 🎉

Play again? (y/n): 
```

## Requirements

- Python 3.x  
- No external packages needed

## License

MIT License — see the [LICENSE](LICENSE) file for full details.

## Author

**Manil**  
Made with ❤️ in IIT Delhi

Feel free to fork, modify, play, and share!
