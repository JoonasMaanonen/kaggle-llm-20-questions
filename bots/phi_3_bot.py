from typing import Any

import outlines
from bots.base_bot import Bot
from data_models.candidate_categories import CandidateCategories
from data_models.guess import Guess
from data_models.observation import Observation
from data_models.question import Question
from bots.few_shot import answer_examples, ask_examples, guess_examples


class Phi3Answerer(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, obs: Observation) -> Any:
        generator = outlines.generate.choice(self.model, ["yes", "no"])
        prompt = answering_prompt(obs, answer_examples())
        # Outlines recommends always printing the actual prompt to avoid bugs
        print(prompt)
        answer = generator(prompt)
        return answer


class Phi3Asker(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, obs: Observation) -> Any:
        if len(obs.questions) == 0:
            return Question(content="Is the keyword a place?")
        generator = outlines.generate.json(self.model, Question)
        prompt = ask_prompt(obs, ask_examples())
        print(prompt)
        answer = generator(prompt)
        return answer


class Phi3Analyser(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, obs: Observation) -> Any:
        generator = outlines.generate.json(self.model, CandidateCategories)
        prompt = analyse_game_history(obs)
        print(prompt)
        answer = generator(prompt)
        return answer


class Phi3Guesser(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, obs: Observation) -> Any:
        generator = outlines.generate.json(self.model, Guess)
        prompt = guess_prompt(obs, guess_examples())
        print(prompt)
        answer = generator(prompt)
        return answer


@outlines.prompt
def analyse_game_history(obs: Observation):
    """
    <|system|>
    # Role
    You are a master analyser of the game 20 questions.
    You carefully provide accurate, thoughtful, nuanced analysis, and are brilliant at reasoning.
    Your task is to accurately analyse the game history of the game 20 questions.

    # Game rules
    In the game 20 questions, the goal is to guess a keyword by asking yes or no questions.
    Each question brings one closer to the keyword by eliminating possibilities.
    The keyword can only be a place or a thing.
    Example of places are but not limited to: countries, cities, rivers, mountains, etc.
    Example of things are but not limited to: animals, objects, food, tools, etc.

    # Game History
    {{ obs.get_game_history() }}

    Think step by step and provide a detailed analysis of the game history.
    After the analysis return the 3 most likely categories for the keyword based on the current information.

    # Output format
    Answer in valid JSON.
    Here is the schema for the output:
    CandidateCategories:
        candidate1 (str): the most likely category for the keyword
        candidate2 (str): the second most likely category for the keyword
        candidate3 (str): the third most likely category for the keyword <|end|>
    """


@outlines.prompt
def ask_prompt(obs: Observation, examples: dict):
    """
    <|system|>
    # Role
    You are a master player of the game 20 questions.
    You are insightful, strategic, and structured in your approach.

    # Task
    You are given history of questions, guesses and answers in the game 20 questions.
    Based on this history you should ask an informative question about the keyword that can be only answered with a yes or no.
    The keyword can only be a place or a thing.
    DO NOT ask questions that have been previously asked in the game history.
    Try to deduce the keyword by narrowing the questions from general to specific, in hopes of guessing the word in the fewest number of questions.
    Ensure that each question focuses on a single attribute or feature.
    Compose your question without using the conjunction 'or'
    Try to make questions short.

    # OUTPUT INSTRUCTIONS
    Answer in valid JSON.
    Here is the schema for the output:
    Question:
        content (str): the question string

    Think step by step and return a valid JSON of type "Question" where the content field is the actual question. <|end|>

    {% for example in examples %}
    <|user|>
    Previous Questions: {{ example.questions }}
    Previous Answers: {{ example.answers }}
    Previous Guesses: {{ example.guesses }} <|end|>
    <|assistant|>
    {{ example.question }} <|end|>
    {% endfor %}

    {{ obs.get_history_text(include_guesses=True) }}
    <|assistant|>
    """


@outlines.prompt
def guess_prompt(obs: Observation, examples: dict):
    """
    <|system|>
    # Role
    You are a master player of the game 20 questions.
    You are accurate, focused, and structured in your approach.

    # Task
    You are given history of questions, guesses and answers in the game 20 questions.
    Based on this history you will try to guess the correct keyword with precision and clarity.
    The keyword can only be a place or a thing.
    Do not guess keywords that have been previously guessed in the game history.

    # OUTPUT INSTRUCTIONS
    Answer in valid JSON.
    Here is the schema for the output:
    Guess:
        content (str): the guess string

    Think step by step and return a valid JSON of type "Guess" where the content field is the actual guess. <|end|>

    {% for example in examples %}
    <|user|>
    Previous Questions: {{ example.questions }}
    Previous Answers: {{ example.answers }}
    Previous Guesses: {{ example.guesses }} <|end|>
    <|assistant|>
    {{ example.guess }} <|end|>
    {% endfor %}
    {{ obs.get_history_text(include_guesses=True) }}
    <|assistant|>
    """


@outlines.prompt
def answering_prompt(obs: Observation, examples: dict):
    """
    <|system|>
    # Role
    You are a master player of the game 20 questions.
    You are accurate, focused and structured in your approach.
    You will answer questions with precision and clarity.

    # Task
    You are given a keyword, which is either a place or a thing.
    Ignore the case of the keyword.
    The guesser will ask you a question about the keyword.
    Ignore the case of the question.
    You must answer this question with either a 'yes' or a 'no'.
    Only answer with 'yes' or 'no', even if the question cannot be answered with those words.

    Think step by step and return 'yes' or 'no' to the question about the keyword. <|end|>

    {% for example in examples %}
    <|user|>
    Question: {{ example.question }}
    Keyword: {{ example.keyword }} <|end|>
    <|assistant|>
    {{ example.answer }} <|end|>
    {% endfor %}

    <|user|>
    Question: {{ obs.questions[-1] }}
    Keyword: {{ obs.keyword }} <|end|>
    <|assistant|>
    """
