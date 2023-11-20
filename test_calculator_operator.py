import calculatorOperator


class TestInputGetter:
    def test_sum(self):
        result = calculatorOperator.sum(3, 5)
        assert result == 8

        result = calculatorOperator.sum(3, -5)
        assert result == -2

    def test_subtraction(self):
        result = calculatorOperator.subtraction(3, 5)
        assert result == -2

        result = calculatorOperator.subtraction(3, -5)
        assert result == 8

    def test_multiplication(self):
        result = calculatorOperator.multiplication(3, 5)
        assert result == 15

        result = calculatorOperator.multiplication(3, -5)
        assert result == -15

    def test_division(self):
        result = calculatorOperator.division(3, 5)
        assert result == 0.6

        result = calculatorOperator.division(3, -5)
        assert result == -0.6
