from pydantic import BaseModel


class ProfileCreateUpdateSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    gender: bool
