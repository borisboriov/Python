from pydantic import BaseModel, field_validator


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: list[str]

    @field_validator("categories")
    def validate_categories(cls, v: list[str]) -> list[str]:
        if not v:
            raise ValueError("Book must have at least one category")
        if len(v) > 5:
            raise ValueError("Book cannot have more than 5 categories")
        return v
