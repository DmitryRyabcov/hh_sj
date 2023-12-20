from api_work.abstract_api import AbstractVacanciesAPI
import requests
from http import HTTPStatus

class HeadHunterAPI(AbstractVacanciesAPI):
    """
    Класс для получения вакансий с hh.ru через API сайта
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, params):
        response = requests.get(self.url, params=params)
        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка! Статус-код: {response.status_code}'
        return response.json()['items']