
import csv
from django.core.management.base import BaseCommand
from finalproject.models import Movie

class Command(BaseCommand):
    help = 'Import data from a CSV file into the Movie model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        with open(csv_file, newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  
            
            for row in reader:
                Movie.objects.create(
                    name = row[0],
                    year = row[1],
                    cert = row[2],
                    runtime = row[3],
                    genre = row[4],
                    imdb = row[5],
                    overview = row[6],
                    meta = row[7],
                    director = row[8],
                    stara = row[9],
                    starb = row[10],
                    starc = row[11],
                    stard = row[12],
                    votes = row[13],
                    gross = row[14]
                )
                
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
