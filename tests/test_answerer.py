import unittest

from bots.llama_3_bot import Llama3CombinedBot
from data_models.observation import Observation


def get_observation(keyword, questions):
    base_observation_dict = {
        "step": 1,
        "questions": questions,
        "guesses": [],
        "answers": [],
        "role": "answerer",
        "turnType": "answer",
        "keyword": keyword,
        "category": "city",
        "remainingOverageTime": 300.0,
    }

    return Observation(**base_observation_dict)


class TestAnswerer(unittest.TestCase):
    def setUp(self):
        self.model = Llama3CombinedBot(model_dir="../models/Meta-Llama-3-8B-Instruct")

    def test_man_made_object(self):
        assert (
            self.model(
                get_observation("Street sign", questions=["Is the keyword a man-made object?"])
            )
            == "yes"
        )
        assert (
            self.model(
                get_observation("Toaster oven", questions=["Is the keyword a man-made object?"])
            )
            == "yes"
        )
        assert (
            self.model(get_observation("Raccoon", questions=["Is the keyword a man-made object?"]))
            == "no"
        )
        assert (
            self.model(
                get_observation("Anesthesia", questions=["Is the keyword a man-made object?"])
            )
            == "no"
        )

    def test_living_thing(self):
        assert (
            self.model(get_observation("frog", questions=["Is the keyword a living thing?"]))
            == "yes"
        )
        assert self.model(get_observation("frog", questions=["Is the keyword an animal?"])) == "yes"

    def test_edible(self):
        assert self.model(get_observation("edamame", questions=["Is the thing edible?"])) == "yes"
        assert (
            self.model(get_observation("habanero pepper", questions=["Is the thing edible?"]))
            == "yes"
        )
        assert self.model(get_observation("handbag", questions=["Is the thing edible?"])) == "no"
        assert (
            self.model(get_observation("Vending machine", questions=["Is the thing edible?"]))
            == "no"
        )

    def test_electric(self):
        assert (
            self.model(get_observation("flashlight", questions=["Is the thing electronic?"]))
            == "yes"
        )
        assert self.model(get_observation("chisel", questions=["Is the thing electronic?"])) == "no"

    def test_list_of_keywords_question(self):
        assert (
            self.model(
                get_observation(
                    "dog",
                    questions=[
                        "Is the keyword in the following list: ['mammal', 'cat', 'dog', 'sheep', 'cow']?"
                    ],
                )
            )
            == "yes"
        )
        assert (
            self.model(
                get_observation(
                    "chisel",
                    questions=[
                        "Is the keyword in the following list: ['mammal', 'cat', 'dog', 'sheep', 'cow']?"
                    ],
                )
            )
            == "no"
        )

    def test_keyword_starts_with_letter(self):
        assert (
            self.model(
                get_observation(
                    "fur",
                    questions=["Does the keyword start with the letter 'f'?"],
                )
            )
            == "yes"
        )

        assert (
            self.model(
                get_observation(
                    "fur trader",
                    questions=["Does the keyword start with the letter 'a'?"],
                )
            )
            == "no"
        )

    def test_keyword_contains_letters(self):
        assert (
            self.model(
                get_observation(
                    "scoreboard",
                    questions=["Does the keyword contain all of the letters: 'c', 's' and 'b'?"],
                )
            )
            == "yes"
        )
        assert (
            self.model(
                get_observation(
                    "muffin tin",
                    questions=["Does the keyword contain all of the letters: 'f', 'a' and 'u'?"],
                )
            )
            == "no"
        )
