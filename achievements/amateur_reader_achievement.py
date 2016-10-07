from achievement import MinorAchievement
from dao.user_book import number_of_pages_read_by_user


class AmateurReaderAchievement(MinorAchievement):

    def id(self):
        return "83F1286B-473C-41D6-A279-7FF94262FEE3"

    def solution(self, user):
        return number_of_pages_read_by_user(user.user_id) > 2500