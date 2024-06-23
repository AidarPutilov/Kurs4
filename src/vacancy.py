


class HHVacancy:

    def __init__(self, name, professional_roles, area, salary_from, salary_to, currency, employer, requirement, responsibility, url):
        self.name = name
        self.professional_roles = professional_roles
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.__salary = self.verify_salary(salary_from, salary_to, currency)
        self.salary_middle = self.get_salary_midle(salary_from, salary_to)
        self.employer = employer
        self.requirement = requirement
        self.responsibility = responsibility
        self.url = url

    def __str__(self):
        return f'{self.name}, {self.employer}, {self.area}, {self.salary}'


    @classmethod
    def verify_salary(cls, salary_from, salary_to, currency) -> str:
        """ Генерация строки с зарплатой, валидация """
        if salary_from and salary_to:
            return f'{salary_from}..{salary_to} {currency}'
        elif salary_from and not salary_to:
            return f'От {salary_from} {currency}'
        elif not salary_from and salary_to:
            return f'До {salary_to} {currency}'
        else:
            return 'Зарплата не указана'

    @classmethod
    def get_salary_midle(cls, salary_from, salary_to):
        """ Вычисление среднего значения зарплаты """
        if salary_from and salary_to:
            return round(0.5 * (int(salary_from) + int(salary_to)))
        elif not salary_to:
            return int(salary_from)
        elif not salary_from:
            return int(salary_to)
        else:
            return 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_from, salary_to, currency):
        self.__salary = self.verify_salary(salary_from, salary_to, currency)

    def __lt__(self, other):
        return self.salary_middle < other.salary_middle

    def __gt__(self, other):
        return self.salary_middle > other.salary_middle


v1 = HHVacancy('Рабочий', 'Слесарь', 'Москва', '', '200', 'руб.', 'Завод', 'Знание SQL', 'Сопровождение DataLake', 'ya.ru')
v2 = HHVacancy('Служащий', 'Менагер', 'Москва', '200', '', 'руб.', 'Управление', 'Знание SQL', 'Сопровождение DataLake', 'ya.ru')


print(v1)
print(v2)
print(v1 < v2)



