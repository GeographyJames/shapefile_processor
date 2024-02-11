from src.app import calculator


class TestCalculator:
    def test_should_perform_addition(self):
        assert calculator.add(1, 2) == 3

    def test_should_perform_subtraction(self):
        assert calculator.subtract(2, 1) == 1

    def test_should_perform_multiplication(self):
        assert calculator.multiply(4, 4) == 16

    def test_should_perform_exponential_operation(self):
        assert calculator.exponent(3, 2) == 9

    def test_should_perform_division(self):
        assert calculator.divide(8, 2) == 4
