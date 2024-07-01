import pytest

from src.exceptions import HeadHunterAPIException


def test_get_data(hh_api):
    with pytest.raises(HeadHunterAPIException):
        hh_api.get_data()