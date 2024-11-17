from django.db import models
import bcrypt
import re
# Create your models here.



class UserManger(models.Manager):
    def basic_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        if len(postData['username'])<5:
            errors['username']="Username should be more that 5 letter"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='email is not Valid'
        if len(postData['password'])<8:
            errors['password']="Password must be more 8 char"
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] ='password not match'

        return errors



class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    birthday=models.DateField(null=True)
    objects=UserManger()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def addUser(data):
    password=data['password']
    hashed_PW=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    User.objects.create(username=data['username'],email=data['email'],password=hashed_PW,birthday=data['Bday'])