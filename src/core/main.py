import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from users.routes import router as user_router


origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=user_router, prefix="/users")


@app.get("/")
async def root():
    return {"message": "Hello world!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
