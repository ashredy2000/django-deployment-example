import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'proThree.settings')
import django
django.setup()
import random
from appThree.models import User
from faker import Faker
fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()
        users = User.objects.get_or_create(firstName = fake_firstname, lastName = fake_lastname, email = fake_email)[0]

if __name__ == '__main__':
    print("Populating")
    populate(50)
    print("Populated")
