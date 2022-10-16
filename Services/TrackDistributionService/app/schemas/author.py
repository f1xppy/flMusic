from pydantic import BaseModel, Field
from typing import Optional


class AuthorBase(BaseModel):
    name: str = Field(title="Псевдоним исполнителя")
    description: Optional[str] = Field(title="Описание исполнителя")


class Author(AuthorBase):
    id: int = Field(title="Идентификатор исполнителя")
    tracks: list = Field(title="Идентификаторы треков исполнителя")
    info: dict = Field(title="Информация о исполнителе")

