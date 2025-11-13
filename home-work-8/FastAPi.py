import uvicorn
from fastapi import FastAPI


LANGUAGES ={
    1: "C++",
    2: "Python",
    3: "GO"
}

app = FastAPI()

@app.post("/fio/{}")

@app.get("/helth")
async def helth():
    return {"mes": "ok"}

@app.get("/langue/{item_id}")
async def lang(item_id):
    return {"mes": LANGUAGES.get(int(item_id), "js")}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )