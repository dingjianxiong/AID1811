--(一)约束：
--     数据遵循的规则，为了保证数据完整性、一致性、有效性

--    1、非空约束(NOT NULL)
--     不允许该字段值有NULL记录
--     create ...(
--     name varchar(20) NOT NULL,
create table customer(
    cust_no varchar(32) not null,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
);
insert into customer(cust_no,cust_name) values("C001",'join');
--     指定字段的值不能为空，插入时如果没有默认值，插入就会报错

--    2、默认约束(DEFAULT 值)
--     插入记录时,不给该字段赋值,则使用默认值
--     create ...(
--     sex enum("M","F","S") not null default "S"
-- 创建时设置默认值：
create table customer(
    cust_no varchar(32) default "0001",
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
);
--   当插入字段时
alter table customer add status int default 0-- 设置默认值为0
insert into customer(cust_no,cust_name,tel_no) values("C001",'jerry','123456789');

--    3、唯一约束：字段不能重复
--       语法：字段名称 类型 unique
create table customer(
    cust_no varchar(32) unique,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
);
-- 插入重复数据，违反唯一约束
insert into customer values("C001",'jerry','123456789');
insert into customer values("C001",'Tom','123456789012');

--    4、主键约束(primary key)：指定字段作为主键，非空、唯一;
--        pk用来唯一标示一笔记录，要求非空、唯一
--        pk和一笔记录之间有唯一对应关系
--        pk可以是一个字段构成，也可以多个属性共同构成
--        语法：字段名称，字段类型 primary key
create table customer(
    cust_no varchar(32) primary Key,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
);
-- 主键不能为空
insert into customer values('jerry','123456789');
--主键不能重复
insert into customer values("C001",'jerry','123456789');
insert into customer values("C001",'jerry','123456789');

--   5、自动增加：字段的值自动增加
-- 当字段设置为自动增长时，插入数据不需要填值，数据库系统会自动在上一个值上增加1
-- 经常和pk配合使用
--语法： 字段名 字段类型 auto_increment
--示例：
create table ai_test(
    id int primary key auto_increment,
    name varchar(32)
);
insert into ai_test values (null,'aaa');
insert into ai_test values (null,'bbb');
insert into ai_test values (null,'ccc');
--   6、外键约束(难点)：某个属性，在当前表不是主键，在另一个表是主键
--   作用：参照外键时 ，外键对应的实体必须存在，保证参照的完整性、一致性
--  使用外键的条件：表的存储引擎必须为InnoDB，被参照字段在另外的表里必须是主键
--             当前表中的字段类型和被参照的表中类型一致
--  语法： 
--        constraint foreign key(当前表字段)
--        references 参照表名（参照字段名称）
--   外键
create table account(
    acct_no varchar (32) primary key,
    cust_no varchar (32) not null,
    -- 在当前表的cust_no上添加外键约束
    -- 参照customer表的cust_no字段
    constraint foreign key (cust_no)
    references customer(cust_no)
);
--插入customer 表中存在的客户
-- 参照完整性正确，可以插入
insert into account values ('0001','C001')
--C0004客户不存在，参照完整性错误
insert into account values ('C0004','C001')
-- 删除被参照的值，也会报错
delete from customer where cust_no='C001';


-- (二)、索引
--   1、定义 ：对数据表的一列或者多列的值进行排序的一种结构(BTree)
--   2、优点 ：加快数据检索速度,唯一索引能保证数据的唯一性，在使用索引字段分组、排序时，效率会提高
--   3、缺点
--     1、占用物理存储空间
--     2、当对表中数据更新时,索引需要动态维护,降低数据维护速度
--     3、降低增、删、改的效率
--   4、索引类别
--      普通索引、唯一索引
--      单列索引、组合索引
--   5、如何创建索引
--        创建表时创建索引
---       语法： 字段名  字段类型 [index | unique |primary key]
--               index(字段名),普通索引
--               unique(字段名),唯一索引
--               primary key  主键，自动成为唯一索引
--        示例1：创建账户交易明细表交易流水号上创建唯一索引
create table acct_trans_detail(
    trans_sn varchar (32) not NULL,-- 交易流水号
    trans_date datetime not NULL,-- 交易时间
    acct_no varchar(32) not NULL,-- 交易账号
    trans_type int,-- 交易类型
                               -- 存款，取款，刷卡，结息
    amt decimal(16,2) not null,-- 交易金额
    unique(trans_sn),-- 在trans_sn上创建唯一索引
    index (trans_date)--  在trans_date上建立普通索引
);
-- 查看索引
show index from acct_trans_detail;
-- 插入数据
insert into acct_trans_detail
values ('20181201011',now(),'622354120001',1,1000);
-- 查询时使用索引字段作为条件，就会使用到索引
select * from acct_trans_detail
where trans_sn='20181201011';
-- 通过修改表的方式创建索引
--create 索引类型 索引名称 on 表名(字段名)
create index trans_date on acct_trans_detail(trans_date);

--alter table 表名 add 索引类型  索引名称(字段)
alter table acct_trans_detail add unique index trans_sn(trans_sn);
-- 删除索引
--drop index 索引名称 on 表名
drop index trans_date on acct_trans_detail

--  索引使用原则
--    使用恰当的索引
--    索引并不是越多越好，索引太多影响增删改效率
--    适合使用索引的情况：字段经常作为查询条件，字段的值相对均匀，
      --       如果某个字段经常用来作为排序依据，适合加索引
--    不适合使用索引的情况
    -- 不经常作为查询条件
    -- 值太少的字段不适合建索引(性别、账户状态)
    -- 数据量太少不适合建立索引
    -- 二进制类型的数据字段不适合建立索引
--   主键、唯一索引效率很高


-- 数据导入导出
--  1、导出
    --  格式：
    --  select 查询语句
    --  into outfile '文件路径'
    --  fields terminated by '字段分隔符'
    --  lines terminated by '行分隔符'
-- 示例：
--   第一步：查看数据库允许导出的目录路径
show variables like 'secure_file%'
--结果：secure_file_priv：   /var/lib/mysql-files/
-- 第二步：执行导出（导出到第一步所看到的目录下）
select * from orders
into outfile '/var/lib/mysql-files/acct.bak'
fields terminated by ','
lines terminated by '\n';
-- 查看
sudo cat /var/lib/mysql-files/acct.bak

--  2、导入
    --格式：
    --   load data infile '备份文件路径'
    --   into table 表名称
    --   fields terminated by '字段分割符'
    --   lines terminated by '行分隔符'
-- 导入
load data infile '/var/lib/mysql-files/acct.bak'
into table orders
fields terminated by ','
lines terminated by '\n';

--  3、表的复制、重命名
     --复制
        -- 将原表完全复制为新表
        create table orders_id select * from orders;
        -- 部分复制
        create table orders_new select order_id,cust_id from orders;
        -- 部分复制(只拷贝表结构)
            -- * 注意：这种方式复制表，不会把键属性复制过来
        create table orders_id select * from orders where amt>5000;
    -- 重命名
        -- 格式：alter table 表名 rename to 新表名
        -- 示例：
            alter table  orders_id  rename [to] orders_new 
--  把eshop里的acct_trans_detail表复制到当前表并给他命名
create table acct_trans_detail select * from eshop.acct_trans_detail;

-- 课堂练习
  ---修改orders表结构
-- 2、在orders_id列上添加主键约束
alter table orders modify order_id varchar(32) primary Key;
--方法二
alter table orders add primary Key(order_id)
-- 3、在cust_id ,orders_date,products_num字段上添加非空约束
alter table orders  modify order_id varchar(32) not null;
alter table orders  modify order_dtae datetime not null;
alter table orders  modify products_num int not null;
-- 4、在status 字段上添加默认值，默认值为1
alter table orders  modify status enum('1','2','3','4','5','6','9') default '1';
-- 5、在order_date 上添加普通索引
create index order_dtae on orders(order_dtae);
-- 2、创建客户信息表customer_new，包含字段有
-- cust_id     客户编号，字符串 ，32 主键
-- cust_tel    客户电话，字符串 ，32 非空
-- cust_name   客户姓名，字符串 ，64 非空
-- address     送货地址，字符串 ，128 非空
create table customer_new(
    cust_id varchar(32) primary Key,
    cust_tel varchar(32) not null,
    cust_name varchar(64) not null,
    address varchar(128) not null
)charset=utf8;
-- 3、为customer_new表添加数据，要求每个orders中的cust_id都有对应的客户信息
insert into customer_new values
('C001','125489777','张三','重庆渝中'),
('C002','125489888','李四','重庆渝北'),
('C003','125489999','小王','重庆沙坪坝');
insert into customer_new values
('C003','125489123','小明','重庆巴南'),
('C004','125489345','小李','重庆大学城'),
('C005','125489678','小吴','重庆江北');
select * from customer_new;
-- 4、在orders表的cust_id上创建外键约束，参照customers表的cust_id字段

alter table orders add constraint cust_id
foreign key(cust_id) references customer_new(cust_id);

show index form orders;