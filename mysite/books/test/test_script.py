from books.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',city='Berkeley', state_province='CA', country='U.S.A.',website='http://www.apress.com/')
p1.save()
p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',city='Cambridge', state_province='MA', country='U.S.A.',website='http://www.oreilly.com/')
p2.save()
p3 = Publisher(name="O'Reilly",)
p3.save()
p4 = Publisher.objects.create(name='learning django',)
publisher_list = Publisher.objects.all()
publisher_list