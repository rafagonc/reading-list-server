from achievement import MinorAchievement
from dao.user_book import number_of_books_comleted_by_user_in_category


class WhereIsMySoulMateAchivement(MinorAchievement):

    def id(self):
        return "BCF02489-4EB1-4265-B1C4-2D5CA175F910"

    def solution(self, user):
        return number_of_books_comleted_by_user_in_category("Romance") > 5
