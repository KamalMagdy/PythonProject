from django.db import models
# from django.contrib.auth import User


#
# class User(models.Model):
#     user_name=models.CharField(max_length=20)
#     user_password=models.IntegerField()
#     user_email=models.CharField(max_length=20)
#     is_blocked=models.CharField(max_length=20)
#     is_admin=models.CharField(max_length=20)
#
#     def is_admin_user(self):
#         if self.is_admin=="yes":
#             return True
#         else:
#             return False
#     def is_blocked_user(self):
#        if self.is_blocked =="yes":
#            return True
#        else:
#            return False
#     is_admin_user.boolean=True
#     is_admin_user.short_description='Admin'
#     is_blocked_user.boolean=True
#     is_blocked_user.short_description='Blocked'