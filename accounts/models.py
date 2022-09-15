from django.db import models
from django.contrib.auth.models import User

gender=(
        ('m','male'),
        ('f','female')
)
 
Specializations=(
                ('عظام','عظام'),('انف واذن وحنجرة','انف واذن وحنجرة'),('نساءوتوليد','نساءوتوليد'),('قلب واوعية دموية','قلب واوعية دموية')
                ,('جلدية','جلدية'),('اطفال حديثي الولادة','اطفال حديثي الولادة'),('امراض دم','امراض دم'),('نفسي','نفسي')
                ,('اورام','اورام'),('باطنه','باطنه'),('تخسيس وتغذية','تخسيس وتغذية'),('جراحة اطفال','جراحة اطفال')
                ,('جراحة اورام','جراحة اورام'),('جراحة اوعية دموية','جراحة اوعية دموية'),('اسنان','اسنان')
                ,('جراحة تجميل','جراحة تجميل'),('جراحه سمنة ومناظير','جراحه سمنة ومناظير'),('مخ واعصاب','مخ واعصاب')
)

governorate=  (('Mansoura', 'Mansoura'),('Alexandria', 'Alexandria'),
                ('Cairo', 'Cairo'),('Minya', 'Minya'),
                ('Tanta', 'Tanta'),('Kafr El Sheikh', 'Kafr El Sheikh'),
                ('Asyut', 'Asyut'),('Damietta', 'Damietta'),
                ('Giza', 'Giza'),('	Ismailia', 'Ismailia'),
                ('Zagazig', 'Zagazig'),('Hurghada', 'Hurghada'),
                )


ratings=  (('recommend', 'recommend'),('neutral', 'neutral'),('not recommend', 'not recommend'))


class Profile(models.Model):
    user=models.ForeignKey(User,verbose_name=('user'),on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    Specialization=models.CharField(max_length=50,choices=Specializations,default='عظام')
    governorate=models.CharField(max_length=50,choices=governorate,default='Cairo')
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    who_i=models.TextField(max_length=2502)
    price=models.IntegerField()
    image=models.ImageField(("الصورة الشخصية"), upload_to='profile',null=True,blank=True )
    facebook=models.CharField(max_length=100,null=True,blank=True)
    twitter=models.CharField(max_length=100,null=True,blank=True)
    gmail=models.CharField(max_length=100,null=True,blank=True)
    join_data=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    gender=models.CharField(max_length=50,choices=gender,default='male')
    def __str__(self):
        return self.name



class Comment(models.Model):
    profile=models.ForeignKey(Profile,related_name='comments', on_delete=models.CASCADE,null=True,blank=True)
    rating=models.CharField(max_length=50,choices=ratings,null=True,blank=True)
    comment_space=models.TextField(max_length=250,null=True,blank=True)
    data_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} at {}'.format(self.comment_space, self.data_added)
