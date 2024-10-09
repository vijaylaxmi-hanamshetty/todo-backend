from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud  
import models  
import schema  

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a single ToDo item
@app.post("/todos/", response_model=schema.ItemResponse)
def create_todo(item: schema.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, item=item)

# View all ToDo items or Read item
@app.get("/todos/", response_model=list[schema.ItemResponse])
def view_todos(db: Session = Depends(get_db)):
    return crud.view_todo(db=db)

# Update a ToDo item
@app.put("/todos/{item_id}", response_model=schema.ItemResponse)
def update_todo(item_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)):
    updated_item = crud.update_todo(db=db, item_id=item_id, item=item)  # Changed 'items' to 'item'
    if updated_item is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return updated_item


# Delete a ToDo item
@app.delete("/todos/{item_id}")
def delete_todo(item_id: int, db: Session = Depends(get_db)):
    result = crud.delete_todo(db=db, item_id=item_id)
    if result is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return {"detail": "ToDo item deleted"}
