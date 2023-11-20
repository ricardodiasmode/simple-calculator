import builtins
from unittest.mock import patch

import calculatorOperator
from inputGetter import get_user_input


class TestInputGetter:
    def test_valid_input(self):
        input_str = "5 + 3"
        expected_result = ["5", "+", "3"]

        with patch.object(builtins, 'input', lambda: input_str):
            result = get_user_input()

        assert result == expected_result

    def test_invalid_input(self):
        input_str = "invalid input"
        expected_result = (None, None, None)

        with patch.object(builtins, 'input', lambda: input_str):
            result = get_user_input()

        assert result == expected_result

    def test_invalid_format_output(self, capsys):
        input_str = "invalid input"
        expected_output = "Invalid input format. Please use the format: {number} {operator} {number}\n"

        with patch.object(builtins, 'input', lambda: input_str):
            get_user_input()

        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_valid_operations(self):
        result = calculatorOperator.operation(5, 3, "+")
        assert result == 8

        result = calculatorOperator.operation(5, 3, "-")
        assert result == 2

        result = calculatorOperator.operation(5, 3, "*")
        assert result == 15

        result = calculatorOperator.operation(6, 3, "/")
        assert result == 2

    def test_invalid_operator(self):
        result = calculatorOperator.operation(5, 3, "%")
        assert result is None
