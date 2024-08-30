from typing import Literal

from pydantic import BaseModel


class Answer(BaseModel):
    reasoning: str
    answer: Literal["yes", "no"]
