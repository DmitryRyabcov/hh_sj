from api_work.abstract_api import AbstractVacanciesAPI
import requests


class HeadHunterAPI(AbstractVacanciesAPI):
    """
    Класс для получения вакансий с hh.ru через API сайта
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text):
        params = {
            "text": text,
            "area": 113,
            "per_page": 100
        }
        response = requests.get(self.url, params=params)
        vacancies = response.json()
        return vacancies["items"]