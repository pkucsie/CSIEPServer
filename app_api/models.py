from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from tyadmin_api_cli.fields import SImageField


class EmailVerifyRecord(models.Model):
    """邮箱验证码model"""
    SEND_CHOICES = (
        ("register", "注册"),
        ("forget", "找回密码"),
        ("update_email", "修改邮箱"),
        ("login_auth", "登录授权"),
    )
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code + ":" + self.email


class OrderStatus(models.Model):
    text = models.CharField(max_length=255, verbose_name="订单状态")
    code = models.IntegerField(default=0, verbose_name="订单状态code", unique=True)

    class Meta:
        verbose_name = '订单状态'
        verbose_name_plural = verbose_name


class Order(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    code = models.CharField(max_length=255, verbose_name="订单号")
    time = models.DateTimeField(auto_now=True, max_length=255, verbose_name="订单生成时间")
    expired = models.IntegerField(default=1800000, verbose_name="过期时间")
    coupon = models.IntegerField(default=0, verbose_name="优惠卷")
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING, verbose_name="订单状态", default="",
                               blank=True, db_constraint=False, related_name="list")
    way = models.ForeignKey("RechargePay", on_delete=models.DO_NOTHING, verbose_name="支付方式", default="", null=True,
                            blank=True, db_constraint=False, related_name="list")

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="所属订单", default="",
                              blank=True, db_constraint=False, related_name="list")
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    img = SImageField(max_length=255, verbose_name="封面图")
    title = models.CharField(max_length=255, verbose_name="标题")
    price = models.IntegerField(default=0, verbose_name="价格")
    isDiscount = models.BooleanField(verbose_name="是否优惠")
    discountPrice = models.IntegerField(default=0, verbose_name="折后价格")

    class Meta:
        verbose_name = '订单小项'
        verbose_name_plural = verbose_name


class CouponRange(models.Model):
    text = models.CharField(max_length=255, verbose_name="优惠券使用范围")
    code = models.IntegerField(default=0, verbose_name="优惠券使用范围code", unique=True)

    class Meta:
        verbose_name = '充值方式'
        verbose_name_plural = verbose_name


class CouponStatus(models.Model):
    text = models.CharField(max_length=255, verbose_name="优惠券状态")
    code = models.IntegerField(default=0, verbose_name="优惠券状态code", unique=True)

    class Meta:
        verbose_name = '充值方式'
        verbose_name_plural = verbose_name


class Coupon(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    orderid = models.CharField(max_length=255, default="", verbose_name="订单id")
    number = models.IntegerField(default=0, verbose_name="金额")
    limit = models.IntegerField(default=0, verbose_name="限制类型")
    starttime = models.DateTimeField(max_length=255, verbose_name="开始时间")
    endtime = models.DateTimeField(max_length=255, verbose_name="结束时间")
    usetime = models.CharField(max_length=255, default="", verbose_name="使用时间")
    range = models.ForeignKey(CouponRange, on_delete=models.DO_NOTHING, verbose_name="优惠券使用范围", default="",
                              blank=True, db_constraint=False, )
    status = models.ForeignKey(CouponStatus, on_delete=models.DO_NOTHING, verbose_name="优惠券使用状态", default="",
                               blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '优惠券'
        verbose_name_plural = verbose_name


class IntegralType(models.Model):
    code = models.CharField(max_length=255, default="0", verbose_name="积分商品类别")
    text = models.CharField(max_length=255, verbose_name="积分商品类别code")

    class Meta:
        verbose_name = '积分商品类别'
        verbose_name_plural = verbose_name


class Integral(models.Model):
    img = SImageField(upload_to="Integral_img", max_length=255, verbose_name="图片")
    title = models.CharField(max_length=255, verbose_name="标题")
    integral = models.IntegerField(default=0, verbose_name="积分数")
    type = models.ForeignKey(IntegralType, on_delete=models.DO_NOTHING, verbose_name="积分商品类型", default="",
                             blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '积分商品'
        verbose_name_plural = verbose_name


class Notice(models.Model):
    code = models.IntegerField(default=0, verbose_name="通知code")
    time = models.DateTimeField(max_length=255, verbose_name="通知时间")
    title = models.CharField(max_length=255, verbose_name="通知标题")

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = verbose_name


class LessonScript(models.Model):
    text = models.CharField(max_length=255, verbose_name="课程角标文本")
    code = models.IntegerField(default=0, verbose_name="课程角标code", unique=True)

    class Meta:
        verbose_name = '课程角标类型'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="课程标题", unique=True)
    introduction = models.CharField(max_length=255, default="", verbose_name="课程介绍")
    img = SImageField(upload_to="Lesson_img", max_length=255, verbose_name="课程图片")
    banner = SImageField(upload_to="Lesson_banner", max_length=255, verbose_name="课程Banner")
    price = models.IntegerField(default=0, verbose_name="课程价格")
    isDiscount = models.BooleanField(verbose_name="是否打折")
    discountPrice = models.IntegerField(default=0, verbose_name="打折后价格")
    time = models.DateTimeField(auto_now=True, max_length=255, verbose_name="课程添加时间")
    persons = models.IntegerField(default=0, verbose_name="学习人数")
    comments = models.IntegerField(default=0, verbose_name="评论数")
    category = models.ForeignKey("LabelType", on_delete=models.DO_NOTHING, verbose_name="课程分类", default="",
                                 blank=True, db_constraint=False)
    type = models.ForeignKey("LessonType", on_delete=models.DO_NOTHING, verbose_name="课程类型", default="",
                             blank=True, db_constraint=False, )
    hard = models.ForeignKey("LessonHardType", on_delete=models.DO_NOTHING, verbose_name="课程难度类型", default="",
                             blank=True, db_constraint=False, )
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, verbose_name="课程讲师", default="",
                                blank=True, db_constraint=False)
    labels = models.ManyToManyField("Label", verbose_name="课程拥有的label", default=None,
                                    blank=True, db_constraint=False)
    script = models.ForeignKey(LessonScript, on_delete=models.DO_NOTHING, verbose_name="课程角标", default="", null=True,
                               blank=True, db_constraint=False)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="问题标题")
    answers = models.IntegerField(default=0, verbose_name="问题回答")
    views = models.IntegerField(default=0, verbose_name="问题点击量")
    icon = SImageField(max_length=255, default="", verbose_name="问题图标")
    isResolve = models.BooleanField(verbose_name="问题是否解决")
    tags = models.ManyToManyField("Label", verbose_name="问题拥有的label", default=None,
                                  blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name


class Cart(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    img = SImageField(max_length=255, verbose_name="封面图", default="")
    title = models.CharField(max_length=255, verbose_name="标题")
    price = models.IntegerField(default=0, verbose_name="价格")
    isDiscount = models.BooleanField(verbose_name="是否优惠")
    discountPrice = models.IntegerField(default=0, verbose_name="折后价格")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


class Consult(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id", default="1", blank=True, null=True)
    like = models.BooleanField(verbose_name="是否点赞", default=False)
    number = models.IntegerField(default=0, verbose_name="点赞数")
    title = models.CharField(max_length=255, verbose_name="咨询标题")
    answer = models.CharField(max_length=1000, verbose_name="咨询回答")
    time = models.DateTimeField(max_length=255, verbose_name="咨询回答")
    course_name = models.CharField(max_length=255, verbose_name="课程名字")

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class User(AbstractUser):
    # REQUIRED_FIELDS = []
    # USERNAME_FIELD = "username"
    #
    # is_active = True
    #
    # @property
    # def is_anonymous(self):
    #     """
    #     Always return False. This is a way of comparing User objects to
    #     anonymous users.
    #     """
    #     return False
    #
    # @property
    # def is_authenticated(self):
    #     """
    #     Always return True. This is a way to tell if the user has been
    #     authenticated in templates.
    #     """
    #     return True

    # username = models.CharField(max_length=255, verbose_name="用户名", unique=True)
    # password = models.CharField(max_length=255, verbose_name="密码")
    nickname = models.CharField(max_length=255, verbose_name="昵称")
    avatar = SImageField(upload_to="User_avatar", max_length=255, default="https://static.mukewang.com/static/img/avatar_default.png",
                        verbose_name="头像")
    sex = models.CharField(max_length=255, default="male", verbose_name="性别")
    job = models.CharField(max_length=255, default="", verbose_name="工作")
    city = models.CharField(max_length=255, default="", verbose_name="城市")
    signature = models.CharField(max_length=255, default="", verbose_name="个性签名")
    hour = models.IntegerField(default=0, verbose_name="学习时长")
    exp = models.IntegerField(default=0, verbose_name="学习经验数")
    integral = models.IntegerField(default=0, verbose_name="积分数")
    follow = models.IntegerField(default=0, verbose_name="follow数")
    fans = models.IntegerField(default=0, verbose_name="粉丝数")
    email = models.CharField(max_length=255, default="", verbose_name="邮箱")
    qq = models.CharField(max_length=255, default="", verbose_name="qq")
    phone = models.CharField(max_length=255, default="", verbose_name="手机号")
    wechat = models.CharField(max_length=255, default="", verbose_name="微信")
    weibo = models.CharField(max_length=255, default="", verbose_name="微博")
    create_time = models.DateTimeField(auto_now=True, verbose_name="注册时间")

    # objects = UserManager()
    #
    # def check_password(self, raw_password):
    #     """
    #     Return a boolean of whether the raw_password was correct. Handles
    #     hashing formats behind the scenes.
    #     """
    #
    #     def setter(raw_password):
    #         self.set_password(raw_password)
    #         # Password hash upgrades shouldn't be considered password changes.
    #         self._password = None
    #         self.save(update_fields=["password"])
    #
    #     return check_password(raw_password, self.password, setter)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Bill(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    orderno = models.CharField(max_length=255, verbose_name="订单号")
    name = models.CharField(max_length=255, verbose_name="课程名字")
    time = models.CharField(max_length=255, verbose_name="时间")
    cost = models.IntegerField(default=0, verbose_name="消费金额")
    way = models.ForeignKey("RechargePay", on_delete=models.DO_NOTHING, verbose_name="账单支方式", default="", null=True,
                            blank=True, db_constraint=False, )

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = verbose_name


class Address(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    name = models.CharField(max_length=255, verbose_name="用户名")
    phone = models.CharField(max_length=255, verbose_name="手机号")
    area = models.CharField(max_length=255, verbose_name="地区")
    address = models.CharField(max_length=255, verbose_name="地址")
    postcode = models.CharField(max_length=255, verbose_name="邮编")
    isDefault = models.BooleanField(verbose_name="是否默认", default=False)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name


class Catalog(models.Model):
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    introduction = models.CharField(max_length=255, default="", verbose_name="课程介绍")
    isComplete = models.BooleanField(verbose_name="是否完结")

    class Meta:
        verbose_name = '课程目录信息'
        verbose_name_plural = verbose_name


class LogType(models.Model):
    text = models.CharField(max_length=255, verbose_name="登录类型")
    code = models.IntegerField(default=0, verbose_name="登录类型code", unique=True)

    class Meta:
        verbose_name = '登录类型'
        verbose_name_plural = verbose_name


class Log(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    time = models.CharField(max_length=255, verbose_name="时间")
    ip = models.CharField(max_length=255, verbose_name="ip地址")
    device = models.CharField(max_length=255, verbose_name="设备")
    city = models.CharField(max_length=255, verbose_name="城市")
    type = models.ForeignKey(LogType, on_delete=models.DO_NOTHING, verbose_name="日志类型", default="", null=True,
                             blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '访问日志'
        verbose_name_plural = verbose_name


class ReadType(models.Model):
    value = models.CharField(max_length=255, verbose_name="类型值")
    sort = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '专栏分类'
        verbose_name_plural = verbose_name


class ReadChapter(models.Model):
    read = models.ForeignKey("Read", on_delete=models.DO_NOTHING, verbose_name="所属专栏", default="",
                             blank=True, db_constraint=False, related_name="chapter")
    title = models.CharField(max_length=255, verbose_name="章节标题")

    class Meta:
        verbose_name = '专栏章节'
        verbose_name_plural = verbose_name


class ReadChapterItem(models.Model):
    read_chapter = models.ForeignKey(ReadChapter, on_delete=models.DO_NOTHING, verbose_name="所属章节", default="",
                                     blank=True, db_constraint=False, related_name="chapter_item")
    title = models.CharField(max_length=255, verbose_name="小章节标题", default="")
    isTry = models.BooleanField(verbose_name="是否试看")
    time = models.DateTimeField(verbose_name="发布时间")

    class Meta:
        verbose_name = '专栏章节小节'
        verbose_name_plural = verbose_name


class TaskTimeline(models.Model):
    taskid = models.CharField(max_length=255, verbose_name="活动id")
    tasktype = models.CharField(max_length=255, verbose_name="分类名称")
    name = models.CharField(max_length=255, verbose_name="活动名称")
    content = models.TextField(max_length=255, verbose_name="活动内容")
    dtime = models.DateField(verbose_name="活动日期")
    stime = models.DateTimeField(verbose_name="开始时间")
    etime = models.DateTimeField(verbose_name="结束时间")
    order = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '时间线'
        verbose_name_plural = verbose_name


class Organization(models.Model):
    ORG_CHOICES = (
        ("director", "指导单位"),
        ("sponsor", "主办单位"),
        ("agency", "银牌金牌"),
        ("donator", "金牌赞助"),
        ("strategy", "战略合作单位"),        
        ("supporter", "支持单位"),
        ("auxorg", "协办单位—机构组织"),
        ("auxuniv", "协办单位—各高校研会"),
        ("auxaux", "协办单位—各高校创协"),
    )    
    name = models.CharField(max_length=255, verbose_name="机构名称", unique=True)
    orgtype = models.CharField(max_length=255, choices=ORG_CHOICES, verbose_name="机构类型", default='sponsor')
    avatar = SImageField(upload_to="org_avatar", max_length=255, verbose_name="机构图标240x80px")    
    service = models.CharField(max_length=255, verbose_name="机构业务")
    orgurl = models.CharField(max_length=255, verbose_name="机构链接", default='')
    introduction = models.TextField(verbose_name="机构介绍")
    order = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name


class VipGuest(models.Model):
    name = models.CharField(max_length=255, verbose_name="嘉宾姓名", unique=True)
    avatar = SImageField(upload_to="vipguest_avatar", max_length=255, verbose_name="嘉宾头像210x280px")
    #corp = models.CharField(max_length=255, verbose_name="嘉宾公司")
    job = models.CharField(max_length=255, verbose_name="嘉宾职业")
    introduction = models.TextField(verbose_name="个人介绍")
    order = models.IntegerField(default=0, verbose_name="排序")
    enable = models.BooleanField(verbose_name="可见", default=True)

    class Meta:
        verbose_name = '嘉宾'
        verbose_name_plural = verbose_name


class Track(models.Model):
    track_key = models.CharField(max_length=50, default="other", verbose_name="赛道唯一标识", unique=True)
    track_name = models.CharField(max_length=50, default="其他", verbose_name="赛道名称", unique=True)

    class Meta:
        verbose_name = '赛道'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.track_name


class Judge(models.Model):
    TRACK_CHOICES = (
        ("public_welfare", "公益"),
        ("education", "教育"),
        ("health", "医疗大健康"),
        ("environment_protection", "环保"),
        ("internet", "互联网"),
        ("ai", "人工智能"),
        ("consumption", "新消费和食品"),
        ("traffic", "汽车交通"),
        ("manufacturing", "先进制造"),
        ("iot_ar_vr", "物联网与AR、VR"),
        ("materials_energy", "新材料与能源"),
        ("other", "其他"),
        ("finance", "金融"),
    )

    name = models.CharField(max_length=255, verbose_name="评委姓名", unique=True)
    # avatar = SImageField(upload_to="judge_avatar", max_length=255, verbose_name="评委头像", blank=True)
    job = models.CharField(max_length=255, verbose_name="评委职业")
    # introduction = models.TextField(verbose_name="评委介绍", blank=True)
    mail = models.EmailField(verbose_name="邮箱", max_length=255)
    order = models.IntegerField(default=0, verbose_name="排序")
    track = models.ManyToManyField(Track, blank=True, verbose_name="赛道")

    class Meta:
        verbose_name = '评委'
        verbose_name_plural = verbose_name


'''
项目管理
'''
class Project(models.Model):
    TRACK_CHOICES = (
        ("public_welfare", "公益"),
        ("education", "教育"),
        ("health", "医疗大健康"),
        ("environment_protection", "环保"),
        ("internet", "互联网"),
        ("ai", "人工智能"),
        ("consumption", "新消费和食品"),
        ("traffic", "汽车交通"),
        ("manufacturing", "先进制造"),

        ("iot_ar_vr", "物联网与AR、VR"),
        ("materials_energy", "新材料与能源"),
        ("other", "其他"),
        ("finance", "金融"),
    )

    GROUP_TYPE_CHOICES = (
        ("creative", "创意组"),
        ("startup", "初创组"),

    )

    project_name = models.CharField(max_length=255, verbose_name="项目名称")
    # project_stage = models.IntegerField(verbose_name="所处阶段")
    project_track = models.ForeignKey(Track, verbose_name="项目赛道", on_delete=models.DO_NOTHING)
    project_group_type = models.CharField(max_length=255, verbose_name="项目组别", choices=GROUP_TYPE_CHOICES)
    project_leader_name = models.CharField(max_length=255, verbose_name="领队姓名")
    project_phone = models.CharField(max_length=255, verbose_name="联系电话")
    project_introduction = models.TextField( verbose_name="项目简介")
    # project_file = models.CharField(max_length=255, verbose_name="项目相关文件")

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name


class Score(models.Model):
    judge = models.ForeignKey(Judge, verbose_name="评委", on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, verbose_name="项目", on_delete=models.DO_NOTHING)
    round = models.IntegerField(default=0, verbose_name="轮次")
    innovation = models.IntegerField(default=0, verbose_name="创新性")
    commercial = models.IntegerField(default=0, verbose_name="商业性")
    competitiveness = models.IntegerField(default=0, verbose_name="竞争力")
    team = models.IntegerField(default=0, verbose_name="团队情况")
    public_benefit = models.IntegerField(default=0, verbose_name="社会收益")
    sum = models.IntegerField(default=0, verbose_name="总分")
    comment = models.TextField(verbose_name="点评")

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = verbose_name

    @property
    def sum_score(self):
        self.sum = self.innovation + self.commercial + self.competitiveness + self.team + self.public_benefit
        self.save()
        return self.sum


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="讲师姓名", unique=True)
    avatar = SImageField(upload_to="Teacher_avatar", max_length=255, verbose_name="讲师头像")
    job = models.CharField(max_length=255, verbose_name="讲师职业")
    introduction = models.TextField(verbose_name="个人介绍")

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    name = models.CharField(max_length=255, verbose_name="评论者", default="")
    avatar = SImageField(upload_to="Comment_avatar", max_length=255, verbose_name="评论头像", default="")
    content_score = models.FloatField(verbose_name="内容分数", default=0)
    easy_score = models.FloatField(verbose_name="简单分数", default=0)
    logic_score = models.FloatField(verbose_name="逻辑分数", default=0)
    time = models.DateTimeField(auto_now=True, verbose_name="评论时间")
    comment = models.CharField(max_length=1000, verbose_name="评论内容", default="")

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Hot(models.Model):
    value = models.CharField(max_length=255, verbose_name="热搜词")
    time = models.DateTimeField(verbose_name="热搜时间", default=datetime.now)

    class Meta:
        verbose_name = '热搜'
        verbose_name_plural = verbose_name


class RechargeAction(models.Model):
    text = models.CharField(max_length=255, verbose_name="充值类型")
    code = models.IntegerField(default=0, verbose_name="充值类型code", unique=True)

    class Meta:
        verbose_name = '充值类型'
        verbose_name_plural = verbose_name


class RechargePay(models.Model):
    text = models.CharField(max_length=255, verbose_name="充值方式")
    code = models.IntegerField(default=0, verbose_name="充值方式code", unique=True)

    class Meta:
        verbose_name = '充值方式'
        verbose_name_plural = verbose_name


class Recharge(models.Model):
    userid = models.CharField(max_length=255, verbose_name="用户id")
    time = models.DateTimeField(auto_now=True, max_length=255, verbose_name="充值时间")
    money = models.IntegerField(default=0, verbose_name="充值金额(分)")
    remark = models.CharField(max_length=255, default="", verbose_name="备注")
    action = models.ForeignKey(RechargeAction, on_delete=models.DO_NOTHING, verbose_name="RechargeAction", default="",
                               blank=True, db_constraint=False, )
    way = models.ForeignKey(RechargePay, on_delete=models.DO_NOTHING, verbose_name="RechargePay", default="",
                            blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '充值记录'
        verbose_name_plural = verbose_name


class LabelFollow(models.Model):
    userid = models.IntegerField(verbose_name="用户id")
    labelid = models.IntegerField(verbose_name="Label的id", default=0)
    title = models.CharField(max_length=255, verbose_name="Label的title")

    class Meta:
        verbose_name = '关注Label'
        verbose_name_plural = verbose_name
        unique_together = ("userid", "labelid")


class Student(models.Model):
    avatar = SImageField(upload_to='pic', max_length=255, verbose_name="头像")
    name = models.CharField(max_length=255, verbose_name="名称")
    number = models.IntegerField(default=0, verbose_name="积分数")
    type = models.ForeignKey("StudentType", on_delete=models.DO_NOTHING, verbose_name="学生类型", default="",
                             blank=True, db_constraint=False, )

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name


class StudentType(models.Model):
    text = models.CharField(max_length=255, verbose_name="学生类型")
    code = models.IntegerField(default=0, verbose_name="学生code", unique=True)

    class Meta:
        verbose_name = '学生类型'
        verbose_name_plural = verbose_name


class Navigation(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    code = models.CharField(max_length=255, verbose_name="code")
    sort = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '首页左侧菜单'
        verbose_name_plural = verbose_name


class Read(models.Model):
    type = models.CharField(max_length=255, verbose_name="类型")
    title = models.CharField(max_length=255, verbose_name="标题", unique=True)
    img = SImageField(upload_to="Read_img", max_length=255, verbose_name="图片")
    detailImg = SImageField(upload_to="Read_detail", max_length=255, verbose_name="细节图片")
    desc = models.CharField(max_length=255, verbose_name="描述")
    price = models.IntegerField(default=0, verbose_name="价格")
    persons = models.IntegerField(default=0, verbose_name="人数")
    term = models.IntegerField(default=0, verbose_name="章节数")
    isRecommend = models.BooleanField(verbose_name="是否推荐", default=False)
    author = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, verbose_name="作者", default="",
                               blank=True, db_constraint=False)

    class Meta:
        verbose_name = '专栏'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="文章名")
    img = SImageField(upload_to="Article_img", max_length=255, verbose_name="图片")
    views = models.IntegerField(default=0, verbose_name="查看量")
    author = models.CharField(max_length=255, verbose_name="作者")
    tag = models.CharField(max_length=255, verbose_name="标签")
    time = models.CharField(max_length=255, verbose_name="时间")
    type = models.ForeignKey("ArticleType", on_delete=models.DO_NOTHING, verbose_name="文章类型", default="",
                             blank=True, db_constraint=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class History(models.Model):
    value = models.CharField(max_length=255, verbose_name="历史记录值")
    time = models.DateTimeField(auto_now=True, max_length=255, verbose_name="记录时间")

    class Meta:
        verbose_name = '搜索历史'
        verbose_name_plural = verbose_name


class QaType(models.Model):
    text = models.CharField(max_length=255, verbose_name="问题类型")
    code = models.IntegerField(default=0, verbose_name="问题类型code", unique=True)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name


class Answer(models.Model):
    user_name = models.CharField(max_length=255, verbose_name="用户名")
    content = models.CharField(max_length=1000, verbose_name="回答内容", default="")

    class Meta:
        verbose_name = '回答'
        verbose_name_plural = verbose_name


class Qa(models.Model):
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    title = models.CharField(max_length=255, verbose_name="问题名称", default="")
    avatar = SImageField(upload_to="Qa_avatar", max_length=255, verbose_name="提问者头像", default="")
    answers = models.IntegerField(verbose_name="回答数", default=0)
    views = models.IntegerField(verbose_name="查看数", default=0)
    chapter = models.CharField(max_length=255, verbose_name="章节名字", default="")
    time = models.DateTimeField(auto_now=True, verbose_name="评论时间")
    comment = models.CharField(max_length=1000, verbose_name="评论内容", default="")
    type = models.ForeignKey(QaType, on_delete=models.DO_NOTHING, verbose_name="问题类型", default="",
                             blank=True, db_constraint=False, )

    class Meta:
        verbose_name = 'Qa'
        verbose_name_plural = verbose_name


class ArticleType(models.Model):
    title = models.CharField(max_length=255, verbose_name="文章类型")
    code = models.IntegerField(default=0, verbose_name="文章code", unique=True)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name


class UserNotice(models.Model):
    messageid = models.ForeignKey(Notice, on_delete=models.DO_NOTHING, verbose_name="通知id", default="",
                                  blank=True, db_constraint=False, related_name="notice")
    userid = models.CharField(max_length=255, verbose_name="通知用户id")
    isRead = models.BooleanField(verbose_name="通知已读")
    isDelete = models.BooleanField(verbose_name="通知已删除")

    class Meta:
        verbose_name = '用户通知'
        verbose_name_plural = verbose_name


class Slider(models.Model):
    img = SImageField(upload_to="Slider_img", max_length=255, verbose_name="图片地址")
    path = models.CharField(default="", max_length=255, verbose_name="跳转地址")
    sort = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '首页Banner'
        verbose_name_plural = verbose_name


class UserLesson(models.Model):
    type = models.ForeignKey("LessonType", on_delete=models.DO_NOTHING, verbose_name="课程类型", default="",
                             blank=True, db_constraint=False, )
    userid = models.CharField(max_length=255, verbose_name="用户id")
    lessonid = models.CharField(max_length=255, verbose_name="课程id")
    title = models.CharField(max_length=255, verbose_name="标题")
    img = SImageField(upload_to="UserLesson_img", max_length=255, verbose_name="图片")
    percent = models.IntegerField(default=0, verbose_name="百分比")
    isFollow = models.BooleanField(verbose_name="是否follow")
    exp = models.IntegerField(default=0, verbose_name="经验")
    hours = models.IntegerField(default=0, verbose_name="小时")
    notes = models.IntegerField(default=0, verbose_name="笔记数量")
    codes = models.IntegerField(default=0, verbose_name="代码片段数量")
    questions = models.IntegerField(default=0, verbose_name="问题数量")
    lastChapter = models.CharField(max_length=255, default="", verbose_name="最后一章节")

    class Meta:
        verbose_name = '用户学习的课程'
        verbose_name_plural = verbose_name


class Nav(models.Model):
    title = models.CharField(max_length=255, verbose_name="名称")
    path = models.CharField(max_length=255, default="/", verbose_name="访问路径")
    icon = models.ImageField(max_length=255, verbose_name="图标")

    class Meta:
        verbose_name = '首页左侧菜单'
        verbose_name_plural = verbose_name


class LabelType(models.Model):
    title = models.CharField(max_length=255, verbose_name="名称")
    code = models.IntegerField(default=0, verbose_name="code")
    sort = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = 'Label类型'
        verbose_name_plural = verbose_name


class LessonType(models.Model):
    code = models.CharField(max_length=255, unique=True, verbose_name="课程类型")
    text = models.CharField(max_length=255, verbose_name="课程类型code")

    class Meta:
        verbose_name = '课程类型'
        verbose_name_plural = verbose_name


class LessonHardType(models.Model):
    code = models.CharField(max_length=255, unique=True, verbose_name="课程难度code")
    text = models.CharField(max_length=255, verbose_name="课程难度")

    class Meta:
        verbose_name = '课程难度类型'
        verbose_name_plural = verbose_name


class Label(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    sort = models.IntegerField(default=0, verbose_name="排序")
    type = models.ForeignKey(LabelType, on_delete=models.DO_NOTHING, verbose_name="Label类型", default="",
                             blank=True, db_constraint=False)

    class Meta:
        verbose_name = 'Label小项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Footer(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    url = models.CharField(max_length=255, verbose_name="url")
    sort = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = '底部配置'
        verbose_name_plural = verbose_name


class CommonPathConfig(models.Model):
    title = models.CharField(max_length=255, verbose_name="名称")
    path = models.CharField(max_length=255, verbose_name="访问路径")
    icon = models.CharField(max_length=500, verbose_name="访问路径")
    type = models.CharField(max_length=500, verbose_name="类型")  # h-header # f-footer

    class Meta:
        verbose_name = '公共头部脚部配置'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name="所属Lesson", default="",
                               blank=True, db_constraint=False)
    title = models.CharField(max_length=255, verbose_name="章节标题")
    introduce = models.CharField(default="", max_length=800, verbose_name="章节介绍")

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Term(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING, verbose_name="所属章节", default="",
                                blank=True, db_constraint=False, related_name="term")
    seconds = models.IntegerField(verbose_name="时长")
    title = models.CharField(default="", max_length=255, verbose_name="小节标题")
    path = models.CharField(max_length=255, verbose_name="访问链接")

    class Meta:
        verbose_name = '小节'
        verbose_name_plural = verbose_name


class SysLog(models.Model):
    action_time = models.DateTimeField(verbose_name="动作时间", default=datetime.now)
    ip_addr = models.CharField(max_length=39, blank=True, null=True, verbose_name="操作ip")
    action_flag = models.CharField(blank=True, null=True, max_length=32, verbose_name="操作flag")
    message = models.TextField(verbose_name="日志记录")
    log_type = models.CharField(default="", max_length=200, verbose_name="日志类型")
    user_name = models.CharField(max_length=200, default="1", verbose_name="用户")

    class Meta:
        verbose_name = "系统日志"
        verbose_name_plural = verbose_name
        ordering = ('-action_time',)


class Album(models.Model):
    ALBUM_CHOICES = (
        ("UNUSE", "待审核"),
        ("COMM", "正常"),
        ("OVER", "结束"),
        ("PEDDING", "停用"),
        ("DEL", "删除"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    userid = models.CharField(max_length=255, verbose_name="用户id")
    title = models.CharField(max_length=255, verbose_name="标题", unique=True)
    content = models.CharField(max_length=255, verbose_name="内容")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="描述")
    status = models.CharField(max_length=255, choices=ALBUM_CHOICES, verbose_name="状态")
    type = models.CharField(max_length=255, default="其他", verbose_name="类型") # 同学时光,校园追忆,校友今夕,活动聚会,个人风采,其他
    order = models.IntegerField(default=9999, verbose_name="排序")

    viewcnt = models.IntegerField(default=0, verbose_name="访问次数")
    favcnt = models.IntegerField(default=0, verbose_name="收藏人数")
    commentcnt = models.IntegerField(default=0, verbose_name="评论数")
    likecnt = models.IntegerField(default=0, verbose_name="点赞数")

    pic = SImageField(upload_to="Album_img", max_length=255, verbose_name="附加图片")

    addtime = models.DateTimeField(auto_now=True, verbose_name="添加时间")
    edittime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    addip = models.CharField(max_length=255, blank=True, null=True, verbose_name="添加IP")
    editip = models.CharField(max_length=255, blank=True, null=True, verbose_name="修改IP")

    class Meta:
        verbose_name = '校友录'
        verbose_name_plural = verbose_name


class Info(models.Model):
    ALBUM_CHOICES = (
        ("UNUSE", "待审核"),
        ("COMM", "正常"),
        ("OVER", "结束"),
        ("PEDDING", "停用"),
        ("DEL", "删除"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    userid = models.CharField(max_length=255, verbose_name="用户id")
    title = models.CharField(max_length=255, verbose_name="标题")
    content = models.CharField(max_length=255, verbose_name="内容")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="描述")
    status = models.CharField(max_length=255, choices=ALBUM_CHOICES, verbose_name="状态")
    type = models.CharField(max_length=255, default="其他", verbose_name="类型") # 资源合作,活动聚会,创业合作,招聘猎头,求职,企业推介,供应采购,商务合作,服务咨询,其他'
    order = models.IntegerField(default=9999, verbose_name="排序")

    viewcnt = models.IntegerField(default=0, verbose_name="访问次数")
    favcnt = models.IntegerField(default=0, verbose_name="收藏人数")
    commentcnt = models.IntegerField(default=0, verbose_name="评论数")
    likecnt = models.IntegerField(default=0, verbose_name="点赞数")

    exptime = models.IntegerField(default=0, verbose_name="过期时间") # 0=永不过期

    province = models.CharField(max_length=255, blank=True, null=True, verbose_name="区域(省)")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="区域(市)")
    county = models.CharField(max_length=255, blank=True, null=True, verbose_name="区域(区)")

    pic = SImageField(upload_to="Album_info", max_length=255, verbose_name="附加图片")

    addtime = models.DateTimeField(auto_now=True, verbose_name="添加时间")
    edittime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    addip = models.CharField(max_length=255, blank=True, null=True, verbose_name="添加IP")
    editip = models.CharField(max_length=255, blank=True, null=True, verbose_name="修改IP")

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name


class Setup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="网站名称")
    content = models.CharField(max_length=255, blank=True, null=True, verbose_name="关于我们")

    logo = SImageField(upload_to="Album_about", max_length=255, verbose_name="网站底图")
    adpic = SImageField(upload_to="Album_about", max_length=255, verbose_name="海报底图")
    
    regcheck = models.IntegerField(default=0, verbose_name="注册是否审核")

    addtime = models.IntegerField(default=0, verbose_name="添加时间")
    edittime = models.IntegerField(default=0, verbose_name="修改时间")
    addip = models.CharField(max_length=255, blank=True, null=True, verbose_name="添加IP")
    editip = models.CharField(max_length=255, blank=True, null=True, verbose_name="修改IP")

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name


class WXUser(models.Model):
    ALBUM_CHOICES = (
        ("UNUSE", "待审核"),
        ("COMM", "正常"),
        ("OVER", "结束"),
        ("PEDDING", "停用"),
        ("DEL", "删除"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    USER_ID = models.CharField(max_length=255, verbose_name="用户id")
    USER_NAME = models.CharField(max_length=255, verbose_name="用户姓名")
    USER_PIC = SImageField(upload_to="Album_head", max_length=255, verbose_name="用户头像")
    USER_PIC_CLOUD_ID = models.CharField(max_length=1024, verbose_name="用户头像云存储地址")

    USER_PHONE_CHECKED = models.CharField(max_length=255, verbose_name="已校验的手机号码")
    USER_MINI_QRCODE = models.CharField(max_length=255, verbose_name="小程序码地址")

    USER_MINI_OPENID = models.CharField(max_length=255, verbose_name="小程序openid")
    USER_UNIONID = models.CharField(max_length=255, verbose_name="微信开放平台unionid")

    USER_WX_OPENID = models.CharField(max_length=255, verbose_name="公众号openid")
    USER_IS_SUBSCRIBE = models.IntegerField(default=0, verbose_name="公众号是否关注")
    USER_SUBSCRIBE_TIME = models.IntegerField(default=0, verbose_name="公众号关注时间")
    
    USER_STATUS = models.CharField(max_length=255, choices=ALBUM_CHOICES, verbose_name="状态")
    USER_INVITE_ID = models.CharField(max_length=255, blank=True, null=True, verbose_name="邀请码")

    USER_ITEM = models.CharField(max_length=255, verbose_name="班级")
    USER_SEX = models.IntegerField(default=1, verbose_name="性别") # 1=男,2=女
    USER_BIRTH = models.IntegerField(default=0, verbose_name="出生年月")
    USER_NATIVE = models.CharField(max_length=255, blank=True, null=True, verbose_name="籍贯")

    USER_OPEN_SET = models.IntegerField(default=1, verbose_name="资料公开方式") # 1=所有用户,8=vip, 3=好友'

    USER_MOBILE = models.CharField(max_length=255, blank=True, null=True, verbose_name="联系电话")
    USER_WECHAT = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信")
    USER_QQ = models.CharField(max_length=255, blank=True, null=True, verbose_name="QQ")
    USER_EMAIL = models.CharField(max_length=255, blank=True, null=True, verbose_name="邮箱")

    USER_ENROLL = models.IntegerField(default=1, blank=True, null=True, verbose_name="入学年份")
    USER_GRAD = models.IntegerField(default=1, blank=True, null=True, verbose_name="毕业年份") 
    USER_EDU = models.CharField(max_length=255, blank=True, null=True, verbose_name="学历") # 中学,高职,大专,本科,硕士,博士,博士后,其他


    # title = models.CharField(max_length=255, verbose_name="标题", unique=True)
    # content = models.CharField(max_length=255, verbose_name="内容")
    # desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="描述")
    
    # type = models.CharField(max_length=255, default="其他", verbose_name="类型") # 资源合作,活动聚会,创业合作,招聘猎头,求职,企业推介,供应采购,商务合作,服务咨询,其他'
    # order = models.IntegerField(default=9999, verbose_name="排序")

    USER_COMPANY = models.CharField(max_length=255, blank=True, null=True, verbose_name="当前单位")
    USER_COMPANY_DEF = models.CharField(max_length=255, blank=True, null=True, verbose_name="当前单位性质") # 保留,机关部门,事业单位,国企,世界500强,外企,上市企业,民营企业,自有企业,个体经营,自由职业,其他
    USER_COMPANY_DUTY = models.CharField(max_length=255, blank=True, null=True, verbose_name="当前职位")
    USER_TRADE = models.CharField(max_length=255, blank=True, null=True, verbose_name="当前行业")
    USER_CITY = models.CharField(max_length=255, blank=True, null=True, verbose_name="当前城市")
    USER_WORK_STATUS = models.CharField(max_length=255, blank=True, null=True, verbose_name="工作状态")


    USER_DESC = models.CharField(max_length=255, blank=True, null=True, verbose_name="自我介绍")
    USER_RESOURCE = models.CharField(max_length=255, blank=True, null=True, verbose_name="可提供资源&需求")

    USER_FAV_CNT = models.IntegerField(default=0, verbose_name="被收藏人数")
    USER_INVITE_CNT = models.IntegerField(default=0, verbose_name="邀请人数")
    USER_VIEW_CNT = models.IntegerField(default=0, verbose_name="被查看次数")
    USER_ALBUM_CNT = models.IntegerField(default=0, verbose_name="发相册数量")
    USER_INFO_CNT = models.IntegerField(default=0, verbose_name="发互助数量")
    USER_MEET_CNT = models.IntegerField(default=0, verbose_name="发起活动次数")
    USER_MEET_JOIN_CNT = models.IntegerField(default=0, verbose_name="活动报名次数")

    USER_WX_GENDER = models.IntegerField(default=1, verbose_name="微信性别") # 0=未定义,1=男,2=女
    USER_WX_AVATAR_URL = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信头像链接")
    USER_WX_NICKNAME = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信昵称")
    USER_WX_LANGUAGE = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信语言")
    USER_WX_CITY = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信城市")
    USER_WX_PROVINCE = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信省份")
    USER_WX_COUNTRY = models.CharField(max_length=255, blank=True, null=True, verbose_name="微信国家")
    USER_WX_UPDATE_TIME = models.IntegerField(default=0, verbose_name="微信信息更新时间")

    USER_ACTIVE = models.CharField(max_length=255, blank=True, null=True, verbose_name="用户动态")
    
    USER_LOGIN_CNT = models.IntegerField(default=0, verbose_name="登录次数")
    USER_LOGIN_TIME = models.IntegerField(default=0, blank=True, null=True, verbose_name="登录时间")

    USER_ADD_TIME = models.IntegerField(default=0, verbose_name="添加时间")
    USER_ADD_IP = models.CharField(max_length=255, blank=True, null=True, verbose_name="添加IP")
    USER_EDIT_TIME = models.IntegerField(default=0, verbose_name="修改时间")
    USER_EDIT_IP = models.CharField(max_length=255, blank=True, null=True, verbose_name="修改IP")

    class Meta:
        verbose_name = '小程序用户'
        verbose_name_plural = verbose_name


class WXAdmin(models.Model):
    ADMIN_ID = models.CharField(max_length=255, verbose_name="用户id")
    ADMIN_NAME = models.CharField(max_length=255, verbose_name="姓名")

    ADMIN_PHONE = models.CharField(max_length=255, verbose_name="电话")
    ADMIN_STATUS = models.IntegerField(default=0, verbose_name="状态") # 0=禁用 1=启用

    ADMIN_LOGIN_CNT = models.IntegerField(default=0, verbose_name="登录次数")
    ADMIN_LOGIN_TIME = models.IntegerField(default=0, verbose_name="登录时间")

    ADMIN_TYPE = models.IntegerField(default=1, verbose_name="类型")

    ADMIN_TOKEN = models.CharField(max_length=255, verbose_name="token")
    ADMIN_TOKEN_TIME = models.CharField(max_length=255, verbose_name="token时间")

    ADMIN_ADD_TIME = models.IntegerField(default=0, verbose_name="添加时间")
    ADMIN_ADD_IP = models.CharField(max_length=255, blank=True, null=True, verbose_name="添加IP")
    ADMIN_EDIT_TIME = models.IntegerField(default=0, verbose_name="修改时间")
    ADMIN_EDIT_IP = models.CharField(max_length=255, blank=True, null=True, verbose_name="修改IP")

    class Meta:
        verbose_name = '小程序管理员'
        verbose_name_plural = verbose_name
