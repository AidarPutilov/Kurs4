import requests
from requests import JSONDecodeError
from abc import ABC, abstractmethod

from src.exceptions import HeadHunterAPIException
from src.settings import HEAD_HUNTER_URL


class ParserAPI(ABC):
    """ Абстрактный класс для чтения данных через API """

    @abstractmethod
    def get_data(self) -> list[dict]:
        pass


class HeadHunterAPI(ParserAPI):
    """ Класс для работы с API HeadHunter """

    def __init__(self, search_word) -> None:
        self.url = HEAD_HUNTER_URL
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'locale': 'RU',
            'text': search_word,
            'page': 0,
            'per_page': 100,
        }

    def get_data(self) -> list[dict]:
        """ Выполнение запроса к HH, получение данных, обработка простых ошибок """
        if self.params['text'] == '':
            raise HeadHunterAPIException('Поисковый запрос не задан')
        vacancies = []
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            is_allowed = response.status_code == 200
            if not is_allowed:
                raise HeadHunterAPIException(f'Ошибка запроса данных status_code: {response.status_code}, {response.text}')
            try:
                vacancies_ = response.json()['items']
                vacancies.extend(vacancies_)
                self.params['page'] += 1
            except JSONDecodeError:
                raise HeadHunterAPIException(f'Ошибка обработки данных данных {response.text}')
        return vacancies


if __name__ == '__main__':
    pass
