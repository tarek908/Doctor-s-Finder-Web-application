from django.db import models

# Create your models here.
# user /
class User(models.Model):
    user = models.TextField(default=None)

#// model for User Maste table
class UserMaster(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    is_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=8, default="")
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_updated = models.DateTimeField(auto_now_add=False, null=True)
    

class getAppointment(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    chose_date = models.CharField(max_length=200)
    descrption = models.TextField(default="")
    visit = models.CharField(max_length=200,default="")
    status = models.BooleanField(default=False)


#// Doctor site registation
class regDoctors(models.Model):
    userId = models.ForeignKey(UserMaster, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    profile = models.ImageField(upload_to="app/img/drDP", default="")
    title = models.CharField(max_length=200, default="")
    degree = models.CharField(max_length=500, default="")
    livesIn = models.CharField(max_length=200, default="")
    workAt = models.CharField(max_length=200, default="" )
    froms = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=200, default="")
    facebook = models.CharField(max_length=600, default="")
    x = models.CharField(max_length=600, default="")
    linkedin = models.CharField(max_length=600, default="")


# patinet
class patinet(models.Model):
    userId = models.ForeignKey(UserMaster, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    img = models.ImageField(upload_to="app/img/pateint")


class Rating(models.Model):
    img = models.ImageField(upload_to="app/rating")
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    status = models.BooleanField(default=False)



    
