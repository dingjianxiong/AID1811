--日期与时间
--		1. date : 表示日期 "YYYY-MM-DD"
--		2. time : 表示时间 "hh:mm:ss"
--		3. datetime : 表示日期时间 "YYYY-MM-DD hh:mm:ss"
--		4. timestamp : 表示日期时间 "YYYY-MM-DD hh:mm:ss"
--		注意 ：
--			日期时间的表示方法 ：
--			使用字符串表示，格式可采用 "2011/11/11 11:11:11"
--			"2011-11-11 11:11:11"
--			"20181201103050"
--		日期时间函数 ：
--			1. now()     取当前系统时间
--          2. sysdate() 取当前系统时间
--			3. curdate() 取当前系统日期
--			4. curtime() 取当前系统时间
--			4. year(date) 根据给定的日期获取年份信息
--			5. date('20111010121212') 获取日期信息
--			6. time('20111010121212') 获取时间信息
--          7. month() 取指定日期中的月份
--          8. day() 取致电该日期的天
--          9. date() 取指定日期时间中的

-- 取当前系统日期时间
select now(),sysdate();
-- 取当前时间日期、时间
select curdate(),curtime();
-- 先取出当前系统日期时间，再取出年份、月份、天
select year(now()),month(now()),day(now());
--先取出当前系统日期时间，再取出日期、时间
select date(now()),time(now());

-- 2、数据操作（更新、删除、重点）
-- 更新操作
		update 表名
            set 字段名=值,字段名=值 where 条件;
        where 条件表达式;
		--注意 ：
			--更新操作中，where条件必须写，如果省略，会
			--将表中所有记录都进行修改
-- 当表中acct_no ='45614525655'时，修改status=2
update acct set status=2 where acct_no ='45614525655';
-- 编写注销账号的sql语句（修改状态、余额为0）
update acct set status=4 balance=0 where '45789632587'

--删除表
		delete from 表名 where 条件;
		--注意 ：
			where 条件可以省略，delete from 表名;
--			表示清空表记录

delete from  acct where acct_no='45789632587'

-- 2、运算符 查询
-- 查询账户状态不等于2的账户；
select * from acct where status<>2;
-- 查询账户小于5000的账户
select * from acct where balance<5000;

-- 2. 逻辑运算符
			--1. and 与
					--连接两个条件，要求同时成立
			---2. or	 或
					--连接条件，表示任意一个条件成立都可以
-- 例子
-- 查询余额大于0  且  状态为2 的账户
select * from acct where balance>0 and status=2;
-- 查询状态为1  或  状态为2 的账户信息
select * from acct where status=1 or status=2;
--多个条件组合
select * from acct where(acct_no ='62551122200' or acct_no='65622551214') and status=1;


--范围比较
-- in 在某个范围（集合）中
-- not in 不在某个范围（集中）中
-- between...and ..在。。。与。。。之间

-- 查询账户在某个指定范围内的账户信息
select *from acct where acct_no in ('62551122200','65622551214');
-- 使用 between 查询余额在某个范围之内的账户信息（包含两个边界值）
select * from  acct where balance between 3000 and 7000;


-- 模糊查询（比较慢，大量使用造成性能下降）
--格式：where字段名称 like ’通配字符串‘
-- 通配符 _匹配单个字符
-- 通配符 %表示匹配任意个字符

-- 查询以D开头的户名的所有账户
select * from acct where acct_name like 'D%';

-- 'D%'表示D 后面可以跟任意个字符
-- '%D%' 表示包含D的都可以查询出来
-- 'D_'表示后面可以跟一个字符


--空/非空判断（NULL是一个特殊值）
-- 判断空：is null
-- 判断非空：is not null

--   查询账户 类型为空/非空的数据
select * from acct where acct_type is null;-- 空
select * from acct where acct_type is not null;-- 非空
-- 查询客户编号为 空字符串 或 为null 的账户
select * from acct where cust_no= '' or cust_no is null;

-- 子句查询：排序、分组、筛选
-- 排序：order by
-- 作用：对查询的结果按照摸个字段进行排序
-- 格式：order by 排序字段[ASC/DESC]
--     ASS表示升序
--     DESC表示降序
--     不写排序 默认为升序

-- 查询账户信息，按照账户余额升序排列
select * from acct order by balance asc;--desc

-- 按照账户信息，按照账户类型升序、金额降序
select *  from acct order by acct_type asc,balance desc;


-- limit 子句
-- 作用：限制查询的结果笔数
-- 格式：limit n 只显示前面n行
--       limit m，n   从m笔开始显示，总共显示n笔（通常用作分页查询）
-- 查询账户余额最大的前3个账户
select acct_no, acct_name, balance 
    from acct 
    order by balance desc
    limit 3;
-- 从第一笔开始，显示3笔数据
select acct_no, acct_name, balance 
    from acct 
    order by balance desc
    limit 0,3;
select acct_no, acct_name, balance 
    from acct 
    order by balance desc
    limit 2,3;
select acct_no, acct_name, balance 
    from acct 
    order by balance desc
    limit 5,3;
    -- 经常利用limit m，n子句进行查询分页处理
    -- m 表示起始的行数（从0开始）
    -- n 表示每页有多少行
    -- 利用当前显示第几行、每页多少行就能计算出m 和 n 的值，实现分页查询
    -- m=（页数-1）* 每页多少笔
    -- n= 每页显示的笔数


--聚合函数
--    1. 对指定字段中的数据进行二次处理
--    2. 分类 ：
--      avg(字段) ：求平均值
select avg(balance)from acct;
--      max(字段) ：求最大值
select max(balance) from acct;
--      min(字段) ：求最小值
select min(balance) from acct;
--      sum(字段) ：求和
select sum(balance) from acct;
--      count(字段) ：统计当前字段中记录的条数
-- count 后的括号中可以跟字段、数字，但是如果跟字段，当字段为null则不会参与统计
select count(*) from acct;


-- group by子句
-- 作用：对查询结果进行分组，通常和聚合函数配合使用
-- 格式：group by 分组字段名称

-- 统计各种状态账户数据量
select count(*),acct_type from acct group by acct_type;
-- 统计各类账户余额的最大值
select acct_type '账户类型',max(balance)'最大余额' from acct group by acct_type;


-- having 子句
--作用：对分组聚合的结果进行过滤
--     需要和group by 子句配合使用
-- 示例：统计各类账户的总余额，过滤掉账户类型为空的
select acct_type '类型',sum(balance)'总余额'
    from acct
    group by acct_type
    having  acct_type is not null;


-- sql语句执行顺序（难点）
select acct_type '类型',sum(balance)'总余额'
    from acct
    where acct_type in(1,2,3,4)
    group by acct_type
    having  acct_type is not null;
    order by acct_type desc
    limit 2;
-- 第一步： from acct
--       首先执行from，找到源数据
-- 第二部：where 条件过滤
--       选出所有满足条件的数据
-- 第三步： group by 子句
--       进行分组
-- 第四步： sum(balance)，acct_type
--       按照分组，对每组进行统计
-- 第五步：having  acct_type is not null;
--       把聚合以后不满足条件的数据过滤掉
-- 第六步： order by acct_type desc
--       按照统计结果排序
-- 第七步：limit 1
--       限定显示的笔数

-- 补充说明：
--      having子句只能对group by 子句的结果进行过滤
--      where只能限定表中实际存在的字段，位于from后；


-- distinct 子句
-- 作用：对某个字段去重
-- 格式：select distinct(字段名称) from 表名称
-- 查看账户表中一共有多少种账户类型
select distinct(acct_type) from acct;
select distinct(acct_type) from acct;


-- 表结构调整（alter table）
create table student(
    stu_no varchar(32),
    stu_name varchar (64)
);
-- 添加字段
--添加到最后一个字段       alter table 表名 add 字段名 数据类型;
alter table student add ade int;-- 添加到最后
--添加到第一个字段		 alter table 表名 add 字段名 数据类型 first;
alter table student add  id int first;
--添加到指定位置		 alter table 表名 add 字段名 数据类型 after 字段名;
alter table student add  tel_no varchar(32) after stu_name;

-- 修改字段
--修改字段类型
--alter table 表名 modify 字段名 类型（长度）
--修改字段名称
--alter table 表名
--change 旧字段名 新字段名 类型（宽度）
-- 示例：
-- 将stu_name 长度修改为（128）
alter table student modify stu_name varchar(128);

-- 将age字段改为stu_age
alter table student change age stu_age int;
-- 修改字段类型
--alter table 表名 modify 字段名 新数据类型;





--创建一个库eshop，并指定编码为utf-8
create database eshop character set utf8;
--创建订单表（orders，utf8编码），包含如下字段
use eshop;
create table orders(
    order_id varchar(32),
    cust_id varchar(32),
    order_dtae DateTime,
    status enum('1','2','3','4','5','6','9'),
    products_num int,
    amt int
);
--order_id 订单编号，字符串 ，32字节
--cust_id  客户编号，字符串，32字节
--order_dtae 下单时间，DateTime类型
--status 订单状态，枚举类型，取值范围（'1','2','3','4','5','6','9')
--1-待付款  2-代发货 
--3-待收货  4-已收货
--5-申请退货 6-已退货
--9-已废弃
--products_num  订单包含的商品数量
--amt        订单总金额，浮点数，两位小数

--至少插入5笔数据（要求数据看上去尽量真实）

insert into orders values
('201801','C001',now(),4,3,4000.00),
('201802','C002',now(),5,5,5000.00),
('201803','C003',now(),6,2,6000.00),
('201804','C004',now(),9,3,9000.00),
insert into orders values
('201804','C004',now(),9,3,7000.00),
('201805','C005',now(),1,3,4000.00),
('201806','C006',now(),2,5,5000.00);
insert into orders values
('201805','C005',now(),'2',2,7000.00),
('201806','C006',now(),'3',5,9000.00);

--编写如下sql语句
--1、查找所有待付款订单
-- select * from acct where status=1 or status=2;
select * from orders where status='1';
--2、查找所有已发货、已收货、申请退货订单
select * from orders where status='3' or status='4' or status='5';
--3、查找某个客户的代发货订单
select cust_id='C002' from orders where status='2';
--4、根据订单编号，查找订单下单日期，订单状态
select status from orders where order_id="201806";
--5、查找某个客户所有订单，并按照下单时间倒序排列
insert into orders values
('201804','C004',now(),2,3,4000.00),
('201805','C005',now(),2,5,5000.00),

select * from orders where cust_id='C005' order by order_dtae desc;
--6、统计每种状态的订单数量
-- select count(*),acct_type from acct group by acct_type;
select count(*),status from orders group by status;
--7、查询单笔订单最大值/最小值/平均值，所有订单总金额
-- select count(*) from acct;
select max(amt) from orders ;
select min(amt) from orders ;
select avg(amt) from orders ;
select sum(amt) from orders ;
--8、查询金额最大的前3笔订单
select * from orders order by amt desc limit 3;
--9、在表的最后添加两个字段：
    alter table orders add invoice int;
    alter table orders add invoice_date DateTime;
--  invoice  开票状态，整数
--  invoice_date   开票日期 ，DateTime 类型
--10、 修改某个订单状态为“已收货”
        --修改字段类型
        --alter table 表名 modify 字段名 类型（长度）
        --修改字段名称
        --alter table 表名
        --change 旧字段名 新字段名 类型（宽度）
        --alter table 表名 modify 字段名 新数据类型;
        update orders set status='4' where order_id='201804';
--11、删除已废弃的订单
delete from  acct where acct_no='45789632587'
delete from orders where status='9';