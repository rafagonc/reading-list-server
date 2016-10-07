from achievement import MajorAchievement
from dao.user_book import number_of_books_completed_by_user


class BookHeroAchievement(MajorAchievement):

    def id(self):
        return "E41D6424-6E84-4270-870E-76FE64DEE232"

    def solution(self, user):
        return number_of_books_completed_by_user(user.user_id) > 50
