from pydantic import BaseModel



class ResearchRequest(BaseModel):
    goal: str