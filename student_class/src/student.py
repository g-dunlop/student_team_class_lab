

from unicodedata import name
from urllib.error import ContentTooShortError


class Student:
    def __init__(self, student_name, student_cohort):
        self.name = student_name
        self.cohort = student_cohort
        # self.fav_lang = student_favorite_lang
    
    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"

