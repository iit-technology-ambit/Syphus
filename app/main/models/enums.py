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
