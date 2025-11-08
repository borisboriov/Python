from pydantic import BaseModel, field_validator, ValidationError


class User(BaseModel):
    name: str
    email: str
    membership_id: str

    @field_validator("email", mode='before')
    def validate_email(cls, email: str) -> str:
        if "@" not in email:
            raise ValueError("Invalid email address")
        return email
