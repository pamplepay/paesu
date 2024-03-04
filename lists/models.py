from .choices import *
from django.conf import settings
from django.db import models


class Paesu_Record(models.Model):

    user_id_p = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    
    # 1. 작성 일자
    date = models.DateField(verbose_name="일자", null=True)
    date_ck = models.CharField(max_length=4, verbose_name="휴일", null=True, blank=True)
    date_weather = models.CharField(max_length=20, verbose_name="날씨", null=True, blank=True)
    date_temperature = models.CharField(max_length=20, verbose_name="기온", null=True, blank=True)


    # 2. 사용량과 배출량(필수)
    waterworks_prevd = models.CharField(max_length=10, verbose_name="상수도 전일", null=True, blank=True)
    waterworks_used = models.CharField(max_length=10, verbose_name="상수도 사용량", null=True, blank=True)
    waterworks_today = models.CharField(max_length=10, verbose_name="상수도 금일", null=True, blank=True)

    underwater_prevd = models.CharField(max_length=10, verbose_name="지하수 전일", null=True, blank=True)
    underwater_used = models.CharField(max_length=10, verbose_name="지하수 사용량", null=True, blank=True)
    underwater_today = models.CharField(max_length=10, verbose_name="지하수 금일", null=True, blank=True)

    diswaste_prevd = models.CharField(max_length=10, verbose_name="폐수배출량 전일", null=True, blank=True)   
    diswaste_used = models.CharField(max_length=10, verbose_name="폐수배출량 사용량", null=True, blank=True)
    diswaste_today = models.CharField(max_length=10, verbose_name="폐수배출량 금일", null=True, blank=True) 

    # 3. 전력 사용량(필수)
    poweruse_prevd = models.CharField(max_length=10, verbose_name="전산전력계지침 전일", null=True, blank=True)
    poweruse_used = models.CharField(max_length=10, verbose_name="전산전력계지침 사용량 ", null=True, blank=True)
    poweruse_today = models.CharField(max_length=10, verbose_name="전산전력계지침 금일", null=True, blank=True)
    poweruse_start = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="전산전력계지침 가동 시작시간", default=9)
    poweruse_end = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="전산전력계지침 가동 종료시간", default=18)
    poweruse_etc = models.CharField(max_length=60, verbose_name="전력량계 참고사항", null=True, blank=True)


    # 4, 추가사항(선택)

    ## 폐수발생량, 재사용량
    genwaster = models.CharField(max_length=20, verbose_name="폐수발생량", null=True, blank=True)
    reuse = models.CharField(max_length=20, verbose_name="재사용량", null=True, blank=True)

    ## 원료 또는 첨가제등의 사용량(선택)
    at_washnum = models.CharField(max_length=10, verbose_name="세차대수", null=True, blank=True)
    at_detergent = models.CharField(max_length=10, verbose_name="세제", null=True, blank=True)
    at_detergent_use = models.CharField(max_length=10, verbose_name="세차1대당 세제사용량", null=True, blank=True)
    at_wax = models.CharField(max_length=10, verbose_name="왁스", null=True, blank=True)
    at_wax_use = models.CharField(max_length=10, verbose_name="세차1대당 왁스사용량", null=True, blank=True)
    at_pom = models.CharField(max_length=10, verbose_name="폼", null=True, blank=True)
    at_pom_use = models.CharField(max_length=10, verbose_name="세차1대당 폼사용량", null=True, blank=True)
    at_sub1 = models.CharField(max_length=40, verbose_name="추가원료1", null=True, blank=True)
    at_sub1_memo = models.CharField(max_length=40, verbose_name="추가원료1 설명", null=True, blank=True)
    at_sub1_use = models.CharField(max_length=10, verbose_name="세차1대당 추가원료1 사용량", null=True, blank=True)
    at_sub2 = models.CharField(max_length=40, verbose_name="추가원료2", null=True, blank=True)
    at_sub2_memo = models.CharField(max_length=40, verbose_name="추가원료2 설명", null=True, blank=True)
    at_sub2_use = models.CharField(max_length=10, verbose_name="세차1대당 추가원료2 사용량", null=True, blank=True)
    at_sub3 = models.CharField(max_length=40, verbose_name="추가원료3", null=True, blank=True)
    at_sub3_memo = models.CharField(max_length=40, verbose_name="추가원료3 설명", null=True, blank=True)
    at_sub3_use = models.CharField(max_length=10, verbose_name="세차1대당 추가원료3 사용량", null=True, blank=True)

    ## 운영시간(선택)
    op_start = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="운영시작시간", default=9)
    op_end = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="운영종료시간", default=18)

    ## 배출시설 가동 시간대(선택)
    emission_start = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="배출시설가동 시작시간", default=9)
    emission_end = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="배출시설 가동 종료시간", default=18)

    ## 방지시설 가동 시간대(선택)
    prev_start = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="방지시설가동 시작시간", default=9)
    prev_end = models.CharField(choices=TIME_CHOICES, max_length=10, verbose_name="방지시설 가동 종료시간", default=18)

    ## 약품 사용량 관련 DB
    med1_name = models.CharField(max_length=60, verbose_name="약품명1", null=True, blank=True)
    med1_used = models.CharField(max_length=10, verbose_name="약품명1 사용량", null=True, blank=True)
    med1_buy = models.CharField(max_length=10, verbose_name="약품명1 구입량", null=True, blank=True)
    med1_balance = models.CharField(max_length=10, verbose_name="약품명1 잔고량", null=True, blank=True)
    med1_etc = models.CharField(max_length=60, verbose_name="약품명1 비고", null=True, blank=True)

    med2_name = models.CharField(max_length=60, verbose_name="약품명2", null=True, blank=True)
    med2_used = models.CharField(max_length=10, verbose_name="약품명2 사용량", null=True, blank=True)
    med2_buy = models.CharField(max_length=10, verbose_name="약품명2 구입량", null=True, blank=True)
    med2_balance = models.CharField(max_length=10, verbose_name="약품명2 잔고량", null=True, blank=True)
    med2_etc = models.CharField(max_length=60, verbose_name="약품명2 비고", null=True, blank=True)

    med3_name = models.CharField(max_length=60, verbose_name="약품명3", null=True, blank=True)
    med3_used = models.CharField(max_length=10, verbose_name="약품명3 사용량", null=True, blank=True)
    med3_buy = models.CharField(max_length=10, verbose_name="약품명3 구입량", null=True, blank=True)
    med3_balance = models.CharField(max_length=10, verbose_name="약품명3 잔고량", null=True, blank=True)
    med3_etc = models.CharField(max_length=60, verbose_name="약품명3 비고", null=True, blank=True)

    med4_name = models.CharField(max_length=60, verbose_name="약품명4", null=True, blank=True)
    med4_used = models.CharField(max_length=10, verbose_name="약품명4 사용량", null=True, blank=True)
    med4_buy = models.CharField(max_length=10, verbose_name="약품명4 구입량", null=True, blank=True)
    med4_balance = models.CharField(max_length=10, verbose_name="약품명4 잔고량", null=True, blank=True)
    med4_etc = models.CharField(max_length=60, verbose_name="약품명4 비고", null=True, blank=True)

    ## 슬러지 처리시설(선택)
    sluge_gene = models.CharField(max_length=10, verbose_name="슬러지 발생량", null=True, blank=True)
    sluge_used = models.CharField(max_length=10, verbose_name="슬러지 처리량", null=True, blank=True)
    sluge_keep = models.CharField(max_length=10, verbose_name="슬러지 보관량", null=True, blank=True)
    sluge_func = models.CharField(max_length=10, verbose_name="슬러지 함수율(%)", null=True, blank=True)
    sluge_place = models.CharField(max_length=60, verbose_name="슬러지 보관장소", null=True, blank=True)
    sluge_selfplace = models.CharField(max_length=60, verbose_name="슬러지 처리장소", null=True, blank=True)
    sluge_corp = models.CharField(max_length=60, verbose_name="슬러지 위탁처리업소명", null=True, blank=True)

    ## 방지시설 고장유무 및 특기사항(선택)
    remarks = models.CharField(max_length=200, verbose_name="특기사항", null=True, blank=True)

    ## 지도 또는 점검 받은 사항(선택)
    advise = models.CharField(max_length=200, verbose_name="지도사항", null=True, blank=True)

    def __str__(self):
        return str(self.user_id_p)

    class Meta:
        db_table="PAESU_RECORD_TB"
        verbose_name="레포트정보"
        verbose_name_plural="레포트정보"

        constraints = [
            models.UniqueConstraint(fields=['date', 'date_ck'], name='유저 기록 unique key')
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)