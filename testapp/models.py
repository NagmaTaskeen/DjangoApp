from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)

    #def __str__(self):
    #    return self.ename
class Subjects(models.Model):
        subId=models.IntegerField()
        subName=models.CharField(max_length=64)

class Teachers(models.Model):
        teacherId=models.IntegerField()
        teacherName=models.CharField(max_length=64)
        teachersQual=models.TextField()
        subId=models.ManyToManyField(Subjects,blank=True,null=True)

class ClassTable(models.Model):
        classId=models.IntegerField()
        class_Name=models.CharField(max_length=64)
        teacherId=models.ManyToManyField(Teachers,blank=True,null=True)



class Students(models.Model):
    stdID=models.IntegerField()
    studentName=models.CharField(max_length=64)
    studentClass=models.ForeignKey(ClassTable,on_delete=models.CASCADE)
    studentAddr=models.TextField()
    studentGrade=models.FloatField()
    classTeacherId=models.ForeignKey(Teachers,blank=True,null=True,on_delete=models.CASCADE)
