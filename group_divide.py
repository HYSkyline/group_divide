# -*- coding:utf-8 -*-
import sys
import random

reload(sys)			# 重新载入sys模块
sys.setdefaultencoding("utf-8")			# 设置程序运行环境编码为utf-8


class Group_Divide:			# 以此次分组任务作为对象
    def __init__(self, mission_name, fpath, groupnum):			# 初始化对象
        self.mission_name = mission_name			# 设置对象名称
        self.fpath = fpath			# 人员名单文件所在路径
        self.groupnum = groupnum			# 需要分组的数量

        self.chiefdic = {}			# 组长所在字典，存储姓名与随机值
        self.memberdic = {}			# 组员所在字典，存储姓名与随机值

    def readlist(self):			# 读取人员名单，并按类别置入字典
        f = open(self.fpath, "r")			# 打开人员名单文件
        contents = f.readlines()			# 读取文件内容(内容形式为"XXX\t0\n"，其中XXX为名称，0/1为组员/组长)
        f.close()			# 断开人员名单文件连接
        self.personnum = len(contents)			# 确定总人数

        for each in contents:				# 对文件内容进行解析，并置入字典
            name, kind = each.split("\t")			# 按换行符分割姓名与类别
            name = name.decode('gbk')			# 姓名变量的编码转换
            kind = kind[:-1]				# 舍去类别变量后的换行符
            random_check = random.random()			# 计算随机值
            if kind == "1":			# 如果类别为1——即为组长
                self.chiefdic[name] = random_check			# 将当前姓名置入组长所在字典
            elif kind == "0":			# 如果类别为0——即为组员
                self.memberdic[name] = random_check			# 将当前姓名置入组员所在字典

        if self.chiefdic:			# 人员名单中含类别区分，即设置组长
            self.groupnum = len(self.chiefdic)			# 按组长的数量重新计算分组数

    def divide(self):			# 按照赋予的随机值进行排序，并返回分组结果
        self.grouplist = [[] for i in range(0, self.groupnum)]			# 初始化名单为二元列表，第一元为分组，第二元为分人员
        if self.chiefdic:			# 如果存在组长设定
            chiefdic_sort = sorted(self.chiefdic.items(), key=lambda ads:ads[1], reverse=False)			# 按各组长的随机值进行升序排列
            for i in range(0, self.groupnum):			# 按照分组数量将组长名称置入每个第二元列表的首个位置
                self.grouplist[i].append(chiefdic_sort[i][0])			# 组长姓名置入每个第二元列表的首位
        memberdic_sort = sorted(self.memberdic.items(), key=lambda ads:ads[1], reverse=False)			# 按各组员的随机值进行升序排列
        for i in range(0, len(self.memberdic)):			# 对组员进行遍历
            self.grouplist[i - (i / 8) * 8].append(memberdic_sort[i][0])			# 将组员姓名轮流置入不同组中

    def printlist(self):			# 输出分组结果
        self.readlist()			# 读入人员名单文件，并分类置入字典
        self.divide()			# 按照赋予的随机值进行排序，并返回分组结果

        for i in range(self.groupnum):			# 对分组列表的第一元列表进行遍历，即分组输出结果
            for ii in range(len(self.grouplist[i])):			# 对第二元列表中的人员进行遍历
                if ii == 0:			# 第二元列表的首位
                    print self.grouplist[i][ii]			# 输出组长姓名
                else:			# 第二元列表非首位
                    print "...." + self.grouplist[i][ii]			# 输出组员姓名

if __name__ == "__main__":			# 当前文件即为执行程序
    print "Link Start!"			# 开始连接！
    print "==" * 6			# 分割线
    mission_name = raw_input("项目名称:".decode("utf-8").encode("gbk"))			# 确定项目名称
    groupnum = raw_input("分组数量:".decode("utf-8").encode("gbk"))			# 输入要分组的数量
    fpath = raw_input("名单文件完整路径:".decode("utf-8").encode("gbk"))			# 输入人员名单文件的完整路径
    print "==" * 6			# 分割线
    group = Group_Divide(mission_name, fpath, int(groupnum))			# 实例化分组对象
    print "Mission name:" + group.mission_name			# 确认项目名称
    print "There are " + str(group.groupnum) + " groups to be divided."			# 确认分组数量
    print "==" * 6			# 分割线
    group.printlist()			# 输出分组结果
    print "==" * 6			# 分割线
    print "Link Logout."			# 断开连接
