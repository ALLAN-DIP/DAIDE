# __author__ = "Sander Schulhoff"
# __email__ = "sanderschulhoff@gmail.com"

# from DAIDE.syntax.daide_object import DAIDE_OBJECT
# from DAIDE.utils.parsing import consume 


# class RESPONSE(DAIDE_OBJECT):
#     """YES, REJ, stuff like that"""
#     def __init__(self, string, response):
#         self.string = string
#         self.response = response

#     def __str__(self):
#         return self.response + " (" + self.msg + ")"

#         @classmethod
#     def parse(cls, string, response):
#         rest = consume(string, response)
#         rest = consume(" (")
#         arrangement, rest = ARRANGEMENT.parse(rest)
#         rest = consume(")")

#         if response == "YES":
#             return YES(arrangement), rest

# class YES(RESPONSE):
#     def __init__(self, arrangement):
#         self.arrangement = arrangement

#         @classmethod
#     def parse(cls, string, response):
#         return super().parse(string, "AND")