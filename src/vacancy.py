class Vacancy:
    """
    Класс для вакансий
    """
    def __init__(self, name, url, salary, description):
        self.name = name  # название вакансии
        self.url = url  # ссылка на вакансию
        self.salary = salary  # зарплата
        self.description = description  # описание вакансии

    def __str__(self):
        if self.salary is None:
            return f"Вакансия - {self.name}, зарплата не указана, {self.url}"
        return f"Вакансия - {self.name}, зарплата - {self.salary}, Ссылка - {self.url}"

    def __lt__(self, other):
        """
        Сравнение зарплат вакансий
        """
        return self.salary or 0 < other.salary or 0

    def __le__(self, other):
        """
        Переопределение метода сравнения <= для экземпляров класса Vacancy
        """
        return self.salary <= other.salary

    def __gt__(self, other):
        """
        Переопределение метода сравнения > для экземпляров класса Vacancy
        """
        return self.salary > other.salary

    def __ge__(self, other):
        """
        Переопределение метода сравнения >= для экземпляров класса Vacancy
        """
        return self.salary >= other.salary

    def __eq__(self, other) :
        """
        Переопределение метода сравнения == для экземпляров класса Vacancy
        """
        return self.salary == other.salary

