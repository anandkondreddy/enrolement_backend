from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import students

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
