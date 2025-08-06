import uuid
from datetime import datetime, UTC

from pydantic import BaseModel, Field, model_validator


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None


class Item(ItemBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime
    updated_at: datetime

    @model_validator(mode="before")
    def set_timestamps(cls, values):
        now = datetime.now(UTC)
        values["created_at"] = values.get("created_at", now)
        values["updated_at"] = values.get("updated_at", now)
        return values
