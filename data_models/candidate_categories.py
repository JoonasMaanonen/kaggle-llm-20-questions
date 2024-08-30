from pydantic import BaseModel


class CandidateCategories(BaseModel):
    candidate1: str
    candidate2: str
    candidate3: str
