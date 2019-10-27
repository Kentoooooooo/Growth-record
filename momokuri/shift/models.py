from django.db import models

# Create your models here.


class Submit(models.Model):
    class Meta:
        db_table = 'submit'
        verbose_name = verbose_name_plural = '提出シフト'

    sort_id = models.IntegerField(verbose_name='sort', default=id, unique=True)
    name = models.CharField(verbose_name='名前', max_length=25)
    memo = models.CharField(verbose_name='メモ', max_length=500)
    d1s = models.CharField(verbose_name='出勤時間1',
                           blank=True, null=True, max_length=4)
    d1e = models.CharField(verbose_name='退勤時間1',
                           blank=True, null=True, max_length=4)
    d2s = models.CharField(verbose_name='出勤時間2',
                           blank=True, null=True, max_length=4)
    d2e = models.CharField(verbose_name='退勤時間2',
                           blank=True, null=True, max_length=4)
    d3s = models.CharField(verbose_name='出勤時間3',
                           blank=True, null=True, max_length=4)
    d3e = models.CharField(verbose_name='退勤時間3',
                           blank=True, null=True, max_length=4)
    d4s = models.CharField(verbose_name='出勤時間4',
                           blank=True, null=True, max_length=4)
    d4e = models.CharField(verbose_name='退勤時間4',
                           blank=True, null=True, max_length=4)
    d5s = models.CharField(verbose_name='出勤時間5',
                           blank=True, null=True, max_length=4)
    d5e = models.CharField(verbose_name='退勤時間5',
                           blank=True, null=True, max_length=4)
    d6s = models.CharField(verbose_name='出勤時間6',
                           blank=True, null=True, max_length=4)
    d6e = models.CharField(verbose_name='退勤時間6',
                           blank=True, null=True, max_length=4)
    d7s = models.CharField(verbose_name='出勤時間7',
                           blank=True, null=True, max_length=4)
    d7e = models.CharField(verbose_name='退勤時間7',
                           blank=True, null=True, max_length=4)
    d8s = models.CharField(verbose_name='出勤時間8',
                           blank=True, null=True, max_length=4)
    d8e = models.CharField(verbose_name='退勤時間8',
                           blank=True, null=True, max_length=4)
    d9s = models.CharField(verbose_name='出勤時間9',
                           blank=True, null=True, max_length=4)
    d9e = models.CharField(verbose_name='退勤時間9',
                           blank=True, null=True, max_length=4)
    d10s = models.CharField(verbose_name='出勤時間10',
                            blank=True, null=True, max_length=4)
    d10e = models.CharField(verbose_name='退勤時間10',
                            blank=True, null=True, max_length=4)
    d11s = models.CharField(verbose_name='出勤時間11',
                            blank=True, null=True, max_length=4)
    d11e = models.CharField(verbose_name='退勤時間11',
                            blank=True, null=True, max_length=4)
    d12s = models.CharField(verbose_name='出勤時間12',
                            blank=True, null=True, max_length=4)
    d12e = models.CharField(verbose_name='退勤時間12',
                            blank=True, null=True, max_length=4)
    d13s = models.CharField(verbose_name='出勤時間13',
                            blank=True, null=True, max_length=4)
    d13e = models.CharField(verbose_name='退勤時間13',
                            blank=True, null=True, max_length=4)
    d14s = models.CharField(verbose_name='出勤時間14',
                            blank=True, null=True, max_length=4)
    d14e = models.CharField(verbose_name='退勤時間14',
                            blank=True, null=True, max_length=4)
    d15s = models.CharField(verbose_name='出勤時間15',
                            blank=True, null=True, max_length=4)
    d15e = models.CharField(verbose_name='退勤時間15',
                            blank=True, null=True, max_length=4)
    d16s = models.CharField(verbose_name='出勤時間16',
                            blank=True, null=True, max_length=4)
    d16e = models.CharField(verbose_name='退勤時間16',
                            blank=True, null=True, max_length=4)

    def __str__(self):
        return self.name
