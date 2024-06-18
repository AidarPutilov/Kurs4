from pathlib import Path


# Каталог с проектом
ROOT_PATH = Path(__file__).parent.parent

# Файл с данными
DATA_FILE_PATH = ROOT_PATH.joinpath('data', 'vacancies.json')

# Файл с тестовыми данными
DATA_FILE_PATH_DEMO = ROOT_PATH.joinpath('data', 'vacancies_demo.json')

# URL с вакансиями HH
HEAD_HUNTER_URL = 'https://api.hh.ru/vacancies'

# Количество строк в ответе на запрос
ITEMS_PER_PAGE = 2

# Количество страниц
PAGES_OF_ITEMS = 2

#print(DATA_FILE_PATH)
