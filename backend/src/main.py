import uvicorn

from fastapi import FastAPI
from api.router import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=True)

app.include_router(api_router)

origins = [
    "*",
    "http://parcing.3s.by",
    "https://parking.3s.by",
    "http://localhost:8080",
    "https://localhost:8080",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8080",
    "http://10.0.1.106:8080",
    "https://10.0.1.106:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    uvicorn.run(app="main:app", host='0.0.0.0',  port=8000, reload=True)


if __name__ == '__main__':
    main()
