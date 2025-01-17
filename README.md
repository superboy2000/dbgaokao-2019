# 数据库课程设计：高考帮——你的高考录取分数速查助手
### 项目简介：
* 本项目拟结合数据库与前端界面的编写实现数据库中内容的查询，与偏好列表的添加删除等操作。
* 通过Python爬取2018年真实的高考分数及录取信息，获得2018年内蒙古高考的详细录取信息等详细数据。
* 同时，相比较于官方公布数据，官方出于防止宣传目的对于排名信息进行了隐藏（排名前100的考生不显示具体名次），本项目根据全部考生信息，进行了再次的排序比较，从而可以详细的查询到每名考生，每个分数的位次
* 考生可根据个人需求，对2018年高考的录取信息进行快速查询。
### 项目内容：
* 使用MySQL、Python、PyQt5 实现数据库与前端界面相配合的数据展示及偏好收藏系统
* [PyQt5连接MySQL](https://blog.csdn.net/jeekmary/article/details/79677285)
* [Python GUI教程：在PyQt5中使用数据库](https://www.codercto.com/a/19041.html)
* 参考项目：[简易人事管理系统](https://blog.csdn.net/weixin_40448659/article/details/82735230)
### 项目分工：
* MySQL数据库设计
* 使用BeautifulSoup4及requests爬虫收集真实高考数据[爬虫收集数据](https://blog.csdn.net/wearge/article/details/79995688)
* GUI界面实现
* 账户注册登录实现
* 加入我的喜好功能：可以将偏好的院校信息加入喜好页面，实现偏好院校速查
* 添加功能……
### 技术细节：
#### MySQL数据库设计
<img src=figure\AccountER图.jpg width = "40%" alt="Accoun E-R图" align=right>
<!-- 插入图片的方法，src中保存图片链接（相对路径或网站链接） -->

* 账户信息记录表：
主要分为：账号密码(Account)、邀请码(InviteList)和个人喜好(favourite)。账户信息设计为邀请注册机制，即输入邀请码，即可完成详细E-R图**如右图**。<br>
    * InvitedList与Account为**一对多关系**，旨在实现通过一个邀请码可以注册所个账号。在邀请码表中，**key作为主键**存储邀请码，而其后的number记录邀请码的剩余使用次数，在注册时将其与剩余注册次数比对，如若未找到对应邀请码或剩余次数为0，则无法进行注册。
    * favourite表与Account相关联，并**以Account中的username与其自身的college_id作为共同主键**，favourite与Account为**多对一关系**，旨在能够实现一个用户可以收藏多个院校功能。
    favourite表中记录了每个用户的收藏院校名录，从这可以查询到每个用户的收藏院校。
    * Account表中保存用户名和密码，其中**以用户名为主键**，用户登录时需要比对用户名与其密码相对应，才可以登录。<br><br>
<img src=figure\院校信息ER图.jpg width = "45%" alt="Accoun E-R图" align=right>
* 院校信息表：包括考生信息表(Candidate)、专业信息表(zhuanye)和院校信息表(college)表中保留了全部院校、专业及考生的信息，其E-R图如右图
    * 院校信息表(college)：院校信息表主要保存了院校的编号和院校名称，并**以院校编号(idcollege)为主键**(用于区分有存在同一院校分多个编号招生的情况)
    * 专业信息表(zhuanye)：以**院校的编号(idcollege)为外键**，专业信息与院校信息为**多对一关系**，即同一院校可以有多个专业。在专业信息表中，以**院校编号(college_id)、专业编号(ID)和科类（文科或理科）(type)共同作为主键**，存在同一专业同时招文科理科考生情况，所以将科类加入主键，防止专业信息出现冲突情况。
    * 考生信息表(Candidate)：考生信息表记录了考生的全部信息，包括：*考生编号(idCandidate)、考生姓名(Candidate_name)、性别(gender)、民族(minzu)、录取状态(status)、录取院校编号(CollegeID)、院校名称(CollegeName)、总分(zf1)、加分条件(addScore)、特征总分（含加分）(tot_score)、录取批次(AdmissionLevel)、录取专业编号(zhuanye_ID)、录取类型(AdmitType)、录取时间(AdmitTime)、语文(Chinese)、数学(Math)、文科综合(CLiberal)、理科综合(CScience)、外语(ForeignLanguage)、外语听力(FLListen)、外语口语(FLSpeaking)、考生类型(type)* 条目组成。其中，以**考生编号(idCandidate)作为唯一主键**。其中，院校编号(CollegeID)、专业编号(zhuanye_ID)和考生类型(type)均为zhuanye表中外键。
    * 由于考生信息包含属性较多，且对于复杂属性，如总分，考生与其为**一对一**关系，所以将复杂属性一并保存入考生表中，未对其进行关系模式的拆分，无需拆分为多个表来保存。<br><br>
<img src=figure\排名表ER图.jpg width = "40%" alt="Accoun E-R图" align=right>
* 排名表：包括文科排名表(rankArt)和理科排名表(rankSci)。
    * 文科排名表与理科排名表均以**分数为主键**，设置排名表主要目的为在进行显示时减少查询需要消耗的复杂度，转而保存为固定数据，无需计算，仅需查找。
    * 其中排名表的数据综合计算插入和官方数据结合，通过计算的参数和官方数据进行组合，生成最终的排名表内容
#### 数据获取
* 数据以2018年内蒙古普通高等学校招生全国统一考试录取信息为主要数据基础，通过Python爬虫(requests、BeautifulSoup4)从网页爬取录取数据，转而存入MySQL数据库进行分类储存，以供查询。
* 院校信息来源：[内蒙古招生考试信息网](https://www.nm.zsks.cn/ptgxzs/xxcx/)
* 排名信息来源：[2018年内蒙古高考成绩排名一分一段（文科/理科）](http://www.gaokw.com/gaokao/neimenggu/188786.html)

### 使用说明：
