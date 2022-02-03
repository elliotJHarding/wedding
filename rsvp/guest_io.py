import codecs
import csv
from rsvp.models import Guest


def import_guest_csv(file):
    r = csv.DictReader(codecs.iterdecode(file, 'utf-8'), delimiter=',')
    for row in r:
        Guest.objects.get_or_create(
            f_name=row['f_name'],
            s_name=row['s_name'],
            full_name=f"{row['f_name']} {row['s_name']}",
            has_plus1=row['p1'],
        )
