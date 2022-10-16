from pydantic import BaseModel, Field

class TrackBase(BaseModel):
    name: str = Field(title="Название трека")
    author_id: int = Field(title="Псевдоним исполнителя")

class Track(TrackBase):
    id: int = Field(title="Идентификатор трека")
    info: dict = Field(title="Информация о треке")
