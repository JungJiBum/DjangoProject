from django.db import models

# Create your models here.


class customer(models.Model):
    # verbose_name 은 admin 페이지에서 보이는 컬럼명이다.
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=32, verbose_name='사용자 이메일')
    password = models.CharField(max_length=300, verbose_name='비밀번호')
    signDate = models.DateField(auto_now_add=True, verbose_name='가입날짜')

    # 데이터가 문자열로 변환될 때 어떻게 나올지(반환해줄지) 정의하는 함수가 __str__이다.
    def __str__(self):
        return self.username


'''
별도로 테이블명을 지정하고 싶을때 쓰는 코드(안해도 무방함)
class Meta:
    db_table = 'user_define_user_table' #테이블명 지정
    verbose_name = '사용자 모임' # 노출되는 테이블 이름 변경
    verbose_name_plural = '사용자 모임'
'''
