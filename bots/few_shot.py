def guess_examples_short():
    examples = [
        {
            "questions": ["Is the keyword a place?"],
            "answers": ["yes"],
            "guesses": [],
            "guess": "Iceland",
        },
        {
            "questions": ["Is the keyword a place?"],
            "answers": ["no"],
            "guesses": [],
            "guess": "carrot",
        },
        {
            "questions": ["Is the keyword a place?"],
            "answers": ["yes"],
            "guesses": [],
            "guess": "Afghanistan",
        },
        {
            "questions": ["Is the keyword a place?"],
            "answers": ["no"],
            "guesses": [],
            "guess": "iron",
        },
    ]
    return examples


def guess_examples():
    examples = [
        {
            "questions": ["Is the keyword a place"],
            "answers": ["no"],
            "guesses": [],
            "guess": "tree",
        },
        {
            "questions": ["Is the keyword a place"],
            "answers": ["yes"],
            "guesses": [],
            "guess": "Amsterdam",
        },
        {
            "questions": ["Is the keyword a place", "Is the keyword in Europe"],
            "answers": ["yes", "yes"],
            "guesses": ["Mount Everest"],
            "guess": "Germany",
        },
        {
            "questions": ["Is the keyword a place", "Is the keyword an animal?"],
            "answers": ["no", "yes"],
            "guesses": ["snail"],
            "guess": "bear",
        },
        {
            "questions": [
                "Is the keyword a place",
                "Is the keyword in Europe",
                "Does the keyword start with the letter 'a'",
            ],
            "guesses": ["Amsterdam", "Germany"],
            "answers": ["yes", "yes", "yes"],
            "guess": "Armenia",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword in Europe?",
                "Is the keyword a country?",
                "Is the keyword in Asia?",
                "Is the keyword the biggest country on its continent?",
            ],
            "guesses": ["Croatia", "Indonesia", "Kenya", "Japan"],
            "answers": ["yes", "no", "yes", "yes", "yes"],
            "guess": "China",
        },
        {
            "questions": [
                "Is the keyword a place",
                "Is the keyword an animal?",
                "Is the keyword man-made?",
                "Is the keyword hand-held?",
            ],
            "answers": ["no", "no", "yes", "yes"],
            "guesses": [
                "fork",
                "ship",
                "car wheel",
            ],
            "guess": "phone",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword in Europe?",
                "Is the keyword in South America?",
                "Is the keyword a country?",
            ],
            "guesses": ["Croatia", "Indonesia", "Amazon"],
            "answers": ["yes", "no", "yes"],
            "guess": "Argentina",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword an animal?",
                "Can the keyword fly?",
            ],
            "answers": ["no", "no", "yes"],
            "guesses": [
                "fork",
                "ship",
            ],
            "guess": "plane",
        },
    ]
    return examples


def ask_examples():
    examples = [
        {"questions": [], "answers": [], "guesses": [], "question": "Is the keyword a place?"},
        {
            "questions": ["Is the keyword a place?"],
            "answers": ["yes"],
            "guesses": ["Finland"],
            "question": "Is the keyword in Europe?",
        },
        {
            "questions": ["Is the keyword a place?", "Is the keyword in Europe?"],
            "answers": ["yes", "yes"],
            "guesses": ["Finland", "Stockholm"],
            "question": "Is the keyword a country?",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword in Europe?",
                "Is the keyword a country?",
            ],
            "answers": ["yes", "yes", "no"],
            "guesses": ["Spain", "Paris", "Barcelona"],
            "question": "Is the keyword a city?",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword in Europe?",
                "Is the keyword a country?",
                "Is the keyword a city?",
            ],
            "answers": ["yes", "yes", "no", "no"],
            "guesses": ["Algeria", "Turkey", "Ankara"],
            "question": "Is the keyword a river?",
        },
        {
            "questions": [
                "Is the keyword a place",
                "Is the keyword in Europe?",
                "Is the keyword a country?",
                "Is the keyword a city?",
                "Is the keyword a river?",
            ],
            "answers": ["yes", "yes", "no", "no", "yes"],
            "guesses": ["India", "Croatia", "Vilna", "Matterhorn"],
            "question": "Is the keyword river?",
        },
        {
            "questions": [
                "Is the keyword a place?",
            ],
            "guesses": ["fork"],
            "answers": ["no"],
            "question": "Is the keyword man-made?",
        },
        {
            "questions": ["Is the keyword a place?", "Is the keyword man-made?"],
            "guesses": ["fork", "tree"],
            "answers": ["no", "no"],
            "question": "Does the keyword breathe?",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword man-made?",
                "Does the keyword breathe?",
            ],
            "guesses": ["fork", "tree", "cat"],
            "answers": ["no", "no", "yes"],
            "question": "Is the keyword a mammal?",
        },
        {
            "questions": [
                "Is the keyword a place?",
                "Is the keyword a city?",
                "Is the keyword a country?",
                "Is the keyword a Southern European country?",
                "Does the country have a land border with Spain?",
            ],
            "guesses": ["Iraq", "China", "Kenya"],
            "answers": ["yes", "no", "yes", "yes", "yes"],
            "question": "Is the country Portugal?",
        },
        {"questions": [], "answers": [], "guesses": [], "question": "Is the keyword a place?"},
    ]
    return examples


def answer_examples_v2_less_is_more():
    examples = [
        {"question": "Is the keyword a place?", "keyword": "Somalia", "answer": "yes"},
        {"question": "Is the keyword a thing?", "keyword": "dog", "answer": "yes"},
        {"question": "Is the keyword a place?", "keyword": "mobile phone", "answer": "no"},
        {"question": "Is the keyword a thing?", "keyword": "Reykjavik", "answer": "no"},
        {"question": "Is the keyword a place?", "keyword": "Rhine", "answer": "yes"},
        {"question": "Is the keyword a thing?", "keyword": "dog", "answer": "yes"},
        {"question": "Is the keyword a place?", "keyword": "moss", "answer": "no"},
        {"question": "Is the keyword a thing?", "keyword": "Kathmandu", "answer": "no"},
    ]
    return examples


def answer_examples_short():
    examples = [
        {
            "question": "Is the keyword a city?",
            "keyword": "chicago illinois",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a city?",
            "keyword": "kemi finland",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a country?",
            "keyword": "malmo sweden",
            "answer": "no",
        },
        {
            "question": "Is the keyword a state?",
            "keyword": "columbus ohio",
            "answer": "no",
        },
    ]
    return examples


def answer_examples():
    examples = [
        {"question": "Is the keyword a place?", "keyword": "mouse", "answer": "no"},
        {"question": "Is it a place?", "keyword": "angola", "answer": "yes"},
        {"question": "Is the keyword a country?", "keyword": "russia", "answer": "yes"},
        {"question": "Is the keyword a thing?", "keyword": "rock", "answer": "yes"},
        {"question": "Is the keyword a thing?", "keyword": "lithuania", "answer": "no"},
        {"question": "Can the keyword breathe?", "keyword": "oman", "answer": "no"},
        {
            "question": "Does the keyword share a border with Russia?",
            "keyword": "Finland",
            "answer": "yes",
        },
        {
            "question": "Does it start with the letter 'a'?",
            "keyword": "Armenia",
            "answer": "yes",
        },
        {
            "question": "Does the country start with the letter 'd'?",
            "keyword": "Singapore",
            "answer": "no",
        },
        {
            "question": "does the thing end in the letter 'E'",
            "keyword": "Europe",
            "answer": "yes",
        },
        {
            "question": "Is the thing related to food or drink in any way?",
            "keyword": "milk",
            "answer": "yes",
        },
        {
            "question": "Does any of the following letter: 'a', 'b', 'c', 'd', 'j', 'e' equals to the first letter of the keyword in lower or upper case?",
            "keyword": "Antarctica",
            "answer": "yes",
        },
        {
            "question": "Is it a thing?",
            "keyword": "salt packet",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a place?",
            "keyword": "cup of coffee",
            "answer": "no",
        },
        {
            "question": "Is it something that can be held in your hand?",
            "keyword": "mango",
            "answer": "yes",
        },
        {
            "question": "Does the keyword start with the letter 'd'?",
            "keyword": "deer",
            "answer": "yes",
        },
        {
            "question": "Does the keyword start with the letter 's'?",
            "keyword": "Suriname",
            "answer": "yes",
        },
        {
            "question": "Is the thing a place?",
            "keyword": "Matterhorn",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a city???",
            "keyword": "santiago chile",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a country?",
            "keyword": "duck",
            "answer": "no",
        },
        {
            "question": "Is the keyword a thing?",
            "keyword": "river",
            "answer": "no",
        },
        {
            "question": "Is the keyword a thing?",
            "keyword": "mountain",
            "answer": "no",
        },
        {
            "question": "Is the keyword a thing?",
            "keyword": "country",
            "answer": "no",
        },
        {
            "question": "Is the keyword a thing?",
            "keyword": "city",
            "answer": "no",
        },
        {
            "question": "Is the keyword in the following list: ['russia', 'china', 'canada', 'united states']?",
            "keyword": "canada",
            "answer": "yes",
        },
        {
            "question": "Is the keyword a place?",
            "keyword": "gun",
            "answer": "no",
        },
        {
            "question": "Is the keyword a place?",
            "keyword": "cat",
            "answer": "no",
        },
        {
            "question": "Is the keyword a place?",
            "keyword": "tool",
            "answer": "no",
        },
        {
            "question": "Is the word contained in the list: ['duck', 'dog', 'bird', 'mouse']?",
            "keyword": "venezuela",
            "answer": "no",
        },
        {
            "question": "Is the place a river in Finland?",
            "keyword": "kemijoki",
            "answer": "yes",
        },
    ]
    return examples
