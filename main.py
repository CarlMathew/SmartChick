from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import emailSending

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials= True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

app.include_router(emailSending.router)
