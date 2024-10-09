from pydantic import BaseModel
class ItemBase(BaseModel):
    title:str
    description: str |None
    
class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id:int
    class Config:
        from_attribute = True