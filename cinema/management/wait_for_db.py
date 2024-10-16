import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        connection = None
        while not connection:
            try:
                connection = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable")

                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
