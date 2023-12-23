from api_work.abstract_api import AbstractVacanciesAPI
import requests
from http import HTTPStatus

class HeadHunterAPI(AbstractVacanciesAPI):
    """
    Класс для получения вакансий с hh.ru через API сайта
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, name):
        params = {
            "name": name,
            "area": 113,
            "per_page": 100
        }
        response = requests.get(self.url, params=params)
        vacancies = response.json()
        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка! Статус-код: {response.status_code}'
        return vacancies["items"]