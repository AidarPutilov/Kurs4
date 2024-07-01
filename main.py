import logging
from src.exceptions import ParserAPIException
from src.head_hunter_api import HeadHunterAPI
from src.saver import JSONSaver
from src.settings import DATA_FILE_PATH
from src.utils import user_interface, filter_vacancies_by_keywords, filter_vacancies_by_salary, sort_vacancies, \
    get_vacancy_units

logger = logging.getLogger(__name__)

def main():

    # Начальный диалог
    user_input = user_interface()

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HeadHunterAPI(user_input['search_word'])

    # Получение вакансий с hh.ru в формате JSON
    try:
        hh_data = hh.get_data()
    except ParserAPIException as e:
        logger.exception(f'Ошибка обращения к HHAPI. {e}')
        print('Сервис не отвечает')

    # Преобразование набора данных из JSON в список объектов

    hh_vacancies = get_vacancy_units(hh_data)

    # Фильтрация по ключевым словам
    filtered_vacancies = filter_vacancies_by_keywords(hh_vacancies, user_input['keywords'])

    # Фильтрация по зарплате
    ranged_vacancies = filter_vacancies_by_salary(filtered_vacancies, user_input['salary_min'], user_input['salary_max'])

    # Сортировка по зарплате
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    # Отбор первых N
    top_vacancies = sorted_vacancies[:user_input['top_n']]

    # Сохранение в файл
    saver = JSONSaver(DATA_FILE_PATH)
    saver.write_vacancies(top_vacancies)

    # Вывод списка вакансий
    print('Вакансии, удовлетворяющие требованиям:')
    [print(vacancy) for vacancy in top_vacancies]
    print(f'Вакансии записаны в файл {DATA_FILE_PATH}')


if __name__ == '__main__':
    main()
