-- Day03回顾
-- 1、SQL查询
--   1、聚合函数
--     avg(...) sum(...) max(...) min(...)
--     count(字段名) ## 空值NULL不会被统计
--   2、group by ：对查询结果进行分组
--     先分组再聚合
--     如果select后的字段名和group by后字段不一致,则必须对该字段进行聚合处理
--   3、having语句 ：对查询结果进行进一步筛选
--     where只能操作表中实际存在的字段(desc 表名;)
--   4、distinct ：不显示字段的重复值
--     select distinct 字段1,字段2 from 表名;
--   5、查询时做数学运算
--     select 字段1+100 as n1,字段2*50 as n2 from 表名
-- 2、嵌套查询(子查询)
--   把内层的查询结果作为外层的查询条件
-- 3、多表查询
--   1、笛卡尔积 ：不加where条件
--   2、多表查询 ：加where条件,只显示匹配到的
-- 4、连接查询
--   1、内连接 ：只显示匹配到的记录
--   2、外连接
--     1、左连接 ：以左表为主显示查询结果
--     2、右连接 ：以右表为主显示查询结果
--   3、select 表名.字段名 from 表1
--      inner/left/right join 表2 on 条件
--      inner/left/right join 表3 on 条件;
-- 5、约束
--   1、非空约束 ：NOT NULL
--   2、默认约束 ：DEFAULT 值
--     ## name varchar(20) NOT NULL DEFAULT "匿名"
-- 6、索引(BTree)
--   1、优点 ：加快数据的查询速度
--   2、缺点 
--     1、占用物理存储空间
--     2、索引需动态维护,占用系统资源
--   3、SQL命令运行时间监测
--       show variables like "%pro%";
--     1、开启 ：mysql> set profiling=1;
--     2、查看 ：mysql> show profiles;
--     3、关闭 ：mysql> set profiling=0;
-- 7、普通(MUL)、唯一(UNI,字段值不重复,但可为NULL)
--   1、创建表时创建 
--     create table 表名(
--     id int,
--     name varchar(20),
--     phnum bigint,
--     index(name),
--     unique(phnum)
--     )charset=utf8;
--   2、已有表中创建
--     create index 索引名 on 表名(字段名);
--     create unique index 索引名 on 表名(字段名);
--   3、查看
--     desc 表名;  --> KEY标志
--     show index from 表名\G;
--   4、删除
--     drop index 索引名 on 表名;
-- **********************************
-- Day04笔记
-- 1、主键(primary key)&&自增长属性(auto_increment)
--   1、使用规则
--     1、一张表中只能有1个主键字段
--     2、约束 ：字段值不允许重复,且不能为NULL
--     3、KEY标志 ：PRI
--     4、通常设置记录编号的字段id为主键,能够唯一锁定1条记录
--   2、创建表时创建,并指定自增长起始值
--     create table 表名(
--       id int primary key auto_increment,
--       name varchar(20)
--     )auto_increment=10000,charset=utf8;
--     ## 已有表中重新指定起始值
--       alter table 表名 auto_increment=20000;
--   3、已有表中添加主键
--     alter table 表名 add primary key(id);
--   4、删除
--     1、删除自增长属性(modify)
--       alter table 表名 modify id int;
--     2、删除主键
--       alter table 表名 drop primary key;
-- 2、外键(foreign key)
--   1、定义 ：让当前表字段值在另一个表的范围内选择
--   2、语法
--     foreign key(从表字段名)
--     references 主表(主表字段名)
--     on delete 级联动作
--     on update 级联动作
--   3、使用规则
--     1、主表、从表字段数据类型要一致
--     2、主表被参考字段 ：主键
--   4、表1：缴费信息表(财务)
--        id  姓名    班级   缴费金额
--         1  唐伯虎  AID10    300
-- 	2  点秋香  AID10    300
-- 	create table jftab(
-- 	id int primary key,
-- 	name varchar(20),
-- 	class char(5),
-- 	money int);

-- 	insert into jftab values
-- 	(1,"唐伯虎","AID10",300),
-- 	(2,"点秋香","AID10",300),
-- 	(3,"文征明","AID10",300);

--      表2：学生信息表(班主任)
--        stuid  姓名    缴费金额
--          1    唐伯虎    300
-- 	 3    祝枝山    300
-- 	create table bjtab(
-- 	stuid int,
-- 	name varchar(20),
-- 	money int,
-- 	foreign key(stuid) references jftab(id)
-- 	on delete cascade
-- 	on update cascade
-- 	);
--   5、级联动作
--     1、cascade ：数据级联删除、更新(参考字段)
--     2、set null：主表更新、删除时,从表相关联记录该字段值设置为NULL
--     3、restrict：从表有相关联记录,不允许主表操作
--   6、删除外键
--     show create table 表名;
--     alter table 表名 drop foreign key 外键名;
--   7、在已有表中添加外键
--     alter table 从表 add foreign key(stuid) references 主表(id)
--     on delete 级联动作
--     on update 级联动作
-- 3、锁 ：目的是解决客户端并发访问的冲突问题
--   1、锁类型分类
--     1、读锁(共享锁)
--       select：加读锁后别人不能更改表记录,但可查询
--     2、写锁(互斥锁、排他锁)
--       update：加写锁后别人不能查询,不能改
--   2、锁粒度
--     1、行级锁 ：Innodb
--       可以加读锁、写锁
--     2、表级锁 ：MyISAM
--       可以加读锁、写锁
-- 4、存储引擎(处理表的处理)
--   1、基本操作
--     1、查看所有的存储引擎
--       mysql>show engines;
--     2、查看已有表的存储引擎
--       mysql>show create table 表名;
--     3、创建表时指定存储引擎
--       mysql>create table 表名(...)engine=MyISAM
--     4、已有表
--       mysql>alter table 表名 engine=InnoDB;
--   2、InnoDB特点
--     1、支持行级锁、外键
--     2、支持事务、事务回滚
--     3、共享表空间
--       表名.frm ：表结构和索引信息
--       表名.ibd ：表记录
--   3、MyISAM特点
--     1、支持表级锁
--     2、独享表空间
--       表名.frm ：表结构
--       表名.myd ：表记录
--       表名.myi ：索引文件
--   4、MEMORY特点
--     1、表结构在硬盘中,表记录在内存中
--     2、服务重启或主机重启后,表记录消失
--   5、如何决定使用哪个存储引擎
--     1、执行查询操作多的表 ：MyISAM(使用InnoDB浪费资源)
--     2、执行写操作多的表   ：InnoDB
-- 5、数据导入 ：把文件系统内容导入到数据库表中
--   1、语法格式
--     load data infile "文件名绝对路径"
--     into table 表名 
--     fields terminated by "分隔符"
--     lines terminated by "\n"
--   2、数据导入步骤
--     1、把文件拷贝到数据库搜索路径中
--       1、查看搜索路径
--         show variables like "secure_file_priv";
--       2、拷贝文件
--         sudo cp scoreTable.csv /var/lib/mysql-files/
--         文件权限问题 ：chmod 644 scoreTable.csv
--     2、创建对应的表
--       库、表都是utf8的
--       create table scoretab(
--       id int,
--       name varchar(20),
--       score float(5,2),
--       phnum char(11),
--       class char(7)
--       )charset=utf8;
--     3、执行数据导入语句
-- 	load data infile "/var/lib/mysql-files/scoreTable.csv"
-- 	into table scoretab
-- 	fields terminated by ","
-- 	lines terminated by "\n"
-- 	;
-- 	常见错误：
-- 	db4.scoretab doesn't exist ：查看表名
-- 	No database selected    ：use db4
-- 	... secure_file_priv ...：chmod 644 scoreTable.csv
-- 	....  entry '1'
--   3、作业
--     tarena : x  : 1000 : 1000 :
--     用户名  密码  UID    GID
--     tarena,,, : /home/tarena   :  /bin/bash
--     用户描述    主目录/家目录     登陆权限
    
--     导入完成后,在第1列添加id字段,主键,自增长,显示宽度为3,位数不够用0填充

--     001  root  x  ...
--     002  tarena x ...
--     003  mysql  x ...
-- 6、数据导出 ：把数据库表中记录保存到系统文件里
--   1、语法格式
--     select ... from 表名 where 条件
--     into outfile "文件名绝对路径"
--     fields terminated by "分隔符"
--     lines terminated by "分隔符"
--   2、把sanguo表中姓名、攻击值、国家导出到sanguo.csv文件中
--     select name,gongji,country from MOSHOU.sanguo
--     into outfile "/var/lib/mysql-files/sanguo.csv"
--     fields terminated by ","
--     lines terminated by "\n"
--     ;
--   3、注意
--     1、导出的内容完全由SQL查询语句决定
--     2、执行导出命令时路径必须指定在搜索路径中
-- 7、数据备份(mysqldump,在Linux终端操作)
--   1、命令格式 
--     mysqldump -u用户名 -p 源库名 > XXX.sql
--   2、源库名表示方式
--     --all-databases     备份所有库
--     库名                备份单个库
--     -B 库1 库2 库3      备份多个库
--     库名 表1 表2 表3    备份多张表
--   3、备份所有库,到/home/tarena/mydata/all.sql
--     mysqldump -uroot -p --all-databases > all.sql
--   4、备份MOSHOU和db4两个库,MOSHOUdb4.sql
--     mysqldump -uroot -p -B MOSHOU db4 > MOSHOUdb4.sql
-- 6、数据恢复(Linux终端中操作)
--   1、命令格式 
--     mysql -u用户名 -p 目标库名 < XXX.sql
--   2、从所有库的备份中恢复某一个库
--     mysql -u用户名 -p --one-database 目标库名 < XXX.sql
--   3、注意 ：如果恢复的库不存在,则必须先创建空库
-- 7、Day03作业答案
--   select  user_id,count(user_id)  from  comment
--   group  by  user_id
--   order  by  count(user_id)  DESC
--   limit  10;



































