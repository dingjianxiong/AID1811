# 自我介绍
#   魏明择
#     01年 参加工作 国企
#     02年 PLC
#     04年 文曲星
#     05-08年 诺亚舟
#     08-12年 医疗电子
#     12年 IT教育
#   联系方式：
#     Email: weimz@tedu.cn
#       班号 + 地址 + 姓名:
#       aid1811 上海 魏明择





# 三大操作系统:
#   UNIX
#     AIX(IBM)
#     Mac OS X (Apple)
#     IOS (Apple 移动端)
#   Linux
#     Ubuntu(免费)
#     Redhat(收费)
#     CentOS
#     Android(安卓)
#   Windows
#     Win3.1
#     Win3.2
#     Win98
#     ...
#     Win10

# 计算机的组成
#   硬件
#     处理器(CPU)
#     运行内存(RAM)
#     主板(总线设备)
#     输入输出设备(显示屏，键盘，鼠标)
#     外部存储设置(硬盘, U盘)
#   软件
#     操作系统软件:
#       Windows, Linux, UNIX
#     应作软件:
#       QQ, 微信



# vmware
#   启动（双击图标，点击启动)

# Ubuntu 开机密码: tarena

# vmware 快捷键
#   ctrl + alt   释放鼠标光标
#   ctrl + alt + enter   全屏/退出全屏

# Linux 简介:
#   1991年 发布第一个公开的版本0.02版

# Linux的基本结构
#   1. 应用程序
#   2. 标准库
#   3. Linux内核
#   4. 硬件

# 终端工具:
#   打开方法:
#     1. 点击图标
#     2. 搜索命令
#       gnome-terminal
#       终端
#   退出终端方法:
#     $ exit
#     ctrl + d 快捷键


# Linux 命令
#   让计算机做事情的指令

# Linux 命令行格式:
#   命令名 [选项]  [参数]
#   注: [] 代表里面的内容可选
  
#   如:
#     $ ls
#     $ ls -l 
#     $ ls -l /home/tarena
#     $ pwd
#     $ cd /

# 文件和目录相关的命令
#   文件是用来存储数据的单位
#   目录是用来管理和分类文件的单位

# pwd 命令
#   作用:
#     用于显示当前操作的路径（当前工作目录)
#   示例:
#     $ pwd
#     /home/tarena

# ls 命令
#   作用:
#     显示指定目录的文件或文件夹信息
#   格式:
#     ls [选项] [文件夹名/文件名]
#   常用选项:
#     -l 列表显示文件的详细信息
#     -a 显示全部文件/文件夹(显示以.开头的文件)
#   如:
#     ls
#     ls -l
#     ls -a
#     ls -la /home/tarena
#     ls /etc
#   注:
#     linux/UNIX下以.开头的文件和文件为默认为隐藏文件
  

# Linux 下的路径
#   目录树
#     目录结构都为树形结构(目录树)
#   路径 Path
#     路径是用来记录一个文件或文件夹的字符串
#      如:
#        /home/tarena
#        /home/tarena/2.txt
#        aid1811/linux/day01.txt
#   根 /  (root)

# 路径分为两种:
#   绝对路径
#   相对路径
# 绝对路径:
#   以 / 字符开头的路径为绝对路径
#     如:
#       /home/tarena/aid1811/linux
#       /etc/passwd
# 相对路径:
#   不以 / 字符开头的路径为相对路径
#   相对是指相对于当前的工作目录（即 pwd 命令显示的目录）

#   开始符号
#     文件名或文件夹名称
#     .   当前文件夹(目录)
#     ..  上一级文件夹(目录)
#     ~   用户主目录(家目录)
#   如:
#     ls -l ../../etc/passwd
#     ls aid1811
#     ls -l ~

# 用户主目录(家目录)  ~
#   用户主目录是指操作系统为每个用户创建，由用户所拥有的目录
#   ~ 代表用户主目录
#     当前用户的用户主目录为:
#       /home/tarena
#       即: 
#         ls ~ 
#         等同于:
#         ls /home/tarena



# cd 命令:
#   用于改变当前的工作目录(进入某个目录)
#   格式:
#     cd [目录名]
#   如:
#     cd /home/tarena
#     cd /
#     cd     # 切换到用户主文件夹
#     cd ..  # 进入上一级目录
#     cd ~   # 进入用户主目录
#     cd -  切换到进入这个文件夹之前的文件夹

# mkdir 命令
#   创建一个或多个文件夹
#   如:
#     mkdir dir1 dir2 dir3    # 多个文件夹用空格隔开 
# rmdir 命令:
#   删除一个或多个文件夹
#   如:
#     rmdir dir1 dir2 dir3
#   注:
#     用rmdir 删除文件夹时，文件夹内必须为空


# touch 命令:
#   作用:
#     1. 如果文件不存在，则创建一个空文件(长度为0字节的文件)
#     2. 如果文件或目录存在，则用系统时间更新它的修改时间
#   格式:
#     touch 文件名
#   示例:
#     touch newfile

# rm 命令
#   删除文件或者文件夹
#   格式:
#     rm [选项] 文件或文件夹
#   常用选项
#     -r 递归删除文件夹内部的文件和文件夹
#     -i 删除前给出提示(y代表yes, n代表no)
#     -f 强制删除，不给任何提示
#   示例:
#     rm a b c d
#     rm -i aaaa.txt
#     rm -r 文件夹


# 练习:
#   在用户主目录下创建
#     1. 创建文件夹 aid1811
#     2. 在aid1811内创建文件夹linux
#     3. 在linux文件夹下创建 python.txt AI.txt ai.txt
#     4. 删除 python.txt
#   实现方法:
#     1. 创建文件夹 aid1811
#       $ cd ~
#       $ mkdir aid1811  # 或 mkdir /home/tarena/aid1811
#     2. 在aid1811内创建文件夹linux
#       $ cd aid1811
#       $ mkdir linux
#     3. 在linux文件夹下创建 python.txt AI.txt ai.txt
#       $ cd linux
#       $ touch python.txt AI.txt ai.txt
#     4. 删除 python.txt
#       $ rm python.txt
    
# 命令的 --help 选项
#   用于显录命令的帮助信息
#   格式:
#     命令名 --help
#   如:
#     ls --help

# man 命令帮助
#   格式:
#     man linux/UNIX命令名
#   作用:
#     查看命令的对应的帮助手册
#   退出键:
#     q <退出>

# Tab 键
#   补全命令名称 或 路径

# 上下键
#   翻出以前执行过的命令

# ctrl + l
#   快速清屏,等同于clear命令



# 通配符:
#   *  代表0个或1个或多个任意字符
#   ?  代表1个任意字符
#   示例:
#     假设有文件:
#       a ab ac abc aabb bc cd
#     rm a*  # 等同于 rm a ab ac abc aabb
#     rm a?  # 等同于 rm ab ac


# cp 命令
#   作用:
#     复制文件或文件夹
#   格式:
#     cp [选项]  源文件或文件夹  目标文件或文件夹
#   常用选项:
#     -a 复制文件夹里的内容

# mv 命令
#   作用:
#     文件的搬移或者更名
#   格式:
#     mv 源文件或文件夹  目标文件或文件夹

# find 查找命令
#   作用:
#     根据文件名等 信息查找指定的文件
#   格式:
#     find 路径 -name "文件名"
#   如:
#     find /etc -name passwd

# grep 命令
#   作用:
#     查找文件中的相应的内容及文本信息
#   格式:
#     grep "内容" [选项] 文件名或路径
#   常用选项:
#     -n 显示行号
#     -r 递归搜索文件夹内的文件
#   示例:
#     查找 /etc下有哪儿个文件里有tedu 这串文字
#     $ grep "tedu" -nr /etc


# gzip 命令
#   作用:
#     用zip压缩算法对文件进行压缩， 生成压缩后的.gz 文件
#   命令格式:
#     gzip 文件名
#   压缩后的文件名通常为 .gz 文件
# gunzip 命令
#   作用:
#     与gzip相反,对用zip压缩算法压缩的文件进行解压缩
#   格式:
#     gunzip 文件名
# 示例:
#   $ gzip a.txt
#   $ ls 
#   $ gunzip a.txt.gz
  