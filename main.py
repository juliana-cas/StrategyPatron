from Context import TicketPriceCalculator
from Strategy import adult_price_strategy, child_price_strategy, student_price_strategy

if __name__ == "__main__":

    calculator = TicketPriceCalculator(adult_price_strategy)
    print("Client: Strategy is set to adult pricing.")
    print("Adult price:", calculator.calculate(100))
    print()


    calculator.strategy = child_price_strategy
    print("Client: Strategy is set to child pricing.")
    print("Child price:", calculator.calculate(100))
    print()


    calculator.strategy = student_price_strategy
    print("Client: Strategy is set to student pricing.")
    print("Student price:", calculator.calculate(100))
