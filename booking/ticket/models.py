from django.db import models
from django.contrib.auth.models import User
from Theatre.models import Seats,Show

# Create your models here.

class tickets(models.Model):
    show = models.ForeignKey(Show,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.show.__str__() + "-" + self.user.username


class seat_reserved(models.Model):
    seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
    show = models.ForeignKey(Show,on_delete=models.CASCADE)
    tickets = models.ForeignKey(tickets,on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['seat','show'],
                             name='unique_reserve')
        ]

    def __str__(self) -> str:
        return self.seat.__str__() + ":" + self.tickets.__str__()


