class Item:
    def __init__(self, id: int, name: str, price: float, measurementUnit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurementUnit = measurementUnit

    def __repr__(self) -> str:
        return "<class 'Item'>"

    def __str__(self) -> str:
        return f"{self.name}: ${self.price}/{self.measurementUnit}"