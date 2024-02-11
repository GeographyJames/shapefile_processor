import calculator


class TestCalculator:
    def test_should_perform_addition(self):
        assert calculator.add(1, 2) == 3
