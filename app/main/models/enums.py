"""
All enums used in the schema are described here.
"""
import enum


class PostType(enum.Enum):
    research = 1
    startup = 2
    technology = 3


class CommentType(enum.Enum):
    comment = 1
    report = 2
    highlight = 3


class PriorityType(enum.Enum):
    less_of_these = -1
    follow = 0
    more_of_these = 1


class Month(enum.Enum):
    jan = 0
    feb = 1
    mar = 2
    apr = 3
    may = 4
    jun = 5
    jul = 6
    aug = 7
    sep = 8
    oct = 9
    nov = 10
    dec = 11

    @classmethod
    def get_month(cls, month):
        month = month.lower()
        if month == "jan":
            return cls.jan
        elif month == "feb":
            return cls.feb
        elif month == "mar":
            return cls.mar
        elif month == "apr":
            return cls.apr
        elif month == "may":
            return cls.may
        elif month == "jun":
            return cls.jun
        elif month == "jul":
            return cls.jul
        elif month == "aug":
            return cls.aug
        elif month == "sep":
            return cls.sep
        elif month == "oct":
            return cls.oct
        elif month == "nov":
            return cls.nov
        elif month == "dec":
            return cls.dec