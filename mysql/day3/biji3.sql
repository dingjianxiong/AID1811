-- 王伟超
--   wangweichao@tedu.cn
-- Day02回顾
-- 1、数据类型
--   1、数值类型
--   2、字符类型
--   3、枚举类型
--   4、日期时间类型
--     1、date
--     2、time
--     3、datetime  : 不给值默认返回NULL
--     4、timestamp ：不给值默认返回系统当前时间
-- 2、日期时间函数
--   1、NOW()
--   2、CURDATE()
--   3、CURTIME()
--   4、YEAR(字段名)
--   5、DATE(字段名)
--   6、TIME(字段名)
-- 3、日期时间运算
--   select .... from 表名 
--   where 字段名 运算符(now()-interval 时间间隔单位)
--   1 day | 2 day | 3 hour
-- 4、表字段操作
--   1、添加(add)
--     alter table 表名 add 字段名 数据类型 first | after 字段名;
--   2、删除(drop)
--     alter table 表名 drop 字段名;
--   3、修改(modify)
--     alter table 表名 modify 字段名 新数据类型;
--   4、表重命名(rename)
--     alter table 表名 rename 新表名;
--   5、表字段重命名(change)
--     alter table 表名 change 原名 新字段名 数据类型;
-- 5、表记录管理
--   1、删除 ：delete from 表名 where 条件;
--   2、修改 ：update 表名 set 字段1=值1,... where 条件;
-- 6、运算符
--   1、数值&&字符&&逻辑比较
--     1、数值 ：> >= < <= = != 
--     2、字符 ：= !=
--     3、逻辑 ：and or
--   2、范围内比较
--     in(值1,值2)
--     not in(值1,值2)
--     between 值1 and 值2 
--   3、空、非空
--     is null
--     is not null
--   4、模糊查询
--     where 字段名 like "%_"
-- 7、SQL查询
--   1、order by 字段名 ASC/DESC
--   2、limit
--     1、limit n
--     2、limit m,n
--     3、分页：每页m条记录,显示第n页内容
--       limit (n-1)*m,m
--   3、聚合函数
--     avg(字段名) sum(...) max(...) min(...)
--     count(字段名)
-- ****************************************
-- Day03笔记
-- 1、SQL查询
--   1、总结
--     3、select 聚合函数 from 表名 
--     1、where 条件
--     2、group by ...
--     4、having ...
--     5、order by ...
--     6、limit ...
--   2、group by ：给查询的结果进行分组
--     1、计算每个国家的平均攻击力
--       select country,avg(gongji) from sanguo 
--       group by country;
--     2、查找所有国家英雄中,英雄数量最多的国家的前2名,显示国家名称和英雄数量
--       select country,count(id) as number from sanguo
--       group by country
--       order by number desc
--       limit 2;

--       先分组      再聚合      去重
--       蜀国
--       蜀国
--       蜀国        100         蜀国

--       魏国
--       魏国        100         魏国

--       吴国
--       吴国        99          吴国
--     3、注意
--       查询字段和group by后字段不一致,则必须对该查询字段进行聚合处理(聚合函数)
--   3、having语句 ：对分组聚合后的结果进一步筛选
--     1、找出平均攻击力>105的国家的前2名,显示国家名称和平均攻击力
--       select country,avg(gongji) from sanguo
--       group by country
--       having avg(gongji)>105
--       order by avg(gongji) desc
--       limit 2;
--     2、注意
--       having语句通常和group by语句联合使用,having语句弥补了where关键字不能与聚合函数使用的不足,where只能操作表中实际存在字段
--   4、distinct ：不显示字段的重复值
--     1、表中有哪些国家
--       select distinct country from sanguo;
--     2、计算蜀国有多少个英雄
--       select count(distinct id) as number from sanguo
--       where country="蜀国";
--   5、查询表记录时做数学运算
--     + - * / %
--     查询时所有英雄攻击力翻倍
--     select name,gongji*2 as xgj from sanguo;
--     update sanguo set gongji=gongji*2;
-- 2、嵌套查询(子查询)
--   1、定义 ：把内层的查询结果作为外层的查询条件
--   2、select .. from 表名 where 字段名 运算符 (查询);
--   3、把攻击值小于平均攻击值的英雄名字和攻击值显示
--     1、先算出平均攻击值
--       select avg(gongji) from sanguo;
--     2、找小于平均值
--       select name,gongji from sanguo where gongji<..
--     3、嵌套查询实现
--       select name,gongji from sanguo where gongji<(select avg(gongji) from sanguo);
--   4、找出每个国家攻击力最高的英雄的名字和攻击值
--     select name,gongji from sanguo 
--     where
--     (country,gongji) in (select country,max(gongji) from sanguo group by country);
-- 3、多表查询
--   1、笛卡尔积 ：select ... from 表1,表2;  不加where
--   2、多表查询 ：加 where 条件
--   3、显示省、市详细信息
--     河北省 石家庄市
--     河北省 廊坊市
--     广东省 深圳市
--     select sheng.s_name,city.c_name from sheng,city
--     where
--     sheng.s_id=city.cfather_id;
--   4、显示省、市、县详细信息
--     select sheng.s_name,city.c_name,xian.x_name from sheng,city,xian
--     where
--     sheng.s_id=city.cfather_id and
--     city.c_id=xian.xfather_id;
-- 4、连接查询
--   1、内连接(inner join ：只显示满足匹配条件的结果)
--     1、select ... from 表1 inner join 表2 on 条件;
--     2、显示省、市详细信息
--       select sheng.s_name,city.c_name from sheng 
--       inner join city
--       on sheng.s_id = city.cfather_id;
--     3、显示省、市、县详细信息
--       select sheng.s_name,city.c_name,xian.x_name from sheng
--       inner join city
--       on sheng.s_id=city.cfather_id
--       inner join xian
--       on city.c_id=xian.xfather_id;
--   2、左外连接(left join：以左表为主显示查询结果)
--     1、select ... from 表1 left join 表2 on 条件;
--     2、显示省、市详细信息,要求省全都显示
--       select sheng.s_name,city.c_name from sheng 
--       left join city
--       on sheng.s_id=city.cfather_id;
--     3、显示省、市、县详细信息,要求 市 全都显示
--       select sheng.s_name,city.c_name,xian.x_name from 
--       sheng right join city 
--       on sheng.s_id=city.cfather_id
--       left join xian
--       on city.c_id=xian.xfather_id;
--   3、右外连接(right join：以右表为主显示查询结果)
-- 5、约束
--   1、非空约束(NOT NULL)
--     不允许该字段值有NULL记录
--     create ...(
--     name varchar(20) NOT NULL,
--   2、默认约束(DEFAULT 值)
--     插入记录时,不给该字段赋值,则使用默认值
--     create ...(
--     sex enum("M","F","S") not null default "S"
-- 6、索引
--   1、定义 ：对数据表的一列或者多列的值进行排序的一种结构(BTree)
--   2、优点 ：加快数据检索速度
--   3、缺点
--     1、占用物理存储空间
--     2、当对表中数据更新时,索引需要动态维护,降低数据维护速度
--   4、索引示例
--     查看变量状态 ：show variables like "%pro%";
--     1、开启运行时间监测
--       mysql> set profiling=1;
--     2、执行1条查询语句(无索引)
--       select name from t1 where name="lucy99999";
--     3、在name字段创建索引
--       create index name on t1(name);
--     4、再执行1条查询语句(有索引)
--       select name from t1 where name="lucy100000";
--     5、查看执行时间
--       mysql> show profiles;
--     6、关闭运行时间监测
--       mysql> set profiling=0;
-- 7、索引分类
--   1、普通索引(index)、唯一索引(unique)使用规则
--     1、可创建多个字段
--     2、普通索引无约束,唯一索引要求字段值不允许重复,但可为NULL
--     3、KEY标志 ：普通(MUL) 唯一(UNI)
--     4、经常用查询的字段、where后、order by排序字段创建索引
--   2、创建
--     create table t1(
--     ... ...,
--     index(字段名),
--     index(字段名),
--     unique(字段名),
--     unique(字段名)
--     )charset=utf8;
--     create [unique] index 索引名 on 表名(字段名);
--   3、查看
--     1、desc 表名; --> KEY标志
--     2、show index from 表名\G;
--   4、删除
--     drop index 索引名 on 表名;









  










-- 在线 ：
--   sudo pip3 install pymysql
-- 离线 ：
--   1、下载 xxx.tar.gz
--   2、进入解压后的目录,找 setup.py
--   3、sudo python3 setup.py install




















