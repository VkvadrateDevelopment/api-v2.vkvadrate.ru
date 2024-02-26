from pydantic import BaseModel

class SOrderUpdate(BaseModel):
    ИдентификаторЗаказаVK: str
    ЗаказКлиента_id: str
    ДокументОплаты_id: str = None
    СуммаОплаты: int

class SOrderResult(BaseModel):
    success: bool
    orders: dict
    error: str = None