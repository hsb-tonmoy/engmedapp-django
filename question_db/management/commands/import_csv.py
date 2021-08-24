#!/usr/bin/env python

"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_data_csv.py').read())
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from accounts.models import Accounts
import csv
from django.core.management import BaseCommand
from question_db.models import Board, Level, Paper, Question, Session, Year


class Command(BaseCommand):
    help = "Load questions from csv file."

    def add_arguments(self, parser) -> None:
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):

        CSV_PATH = kwargs['path']

        contSuccess = 0

        with open(CSV_PATH, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
            next(spamreader, None)
            print('Loading...')
            for row in spamreader:
                question = Question.objects.create(board=Board.objects.get(name=row[0]), level=Level.objects.get(name=row[1]), paper=Paper.objects.get_or_create(name=str(row[2])), year=Year.objects.get_or_create(name=row[3]), session=Session.objects.get_or_create(name=row[4]), title=row[5],
                                                   excerpt=row[6], content=row[7], verified_explanation=row[8], author=Accounts.objects.get(username="SirDarknight"))
                tags = row[9].split(",")
                for tag in tags:
                    question.tags.add(tag)

                contSuccess += 1
            print(f'{str(contSuccess)} inserted successfully! ')
