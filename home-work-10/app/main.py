from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import students

app = FastAPI(title="Student CRUD API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)

@app.get("/")
def root():
    return {"message": "Student CRUD API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "healthy"}
