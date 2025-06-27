from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "100.116.235.12:5000","http://127.0.0.1:8080","http://172.27.0.2:8080", "http://172.27.0.3:8080","https://homegymbe.onrender.com", "https://685e8bc9c651b36cdd948228--homegymfe.netlify.app:8080", "https://685e8bc9c651b36cdd948228--homegymfe.netlify.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello, World!from back end"
