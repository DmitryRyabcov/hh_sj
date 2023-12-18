from src.vacancy import Vacancy


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    """
    Функция для фильтрации вакансий по ключевым словам
    """
    vacancies = []
    for v in hh_vacancies:
        for word in filter_words:
            if word.lower() in v["name"].lower():
                try:
                    vacancies.append(
                        Vacancy(v["name"], v["alternate_url"], v["salary"]["from"], v["snippet"]["responsibility"]))
                except TypeError:
                    continue

    for v in superjob_vacancies:
        for word in filter_words:
            if word.lower() in v["profession"]:
                vacancies.append(Vacancy(v["profession"], v["link"], v["payment_from"], v["candidat"]))
    return vacancies


def sort_vacancies(filtered_vacancies):
    """
    Функция для сортировки списка вакансий по зарплате
    """
    return sorted(filtered_vacancies, key=lambda v: v.salary or 0, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Получение первых top_n вакансий
    """
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    """
    Вывод всех вакансий
    """
    count = 0
    for v in vacancies:
        count += 1
        print(f'{count}.{v}')