#账户管理系统，实现账户增删改查
import pymysql


db_conn=None#连接对象
def conn_database():#连接数据库
    global db_conn
    try:
        host=input("请输入服务器地址:"),'服务器地址输入错误'
        # host='localhost'  #服务器地址
        user=input("请输入用户名:"),'未找到用户名'
        # user='root'       #登录用户名
        password=input("请输入密码:"),'密码输入错误'
        # password='123456' #登录密码
        dbname=input("请输入指定数据库:")
        # dbname='bank'     #指定数据库
    except Exception as e:
        print("请重新输入")
        print(e)
    db_conn=pymysql.connect(host,user,password,dbname)
    sql='''select * from '''
    if not db_conn:
        print("连接数据库失败")
        return -1
    else:#连接成功
        return 0








def close_database():
    global db_conn
    if db_conn:#判断对象是否为空
        db_conn.close()
def print_menu():#打印菜单
    menu='''
    --------------账户管理系统-------------
        1- 查询账户信息
        2- 新建账户
        3- 修改账户
        4- 删除账户
        5- 提出
    '''
    print(menu)#打印菜单
    return

#查询账户,如果用户输入账号，则以账号为条件进行查询
#如果不输入，则查询所有账户
def query_acct():
    acct_no=input("请输入你要查询的账号：")
    if acct_no and acct_no!='':#用户输入了账户
        sql=''' select * from acct
                where acct_no='%s'
        ''' % acct_no
    else:#用户未输入账户，查询所有
        sql="select * from acct"
    #获取游标
    global db_conn
    cursor=db_conn.cursor()
    try:
        cursor.execute(sql)#执行sql语句
        result=cursor.fetchall()#获取所有数据
        for x in result:#遍历，打印
            acct_no=x[0]
            acct_name=x[1]#户名
            if x[6]:  #判断是否为空
                balance=float(x[6])  #余额
            else:
                balance=0.00#余额为空设置为0
            print('账户：%s,户名：%s,余额：%.2f'  %  (acct_no,acct_name,balance))
    except Exception as e:
        print("查询异常")
        print(e)

def new_acct():
    try:
        acct_no=input("请输入账号：")
        acct_name=input("请输入户名：")
        acct_type=input("请选择账户类型  1-借记卡  2-理财卡：")
        balance=float(input("请输入开户金额："))
        assert acct_type in ['1','2']#判断acct_type是否合法
        assert balance >=10.00#判断balance是否合法
        #拼装sql语句，执行插入
        sql = '''insert into acct(acct_no,acct_name,acct_type,balance)
        values('%s','%s','%s','%.2f')
        '''% (acct_no,acct_name,acct_type,balance)
        #获取游标，执行
        global db_conn
        cursor=db_conn.cursor()
        cursor.execute(sql)#执行
        db_conn.commit()#提交
        print("插入成功")

    except Exception as e:
        print("插入失败")
        print(e)
    return
def update_acct():
    try:
        acct_no=input("请输入修改的账户：")
        balance=float(input("请输入你修改的账户金额："))
        sql='''update acct set balance='%.2f'
        where acct_no='%s'
        '''% (balance,acct_no)
        global db_conn
        cursor=db_conn.cursor()
        cursor.execute(sql)#执行
        db_conn.commit()#提交
        print("修改成功")
    except Exception as e:
        print("修改失败")
        print(e)
    return
def delete_acct():
    try:
        acct_no=input("请输入修改的账户：")
        sql='''delete from acct
        where acct_no='%s'
        '''% acct_no
        global db_conn
        cursor=db_conn.cursor()
        cursor.execute(sql)#执行
        db_conn.commit()#提交
        print("删除成功")
    except Exception as e:
        print("删除失败")
        print(e)
    return
#main
def main():
    #连接数据库
    if conn_database()<0:
        return
    #循环打印菜单，根据选择的菜单
    #调用不同的函数进行处理
    while True:
        print_menu()#打印菜单
        oper=input("请选择操作：")
        if not oper:#未输入值
            continue
        if oper=='1':#查询
            query_acct()
        elif oper=='2':#新建
            new_acct()
        elif oper=='3':#修改
            update_acct()
        elif oper=='4':#删除
            delete_acct()
        elif oper=='5':#退出
            break
        else:
            print("请输入正确的值")
            continue
    #关闭数据库
    close_database()
#主函数
if __name__=='__main__':
    main()