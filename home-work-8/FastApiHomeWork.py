# Задание 1
# Создайте сервис для сбора обращения абонентов на основе FastAPI.
# Эндпойнт должен принимать следующие атрибуты:
#
# фамилия – с заглавной буквы, содержит только кирилицу;
# имя – с заглавной буквы, содержит только кирилицу;
# дату рождения;
# номер телефона;
# e-mail.
# Все переданные атрибуты должны валидироваться с помощью модели Pydantic.
# Результат сохраняется на диске в виде json-файла, содержащего переданные атрибуты.
import json
from datetime import date

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

CyrillicStr = Annotated[str, Field(pattern=r"^[А-ЯёЁ][а-яА-ЯёЁ\s]*$")]

class Fio(BaseModel):
    first_name: CyrillicStr
    last_name: CyrillicStr
    birth_date: date
    phone_number: str
    email: str


app = FastAPI()


@app.post("/fio")
def post_fio(fio: Fio):
    with open("files/fio.json", "w", encoding="utf-8") as fio_file:
        fio_file.write(fio.model_dump_json(indent=2) + "\n\n")

    return {"status": "success", "fio": fio.model_dump(mode='json')}


@app.get("/health")
async def health():
    return {"mes": "ok"}




if __name__ == "__main__":
    uvicorn.run(
        "FastApiHomeWork:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )