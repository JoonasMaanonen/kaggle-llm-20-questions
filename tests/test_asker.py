import unittest

from bots.llama_3_bot import Llama3CombinedBot
from data_models.observation import Observation


def get_observation(keyword, questions, answers, turn_type, guesses=[]):
    base_observation_dict = {
        "step": 1,
        "questions": questions,
        "guesses": guesses,
        "answers": answers,
        "role": "guesser",
        "turnType": turn_type,
        "keyword": keyword,
        "category": "country",
        "remainingOverageTime": 300.0,
    }

    return Observation(**base_observation_dict)


class TestAsker(unittest.TestCase):
    def setUp(self):
        self.model = Llama3CombinedBot(model_dir="../models/Meta-Llama-3-8B-Instruct")

    def test_two_questions_should_win(self):
        question = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is is a type of mustard?",
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes"],
                turn_type="ask",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english mustard",
                ],
            )
        )
        answer = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is is a type of mustard?",
                    question,
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes"],
                turn_type="answer",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english mustard",
                ],
            )
        )
        guess = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is the spice a type of mustard?",
                    question,
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes", answer],
                turn_type="guess",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english mustard",
                ],
            )
        )
        second_question = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is is a type of mustard?",
                    question,
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes", answer],
                turn_type="ask",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english_mustard",
                    guess,
                ],
            )
        )
        second_answer = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is is a type of mustard?",
                    question,
                    second_question,
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes", answer],
                turn_type="answer",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english_mustard",
                    guess,
                ],
            )
        )
        second_guess = self.model(
            get_observation(
                "Dijon mustard",
                questions=[
                    "Is the keyword a place?",
                    "Is the thing a man-made object?",
                    "Is the thing edible?",
                    "Is the thing a spice?",
                    "Is the spice typically used in European cuisine?",
                    "Is is a type of mustard?",
                    question,
                    second_question,
                ],
                answers=["no", "yes", "yes", "yes", "yes", "yes", answer, second_answer],
                turn_type="guess",
                guesses=[
                    "dog",
                    "chisel",
                    "oatmeal",
                    "Ketchup",
                    "herbes de provence",
                    "english_mustard",
                    guess,
                ],
            )
        )
        assert guess.lower() == "dijon mustard" or second_guess.lower() == "dijon mustard", (
            f"failed test with the sequence: '{question}', answer: '{answer}', guess: '{guess}' "
            f"'{second_question}', answer: '{second_answer}', guess: '{second_guess}'"
        )
