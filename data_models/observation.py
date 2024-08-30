import itertools
from typing import Iterator, Literal

from pydantic import BaseModel


class Observation(BaseModel):
    step: int
    role: Literal["guesser", "answerer"]
    turnType: Literal["ask", "answer", "guess"]
    keyword: str
    category: str
    questions: list[str]
    answers: list[str]
    guesses: list[str]
    remainingOverageTime: float

    @property
    def empty(self) -> bool:
        return all(len(t) == 0 for t in [self.questions, self.answers, self.guesses])

    def get_history(self) -> Iterator[tuple[str, str, str]]:
        return zip(self.questions, self.answers, self.guesses)

    def get_game_history(self) -> str:
        return "\n".join(
            f"""
Question: {question}
Answer: {answer}
Guess: {guess}
Incorrect guess!"""
            for turn, (question, answer, guess) in enumerate(self.get_history())
        )

    def get_history_text(self, *, include_guesses: bool = False) -> str:
        return f"""
            <|user|>
            Previous Questions: {self.questions}
            Previous Answers: {self.answers}
            Previous Guesses: {self.guesses} <|end|>
            """

    def get_history_text_llama(self, *, include_guesses: bool = False) -> str:
        return f"""
            Previous Questions: {self.questions}
            Previous Answers: {self.answers}
            """
