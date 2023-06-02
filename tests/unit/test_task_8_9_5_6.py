import pytest

from task_8_9.task_8_9_5_6 import is_leap_year, input_validation_month, input_validation_year


@pytest.mark.parametrize('input_param, expected', [(2020, 'Leap'), (2015, 'Ordinary')])
def test_is_leap_year(input_param, expected):
    actual = is_leap_year(input_param)
    assert expected == actual


def test_input_validation_month_negative(monkeypatch, capsys):
    input_values = ['Ghr', 'September']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    input_validation_month()
    captured = capsys.readouterr()
    assert captured.out == 'The entered month does not exist\n'


def test_input_validation_month(monkeypatch):
    input_values = ['September']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    actual = input_validation_month()
    assert actual == (30, 'September')


def test_input_validation_year_negative(monkeypatch, capsys):
    input_values = ['-2023', '2023']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    input_validation_year()
    captured = capsys.readouterr()
    assert captured.out == 'year cannot be negative\n'


def test_input_validation_year(monkeypatch):
    input_values = ['2023']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    actual = input_validation_year()
    assert actual == 2023