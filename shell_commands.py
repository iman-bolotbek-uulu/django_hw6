from employee.models import *
from django.db.models import Q, Subquery

# p1 = Passport(employee=Employee.objects.create(name='Iman', birth_date='2003-02-01', position='Python Backend Developer', salary=1000, work_experience='2022-12-09'), inn='1234567891234567', id_card='123456789123')
# p2 = Passport(employee=Employee.objects.create(name='Ulan', birth_date='2004-01-03', position='Java Backend Developer', salary=500, work_experience='2022-12-09'), inn='1234567891234598', id_card='123456789198')
# p3 = Passport(employee=Employee.objects.create(name='Rustam', birth_date='2002-02-01', position='Javascript Frontend Developer', salary=1500, work_experience='2022-12-09'), inn='1234567891234599', id_card='123456789199')
# p4 = Passport(employee=Employee.objects.create(name='Marat', birth_date='2000-01-03', position='PHP Backend Developer', salary=2000, work_experience='2022-12-09'), inn='1234567891234510', id_card='123456789110')
# p1.save()
# p2.save()
# p3.save()
# p4.save()
# #
# del1 = Employee.objects.all()[3]
# del1.delete()
#
#
# pj = WorkProject(project_name='django_hw6')
# pj.save()
#
# same_experience_date = Employee.objects.filter(work_experience='2022-12-09')
# m1 = list(same_experience_date)
# pj.members.set(m1)
#
#
# del2 = Employee.objects.all()[2]
# del2.delete()
#
#
# p5 = Passport(employee=Employee.objects.create(name='Uluk', birth_date='1999-01-03', position='Ruby Backend Developer', salary=3000, work_experience='2022-11-09'), inn='1234567891234511', id_card='123456789111')
# p5.save()
#
# c1 = Client(name='Billi', birth_date='1990-01-01', address='Moscow street 40/99', phone_number='509777777')
# c2 = Client(name='Alex', birth_date='1991-01-01', address='Bishkek street 40/97', phone_number='509777755')
# c3 = Client(name='Alan', birth_date='1993-01-01', address='New-York street 40/98', phone_number='509777766')
# c1.save()
# c2.save()
# c3.save()
#
# vip_c1 = VIPClient(name='Alan', birth_date='1993-01-01', address='New-York street 40/98', phone_number='509777766',
#                    donation_amount=100000)
# vip_c1.save()
#
# del3 = Client.objects.all()[0]
# del3.delete()
#
# all_employee = Employee.objects.all()
# print(f'All employee:{all_employee}')
#
# employee = Employee.objects.all()
# passport = Passport.objects.all()
# print(f'All employee and passport:{employee} {passport}')
#
# all_projects = WorkProject.objects.all()
# print(f'All project:{all_projects}')
#
#
# me_projects = WorkProject.objects.filter(members__name__icontains='Iman')
# print(f'All project with me:{me_projects}')
#
# all_clients = Client.objects.all()
# print(f'All client:{all_clients}')
#
# all_vip_clients = VIPClient.objects.all()
# print(f'All vip client:{all_vip_clients}')






# id = Membership.objects.filter(employee='Iman').values('id')[0]['id']
# id = Employee.objects.filter(name='Ulan').values_list('id', flat=True).first()
# id = Employee.objects.filter(name='Iman').values('id')[0]['id']
# m1 = Employee.objects.get(employee='Iman')
# print(id)









