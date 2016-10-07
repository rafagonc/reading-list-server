from achievement import MinorAchievement
from dao.user_book import number_of_books_completed_by_user


class BooksSmartsAchievement(MinorAchievement):

    def id(self):
        return "A83C3DA1-0C72-4766-9E2C-F7E48EBC642D"

    def solution(self, user):
        return number_of_books_completed_by_user(user.user_id) > 10
