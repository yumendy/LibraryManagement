# 图书管理系统说明

### 系统说明

* 本系统使用Python的Django框架搭建。
* 前端部分使用bootstrap。

### 运行说明

* 请参考Django官方文档[下载](https://www.djangoproject.com/download/)Django1.71版。
* 请按照Django官方文档[安装](https://docs.djangoproject.com/en/1.7/intro/install/)Django。
* 如果是水果电脑。。。请额外安装[PIL](http://www.pythonware.com/products/pil/)库。
* 通过终端进入项目文件夹。
* 在终端中执行`python manage.py runserver`命令即可运行本地开发服务器。
* 在浏览器里访问`http://127.0.0.1:8000`即可查看该网站。

### 功能实现

* 实现了用户权限相关的基本操作（注册、登陆、修改密码、注销）
* 实现了用户分级（普通用户与管理员用户）
* 管理员账号：yumendy 密码：admin。
* 管理员可以添加图书（图书的图片上传实在没时间写了喵T^T）
* 任何用户都可以查看、检索图书
* 图书分类列表随添加的图书而改变。
* 检索支持对图书名的模糊检索。
* 图书分页为每页5个。
* 搜索框自动提交的时间为距离上次按键抬起1.5秒。

### 遇到的问题以及解决办法

* django的分页插件不会用>_<
    * 果断的跑去官方文档查了。。。。
* js表单的延迟提交有点问题。。。
    * Google一下马上搞定~

### 截图神马的都在文件夹里啦~

##### 数据结构的作业还没写完~滚去写作业了~~

差点忘了联系方式：

> 段艺：

> 6089寝室

> 电话:13351015622

> QQ:306359430

> 邮箱: yumendy@163.com

> 主页: http://yumendy.com

> GitHub: https://github.com/yumendy