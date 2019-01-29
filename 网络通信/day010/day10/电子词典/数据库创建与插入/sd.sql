-- 进入数据库
mysql -hlocalhost -uroot -p123456
-- 创建数据库dict
create database dict;
--　使用数据库
use dict;
--　创建单词表结构
create table worlds(
    id int primary key auto_increment,
    world varchar(128) not null,
    interpret text
)default charset=utf8;

-- 创建用户信息表
create table users(
    id varchar(32) primary key,
    name varchar(32) not null,
    password varchar(32) not null
)default charset=utf8;

-- 创建历史记录表
create table history(
    id varchar(32) primary key,
    name varchar(32) unique,
    world varchar(128) not null,
    time datetime not null
)default charset=utf8;
-- 修改类型
alter table users modify id int auto_increment;
alter table users modify password varchar(32) default '000000';

alter table worlds modify id int auto_increment;

