from django.db import models


# Create your models here.


class BusinessStaff(models.Model):
    branch = models.ForeignKey('businesses.BusinessBranch', on_delete=models.CASCADE, related_name='staffs')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='staffs')
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StaffPermission(models.Model):
    staff = models.ForeignKey(BusinessStaff, on_delete=models.CASCADE, related_name='permissions')
    write_business = models.BooleanField(default=False)
    write_branch = models.BooleanField(default=False)
    write_product = models.BooleanField(default=False)
