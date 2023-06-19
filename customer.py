class Customer:
    def __init__(self, firstName: str, lastName: str) -> None:
        self.firstName = firstName;
        self.lastName = lastName;

    def __repr__(self) -> str:
        return "<class 'Customer'>"

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"