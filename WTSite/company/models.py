from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Company(models.Model):
    commander = models.OneToOneField(User, on_delete=models.PROTECT, related_name='CompanyCommander',
                                     verbose_name="командир")
    field_commander = models.OneToOneField(User, on_delete=models.PROTECT, related_name='CompanyFieldCommander',
                                           blank=True, verbose_name="полевой командир")
    name = models.CharField("название", max_length=24)
    description = models.CharField("описание", max_length=300)
    power = models.IntegerField("сила", blank=True)
    current_contract = models.OneToOneField('Contract', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рота"
        verbose_name_plural = "Роты"
        ordering = ['power']


class Contract(models.Model):
    description = models.CharField("описание", max_length=300)
    client = models.OneToOneField(User, verbose_name="Заказчик", on_delete=models.DO_NOTHING)
    executor = models.OneToOneField(Company, verbose_name="Исполнитель", on_delete=models.DO_NOTHING)
    price = models.IntegerField("цена")

    def __str__(self):
        return "Исполнитель - " + str(self.executor) + "|" + "Заказчик - " + str(self.client)

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
