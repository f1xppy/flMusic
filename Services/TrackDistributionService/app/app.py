from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas.author import Author, AuthorBase
from .schemas.track import Track, TrackBase
import typing

FAKE_AUTHOR_INFO = {
    "real_name": "Андрей Федотов",
    "country": "Россия"
}

FAKE_TRACK_INFO = {
    "date": "15.10.2022",
    "label": "Nedostupnost"
}

app = FastAPI(
    version="1", title="Track Distribution Service"
)
authors: typing.Dict[int, Author] = {}
tracks: typing.Dict[int, Track] = {}


@app.post(
    "/authors", status_code=201, response_model=Author, summary="Добавляет исполнителя в базу"
)
async def add_author(author: AuthorBase) -> Author:
    authid = int(len(authors) + 1)
    tr = []
    if authid in tracks:
        i = 1
        while i != len(tracks)+1:
            if tracks[i].author_id == authid: tr.append(i)
            i += 1





    result = Author(
        **author.dict(), id=len(authors) + 1, tracks=tr, info=FAKE_AUTHOR_INFO
    )
    authors[result.id] = result
    return result


@app.post("/tracks", status_code=202, response_model=Track, summary="Добавляет трек в базу")
async def add_track(track:TrackBase) -> Track:
    result = Track(
        **track.dict(), id = len(tracks)+1, info = FAKE_TRACK_INFO
    )
    tracks[result.id] = result
    return result


@app.get(
    "/authors", summary="Возвращает список исполнителей", response_model=list[Author]
)
async def get_authors_list() -> typing.Iterable[Author]:
    return [v for k, v in authors.items()]



@app.get(
    "/tracks", summary="Возвращает список треков", response_model=list[Track]
)
async def get_tracks_list() -> typing.Iterable[Track]:
    return [v for k, v in tracks.items()]



@app.get(
    "/authors/{authorId}", summary="Возвращает информацию о конкретном исполнителе"
)
async def get_author_info(authorId: int) -> Author:
    if authorId in authors: return authors[authorId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})



@app.get(
    "/tracks/{trackId}", summary="Возвращает информацию о конкретном треке"
)
async def get_track_info(trackId: int) -> Track:
    if trackId in tracks: return tracks[trackId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.put(
    "/authors/{authorId}", summary="Обновляет информацию об исполнителе"
)
async def update_author(authorId: int, author: AuthorBase) -> Author:
    if authorId in authors:
        authid = authorId
        tr = []
        if authid in tracks:
            i = 1
            while i != len(tracks)+1:
                if tracks[i].author_id == authid: tr.append(i)
                i += 1
        result = Author(
            **author.dict(), id=authorId, tracks=tr, info=FAKE_AUTHOR_INFO
        )
        authors[authorId] = result
        return authors[authorId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.delete("/authors/{authorId}", summary="Удаляет исполнителя из базы")
async def delete_author(authorId: int) -> Author:
    if authorId in authors:
        del authors[authorId]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.delete("/tracks/{trackId}", summary="Удаляет трек из базы")
async def delete_track(trackId: int) -> Track:
    if trackId in tracks:
        del tracks[trackId]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

