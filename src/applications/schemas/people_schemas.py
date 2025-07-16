from datetime import datetime

from pydantic import BaseModel, Field


class People(BaseModel):
    id: str | None = None
    name: str
    age: int
    birthdate: str | datetime
    last_name: str | None = None


