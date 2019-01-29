-- 嵌套查询(子查询)
--    1、定义 ：把内层的查询结果作为外层的查询条件
--    2、select .. from 表名 where 字段名 运算符 (查询);
--    例如： 查询发生过的交易的账户信息
--         select * from acct where acct_no in
--         (--外层查询 select distinct acct_no from accy_trans_detail)
--        说明：括号中的部分称为子查询，先执行子查询，返回一个结果集，在执行外层查询，
--             子查询返回的结果要和外查询的条件匹配，子查询只执行一次
--    3、什么情况使用子查询
--       一个查询语句无法实现
--       一个查询语句不方便、不直观
--    4、单表查询
--       -示例：查询所有余额大于平均余额的账户
--            select * from acct where balance >(select avg(balance) from acct)
-- 多表查询
--      多表查询 ：加 where 条件
--      1、示例： 查询所有发生过交易的账户信息
select  * from acct where acct_no in (select distinct acct_no from acct_trans_detail);
--      2、查询所有未发生过的大金额交易的账户信息
select * from acct where acct_no not in(select distinct acct_no from acct_trans_detail);
--      3、查询所有发生过的大金额交易的账户信息 
select * from acct where acct_no  in ( select distinct acct_no from acct_trans_detail where amt >5000);

--   笛卡尔积 ：两个集合乘积，每个集合中元素两两组合产生的新集合
--       意义： 表示两个集合所有可能的情况组合
      --   A：学生集合    B:课程集合
      --   A和B的笛卡尔积表示所有学生可能的选课情况
     --     C：所有声母   D：所有韵母  
           --C和D的笛卡尔积表示所有有可能的拼音组合
        --   笛卡尔积和关系（二维表）
        --   笛卡尔集中可能含有不存在（没有实际意义）数据
             -- 去掉部分数据就是关系
        --  例如bun在汉语拼音中不存在，应该去掉
--          语法： select ... from 表1,表2;  不加where

-- 连接查询：
--        将两个（或两个以上）的表连接起来得到一个新表（叫表的连接
--   什么时候使用连接查询：当从一个表中无法获得所有想要的数据时，使用联合查询（前提是两个表数据有关联关系）
--   1、内连接 ：只显示匹配到的记录
--   2、外连接
--     1、左连接 ：以左表为主显示查询结果
--     2、右连接 ：以右表为主显示查询结果
--   3、select 表名.字段名 from 表1
--      inner/left/right join 表2 on 条件
--      inner/left/right join 表3 on 条件;
--     1、内连接(inner join ：只显示满足匹配条件的结果)
--     、select ... from 表1 inner join 表2 on 条件;
--     2、左外连接(left join：以左表为主显示查询结果)
--     、select ... from 表1 left join 表2 on 条件;
--     3、右外连接(right join：以右表为主显示查询结果)
--      select ... from 表1 right join 表2 on 条件;
--  连接分类（默认内连接）：
--      内连接：关联到的数据显示，没有关联到的数据不显示
--           格式：select 字段列表  from 表A inner join 表B on 关联条件
--         示例： 
--             select a.acct_no,a.acct_name,c.tel_no from acct a 
--             inner join customer c
--              on a.cust_no=c.cust_no;
--     外链接： 没有关联到的数据也显示(指定那个表的数据全部显示)
--          左连接：左表内全部显示，右表匹配
--                select 字段列表 from 表A left join 表B on 关联条件
--             示例：查询账户、户名、客户电话，如果账户对应的客户不存在也要显示账户、户名
--               select a.acct_no,a._acct_name ,c.tel_no from acct a
--                 left join customer c 
--                 on a.cust_no =c.cust_no;
--           右连接：右表内全部显示，左表匹配
--               select 字段列表 from 表A right join 表B on 关联条件
--             
--                 select a.acct_no,a._acct_name ,c.tel_no 
---                from acct a
--                 right join customer c 
--                 on a.cust_no =c.cust_no;

--  权限管理（难点）
--      1、权限：用户可以进行哪些操作
--      2、分类：
--           用户类：创建用户、删除用户、给用户权限
--           库操作：创建库、删除库
--           表操作： 创建表、删除表
--           数据操作：增、删、改、查
--      3、权限表：
--      查看权限表： use mysql;
--                 select * from user where user='root'\G;
--            查看自己的权限：show grants;
--            查看别人的权限：show grants for 'Tom'@'localhost';
--          user：最重要的权限表，记录了允许连接到服务器的用户即具有的权限
--          db：记录库的授权信息
--                 select * from db where user='jerry'\G;
--          tables_priv：记录表达授权信息
--          columns_priv:记录字段的授权信息
--          with grant option 允许向其他用户授权
--      授权语法：grant 权限列表  on 库名称.表名称
--              to ‘用户名’ @ ‘客户端地址’
--               [identified by '密码']
--               [with grant option]
--         说明：
--            权限列表：被授权用户拥有哪些权限
--               all privileges：所有权限
--               select，insert，update：分别指定权限
--           库名称.表名称
--                *.*      为所有库、所有表授权 
--                bank.*   表示bank 库下所有表
--               bank.acct 特质bank库下的acct表
--           客户端地址：
--                   %       表示所有客户端
--               localhost   表示本机
--               192.168.1.5 表示制定192.168.1.5这台机器
--        示例： 
        --    给Daniel 用户授予所有库、所有表的所有权限，并且将密码设置为"123456"
        --    允许该用户向其他用户授权
        --    grant all privileges on *.*
        --    to 'Daniel'@'%'
        --    identified by '123456'
        --    with grant option;
        --   执行成功后，重新加载权限设置生效：
        --       flush privileges
        --   重新Daniel用户登录验证：
        --       mysql -uDaniel -p123456
--      示例：
           -- 给Tom用户授权，能对所有库、所有表进行查询，限定只能从本机登录并将密码设置为‘123456’
           -- grant select on *.*
           -- to 'Tom'@'localhost'
           -- identified by '123456';
           --
--   课堂练习：
--       给用户jerry授权，只能访问bank库下的表，能够对该库的所有表实现增、删、改、查
--         （insert，delete，update，select）
        grant insert,delete,update,select on bank.* to 'jerry'@'%' identified by '123456';
--      查询jerr的权限：select * from db where user='jerry'\G;
-- 查看自己的权限：show grants;
-- 查看其他用户的权限(用户权限足够高)：show grants for 'Tom'@'localhost';

-- 吊销权限
     -- revoke 权限列表 on 库名.表名
     -- from '用户'@'客户地址'
-- 示例：吊销Jerry 用户bank库下的delete权限
--      revoke delete on bank.* from 'jerry'@'%'


-- 数据库事物  （重点）
   --   什么是事物：数据库的一系列操作要么全都执行。要么全都不执行
   --  作用：保证数据一致性、正确性
   --  例如： 001向002账户转1000元钱
         -- 001减去1000元
         -- 002加上100元
    -- 使用事物的场景
    --    对数据进行修改
    --    如果修改成功，则提交事物，失败则回滚，所有修改都被撤销
  -- MySQL中，启用事物的表必须是InnoDB存储引擎
--事物特征：ACID特征
     -- 原子性（Atomicity）：事物是个一个整体，要么全都执行，要么全都不执行，控制事物的一致性
     -- 一致性（Consistency）：强调状态，事物执行完成后，从一个一致性状态，变成另一个一致性状态
     -- 隔离性（Isolation）：事物之间不相互影响、干扰
     -- 持久性（Durability）：事物一旦提交，对数据库的修改，就必须持久保存
--  mysql中操作事物
   --   启动：start transaction
   --   提交：commit
   --   回滚：rollback
     --示例：利用事物控制转账操作
    -- 1、开始事物：
    --    start transaction;
    -- 2、修改转出账户余额
     --   update acct set balance =balance +1000 where acct_no='13668498248'
    -- 3、修改转入账户余额
     --   update acct set balance =balance -1000 where acct_no='62551122200'
    -- 4、提交事物
     -- commit     --提交
    -- 第一次，四个步骤全部执行
    -- 第二次，执行前两个步骤，然后rollback回滚，第二步修改的数据会被取消，
         -- 在回滚前，登录一个客户端查询数据
    --  rollback  --回滚
 

-- 课堂练习：
--   使用eshop库，
--  1、利用子查询，查询索引订单状态为‘申请退货’的客户的名称、电话号码
select  cust_name,cust_tel from customer_new 
where cust_id in(select  cust_id from orders where status='5');
--  2、利用连接查询，查询状态为‘待送货’订单信息

select  
orders.order_id,
orders.order_dtae,
orders.cust_id,
customer_new.cust_tel,
customer_new.address
from customer_new right join  orders on customer_new.cust_id=orders.cust_id where status='3';

-----有误 select  
-- orders.order_id,
-- orders.order_dtae,
-- orders.cust_id,
-- customer_new.cust_tel,
-- customer_new.address
-- from customer_new orders where status='3' and customer_new.cust_id=orders.cust_id;
--     查询结果包含的字段有：订单编号  下单时间  客户编号  客户电话  送货地址
--  3、创建eshop_admin用户，并授权：
     --  eshop库的所有表、所有权限
     -- 允许从任意客户端登录
     -- 设置密码
     grant all privileges on *.*
           to 'eshop_admin'@'%'
           identified by '123456'
           with grant option;
    -- 执行成功后，重新加载权限设置生效：
              flush privileges
        --   重新Daniel用户登录验证：
              mysql -uDaniel -p123456
--  4、创建eshop_user用户，并授权
--     eshop库的所有表的查询权限
     -- 允许从任意客户端登录
     -- 设置密码
     --给用户jerry授权，只能访问bank库下的表，能够对该库的所有表实现增、删、改、查
--         （insert，delete，update，select）
        grant select on eshop.* to 'eshop_user'@'%' identified by '123456';
    -- 执行成功后，重新加载权限设置生效：
              flush privileges
        --   重新Daniel用户登录验证：
              mysql -uDaniel -p123456
