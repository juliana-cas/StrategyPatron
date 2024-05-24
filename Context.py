class TicketPriceCalculator:
    def __init__(self, strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def calculate(self, base_price: int) -> float:
        return self._strategy(base_price)
