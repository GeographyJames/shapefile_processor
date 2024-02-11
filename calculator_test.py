import calculator


class TestCalculator:
    def test_should_perform_addition(self):
        assert calculator.add(1, 2) == 3

    def test_should_perform_subtraction(selp):
        assert calculator.subtract(2, 1) == 1
