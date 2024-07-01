class HHVacancy:
    """ Класс для работы с звписями Head Hunter API """

    def __init__(self, pk, name, area, salary_from, salary_to, currency, employer, requirement, url):
        self.__pk = pk
        self.__name = name
        self.__area = area
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__currency = currency
        self.__salary = self.verify_salary(salary_from, salary_to, currency)
        self.__salary_middle = self.get_salary_middle(salary_from, salary_to)
        self.__employer = employer
        self.__requirement = requirement
        self.__url = url

    def __str__(self):
        return f'{self.__name}, {self.__employer}, {self.__area}, {self.__salary}'

    def __lt__(self, other):
        return self.__salary_middle < other.__salary_middle

    def __gt__(self, other):
        return self.__salary_middle > other.__salary_middle

    def __hash__(self):
        return hash(self.__pk)

    @property
    def pk(self):
        return self.__pk

    @property
    def name(self):
        return self.__name

    @property
    def salary_middle(self):
        return self.__salary_middle

    @staticmethod
    def verify_salary(salary_from, salary_to, currency) -> str:
        """ Генерация строки с зарплатой, валидация """
        if salary_from and salary_to:
            if salary_from == salary_to:
                return f'{salary_to} {currency}'
            return f'{salary_from}..{salary_to} {currency}'
        elif salary_from and not salary_to:
            return f'От {salary_from} {currency}'
        elif not salary_from and salary_to:
            return f'До {salary_to} {currency}'
        else:
            return 'Зарплата не указана'

    @staticmethod
    def get_salary_middle(salary_from, salary_to):
        """ Вычисление среднего значения зарплаты """
        if salary_from and salary_to:
            return round(0.5 * (int(salary_from) + int(salary_to)))
        elif salary_to:
            return int(salary_to)
        elif salary_from:
            return int(salary_from)
        else:
            return 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_from, salary_to, currency):
        self.__salary = self.verify_salary(salary_from, salary_to, currency)

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        """ Создание вакансии """
        pk = vacancy_data.get('id')
        name = vacancy_data.get('name')
        if vacancy_data['area']:
            area = vacancy_data.get('area').get('name')
        else:
            area = None
        if vacancy_data['salary']:
            salary_from = vacancy_data.get('salary').get('from')
            salary_to = vacancy_data.get('salary').get('to')
            currency = vacancy_data.get('salary').get('currency')
        else:
            salary_from = None
            salary_to = None
            currency = None
        if vacancy_data['employer']:
            employer = vacancy_data.get('employer').get('name')
        else:
            employer = None
        if vacancy_data['snippet']:
            requirement = vacancy_data.get('snippet').get('requirement')
        else:
            requirement = None
        url = vacancy_data.get('alternate_url')
        return cls(pk, name, area, salary_from, salary_to, currency, employer, requirement, url)

    def to_dict(self) -> dict:
        """ Преобразование объекта в словарь для записи в файл """
        return {
            'id': self.__pk,
            'name': self.__name,
            'area': self.__area,
            'salary_from': self.__salary_from,
            'salary_to': self.__salary_to,
            'currency': self.__currency,
            'employer': self.__employer,
            'requirement': self.__requirement,
            'url': self.__url
        }


if __name__ == '__main__':
    pass
