from django.test import TestCase
from django.utils.text import slugify
from .models import Board, Level, Paper, Year, Session, Question

boards_list = ['Edexcel', 'Cambridge']

for board in boards_list:
    board_obj = Board()
    board_obj.name = board
    board_obj.save()

levels_list = ['O', 'AS', 'A']

for level in levels_list:
    level_obj = Level()
    level_obj.name = level
    level_obj.save()


papers_list = ['1123 - English Language', '2210 - Computer Science', '2281 - Economics', '3204 - Bengali', '4024 - Mathematics D', '4037 - Mathematics Additional',
               '5014 - Environmental Management', '5054 - Physics', '5070 - Chemistry', '7010 - Computer Studies', '7094 - Bangladesh Studies', '7110 - Principles of Accounts', '7707 - Accounting']

for paper in papers_list:
    pap_obj = Paper()
    pap_obj.name = paper
    pap_obj.save()

years_list = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013,
              2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001]

for year in years_list:
    year_obj = Year()
    year_obj.name = str(year)
    year_obj.save()


sessions_list = ['Oct Nov', 'May Jun', 'Jan Feb', 'Aug Sep']

for session in sessions_list:
    ses_obj = Session()
    ses_obj.name = session
    ses_obj.save()
