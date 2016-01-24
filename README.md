# 图书管理系统说明V2.0


### 项目介绍及再版说明（2016-01-24）

 其实一开始做这个小项目在2014年的9到11月，当时是作为加入Pureweber开发组的大作业完成的。虽然用了两个月的时间，但是做出的东西还是有很多的缺陷。前些日子在整理GitHub时又想起来了这个项目，记得曾经还在Django中国社区里安利初学者来读代码什么的。但是想想里面还有很多不规范的代码和一些很糟糕的写法就感觉很蛋疼。本来想直接删除了好了，但是后来想想，何不花点时间把这个小项目重构一下，就可以给以后学习Django的同学一个完整的项目参考，就可以代替了一般培训课程或者老师上课PPT里那种陈旧或者不完整的例子。
于是一共花费了大约两天时间对项目进行了重构，主要做了以下方面的工作：

* 将Django的版本更新到了最新的1.9.1。

* 修改了原先项目中不规范的格式、变量名等。

* 更改了项目的目录结构，换成了Django官方推荐的目录结构模式。

* 将原来缺失的文件上传保存部分补充完整了。

* 更改了用户部分的代码，将原来手动设置session的方式去掉了，替换为Django用户模块默认的登录态保存方式.

* 修复了注册用户时用户提交空密码可能造成的安全漏洞。

* 做了对python3的支持。改动不多。


### 项目所涉及的和Django相关的功能

项目的目的是为了给Django的初学者一个完整项目的参考案例，所以尽可能多的选择了初学者常用的方法处理一些问题，比如在视图的处理上选择了视图处理函数，而不是更好用的视图处理类。在参数传递上只使用了标准的POST和GET的方式传参，而没有使用url地址中提取参数的办法。该项目中主要涉及到的Django框架相关的内容有：

* Models模型字段用法，外键关系用法。 [文档](https://docs.djangoproject.com/en/1.9/topics/db/models/)

* 使用ORM进行数据库查询。 [文档](https://docs.djangoproject.com/en/1.9/topics/db/queries/)

* Urls配置文件的写法，Urls命名与反向查询。 [文档](https://docs.djangoproject.com/en/1.9/topics/http/urls/)

* Views视图处理函数。 [文档](https://docs.djangoproject.com/en/1.9/topics/http/views/)

* Templates模板。 [文档](https://docs.djangoproject.com/en/1.9/ref/templates/language/)

* 在admin站点中注册模型。 [文档](https://docs.djangoproject.com/en/1.9/ref/contrib/admin/)

* Django自带用户模块的注册和登录。 [文档](https://docs.djangoproject.com/en/1.9/topics/auth/default/)

* 对Django自带的用户模块进行拓展。 [文档](https://docs.djangoproject.com/en/1.9/topics/auth/customizing/)

* 静态文件处理。 [文档](https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/)

* 还有一大堆其他的……


### 系统说明

* 本系统使用Python的Django框架搭建。
* 前端部分使用bootstrap。


### 运行说明

* 请参考Django官方文档[下载](https://www.djangoproject.com/download/)Django<del>1.71</del>1.9.1版。
* 请按照Django官方文档[安装](https://docs.djangoproject.com/en/1.9/intro/install/)Django。
* 如果是水果电脑。。。请额外安装[PIL](http://www.pythonware.com/products/pil/)库。
* 通过终端进入项目文件夹。
* 在终端中执行`python manage.py runserver`命令即可运行本地开发服务器。
* 在浏览器里访问`http://127.0.0.1:8000`即可查看该网站。


### 功能实现

* 实现了用户权限相关的基本操作（注册、登陆、修改密码、注销）
* 实现了用户分级（普通用户与管理员用户）
* 管理员账号：yumendy 密码：admin。
* 管理员可以添加图书<del>（图书的图片上传实在没时间写了喵T^T）</del>
* 管理员可以添加图书图片
* 任何用户都可以查看、检索图书
* 图书分类列表随添加的图书而改变。
* 检索支持对图书名的模糊检索。
* 图书分页为每页5个。
* 搜索框自动提交的时间为距离上次按键抬起1.5秒。


### 联系我

差点忘了联系方式， 欢迎大家与我一起探讨Django相关的知识：

> 段艺：

> 电话:13351015622

> QQ:306359430

> 邮箱: yumendy@163.com

> 主页: http://yumendy.com

> GitHub: https://github.com/yumendy
