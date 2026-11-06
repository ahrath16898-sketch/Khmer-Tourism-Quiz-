
import random
from typing import Dict
from .question import QUESTIONS
from .display import display_question, display_result, display_loading

class QuizGame:

    def __init__(self):
        self.questions = QUESTIONS.copy()
        self.score = 0
        self.total_questions = len(self.questions)
        self.correct_answers = 0
        self.wrong_answers = 0
        self.shuffled_questions = []

    def shuffle_questions(self) -> None:
        self.shuffled_questions = self.questions.copy()
        random.shuffle(self.shuffled_questions)

    def ask_question(self, question_data: Dict) -> bool:
        question_text = question_data["question"]
        options = question_data["options"]
        correct_index = question_data["correct"]

        user_choice = display_question(question_text, options)

        is_correct = user_choice == correct_index

        if is_correct:
            self.score += 10
            self.correct_answers += 1
        else:
            self.wrong_answers += 1

        display_result(
            is_correct,
            options[correct_index],
            question_data.get("fun_fact", "ស្វែងយល់បន្ថែមអំពីកម្ពុជា!")
        )
        return is_correct

    def start_quiz(self) -> None:
        display_loading()

        self.shuffle_questions()

        for i, question_data in enumerate(self.shuffled_questions, 1):
            print(f"\n សំណួរ {i}/{self.total_questions}")
            print("-" * 40)

            self.ask_question(question_data)

        self.show_final_results()

    def show_final_results(self) -> None:
        print("\n" + "=" * 60)
        print(" បញ្ចប់កម្រងសំណួរ! ".center(60))
        print("=" * 60)
        print(f"\n ពិន្ទុចុងក្រោយ: {self.score} ពិន្ទុ")
        print(f" ចម្លើយត្រឹមត្រូវ: {self.correct_answers}")
        print(f" ចម្លើយមិនត្រឹមត្រូវ: {self.wrong_answers}")
        print(f" ចំនួនសំណួរសរុប: {self.total_questions}")

        percentage = (self.correct_answers / self.total_questions) * 100 \
            if self.total_questions > 0 \
            else 0
        print(f" ភាពត្រឹមត្រូវ: {percentage:.1f}%")

        print("\n" + "~" * 60)
        print(get_result_level(self.score))
        print("~" * 60)

        print("\n ស្ថិតិរហ័ស:")
        print(f"• ពិន្ទុក្នុងមួយសំណួរ: ១០ ពិន្ទុ")
        print(f"• ពិន្ទុសរុបដែលអាចទទួលបាន: {self.total_questions * 10} ពិន្ទុ")
        print(f"• ទទួលបាន: {self.score} ពិន្ទុ")
        print(f"• បាត់បង់: {(self.total_questions * 10) - self.score} ពិន្ទុ")

    def reset_game(self) -> None:
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.shuffle_questions()

def get_result_level(score: int) -> str:
    if score >= 40:
        return " ពូកែណាស់! អ្នកគឺជាអ្នកជំនាញទេសចរណ៍ខ្មែរ! "
    elif score >= 30:
        return " ល្អ! អ្នកស្គាល់កម្ពុជាច្បាស់ណាស់!"
    elif score >= 20:
        return " មធ្យម! បន្តរៀនអំពីកម្ពុជាដ៏ស្រស់ស្អាត!"
    else:
        return " ត្រូវការអនុវត្តបន្ថែម! ស្វែងយល់បន្ថែមអំពីអច្ឆរិយវត្ថុរបស់កម្ពុជា!"