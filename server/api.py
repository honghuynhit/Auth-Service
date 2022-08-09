from fastapi import FastAPI


from server.config.config import Config
from .routes import router as NoteRouter

app = FastAPI()

config = Config()
# setting = Settings()

# @lru_cache()
# def get_settings():
#     '''But as we are using the @lru_cache() decorator on top, the Settings object will be created only once, the first time it's called.
#     '''
#     return Settings()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }



app.include_router(NoteRouter, prefix="/note")