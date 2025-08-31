import random

def get_computer_choice(user_history):
    """
    Computer choice generator.
    If no user history -> random choice
    If user history available -> AI predicts based on probability
    """
    choices = ["rock", "paper", "scissors"]

    if not user_history:
        return random.choice(choices)

    # Count user moves
    rock_count = user_history.count("rock")
    paper_count = user_history.count("paper")
    scissors_count = user_history.count("scissors")

    # Find most common user move
    most_common = max(["rock", "paper", "scissors"], 
                      key=lambda move: user_history.count(move))

    # AI strategy: play the move that beats user's most common move
    if most_common == "rock":
        return "paper"     # paper beats rock
    elif most_common == "paper":
        return "scissors"  # scissors beats paper
    else:
        return "rock"      # rock beats scissors


def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "✅ You win!"
    else:
        return "❌ Computer wins!"


def play_game():
    print("🎮 Rock-Paper-Scissors Game 🎮")
    print("Type 'quit' to exit.\n")
    user_history = []

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if user_choice == "quit":
            print("👋 Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice! Please try again.")
            continue

        # Computer makes choice (AI enabled)
        computer_choice = get_computer_choice(user_history)

        print(f"🤖 Computer chose: {computer_choice}")
        print(f"🏆 Result: {decide_winner(user_choice, computer_choice)}\n")

        # Save user move for AI
        user_history.append(user_choice)


# Run the game
if __name__ == "__main__":
    play_game()
