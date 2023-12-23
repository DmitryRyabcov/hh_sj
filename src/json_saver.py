import json
from api_work.abstract_api import AbstractJSONSaver
from src.vacancy import Vacancy

class JSONSaver(AbstractJSONSaver):
    """
    Класс для добавления/удаления вакансий из vacancies.json
    """
    def __init__(self, filename='vacancy.json'):
        self.filename = filename

        with open(self.filename, 'w', encoding='UTF-8') as file:
            file.write(json.dumps([], indent=2, ensure_ascii=False))
    def add_vacancy(self, vacancy):
        """
        Добавляет класс вакансии в vacancies.json
        """
        try:
            with open(self.fiename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = []

        data.append(vars(vacancy))

        with open(self.filename, "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_vacancies(self, salary):
        """
        Возвращает список вакансий по указанной зарплате
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            salaries = json.load(file)
            matching_vacancies = [vacancy for vacancy in salaries if vacancy["salary"] == salary]
            return [Vacancy(**vacancy) for vacancy in matching_vacancies]
    def delete_vacancy(self, vacancy):
        """
        Удаление класса вакансии из vacancies.json
        """
        with open("vacancies.json", "r", encoding="UTF-8") as file:
            vacancies = json.load(file)

        undel_vacancies = [obj for obj in vacancies if obj["url"] != vars(vacancy)["url"]]

        with open("vacancies.json", "w") as file:
            json.dump(undel_vacancies, file, indent=2, ensure_ascii=False)