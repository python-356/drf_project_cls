from django.db import models
from datetime import datetime

# Create your models here.


Week = [
    (0, "周一"),
    (1, "周二"),
    (2, "周三"),
    (3, "周四"),
    (4, "周五"),
    (5, "周六"),
    (6, "周七"),
]
Subject = [
    (0, "大数据"),
    (1, "Python"),
    (2, "HTML"),
]
Bay = [
    (0, "上午"),
    (1, "下午"),
]


class Classroom(models.Model):
    name = models.CharField(max_length=25, verbose_name='班号')
    subject = models.SmallIntegerField(choices=Subject, blank=False, verbose_name='所属学科')
    # subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='专业')

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=25, verbose_name='教师名称')

    class Meta:
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=25, verbose_name='学生名称')
    cls = models.ForeignKey(Classroom, on_delete=models.CASCADE, verbose_name='所属班级')
    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=25, verbose_name='课程名称')
    teacher = models.ManyToManyField(Teacher, verbose_name='讲师')
    description = models.TextField(max_length=120, verbose_name='课程描述')
    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ClassSchedule(models.Model):
    week = models.SmallIntegerField(choices=Week, blank=False, verbose_name='日期')
    time = models.SmallIntegerField(choices=Bay, blank=False, verbose_name='时间段')
    cls = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, verbose_name='班级')
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课堂名称')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='讲师')
    # 学科

    class Meta:
        verbose_name = "课程表信息"
        verbose_name_plural = verbose_name
