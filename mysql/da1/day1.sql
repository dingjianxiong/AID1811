-- 1. 创建表
--			create table 表名(字段名 数据类型,
--			字段名 数据类型,
--			字段名 数据类型);
---		2. 查看表的字符集
--			show create table 表名;
--		3. 查看表结构（表中包含哪些字段）
--			desc 表名;
--		4. 删除表
--			drop table 表名;
-- 创建acct（账户）
create table acct2(
    acct_no varchar(32),
    acct_name varchar(128),
) default charset=utf8;

--重新创建acct
create table acct(
    acct_no varchar(32),   -- 账号，字符串，32字节
    acct_name varchar(128),-- 户名，128字节
    aust_no varchar(32),   -- 客户编号
    acct_type int,         -- 账号类型，整数型
    reg_date date,         -- 开户日期，日期类型
    status int,            -- 账号状态，整数型
    balance decimal(16,2)  -- 数字类型
                           -- 最长16位，2位小数
)default charset=utf8;

-- 插入
-- now() 表示当前日期
insert into acct
values("13668498248","jerry","C001",1,now(),1,1000.00)

-- 使用一个sql语句插入多笔数据
insert into acct values
('62551122200','Tom',"C006",1,NOW(),1,2000.00),
('62551122201','Dekie',"C007",1,NOW(),1,4000.00),
('62551122202','Dekes',"C008",1,NOW(),1,6000.00);
-- 指定字段插入
insert into acct(acct_no,acct_name)
values("45614525655","Emma");

-- 查询
-- 查询所有数据：  select * from 表名；
select * from acct;
-- select * from 表名 [where 条件]
-- select 字段列表 from 表名 [where 条件]
-- select 指定字段
select acct_no,acct_name,balance from acct;

-- 查询指定的字段，并为字段起别名
select acct_no"账号",
       acct_name "户名",
       balance "余额"
from acct;
-- 或者
select acct_no as "账户",acct_name as "户名",balance as "余额" from acct;

-- 查询时，使用字段的值进行计算
-- 查询账户余额，以万元为单位显示
select acct_no"账号",
       acct_name "户名",
       balance/10000"余额(万元)"
from acct;
-- 带条件的查询
select * from acct
where acct_no="62551122200";

-- 带两个条件的查询，两个条件同时满足
select *from acct
where acct_no="62551122200" and acct_name="Tom";
-- 带两个条件的查询，满足一个
select acct_no,acct_name,balance
from acct
where acct_name="Tom"
    or  acct_name='Dekie';


--char 和 varchar 类型示例
create table tmp(
    acct_no char(10),
    acct_name varchar(32)  
);
insert into tmp values('C001',"jerry");

-- enum, set 类型
create table enum_test(
    name varchar(32),
    sex enum('boy','girl'),-- 两者选一
    course set('music','dance','paint')
);
-- 在枚举范围内，可以插入
insert into enum_test
values ("Jerry",'girl','music,dance');
-- 在枚举范围之外，插入报错，football不在范围内
insert into enum_test
values ("Jerry",'girl','music,football');
