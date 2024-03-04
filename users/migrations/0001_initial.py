# Generated by Django 4.1.7 on 2023-05-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=15, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('hp', models.CharField(max_length=11, null=True, unique=True, verbose_name='휴대폰번호')),
                ('email', models.CharField(max_length=33, null=True, unique=True, verbose_name='이메일')),
                ('level', models.CharField(choices=[('2', 'Lv2_사용자'), ('1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=2, max_length=18, verbose_name='등급')),
                ('business_name', models.CharField(max_length=33, null=True, verbose_name='사업자상호')),
                ('business_add', models.CharField(max_length=33, null=True, verbose_name='사업자주소')),
                ('business_regnum', models.CharField(max_length=33, null=True, unique=True, verbose_name='사업자등록번호')),
                ('region', models.CharField(choices=[('0', '군포')], max_length=18, null=True, verbose_name='지역')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'USER_TB',
            },
        ),
    ]
