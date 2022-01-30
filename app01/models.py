# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2022/01/30 09:34:43
@Author  :   James 
@Desc    :   models.py
@Version :   1.0
'''

from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)                         #自增主键
    title = models.CharField(max_length=32)                         #书名
    price = models.DecimalField(max_digits=5,decimal_places=2)      #价格
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE) #出版商
    pub_date = models.DateField()                                   #初版时间
    author = models.ManyToManyField("Author")                       #作者                             

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age  = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    gender_choices = (
        (0,"女"),
        (1,"男"),
        (2,"保密")
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
        