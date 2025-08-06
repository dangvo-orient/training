from datetime import datetime, UTC
from typing import Any

from app.models import Item, ItemCreate, ItemUpdate
from fastapi import APIRouter, HTTPException

router = APIRouter()

items: dict[str, Item] = {}


@router.post("", response_model=Item)
def create_item(item_create: ItemCreate) -> Any:
    # Create the item
    item = Item(**item_create.model_dump())

    # Save to the database
    items[item.id] = item

    return item


@router.get("", response_model=list[Item])
def retrieve_items() -> Any:
    return [v for v in items.values()]


@router.get("/{item_id}", response_model=Item)
def retrieve_item(item_id: str) -> Any:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: str, item_update: ItemUpdate) -> Any:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    # Get the existing item
    item = items[item_id]

    # Update the data
    updated_data = item_update.model_dump(exclude_unset=True)

    for k, v in updated_data.items():
        setattr(item, k, v)

    item.updated_at = datetime.now(UTC)

    # Save to the database
    items[item.id] = item
    return item


@router.delete("/{item_id}")
def delete_item(item_id: str) -> dict[str, Any]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    del items[item_id]

    return {"message": f"Successfully deleted item '{item_id}'"}
