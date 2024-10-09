from sqlalchemy.orm import Session
from schema import ItemCreate
from models import Item

# Create ToDo
def create_todo(db: Session, item: ItemCreate):
    db_item = Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# View all ToDos
def view_todo(db: Session):
    return db.query(Item).all()

# Update ToDo
def update_todo(db: Session, item_id: int, item: ItemCreate):
    todo_item = db.query(Item).filter(Item.id == item_id).first()
    if todo_item is None:
        return None  

    todo_item.title = item.title
    todo_item.description = item.description
    db.commit()
    db.refresh(todo_item)
    return todo_item

# Delete ToDo
def delete_todo(db: Session, item_id: int):
    todo_item = db.query(Item).filter(Item.id == item_id).first()
    if todo_item is None:
        return None  
    db.delete(todo_item)
    db.commit()
    return {"detail": "ToDo item deleted"}
