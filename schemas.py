from pydantic import BaseModel
from fastapi import Header


class GettingValues(BaseModel):
    values: str