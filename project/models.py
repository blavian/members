from django.db import models
class Account(models.Model):
    name= models.CharField(max_length = 50, unique = True)

    def __str__(self):
     return self.name

class Members(models.Model):
    first_name = models.CharField(max_length = 30, blank = True)
    last_name = models.TextField(max_length = 30, blank = True)
    phone_number = models.CharField(max_length=11)
    client_member_id = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Audience_Member'
        constraints = [
            models.UniqueConstraint(fields=["account_id", "client_member_id"],name="unique_account_client_member_id"),
            models.UniqueConstraint(fields=["account_id", "phone_number"], name="unique_account_phone_number")
            ]
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone_number}' 
