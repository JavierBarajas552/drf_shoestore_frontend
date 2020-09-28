from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = 'Populates ShoeType and ShoeColor with data'

    def handle(self, *args, **options):
        ShoeColor.objects.create(
            color_name='RED'
        )
        ShoeColor.objects.create(
            color_name='ORANGE'
        )
        ShoeColor.objects.create(
            color_name='YELLO'
        )
        ShoeColor.objects.create(
            color_name='GREEN'
        )
        ShoeColor.objects.create(
            color_name='BLUE'
        )
        ShoeColor.objects.create(
            color_name='INDIGO'
        )
        ShoeColor.objects.create(
            color_name='VIOLET'
        )
        ShoeColor.objects.create(
            color_name='WHITE'
        )
        ShoeColor.objects.create(
            color_name='BLACK'
        )
        ShoeType.objects.create(
            style='sneaker'
        )
        ShoeType.objects.create(
            style='boot'
        )
        ShoeType.objects.create(
            style='sandal'
        )
        ShoeType.objects.create(
            style='dress'
        )
        ShoeType.objects.create(
            style='other'
        )
        self.stdout.write(self.style.SUCCESS('Data created'))
