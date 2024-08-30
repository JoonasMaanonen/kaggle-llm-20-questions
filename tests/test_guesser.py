import unittest

from bots.llama_3_bot import Llama3CombinedBot
from data_models.observation import Observation


def get_observation(keyword, questions, answers, guesses=[]):
    base_observation_dict = {
        "step": 1,
        "questions": questions,
        "guesses": guesses,
        "answers": answers,
        "role": "guesser",
        "turnType": "guess",
        "keyword": keyword,
        "category": "country",
        "remainingOverageTime": 300.0,
    }

    return Observation(**base_observation_dict)


class TestGuesser(unittest.TestCase):
    def setUp(self):
        self.model = Llama3CombinedBot(model_dir="../models/Meta-Llama-3-8B-Instruct")

    def test_fixed_guess(self):
        assert (
            self.model(
                get_observation("Finland", questions=["Is the keyword Finland?"], answers=["yes"])
            ).lower()
            == "finland"
        )

    def test_questions_chars(self):
        assert (
            "?"
            not in self.model(
                get_observation("Finland", questions=["Is the keyword a place?"], answers=["yes"])
            ).lower()
        )

    def test_letter_reasoning(self):
        assert (
            self.model(
                get_observation(
                    "Peru",
                    questions=[
                        "Is it a country?",
                        "Is it in South America?",
                        "Does the country start with the letter 'p'",
                        "Is it Paraguay?",
                    ],
                    answers=["yes", "yes", "yes", "no"],
                    guesses=["China", "Brazil", "Paraguay"],
                )
            ).lower()
            == "peru"
        )

    def test_logical_reasoning_country(self):
        assert (
            self.model(
                get_observation(
                    "Finland",
                    questions=[
                        "Is the keyword a place?",
                        "Is the keyword a nordic country?",
                        "Is the capital of the keyword country Helsinki?",
                    ],
                    answers=["yes", "yes", "yes"],
                    guesses=[
                        "Amsterdam",
                        "Norway",
                    ],
                )
            ).lower()
            == "finland"
        )

    def test_logical_reasoning_geography(self):
        assert (
            self.model(
                get_observation(
                    "Japan",
                    questions=[
                        "Is the keyword a place?",
                        "Is the keyword an asian country?",
                        "Is the country an island?",
                        "Does the country start with the letter 'j'?",
                    ],
                    answers=["yes", "yes", "yes", "yes"],
                    guesses=[
                        "Amsterdam",
                        "China",
                        "Indonesia",
                    ],
                )
            ).lower()
            == "japan"
        )
        assert (
            self.model(
                get_observation(
                    "Russia",
                    questions=[
                        "Is the keyword a place?",
                        "Is the keyword an european country?",
                        "Is the country the largest country in europe?",
                    ],
                    answers=["yes", "yes", "yes"],
                    guesses=[
                        "Amsterdam",
                        "Japan",
                    ],
                )
            ).lower()
            == "russia"
        )

    def test_geographical_reasoning_only_single_option(self):
        guess = self.model(
            get_observation(
                "Norway",
                questions=[
                    "Is the keyword a country?",
                    "Is it a nordic country?",
                    "Does it border Sweden?",
                    "Is the country part of the European Union?",
                ],
                answers=["yes", "yes", "yes", "no"],
                guesses=["Angola", "Sweden", "Finland"],
            )
        )
        assert guess.lower() == "norway"

    def test_no_duplicate_guesses(self):
        for _ in range(3):
            guess = self.model(
                get_observation(
                    "Norway",
                    questions=[
                        "Is the keyword a country?",
                        "Is it a nordic country?",
                        "Does it border Sweden?",
                        "Is the country part of the European Union?",
                    ],
                    answers=["yes", "yes", "yes", "yes"],
                    guesses=["Angola", "Sweden", "Finland"],
                )
            )
            assert guess.lower() != "finland" and guess.lower() != "sweden"

        for _ in range(3):
            guess = self.model(
                get_observation(
                    "Norway",
                    questions=[
                        "Is the keyword a country?",
                        "Is it a nordic country?",
                        "Does it border Sweden?",
                        "Is the country part of the European Union?",
                    ],
                    answers=["yes", "yes", "yes", "yes"],
                    guesses=["Finland", "Finland", "Finland"],
                )
            )
            assert guess.lower() == "denmark"
