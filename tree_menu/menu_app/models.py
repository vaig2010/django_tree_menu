from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    