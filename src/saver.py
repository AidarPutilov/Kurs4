import json
from abc import ABC, abstractmethod

from src.settings import DATA_FILE_PATH, DATA_FILE_PATH_DEMO
from src.vacancy import HHVacancy


class Saver(ABC):
    """ Абстрактный класс для работы с файлами с вакансиями """
    @abstractmethod
    def load_data(self) -> list[dict]:
        pass

    @abstractmethod
    def write_data(self, data: list[dict]) -> None:
        pass

    @abstractmethod
    def write_vacancies(self, vacancies: list[HHVacancy]) -> None:
        pass

    @abstractmethod
    def add_vacancies(self, vacancies: list[HHVacancy]) -> None:
        pass

    @abstractmethod
    def del_vacancies(self, vacancies: list[HHVacancy]) -> None:
        pass


class JSONSaver(Saver):
    def __init__(self, path):
        self.__path = path

    def load_data(self) -> list[dict]:
        """ Чтение файла с JSON-данными """
        with open(self.__path, encoding='utf-8') as f:
            return json.load(f)

    def write_data(self, data: list[dict]) -> None:
        """ Запись JSON-данных в файл. Данные перезаписываются """
        with open(self.__path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def write_vacancies(self, vacancies: list[HHVacancy]) -> None:
        """ Запись вакансий в файл. Данные перезаписываются """
        self.write_data([vacancy.to_dict() for vacancy in vacancies])

    def add_vacancies(self, vacancies: list[HHVacancy]) -> None:
        """ Добавление вакансий в файл """
        items = self.load_data()
        for vacancy in vacancies:
            if vacancy.pk not in [item['id'] for item in items]:
                items.append(vacancy.to_dict())
        self.write_data(items)

    def del_vacancies(self, vacancies: list[HHVacancy]) -> None:
        """ Удаление вакансий в файле """
        old_items = self.load_data()
        del_ids = [vacancy.pk for vacancy in vacancies]
        new_items = [item for item in old_items if item['id'] not in del_ids]
        self.write_data(new_items)

if __name__ == '__main__':

    # s1 = JSONSaver(DATA_FILE_PATH_DEMO)
    # ss = s1.load_data()
    # print(ss)
    #
    # v1 = HHVacancy(1, 'Служащий', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'ya.ru')
    # v2 = HHVacancy(2, 'Служащий', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'ya.ru')
    # v3 = HHVacancy(3, 'Служащий', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'ya.ru')
    # v4 = HHVacancy(4, 'Служащий', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'ya.ru')
    # v5 = HHVacancy(5, 'Служащий', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'ya.ru')
    #
    # s1.write_vacancies([v1, v2, v3, v4, v5])

    # s1.add_vacancies([v3, v2])

    # s1.del_vacancies([v2, v3])
