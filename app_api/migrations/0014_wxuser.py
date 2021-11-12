# Generated by Django 3.1.2 on 2021-11-09 17:53

from django.db import migrations, models
import tyadmin_api_cli.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0013_auto_20211109_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='WXUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=255, verbose_name='用户id')),
                ('name', models.CharField(max_length=255, verbose_name='用户姓名')),
                ('pic', tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='Album_head', verbose_name='用户头像')),
                ('piccloudid', models.CharField(max_length=1024, verbose_name='用户头像云存储地址')),
                ('phonechecked', models.CharField(max_length=255, verbose_name='已校验的手机号码')),
                ('miniqrcode', models.CharField(max_length=255, verbose_name='小程序码地址')),
                ('miniopenid', models.CharField(max_length=255, verbose_name='小程序openid')),
                ('unionid', models.CharField(max_length=255, verbose_name='微信开放平台unionid')),
                ('wxopenid', models.CharField(max_length=255, verbose_name='公众号openid')),
                ('issubscribe', models.IntegerField(default=0, verbose_name='公众号是否关注')),
                ('subscribetime', models.IntegerField(default=0, verbose_name='公众号关注时间')),
                ('status', models.CharField(choices=[('UNUSE', '待审核'), ('COMM', '正常'), ('OVER', '结束'), ('PEDDING', '停用'), ('DEL', '删除')], max_length=255, verbose_name='状态')),
                ('inviteid', models.CharField(blank=True, max_length=255, null=True, verbose_name='邀请码')),
                ('item', models.CharField(max_length=255, verbose_name='班级')),
                ('sex', models.IntegerField(default=1, verbose_name='性别')),
                ('birth', models.CharField(max_length=255, verbose_name='出生年月')),
                ('native', models.CharField(blank=True, max_length=255, null=True, verbose_name='籍贯')),
                ('openset', models.IntegerField(default=1, verbose_name='资料公开方式')),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='联系电话')),
                ('wechat', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信')),
                ('qq', models.CharField(blank=True, max_length=255, null=True, verbose_name='QQ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='邮箱')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='当前单位')),
                ('companytype', models.CharField(blank=True, max_length=255, null=True, verbose_name='当前单位性质')),
                ('companyduty', models.CharField(blank=True, max_length=255, null=True, verbose_name='当前职位')),
                ('trade', models.CharField(blank=True, max_length=255, null=True, verbose_name='当前行业')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='当前城市')),
                ('workstatus', models.CharField(blank=True, max_length=255, null=True, verbose_name='工作状态')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='自我介绍')),
                ('resource', models.CharField(blank=True, max_length=255, null=True, verbose_name='可提供资源&需求')),
                ('favcnt', models.IntegerField(default=0, verbose_name='被收藏人数')),
                ('invitecnt', models.IntegerField(default=0, verbose_name='邀请人数')),
                ('viewcnt', models.IntegerField(default=0, verbose_name='被查看次数')),
                ('albumcnt', models.IntegerField(default=0, verbose_name='发相册数量')),
                ('infocnt', models.IntegerField(default=0, verbose_name='发互助数量')),
                ('meetcnt', models.IntegerField(default=0, verbose_name='发起活动次数')),
                ('meetjoincnt', models.IntegerField(default=0, verbose_name='活动报名次数')),
                ('wxsex', models.IntegerField(default=1, verbose_name='微信性别')),
                ('wxavatar', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信头像链接')),
                ('wxnickname', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信昵称')),
                ('wxlanguage', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信语言')),
                ('wxcity', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信城市')),
                ('wxprovince', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信省份')),
                ('wxcountry', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信国家')),
                ('wxupdatetime', models.IntegerField(default=0, verbose_name='微信信息更新时间')),
                ('logincnt', models.IntegerField(default=0, verbose_name='登录次数')),
                ('logintime', models.IntegerField(blank=True, default=0, null=True, verbose_name='登录时间')),
                ('addtime', models.IntegerField(default=0, verbose_name='添加时间')),
                ('edittime', models.IntegerField(default=0, verbose_name='修改时间')),
                ('addip', models.CharField(blank=True, max_length=255, null=True, verbose_name='添加IP')),
                ('editip', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改IP')),
            ],
            options={
                'verbose_name': '小程序用户',
                'verbose_name_plural': '小程序用户',
            },
        ),
    ]