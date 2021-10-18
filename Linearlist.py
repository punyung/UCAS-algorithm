
# 红色波浪号一定要改，橙色也要改，绿色不用
# 首先
# 线性表：相同特性 数据元素的一个 有限的序列
# 只有一个表头，一个表尾，表头没有前驱，表尾没有后继；其余元素有且仅有一个前驱和一个后继
# 共有两种存储结构：顺序存储结构 & 链式存储结构
# py中的顺序表为list，建立空list时，系统会分配能容纳8个元素的存储区，执行插入操作时，系统就更换一个4倍大的存储区；
# 若增加4倍大的区域时，超过50000（阈值），则采用加一倍的方法
# py中的单链表需要用class创建类，再自己根据单链表的特性创建类属性，一个用于存放标识，一个用于存放数据

# 定义一个单链表的结点 (类）
class SingleNode(object):
    def __init__(self,item):
        self.item = item  # item 用于存放数据
        self.next = None  # next表示下一个节点的标识（信息）


class SingleLinkedList(object):
    def __init__(self): # self参数是类下面所有方法必须的参数，表示指向当前对象的指针
        self.head = None # 单链表中的头结点

# 单链表的操作
# 在单链表下面分别创建方法
# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# additem() 插入一个元素，插入位置并未提前指定
# remove(item) 删除节点
# search(item) 查找节点是否存在

    def is_empty(self):
        return self.head == None

    def length(self):
        cur = self.head # 刚开始指向头结点的对象，指向对象的首地址
        count = 0
        # 当指针指向尾结点时，point = 0
        while point != 0:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while point != 0:
        print (point.item)
        point = point.next
        print (" ")

    def add(self,item):
        node = SingleNode(item) # node是要插入的新元素
        node.next = self.head
        self.head = node

    def append(self,item):
        node = SingleNode(item)
        #
        if self.








