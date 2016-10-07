from achievement import MiddleAchievement
from dao.user_book import number_of_books_completed_by_user


class BooksBathAndBeyondAchievement(MiddleAchievement):

    def id(self):
        return "1EA11F0D-4AF5-4D62-AE57-DCF3771271A8"

    def solution(self, user):
        return number_of_books_completed_by_user(user.user_id) > 25
