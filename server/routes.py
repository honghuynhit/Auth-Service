from fastapi import APIRouter, Body, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.config.config import Config
from server.model import NoteSchema
from server.utils.pagination import ss_pagination

router = APIRouter()
config = Config()


@router.get("/")
def get_notes(request: Request) -> dict:
    try:
        filter = {}
        projection = {'_id': False}
        notes = config.MONGO_CLIENT[f'{config.DB_NAME}']['user'].find(filter=filter, projection=projection)
        api_data = []
        for  _api in notes:
            api_data.append(_api)
        return JSONResponse(content={'data': api_data}, status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
    # print(notes)
    # return {
    #     "data": jsonable_encoder(notes)
    # }

# @router.get("/{id}")
# async def get_note(id: str) -> dict:
#     if int(id) > len(notes):
#         return {
#             "error": "Invalid note ID"
#         }

#     for note in notes.keys():
#         if note == id:
#             return {
#                 "data": notes[note]
#             }

#     return {
#         "Error": "Invalid ID"
#     }

# @router.post("/")
# def add_note(note: NoteSchema = Body(...)) -> dict:
#     notes[str(len(notes)+1)] = note.dict()

#     return {
#         "message": "Note added successfully"
#     }
# #
# @router.put("/{id}")
# def update_note(id: str, note: NoteSchema):
#     stored_note = notes[id]
#     if stored_note:
#         stored_note_model = NoteSchema(**stored_note)
#         update_data = note.dict(exclude_unset=True)
#         updated_note = stored_note_model.copy(update=update_data)
#         notes[id] = jsonable_encoder(updated_note)
#         return {
#             "message": "Note updated successfully"
#         }
#     return {
#         "error": "No such note exist"
#     }

# @router.delete("/{id}")
# def delete_note(id: str) -> dict:
#     if int(id) > len(notes):
#         return {
#             "error": "Invalid note ID"
#         }

#     for note in notes.keys():
#         if note == id:
#             del notes[note]
#             return {
#                 "message": "Note deleted"
#             }

#     return {
#         "error": "Note with {} doesn't exist".format(id)
#     }

