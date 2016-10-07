from . import achievement_point_middle_mult_factor, achievement_point_major_mult_factor, achievement_point_minor_mult_factor, achievement_point_initial_factor
from exc.abstract_class import AbstractClassException
import re


class Achievement:

    def __init__(self):
        pass

    def name(self):
        def convert(name):
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
            return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
        return convert(type(self).__name__)

    def solution(self, user):
        raise AbstractClassException()

    def id(self):
        raise AbstractClassException()

    def points(self):
        raise AbstractClassException()

    def completed(self):
        return self.solution() is True


class MajorAchievement(Achievement):

    def points(self):
        return achievement_point_initial_factor * achievement_point_major_mult_factor


class MinorAchievement(Achievement):

    def points(self):
        return achievement_point_initial_factor * achievement_point_minor_mult_factor


class MiddleAchievement(Achievement):

    def points(self):
        return achievement_point_initial_factor * achievement_point_middle_mult_factor
