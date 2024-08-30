from pydantic import BaseModel


class Question(BaseModel):
    reasoning: str
    question: str
