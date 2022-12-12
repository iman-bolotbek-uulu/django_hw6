from django.db import models
from datetime import date
from django.utils import timezone


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    birth_date = models.DateField(verbose_name='Birth date')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    # def get_age(self):
    #     return date.today() - self.birth_date


class Employee(AbstractPerson):
    position = models.CharField(max_length=30, verbose_name='Position')
    salary = models.IntegerField(verbose_name='Salary')
    work_experience = models.DateField(verbose_name='Work experience')

    def __str__(self):
        return f'{self.position} - {self.salary} - {self.work_experience}'


class Passport(models.Model):
    inn = models.CharField(max_length=16)
    id_card = models.CharField(max_length=12)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='passports')

    def __str__(self):
        return self.employee.name

    def get_gender(self):
        if '1' in self.inn[0]:
            return 'Female'
        elif '2' in self.inn[0]:
            return 'Male'

    def save(self, *args, **kwargs):
        print('INN saved!'
              'ID card saved!'
              'Employee ID saved!')
        super().save(*args, **kwargs)


class WorkProject(models.Model):
    project_name = models.CharField(max_length=30, verbose_name='Project name')
    members = models.ManyToManyField(Employee, related_name='projects', through='Membership')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        print('Project name saved!')
        super().save(*args, **kwargs)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return f'Employee - {self.employee.name},project - {self.project},date of joined - {self.date_joined}'

    def save(self, *args, **kwargs):
        print('Employee saved!'
              'Project name saved!'
              'Date joined saved!')
        super().save(*args, **kwargs)


class Client(AbstractPerson):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class VIPClient(Client):
    vip_status_start = models.DateField(auto_now=True, verbose_name='VIP start')
    donation_amount = models.IntegerField(verbose_name='Amount donated by client')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print('VIP status start date saved!'
              'Donation amount saved!')
        super().save(*args, **kwargs)











