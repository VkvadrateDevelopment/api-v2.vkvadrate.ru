from pydantic import BaseModel
from typing import Optional

class SOrderUpdate(BaseModel):
    ИдентификаторЗаказаVK: str
    ЗаказКлиента_id: str
    ДокументОплаты_id: Optional[str] = None
    СуммаОплаты: int

class SOrderResult(BaseModel):
    success:bool
    error:Optional[str] = None