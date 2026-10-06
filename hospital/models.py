from django.db import models

class UserComplaints(models.Model):
    email = models.EmailField()
    comment = models.TextField() 
    
    def __str__(self):
        return self.email
    
class department(models.Model):
    dep_name=models.CharField(max_length=20)
    dep_description=models.TextField()
    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name
    
class hospital(models.Model):
    hos_name=models.CharField(max_length=100)
    hos_des=models.CharField(max_length=400)
    hos_img=models.ImageField(upload_to='hospital')
    def __str__(self):
        return self.hos_name
    
class vir(models.Model):
    p_name=models.CharField(max_length=30)
    p_age=models.CharField(max_length=10)
    p_phone=models.CharField(max_length=12)
    p_email=models.EmailField()
    p_department=models.CharField(max_length=50)
    p_bookedon=models.DateField(auto_now=True)
    def __str__(self):
        return self.p_name
    

class online(models.Model):
    c_name=models.CharField(max_length=30)
    c_number=models.CharField(max_length=16)
    c_month=models.CharField(max_length=20)
    c_cvv=models.CharField(max_length=3)
    c_year=models.CharField(max_length=4)
    c_date=models.DateField(auto_now=True)
    def __str__(self):
        return self.c_name
    
class tokenbooking(models.Model):
    b_name = models.CharField(max_length=30)
    b_age = models.CharField(max_length=2)
    b_place = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=12)
    b_department = models.CharField(max_length=50)
    b_doctor = models.CharField(max_length=30)
    b_date = models.CharField(max_length=10)
    b_datein = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.b_name
    








  


