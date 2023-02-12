from django.db import models

# Create your models here.
class Movies(models.Model):
    LANGUAGE_CHOICES = [
        ('Hin','Hindi'),
        ('Eng','English'),
        ('Kan','Kannada')]
    title = models.CharField(max_length=100,unique=True)
    language = models.CharField(max_length=20,choices=LANGUAGE_CHOICES)
    duration = models.DurationField()

    def __str__(self) -> str:
        return self.title

class Theatre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Halls(models.Model):
    name = models.CharField(max_length=20)
    theatre = models.ForeignKey(Theatre,on_delete= models.CASCADE)
    models.UniqueConstraint((name,theatre), name="unique_hall")

    def __str__(self) -> str:
        return self.theatre.name +":" + self.name


class Seats(models.Model):
    COLUMN_CHOICES = [
        ('A','A'),
        ('B','B'),
        ('C','C')]
    number = models.IntegerField()
    row = models.IntegerField()
    column = models.CharField(max_length=3,choices=COLUMN_CHOICES)
    hall = models.ForeignKey(Halls,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.column + str(self.row) + '-' + str(self.number)

class Show(models.Model):
    start_time = models.DateTimeField()
    cost = models.IntegerField()
    hall = models.ForeignKey(Halls,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)

    @staticmethod
    def end_time(self):
        return self.start_time + self.movie.duration

    def __str__(self) -> str:
        return self.movie.__str__ ()+ "-" + self.hall.__str__ () +": " + self.start_time.strftime("%Y-%m-%d_%H:%M:%S")
    

