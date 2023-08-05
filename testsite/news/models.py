from django.db import models
from django.urls import reverse


class News(models.Model):   # класс news должен быть подклассом django.db models (наследование :))
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # () - данное поле не обязательно к заполнению (по умолчанию False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')    # () - при создании записи будет выставлена неизменная дата создания (по умолчанию False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')    # () - при каждом редактировании записи дата будет обновляться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')    # () - указываем путь, куда сохранять файлы // есть еще File.Field // сохраняют путь к файлу // File - файлы любого типа, Image - только фоточки // папка в папке: Y - year , m - month, d - day
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория')       # обеспечивает защиту от удаления связных данных

    def __str__(self):          # При чтении объекта будет срабатывать метод str, который возвращает строковое представление объекта (в нашем случае только название)
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'        # Наименование модели в единственном числе // verbose = подробный
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')      # Если True, для этого поля будет создан индекс базы данных

    def get_absolute_url(self):
        return reverse('view_category', kwargs={"category_id": self.pk})


    def __str__(self):          # При чтении объекта будет срабатывать метод str, который возвращает строковое представление объекта (в нашем случае только название)
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']