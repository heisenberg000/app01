# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2022/01/30 09:45:44
@Author  :   James 
@Desc    :   views.py
@Version :   1.0
'''

from django.shortcuts import render,HttpResponse
from app01.models import Book

def add_book(request):
    # 方法1
    # book = Book(title="django新手教程",price=300,publish="大疆文学出版社",pub_date="2020-08-02")
    # book.save()
    # 方法2
    book = Book.objects.create(title="java新手教程",price=199,publish="人民教育出版社",pub_date="2007-10-13")
    # print(book,type(book))
    return HttpResponse("<p>数据添加成功!</p>")

def find_books(request):
    books = Book.objects.all()
    print(books,type(books)) # <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]> <class 'django.db.models.query.QuerySet'>
    return HttpResponse("<p>查询数据成功</p>")

def find_book(request,book_id):
    # 查询符合条件的结果集
    # book = Book.objects.filter(id=book_id).order_by("-price")
    # 查询不符合条件的结果集, value方法相当于结果集
    book = Book.objects.exclude(id=book_id).order_by("-price").values("title","price")
    # 查询单一结果，如果不存在或者存在多个结果，都会报错
    # book = Book.objects.get(id=book_id)
    print(book) # <QuerySet [<Book: Book object (1)>]>
    return HttpResponse("<p>{}</p>".format(book[0]["title"] if book.exists() else "未查到数据"))

def del_book(request,book_id):
    book = Book.objects.filter(pk=book_id).first().delete()
    return HttpResponse(book)

def update_book(request):
    # 更新方法1
    book = Book.objects.filter(pk=3).first()
    book.price = 100
    book.save()
    # 更新方法2
    # 返回受影响条数
    books = Book.objects.filter(pk__range=[1,2]).update(price=88)
    return HttpResponse(books)