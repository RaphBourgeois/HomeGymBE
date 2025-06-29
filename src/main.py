from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["https://homegymfe.netlify.app:5000/","https://homegymfe.netlify.app/","*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://homegymfe.netlify.app/:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello, World!from back end"
