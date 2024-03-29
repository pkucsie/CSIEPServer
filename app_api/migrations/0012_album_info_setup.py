# Generated by Django 3.1.2 on 2021-11-08 16:39

from django.db import migrations, models
import tyadmin_api_cli.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0011_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255, verbose_name='用户id')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='标题')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.CharField(choices=[('UNUSE', '待审核'), ('COMM', '正常'), ('OVER', '结束'), ('PEDDING', '停用'), ('DEL', '删除')], max_length=255, verbose_name='状态')),
                ('type', models.CharField(default='其他', max_length=255, verbose_name='类型')),
                ('order', models.IntegerField(default=9999, verbose_name='排序')),
                ('viewcnt', models.IntegerField(default=0, verbose_name='访问次数')),
                ('favcnt', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('commentcnt', models.IntegerField(default=0, verbose_name='评论数')),
                ('likecnt', models.IntegerField(default=0, verbose_name='点赞数')),
                ('pic', tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='Album_img', verbose_name='附加图片')),
                ('addtime', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('edittime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('addip', models.CharField(blank=True, max_length=255, null=True, verbose_name='添加IP')),
                ('editip', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改IP')),
            ],
            options={
                'verbose_name': '校友录',
                'verbose_name_plural': '校友录',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255, verbose_name='用户id')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.CharField(choices=[('UNUSE', '待审核'), ('COMM', '正常'), ('OVER', '结束'), ('PEDDING', '停用'), ('DEL', '删除')], max_length=255, verbose_name='状态')),
                ('type', models.CharField(default='其他', max_length=255, verbose_name='类型')),
                ('order', models.IntegerField(default=9999, verbose_name='排序')),
                ('viewcnt', models.IntegerField(default=0, verbose_name='访问次数')),
                ('favcnt', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('commentcnt', models.IntegerField(default=0, verbose_name='评论数')),
                ('likecnt', models.IntegerField(default=0, verbose_name='点赞数')),
                ('exptime', models.IntegerField(default=0, verbose_name='过期时间')),
                ('province', models.CharField(blank=True, max_length=255, null=True, verbose_name='区域(省)')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='区域(市)')),
                ('county', models.CharField(blank=True, max_length=255, null=True, verbose_name='区域(区)')),
                ('pic', tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='Album_info', verbose_name='附加图片')),
                ('addtime', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('edittime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('addip', models.CharField(blank=True, max_length=255, null=True, verbose_name='添加IP')),
                ('editip', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改IP')),
            ],
            options={
                'verbose_name': '信息',
                'verbose_name_plural': '信息',
            },
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='网站名称')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='关于我们')),
                ('logo', tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='Album_about', verbose_name='网站底图')),
                ('adpic', tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='Album_about', verbose_name='海报底图')),
                ('regcheck', models.IntegerField(default=0, verbose_name='注册是否审核')),
                ('addtime', models.IntegerField(default=0, verbose_name='添加时间')),
                ('edittime', models.IntegerField(default=0, verbose_name='修改时间')),
                ('addip', models.CharField(blank=True, max_length=255, null=True, verbose_name='添加IP')),
                ('editip', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改IP')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
    ]
