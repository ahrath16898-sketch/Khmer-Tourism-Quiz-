
import time
from typing import List

COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "PURPLE": "\033[95m",
    "CYAN": "\033[96m",
    "BOLD": "\033[1m",
    "END": "\033[0m"
}

def display_welcome() -> None:
    print("=" * 70)
    print(COLORS["BOLD"] + " សូមស្វាគមន៍មកកាន់កម្រងសំណួរទេសចរណ៍ខ្មែរ!".center(70) + COLORS["END"])
    print("=" * 70)

    print("\n" + COLORS["CYAN"] + " សាកល្បងចំណេះដឹងរបស់អ្នកអំពីបេតិកភណ្ឌដ៏សម្បូរបែបរបស់កម្ពុជា!" + COLORS["END"])
    print("\n សេចក្តីណែនាំ:")
    print("  • អ្នកនឹងទទួលបានសំណួរច្រើនជម្រើស")
    print("  • វាយលេខ (១, ២, ឬ ៣) នៃចម្លើយរបស់អ្នក")
    print("  • ចម្លើយត្រឹមត្រូវនីមួយៗផ្តល់ពិន្ទុ ១០")
    print("  • អង្គហេតុគួរឱ្យចាប់អារម្មណ៍នឹងត្រូវបានចែករំលែកបន្ទាប់ពីសំណួរនីមួយៗ")
    print("  • កម្រិតលទ្ធផលចុងក្រោយរបស់អ្នកនឹងត្រូវបានបង្ហាញនៅចុងបញ្ចប់!")
    print("  • អ្នកអាចលេងម្តងទៀតបន្ទាប់ពីបញ្ចប់កម្រងសំណួរ")

    print("\n" + "~" * 70)
    print(COLORS["YELLOW"] + " គន្លឺះ: អានសំណួរនីមួយៗដោយប្រុងប្រយ័ត្នមុនពេលឆ្លើយ!" + COLORS["END"])
    print("~" * 70)

    input("\nចុច Enter ដើម្បីចាប់ផ្តើមកម្រងសំណួរ...")

def display_question(question: str, options: List[str]) -> int:
    print("\n" + COLORS["BOLD"] + f" {question}" + COLORS["END"])
    print("-" * 50)

    for i, option in enumerate(options, 1):
        print(f"   {COLORS['BLUE']}{i}{COLORS['END']}. {option}")

    print("-" * 50)

    while True:
        user_input = input(COLORS["YELLOW"] + "ចម្លើយរបស់អ្នក (១, ២, ឬ ៣): " + COLORS["END"]).strip()

        if user_input in ['1', '2', '3']:
            return int(user_input) - 1

        print(COLORS["RED"] + " ការបញ្ចូលមិនត្រឹមត្រូវ។ សូមវាយបញ្ចូល ១, ២, ឬ ៣។" + COLORS["END"])

def display_result(is_correct: bool, correct_answer: str, fun_fact: str = "") -> None:
    if is_correct:
        print("\n" + COLORS["GREEN"] + " ត្រឹមត្រូវ! អស្ចារ្យណាស់! (+១០ ពិន្ទុ) " + COLORS["END"])
    else:
        print("\n" + COLORS["RED"] + f" មិនត្រឹមត្រូវ! ចម្លើយត្រឹមត្រូវគឺ: {COLORS['BOLD']}{correct_answer}{COLORS['END']}" + COLORS["END"])

    if fun_fact:
        print(COLORS["CYAN"] + f" អង្គហេតុគួរឱ្យចាប់អារម្មណ៍: {fun_fact}" + COLORS["END"])

    time.sleep(2)

def display_loading() -> None:
    print("\n" + COLORS["PURPLE"] + " កំពុងរៀបចំសំណួររបស់អ្នក..." + COLORS["END"])
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n" + COLORS["GREEN"] + " រួចរាល់!" + COLORS["END"] + "\n")
    time.sleep(0.5)

def display_goodbye() -> None:
    print("\n" + "=" * 70)
    print(COLORS["BOLD"] + " សូមអរគុណដែលបានលេងកម្រងសំណួរទេសចរណ៍ខ្មែរ! ".center(70) + COLORS["END"])
    print("=" * 70)

    print("\n" + COLORS["YELLOW"] + " សូមអញ្ជើញមកទស្សនាកម្ពុជាឆាប់ៗ! " + COLORS["END"])
    print("    ទស្សនាអច្ឆរិយវត្ថុអង្គរវត្ត សម្រាកលើឆ្នេរដ៏ស្រស់ស្អាត")
    print("    និងទទួលបទពិសោធន៍ពីភាពកក់ក្តៅនៃរាក់ទាក់ពីប្រជាជនកម្ពុជា! ")

    print("\n" + "~" * 70)
    print(" បន្តរៀនអំពីកម្ពុជា:")
    print("   • ចូលមើល: www.tourismcambodia.com")
    print("   • តាមដាន: @TourismCambodia")
    print("~" * 70)

    print("\n" + COLORS["PURPLE"] + " ជួបគ្នាលើកក្រោយ! " + COLORS["END"])
    print("=" * 70)