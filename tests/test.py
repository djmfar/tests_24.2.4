import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1,1) == 2

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self,5,1) == 4

    def test_division_correctly(self):
        assert self.calc.division(self,3,2) == 1.5

    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1,1) == 3

    def test_multiply_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)


    def teardown(self):
        print("Выполнение метода Teardown")