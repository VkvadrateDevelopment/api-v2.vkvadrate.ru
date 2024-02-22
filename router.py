from fastapi import APIRouter
from schemas import SOrderUpdate

router = APIRouter(
    prefix='/v1',
    tags=['Вквадрате API'],
)

@router.post('/order')
async def update_order(orders: list[SOrderUpdate]) -> list[SOrderUpdate]:
    
    return orders