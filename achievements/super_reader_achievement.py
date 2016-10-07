from achievement import MiddleAchievement
from dao.user_book import number_of_pages_read_by_user


class SuperReaderAchievement(MiddleAchievement):

    def id(self):
        return "DE43CBA9-945A-4B1E-B34D-217DF6F5FFCD"

    def solution(self, user):
        return number_of_pages_read_by_user(user.user_id) > 10000
