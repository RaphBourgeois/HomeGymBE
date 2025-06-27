from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://685e8bc9c651b36cdd948228--homegymfe.netlify.app:8080", "https://685e8bc9c651b36cdd948228--homegymfe.netlify.app/",https://homegymfe.netlify.app/,https://homegymfe.netlify.app:8080],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello, World!from back end"
