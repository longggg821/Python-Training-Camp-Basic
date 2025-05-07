"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 请在下方编写代码
##    l=[]
##    if operation=='union':
##        l=set1
##        for v in set2:
##            l.add(v)
##    elif operation=='intersection':
##        for v in set1:
##            if v in set2:
##                l.append(v)
##    else:
##        for v in set1:
##            if v not in set2:
##                l.append(v)
##    print(l)
##    return l
    if operation=='union':
        return set1 | set2
    elif operation=='intersection':
        return set1 & set2
    else:
        return set1 - set2
if __name__=='__main__':
    math_club = {"张三", "李四", "王五"}
    coding_club = {"李四", "王五", "赵六"}
    result = student_set_operations(math_club, coding_club, "intersection")
    print(result)

