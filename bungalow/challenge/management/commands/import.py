import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from bungalow.challenge.serializers import PropertySerializer


class Command(BaseCommand):
    help = 'Import a CSV data dump into the property table.'
    missing_args_message = (
        "No database dump specified. Please provide the path of at least "
        "one CSV file in the command line."
    )

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='dump', nargs='+', help='DB export labels.')

    def handle(self, *export_labels, **options):
        self.verbosity = options['verbosity']

        with transaction.atomic():
            self.loaddata(export_labels)

    def loaddata(self, export_labels):
        loaded_count = import_count = 0
        for export_label in export_labels:
            with open(export_label, "r") as csvfile:
                line = 0
                reader = csv.DictReader(csvfile)
                for line, property in enumerate(reader, start=1):
                    property = {k: None if not v and type(v) == str else v for k, v in property.items()}
                    serializer = PropertySerializer(data=property)
                    if not serializer.is_valid():
                        self.stdout.write(f"Failed to import line {line}.")
                        if self.verbosity >= 1:
                            self.stdout.write(serializer.errors)
                    serializer.create(serializer.validated_data)
                    import_count += 1
                loaded_count += line

        if self.verbosity >= 1:
            self.stdout.write(
                "Imported %d object(s) from %d import(s)"
                % (line, import_count)
            )
