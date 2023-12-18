from abc import ABC, abstractmethod


class AbstractVacanciesAPI(ABC):
    """
    Абстрактный класс для классов HeadHunter и SuperJob
    """

    @abstractmethod
    def get_vacancies(self, text):
        pass


class AbstractJSONSaver(ABC):
    """
    Абстрактный класс для класса JSONSaver
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass