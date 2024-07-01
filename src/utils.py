from src.vacancy import HHVacancy


def get_vacancy_units(vacancies: list[dict]) -> list[HHVacancy]:
    """ Преобразование словарей HH в вакансии """

    return [HHVacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[HHVacancy]) -> list[HHVacancy]:
    """ Сортировка вакансий по средней величине зарплаты """

    return sorted(vacancies, reverse=True)


def filter_vacancies_by_keywords(vacancies: list[HHVacancy], keywords: list) -> list[HHVacancy]:
    """ Выборка вакансий по ключевым словам в названии """

    new_vacancies = []
    for vacancy in vacancies:
        for keyword in keywords:
            if keyword in vacancy.name:
                new_vacancies.append(vacancy)
                break
    return new_vacancies


def filter_vacancies_by_salary(vacancies: list[HHVacancy], min, max) -> list[HHVacancy]:
    """ Выборка вакансий по максимальной и минимальной зарплате """

    new_vacancies = []
    for vacancy in vacancies:
        if min <= vacancy.salary_middle <= max:
            new_vacancies.append(vacancy)
    return new_vacancies


def user_interface() -> dict:
    """ Начальный диалог с пользователем, возвращает словарь с введёнными данными """

    return {
        'search_word': 'python',
        'keywords': ['python'],
        'top_n': 10,
        'salary_min': 0,
        'salary_max': 100000
    }

    print('Поиск вакансий на HeadHunter по ключевому слову')
    search_word = input('Введите поисковый запрос: ')

    # Обработка ввода числовых значений
    flag = True
    while flag:
        try:
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
            salary_max = int(input('Введите максимальную зарплату: '))
            salary_min = int(input('Введите минимальную зарплату: '))
        except:
            print('Ошибка ввода. Повторите')
        else:
           flag = False

    keywords: list = input('Введите ключевые слова через пробел: ').split(' ')

    # Случай, если мини и макси перепутаны
    if salary_min > salary_max:
        temp = salary_min
        salary_min = salary_max
        salary_max = temp

    return {
        'search_word': search_word,
        'keywords': keywords,
        'top_n': top_n,
        'salary_min': salary_min,
        'salary_max': salary_max
    }


if __name__ == '__main__':
    pass
