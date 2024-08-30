from typing import Any

import outlines
from bots.base_bot import Bot
from bots.question_tree import question_tree_root, traverse_tree
from data_models.answer import Answer
from data_models.guess import Guess
from data_models.observation import Observation
from data_models.question import Question


class Llama3CombinedBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, obs: Observation) -> Any:
        if obs.turnType == "answer":
            return self.answer(obs)
        elif obs.turnType == "guess":
            return self.guess(obs)
        elif obs.turnType == "ask":
            return self.ask(obs)
        else:
            raise ValueError("Incorrect turnType!")

    def answer(self, obs: Observation) -> str:
        generator = outlines.generate.json(self.model, Answer)
        prompt = answering_prompt(obs)
        # Outlines recommends always printing the actual prompt to avoid bugs
        print(prompt)
        answer = generator(prompt)
        return answer.answer

    def guess(self, obs: Observation) -> str:
        # Predetermined start path to put the LLM on the right track.
        question, guess = traverse_tree(question_tree_root, obs.answers)
        if guess:
            return guess
        generator = outlines.generate.json(self.model, Guess)
        prompt = guess_prompt(obs)
        print(prompt)

        final_guess = None
        # Trick to try preventing the guesser from guessing things that have already been guessed before.
        for _ in range(3):
            answer = generator(prompt)
            # Apply certain postprocessing for chars that are not allowed in the keyword.
            answer.guess = answer.guess.replace("_", " ")
            answer.guess = answer.guess.split(" or ")[0]
            if answer.guess not in obs.guesses:
                final_guess = answer.guess
                break
        return final_guess if final_guess else answer.guess

    def ask(self, obs: Observation) -> str:
        # Predetermined start path to put the LLM on the right track.
        question, guess = traverse_tree(question_tree_root, obs.answers)
        if question:
            return question
        generator = outlines.generate.json(self.model, Question)
        prompt = asker_prompt_thing(obs)
        print(prompt)
        answer = generator(prompt)
        return answer.question


@outlines.prompt
def summariser_prompt(obs):
    """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    # Task
    You are responsible for accurately summarising a historical game of 20 questions into bullet points.
    Only include information in the summary that is essential for the guessing the keyword correctly.
    Remove any irrelevant or factually conflicting information.
    Return the summary in valid JSON in the field 'summary'.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    {{ obs.get_game_history() }}
    <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """


@outlines.prompt
def fact_checker_prompt(obs, summary):
    """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    # Task
    You are responsible for fact checking a summary of 20 questions game against a raw game history event data.

    Think step by step and check that the extracted summary is factually consistent
    with the raw historical event data.

    Then, return the factually consistent summary of the game in valid JSON in the field 'factually_correct_summary'.
    <|eot_id|><|start_header_id|>user<|end_header_id|>

    Here is the raw historical event data:
    {{ obs.get_game_history() }}

    Here is the extracted summary:
    {{ summary }}
    <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """


@outlines.prompt
def guess_prompt(obs: Observation):
    """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    # Role
    You are a master player of the game 20 questions.
    You are accurate, logical, and factual in your approach.
    Your role is to guess the hidden keyword correctly.

    # Task
    You are given history of questions, answers and guesses in the game 20 questions.
    Based on this history you should guess the correct keyword.

    # Keyword type
    The keyword is ALWAYS some sort of a thing.
    Things could be for instance: objects, animals, plants, concepts etc.
    The keyword is NEVER a person or a place.

    Think step by step, reflecting on the game history and the possible correct keywords.
    After thinking, choose the most likely keyword that has not been guessed previously.
    Finally return a valid JSON of type "Guess" where the thinking and reflection are in the 'reasoning' field and the chosen guess is in the 'guess' field. <|eot_id|><|start_header_id|>user<|end_header_id|>
    # Game history
    {{ obs.get_game_history() }}

    # Current Guess
    Question: {{ obs.questions[-1] }}
    Answer: {{ obs.answers[-1] }}
    Guess: <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """


@outlines.prompt
def answering_prompt(obs: Observation):
    """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    # Role
    You are a trivia game expert playing the game 20 questions.
    You are logical, structured, and precise in your answers.

    # Task
    In the game you are given a keyword.
    The guesser will ask you a question about this keyword.
    You must accurately answer this question with either a 'yes' or a 'no'.

    Think step by step, carefully reflecting on the question and the keyword.
    Then return a valid JSON of type "Answer" where the thinking and reflection steps are in the 'reasoning' field and the answer is in the 'answer' field. <|eot_id|><|start_header_id|>user<|end_header_id|>
    Keyword: {{ obs.keyword }}
    Question: {{ obs.questions[-1] }}
    Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """


@outlines.prompt
def asker_prompt_thing(obs: Observation):
    """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    # Role
    You are a master player of the game 20 questions.
    You are insightful, strategic, and logical in your approach.
    Your role is to ask a question about the keyword, so that the guesser is able to guess the keyword correctly.

    # Task
    You are given history of questions, answers and guesses in the game 20 questions.
    Based on this history you should ask an informative question about the keyword that can be only answered with a 'yes' or 'no'.
    Use each answer to inform the next question, focusing on eliminating the largest number of possibilities.
    Ask questions that are short and unambigous.
    Avoid questions that leave room for interpretation.

    # Keyword type
    The keyword is ALWAYS some sort of a thing.
    Things could be for instance: objects, animals, plants, concepts etc.
    The keyword is NEVER a person or a place.

    Analyse the game history step by step listing the key facts in few bullet points.
    Based on this analysis list possible keyword candidates that have not yet been ruled out by the previous questions and answers.
    Finally, craft a question that is likely to split the remaining keyword candidates in half.
    Return a valid JSON of type "Question" where all the analysis and keyword candidate steps are in the 'reasoning' field and the crafted question is in the 'question' field. <|eot_id|><|start_header_id|>user<|end_header_id|>
    # Game history
    {{ obs.get_game_history() }}

    # Current question
    Question: <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """
