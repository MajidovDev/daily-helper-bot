from django.db import models
from users_app.models import UserModel

NC, DONE = ("not completed", "done")


class TodosModel(models.Model):
    title = models.CharField(max_length=51)
    description = models.TextField()
    creator = models.ForeignKey(UserModel, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        (NC, NC),
        (DONE, DONE)
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NC)

    def __str__(self):
        return f"{self.creator} - {self.title}"