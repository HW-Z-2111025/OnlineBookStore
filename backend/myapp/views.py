import json
from django.http import JsonResponse
from myapp.models import *
from django.db import connection, transaction
import datetime
from django.shortcuts import render


# Create your views here.
def check_login(request):
    print('请求check_login')
    data = json.loads(request.body.decode('utf-8'))
    try:
        if data['username'] == 'admin' and data['password'] == '12345':
            return JsonResponse({'code': 1, 'data': 1})
        else:
            return JsonResponse({'code': 1, 'data': 0})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def show_books(request):
    try:
        obj_books = Books.objects.all().values()
        books = list(obj_books)
        return JsonResponse({'code': 1, 'data': books})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def show_users(request):
    try:
        obj_users = Users.objects.all().values()
        users = list(obj_users)
        return JsonResponse({'code': 1, 'data': users})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def show_orders(request):
    try:
        obj_orders = Orders.objects.all().values()
        orders = list(obj_orders)
        return JsonResponse({'code': 1, 'data': orders})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def show_payments(request):
    try:
        obj_payments = Payments.objects.all().values()
        payments = list(obj_payments)
        return JsonResponse({'code': 1, 'data': payments})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def show_shoppingcart(request):
    try:
        obj_shoppingcart = ShoppingCart.objects.all().values()
        shoppingCart = list(obj_shoppingcart)
        return JsonResponse({'code': 1, 'data': shoppingCart})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': str(e)})


def add_order(request):
    print('请求add_order')
    data = json.loads(request.body.decode('utf-8'))
    user_id = data['user_id']
    book_id = data['book_id']
    quantity = data['quantity']

    try:

        # 获取当前日期
        order_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # 查询书籍价格
        with connection.cursor() as cursor:
            cursor.execute("SELECT price FROM Books WHERE book_id = %s", [book_id])
            row = cursor.fetchone()
            if row:
                price = row[0]
            else:
                return JsonResponse({'code': 0, 'msg': '书籍不存在'})

        # 计算总价
        total_price = int(price) * int(quantity)

        order_count = Orders.objects.count()

        order_count = order_count + 1

        print(order_count, total_price)
        # 插入订单数据
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Orders (order_id, quantity, total_price, date, book_id_id, user_id_id ) VALUES (%s, %s, %s, %s, %s, %s)",
                [order_count, quantity, str(total_price), order_date, book_id, user_id])
        print('add_order执行完毕')
        return JsonResponse({'code': 1, 'msg': '订单添加成功'})
    except Exception as e:
        print('add_order执行完毕，执行失败')
        return JsonResponse({'code': 0, 'msg': str(e)})


def delete_order(request):
    print('请求delete_order')
    data = json.loads(request.body.decode('utf-8'))
    order_id = data['order_id']
    try:
        # 获取订单对应的book_id和quantity
        with connection.cursor() as cursor:
            cursor.execute("SELECT book_id_id, quantity FROM Orders WHERE order_id = %s", [order_id])
            result = cursor.fetchone()
            book_id, quantity = result[0], result[1]

        # 执行删除事务
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Payments WHERE order_id_id = %s", [order_id])
                cursor.execute("DELETE FROM Orders WHERE order_id = %s", [order_id])

            # 更新Books表中对应book_id的inventory
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Books SET inventory = inventory + %s WHERE book_id = %s", [quantity, book_id])
        print('delete_order执行成功')
        return JsonResponse({'code': 1, 'msg': '订单删除成功'})
    except Exception as e:
        print('delete_order执行失败')
        return JsonResponse({'code': 0, 'msg': str(e)})


def change_order(request):
    print('请求change_order')
    data = json.loads(request.body.decode('utf-8'))
    order_id = data['order_id']
    new_number = data['number']
    try:
        with connection.cursor() as cursor:
            cursor.callproc('update_order', [int(order_id), int(new_number)])
        print('change_order执行成功')
        return JsonResponse({'code': 1, 'msg': '订单更改成功'})
    except Exception as e:
        print('change_order执行失败')
        return JsonResponse({'code': 0, 'msg': str(e)})


def infoorder(request):
    print('请求infoorder')
    data = json.loads(request.body.decode('utf-8'))
    order_id = data['order_id']
    try:
        # 使用 SQL 语句查询视图
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM UserOrders WHERE order_id = %s", [order_id]
            )
            # 获取查询结果
            rows = cursor.fetchall()

            # 将查询结果转换为字典列表
            result = []
            for row in rows:
                result.append({
                    'order_id': row[0],
                    'title': row[1],
                    'quantity': row[2],
                    'total_price': row[3],
                    'order_date': row[4],
                    'username': row[5]
                })
        print('infoorder执行成功')
        return JsonResponse({'code': 1, 'data': result})
    except Exception as e:
        print('infoorder执行失败')
        return JsonResponse({'code': 0, 'msg': str(e)})