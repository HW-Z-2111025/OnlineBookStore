from django.db import models


# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    inventory = models.IntegerField()

    class Meta:
        db_table = 'Books'
        managed = True


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Users'
        managed = True


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = 'Orders'
        managed = True


class Payments(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_date = models.DateField()

    class Meta:
        db_table = 'Payments'
        managed = True


class ShoppingCart(models.Model):
    shopping_cart_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'ShoppingCart'
        managed = True
