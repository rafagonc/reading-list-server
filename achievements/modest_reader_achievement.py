from achievement import MinorAchievement
from dao.user_book import number_of_pages_read_by_user


class AvidReaderAchievement(MinorAchievement):

    def id(self):
        return "1EADF516-8963-4B3A-A3FF-3446A8E2C2F0"

    def solution(self, user):
        return number_of_pages_read_by_user(user.user_id) > 5000
