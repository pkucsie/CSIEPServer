# Django3.1 + DjangoRestful Framework + Ant Design Pro V4 大学生创新创业大赛平台

[![Build Status](https://travis-ci.org/mtianyan/hexoBlog-Github.svg?branch=master)](https://travis-ci.org/mtianyan/hexoBlog-Github)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

使用TyAdmin(现代化的Xadmin替代品)生成管理后台前后端，并自动对接。✨ 强烈推荐使用:

>https://github.com/mtianyan/tyadmin_api_cli

📨 互动交流微信: 1

- 前台体验地址:
- 在线体验地址:


主页参考：
https://events.pedaily.cn/customized/923/

>账号: pkucsie
密码: 123456

# 前后台效果展示

![](http://cdn.pic.mtianyan.cn/blog_img/20201204233749.png)

![](http://cdn.pic.mtianyan.cn/blog_img/20201204233849.png)

>https://github.com/mtianyan/tyadmin_api_cli


Vue前台代码地址: https://github.com/mtianyan/vue-mooc
Vue前台代码原作者及文档: https://github.com/wangtunan/vue-mooc

## 运行指南:

### docker运行

```
git clone https://github.com/pkucsie/CSIEPServer.git
cd CSIEPServer
docker-compose up

# 导入数据
docker exec -it onlinemooc_mtianyan_mysql_1 bash
mysql -u root -p -D online_mooc < sql/online_mooc.sql
# 输入密码: mtianyanroot
```

### 本地环境运行

后端项目运行:

```
git clone https://github.com/pkucsie/CSIEPServer.git
cd CSIEPServer
pipenv shell
pip install -r requirements.txt

# Navicat创建数据库，导入mxonline3.sql
# 修改settings.py 中数据库密码

python manage.py runserver
```

## 配置指南:

### Django运行

目前数据库调整为sqlite，方便大家使用

运行python manage.py runserver 0.0.0.0:8011

ORM使用
生成sql脚本python manage.py makemigrations
同步sql脚本python manage.py migrate

### 后台管理页面

#### [已经安装不需要配置]安装tyadmin-api-cli并注册tyadmin-api-cli

```diff
pip install tyadmin-api-cli

INSTALLED_APPS = [
+    'captcha',
+    'tyadmin_api_cli',
]

+TY_ADMIN_CONFIG = {
+    'GEN_APPS': ['demo']
+}

# 方便拷贝

    'captcha',
    'tyadmin_api_cli',

TY_ADMIN_CONFIG = {
    'GEN_APPS': ['demo']
}
```

GEN_APPS: 填写你想要生成的app列表。

#### 初始化 后端app(tyadmin_api) + 前端项目(tyadmin)  && 生成后端自动化的视图，过滤器，路由，序列器 + 前端页面及路由菜单

生成后端页面依赖，需安装Node.js -> https://www.runoob.com/nodejs/nodejs-install-setup.html

>安装Node.js 10以上，推荐安装版本Latest LTS Version: 12.19.0

```
python manage.py init_admin && python manage.py gen_all && cd tyadmin && npm install && npm run build
```

>耐心等待一会，build 会输出 前端页面到templates文件夹，生成前端js,css 等到static文件夹

#### 当项目新增了model，我该如何为新model生成前端页面+后端接口

```diff
+TY_ADMIN_CONFIG = {
+    'GEN_APPS': ['demo','new_app']
+}
```
如上GEN_APPS 中添加新app的name，然后运行下面命令

```
python manage.py gen_all && cd tyadmin && npm run build
```

#### 如何运行生成的前端独立项目

```
cd tyadmin
npm install
npm run start:dev # 默认会运行在8001端口
```

请确认django运行在8000端口，访问 http://127.0.0.1:8001/xadmin/

## 各部分位置说明

### 页面路由文件

app_api/urls.py

### 数据库表文件

app_api/models.py

### 页面视图文件

app_api/views.py

### 页面字段序列号

app_api/serializers.py

### 管理后台页面js文件

templates目录

# 主页面接口

1、banner http://127.0.0.1:8000/api/v1/home/slider
2、时间线 http://127.0.0.1:8000/api/v1/home/timeline
3、赛事嘉宾 http://127.0.0.1:8000/api/v1/home/vipguest
4、组织机构 http://127.0.0.1:8000/api/v1/home/org
5、footer http://127.0.0.1:8000/api/v1/footer


# 附录

## model->前端对应关系

|  字段类型   | 前端展示  |
|  ----  | ----  |
| ForeignKey  | 单选 |
| ManyToManyField  | 多选 & 多彩标签展示 |
| richTextField  | 富文本展示 |
| CharField or IntegerField(with choices)  | 多选 |
| CharField or IntegerField  | 输入框 |
| ImageField  | 带预览上传，可选头像，图片列表展示 |
| FileField  | 文件上传 |
| TextField  | TextArea框 |
| BooleanField | Switch选择|
| IntegerField | 数字input|
| DateField| Date选择器|
| DateTimeField| DateTime选择器|

### ForeignKey自动生成下拉单选菜单, ManyToManyField自动生成下拉多选菜单或穿梭框

![](http://cdn.pic.mtianyan.cn/blog_img/20201202214922.png)

![](http://cdn.pic.mtianyan.cn/blog_img/20201202214936.png)

![](http://cdn.pic.mtianyan.cn/blog_img/20201202214957.png)

### richTextField 自动生成富文本

```
detail = richTextField(verbose_name="课程详情")
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010193352.png)

### CharField和IntegerField choices 自动生成表单前端下拉选择框。

```python
GENDER_CHOICES = (
   ("male", "男"),
   ("female", "女")
)
gender = CharField(verbose_name="性别",choices=GENDER_CHOICES)
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010190635.png)

### ImageField 自动生成带预览的表单上传功能，列表页可选两种展示方式。

```python
avatar = ImageField(verbose_name="头像") # 变量名为avatar或logo的会自动为头像样式
image = ImageField(verbose_name="封面图")    
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010191641.png)

![](http://cdn.pic.mtianyan.cn/blog_img/20201010191917.png)

![](http://cdn.pic.mtianyan.cn/blog_img/20201010191843.png)

### FileField 字段生成文件上传功能。

```
download = FileField(verbose_name="资源文件")
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010193041.png)

### TextField 自动生成前端TextArea 框

```python
desc = TextField(verbose_name="课程描述")
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010192813.png)

### BooleanField 自动前端 Boolean 单选

```python
is_banner = BooleanField(verbose_name="是否轮播")
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010193001.png)

### IntegerField 自动前端 Int 输入框
```
learn_times = IntegerField(verbose_name="学习时长(分钟数)")
```
![](http://cdn.pic.mtianyan.cn/blog_img/20201010193445.png)

### DateField 自动前端 Date选择框

```
birthday = DateField(verbose_name="生日")
```
![](http://cdn.pic.mtianyan.cn/blog_img/20201010193614.png)

### DateTimeField 自动表单 DateTime 选择框，时间范围筛选器。

```
last_login = DateTimeField(verbose_name="上次登录")
```

![](http://cdn.pic.mtianyan.cn/blog_img/20201010193852.png)

>注意设置了default，auto_now的不会出现在表单

![](http://cdn.pic.mtianyan.cn/blog_img/20201010195116.png)
