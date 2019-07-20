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
