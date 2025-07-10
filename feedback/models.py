from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)  # имя
    email = models.EmailField()  # email
    phone = models.CharField(max_length=20, blank=True, null=True)  # телефон
    
    subject_choices = [
        ('booking', 'Бронирование столика'),
        ('delivery', 'Доставка'),
        ('catering', 'Кейтеринг'),
        ('feedback', 'Отзыв'),
        ('other', 'Другое'),
    ]
    subject = models.CharField(max_length=50, choices=subject_choices)  # тема
    
    message = models.TextField()  # сообщение
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')  # type: ignore # статус прочтения
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
