from pydantic import BaseModel


class Guess(BaseModel):
    reasoning: str
    guess: str
