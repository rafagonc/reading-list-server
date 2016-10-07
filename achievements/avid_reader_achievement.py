from achievement import MajorAchievement
from dao.user_book import number_of_pages_read_by_user


class AvidReaderAchievement(MajorAchievement):

    def id(self):
        return "14317D69-70C7-40BD-ABC2-1F369DE15FEA"

    def solution(self, user):
        return number_of_pages_read_by_user(user.user_id) > 20000
