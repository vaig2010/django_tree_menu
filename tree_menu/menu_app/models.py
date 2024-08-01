from django.db import models

class Menu(models.Model):
    name = models.CharField('Название меню', max_length=255)

    class Meta:
        verbose_name = 'Главное меню'
        verbose_name_plural = 'Главные меню'

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField('Название пункта меню', max_length=255)
    url = models.CharField('URL', max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
