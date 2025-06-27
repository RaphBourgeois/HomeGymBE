from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["https://685e8bc9c651b36cdd948228--homegymfe.netlify.app:8080", "https://685e8bc9c651b36cdd948228--homegymfe.netlify.app/","https://homegymfe.netlify.app/","https://homegymfe.netlify.app:8080"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")https://github.com/RaphBourgeois/HomeGymBE/branches
def home():
    return "Hello, World!from back end"
