
from khmer_quiz import QuizGame, display_welcome, display_goodbye, COLORS

def main():
    while True:
        display_welcome()

        game = QuizGame()
        game.start_quiz()

        print("\n" + "=" * 60)
        print("ចង់លេងម្តងទៀតទេ?".center(60))
        print("=" * 60)

        while True:
            choice = input("\nតើអ្នកចង់លេងម្តងទៀតទេ? (y/n): ").lower().strip()

            if choice in ['y', 'yes']:
                print("\n" + " កំពុងចាប់ផ្តើមហ្គេមថ្មី..." + "\n")
                break
            elif choice in ['n', 'no']:
                display_goodbye()
                return

            else:
                print(COLORS["RED"] + " ការបញ្ចូលមិនត្រឹមត្រូវ។ សូមវាយបញ្ចូល 'y' ឬ 'n'។" + COLORS["END"])

if __name__ == "__main__":
    main()
