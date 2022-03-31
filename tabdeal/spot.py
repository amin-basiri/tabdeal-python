from tabdeal.client import Client
from tabdeal.enums import OrderSides, OrderTypes, RequestTypes, SecurityTypes
from tabdeal.utils import check_new_order_params


class Spot(Client):
    def new_order(
        self,
        symbol: str,
        side: OrderSides,
        type: OrderTypes,
        quantity: int,
        price: float = None,
        stop_price: float = None,
    ):
        check_new_order_params(type, price=price, stop_price=stop_price)

        data = {
            "symbol": symbol,
            "side": side.value,
            "type": type.value,
            "quantity": quantity,
            "price": 0 if not price else price,
            "stopPrice": 0 if not stop_price else stop_price,
        }

        return self.request(
            url="order",
            method=RequestTypes.POST,
            security_type=SecurityTypes.TRADE,
            data=data,
        )

    def get_open_orders(self, symbol: str = None):
        data = dict() if not symbol else dict(symbol=symbol)

        return self.request(
            url="openOrders",
            method=RequestTypes.GET,
            security_type=SecurityTypes.TRADE,
            data=data,
        )

    def get_order(self, symbol: str, order_id: str):
        data = {
            "symbol": symbol,
            "orderId": order_id,
        }

        return self.request(
            url="order",
            method=RequestTypes.GET,
            security_type=SecurityTypes.TRADE,
            data=data,
        )

    def cancel_order(self, symbol: str, order_id: str):
        data = {
            "symbol": symbol,
            "orderId": order_id,
        }

        return self.request(
            url="order",
            method=RequestTypes.DELETE,
            security_type=SecurityTypes.TRADE,
            data=data,
        )