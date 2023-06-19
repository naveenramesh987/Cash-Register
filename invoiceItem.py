from item import Item

class InvoiceItem:
    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:
        self.item = item
        self.qty = qty
        self.discount = discount
        # Private Member
        self._sub_total = (item.price * qty) - discount

    def __repr__(self) -> str:
        return "<class 'InvoiceItem'>"

    def __str__(self) -> str:
        return (
            f"Item => {self.item}, Qty: {self.qty}, Discount: ${self.discount},"
            f" Sub Total: {self.get_sub_total():.2f}"
        )

    def get_sub_total(self) -> float:
        return self._sub_total

    def dict(self) -> dict:
        return {
            "name": self.item.name,
            "quantity": self.qty,
            "discount": self.discount,
            "sub_total": self.get_sub_total(),
        }