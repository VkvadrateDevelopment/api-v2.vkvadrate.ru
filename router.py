from fastapi import APIRouter
from schemas import SOrderUpdate, SOrderResult
import requests

router = APIRouter(
    prefix='/v1',
    tags=['Вквадрате API'],
)

@router.post('/order')
async def update_order(orders: list[SOrderUpdate]):
    res = {
        'success': False,
        'error': 'Order id 1c empty'
    }
    orders_dict = {}
    for order in orders:
        if len(order.ЗаказКлиента_id)>0:
            if len(order.ДокументОплаты_id) > 0:
                res = {
                    'success': True,
                    'error': ''
                }
                #добавляем оплату к заказу
                #res = requests.get()
                orders_dict[order.ЗаказКлиента_id] = 'order_payment_add'
            else:
                # обновляем или создаем заказ
                res = {
                    'success': True,
                    'error': ''
                }
                orders_dict[order.ЗаказКлиента_id] = 'order_update'
        else:
            res = {
                'success': False,
                'error': 'Order id 1c empty'
            }

    #     if len(order['ДокументОплаты_id']) > 0:
    #         res = {
    #             'success': False,
    #             'error': 'Order id 1c empty'
    #         }
    #         #добавляем оплату к заказу
    #         #res = requests.get()
    #     else:
    #         # обновляем или создаем заказ
    #         if len(order['ЗаказКлиента_id'])>0:
    #             res = {
    #                 'success': True,
    #                 'error': ''
    #             }
    #             #res = requests.get('https://erp-dev.vkvadrate.ru/api/orders/update-order-status/?order-id=', order['ЗаказКлиента_id'])
    #         else:
    #             res = {
    #                 'success': False,
    #                 'error': 'Order id 1c empty'
    #             }
    #     orders_id_str = orders_id_str, str(order['ЗаказКлиента_id']), ', '
    order_result = SOrderResult(
        success=res['success'],
        orders=orders_list,
        error=res['error']
    )

    #return order_result
    return order_result