import requests
from abc import ABC, abstractmethod
from src.settings import HEAD_HUNTER_URL, ITEMS_PER_PAGE, PAGES_OF_ITEMS, DATA_FILE_PATH


class ParserAPI(ABC):
    """ Абстрактный класс для чтения данных через API """

    def __init__(self, work_file):
        self.work_file = work_file

    @abstractmethod
    def load_data_from_url(self):
        pass


class HeadHunterAPI(ParserAPI):
    """ Класс для работы с API HeadHunter """
    def __init__(self, work_file):
        self.url = HEAD_HUNTER_URL
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': ITEMS_PER_PAGE}
        self.vacancies = []
        super().__init__(work_file)

    def load_data_from_url(self, keyword):
        """ Загрузка данных с сайта HH по ключевому слову """
        self.params['text'] = keyword
        while self.params.get('page') != PAGES_OF_ITEMS:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def save_data_to_file(self):
        """ Сохрвнение данных в файл """
        with open(self.work_file, 'w', encoding='UTF-8') as f:
            print(self.vacancies, file=f)

hh_list = HeadHunterAPI(DATA_FILE_PATH)
hh_list.load_data_from_url('Python')
hh_list.save_data_to_file()
#print(hh_list.vacancies)
#print(len(hh_list.vacancies))
