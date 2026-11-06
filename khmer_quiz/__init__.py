
__name__ = "Rath"
__email__ = "ahrath16898@gmail.com"
__status__ = "Development"

from .question import QUESTIONS
from .game_logic import QuizGame, get_result_level
from .display import (
    display_welcome,
    display_question,
    display_result,
    display_goodbye,
    display_loading,
    COLORS
)
__all__ = [
    'QUESTIONS',
    'QuizGame',
    'get_result_level',
    'display_welcome',
    'display_question',
    'display_result',
    'display_goodbye',
    'display_loading',
    'COLORS'
]