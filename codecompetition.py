import random

# List of video games and hints
games_with_clues = {
    "Pokemon Go": "An open-world adventure where you can capture cute creatures to increase your power.",
    "Subway Surfers": "A challenging game where your character has to run from a dog and an inspector.",
    "Mobile Legends": "Fight your opponent and buy more powerful characters.",
    "Hollow Knight": "A metroidvania game featuring a bug-like hero.",
    "Portal": "A puzzle-platform game involving teleportation.",
    "Celeste": "A platformer focusing on climbing a mountain.",
    "The Witcher 3: Wild Hunt": "An open-world RPG featuring a monster hunter."
}

def video_game_guessing_game():
    game, clue = random.choice(list(games_with_clues.items()))

    attempts = 0
    
    max_attempts = 5

    print("Welcome to the Video Game Guessing Game!")
    print("You have to guess the name of a video game.")
    print(f"Clue: {clue}")
    print(f"You have {max_attempts} attempts to guess.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ").strip()

        if guess.lower() == game.lower():
            print(f"Congratulations! You guessed the game: '{game}' in {attempts + 1} attempts.")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Wrong guess! You have {remaining_attempts} attempts left.")
            
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct answer was: '{game}'.")

if __name__ == "__main__":
    video_game_guessing_game()