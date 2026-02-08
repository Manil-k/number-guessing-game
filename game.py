#CLI-Game Random Number Guessing Game

import random

def game(max_number, attempts):
    number = random.randint(1, max_number)   
    print("-" * 60)
    print(f"The number is between 1 and {max_number}.")
    print(f"You have {attempts} attempts")
    print("-" * 60)
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == number:
            print("Viola! You guessed it correct 🎉")
            return True   # won
        elif guess < number:
            print("Too low!", end=" ")
        else:
            print("Too high!", end=" ")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"\nGame Over! The number was → {number}")
    return False   # lost






def main():
    print("=" * 60)
    print("  Welcome to Number Guessing Game  ".center(60, "="))
    print("=" * 60)
    print("\nPress ENTER to continue...")
    input()

    while True:
        diff = input("Enter Difficulty Level → [E]asy, [M]edium, [H]ard  (or Q to quit): ").strip().upper()

        if diff == 'Q':
            print("Thanks for playing! Bye 👋")
            break

        if diff == 'E':
            n, a = 50, 10
        elif diff == 'M':
            n, a = 100, 7
        elif diff == 'H':
            n, a = 200, 5   # you can make hard harder
        else:
            print("Invalid choice! Please enter E, M, H or Q")
            continue

        print(f"\n→ {diff} mode selected")
        game(n, a)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("See you next time!")
            break


if __name__ == '__main__':
    main()
