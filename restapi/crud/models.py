from django.db import models

# Create your models here.

class Bank(models.Model):
      ifsc_code=models.CharField(max_length=20,null=False,blank=False)
      city=models.CharField(max_length=20,null=False, blank=False)
      region=models.CharField(max_length=20,null=False, blank=False)

      def __str__(self):
            return self.ifsc_code

class customer(models.Model):
       cust_id=models.CharField(max_length=20,null=False,blank=False)
       bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
       account_type=models.CharField(max_length=20,null=False, blank=False)

       def __str__(self):
            return self.cust_id


class LandingPageVisitor(models.Model):
   visit_date=models.DateField((u"Conversation Date"), blank=True)
   visit_time=models.TimeField((u"Conversation Time"), blank=True)

  
class BalanceActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class LoanActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class FundsActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class LoginActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class LoggedIn(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

    
      
     
      

