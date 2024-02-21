from typing import Dict

from fastapi import APIRouter
from schemas import SOrderUpdate, SOrderResult

router = APIRouter(
    prefix='/v1',
    tags=['Вквадрате API'],
)

@router.post('/order')
async def update_order(order: SOrderUpdate) -> SOrderUpdate:
    return order