from functions import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
from api_work.hh_api import HeadHunterAPI
from api_work.sj_api import SuperJobAPI
from src.json_saver import  JSONSaver

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()

hh_vacancies = hh_api.get_vacancies('Python')
sj_vacancies = sj_api.get_vacancies('Python')
def user_interaction():
    """
    Главная функция проекта.
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, sj_vacancies, filter_words)
    json_saver = JSONSaver()

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    json_saver.add_vacancies(top_vacancies)


if __name__ == '__main__':
 user_interaction()