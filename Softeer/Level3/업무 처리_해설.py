#!/usr/bin/env python
# coding: utf-8

# # H는 조직도 트리의 높이 (1 <= H <= 10)
# while True:
#     h = int(input("H는 조직도 트리의 높이 (1 <= H <= 10) : "))
#     
#     if 1<=h or h<=10:
#         break
#         
#     else:
#         print("범위가 틀렸습니다.\n")
#     
# # K는 직원 당 주어진 업무의 개수 (1 <= K <= 10)
# while True:
#     k = int(input("K는 직원 당 주어진 업무의 개수 (1 <= K <= 10) : "))
#     
#     if 1<=k or k<=10:
#         break
#         
#     else:
#         print("범위가 틀렸습니다.\n")
#         
#         
# # R은 업무 진행 일 수 (1 <= R <= 1000)
# while True:
#     r = int(input("R은 업무 진행 일 수 (1 <= R <= 1000) : "))
#     
#     if 1<=r or r<=1000:
#         break
#         
#     else:
#         print("범위가 틀렸습니다.\n")

# In[1]:


# 이진트리 구현
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
class BinaryTree():
    def __init__(self):
        self.root = None


# In[2]:


def get_tree(tree):
    # 부장님부터 트리 이어주기
    tree[0].left = tree[1]
    tree[0].right = tree[2]

    # 부하직원들 트리 이어주기
    get_tree = int(((total_emp-1) / 2) - 1) # 자식 트리가 있는 노드만 추출
    for p_tree in range(1, get_tree+1): # 부장님 제외 부하직원들
        #print(p_tree, end=' : ')
        #print(p_tree*2+1, p_tree*2+2)
        tree[p_tree].left = tree[p_tree*2+1]
        tree[p_tree].right = tree[p_tree*2+2]
        
    return tree


# In[3]:


# 트리 초기화
def init_tree():
    tree = [Node([0]) for i in range(total_emp)]
    tree = get_tree(tree)
    
    return tree


# In[4]:


h, k, r = map(int, input().split())


# In[5]:


print("\n#####\n")
print("조직도 트리 높이 h = {}".format(h))
print("직원 당 주어진 업무의 개수 k = {}".format(k))
print("업무 진행 일 수 r = {}".format(r))


# In[6]:


# 총 직원수 계산
total_emp = 1
emp_num = 1
for emp_layer in range(h):
    emp_num = emp_num*2  
    #print(emp_num)
    total_emp += emp_num
    
#print("부장님 포함 총 직원 수 :", total_emp)


# In[7]:


# 말단 직원 인원 수 = h * 2
employees = pow(2, h)

emp_total_works = list() # 2차원 배열로 업무 번호 저장
work_ = 0

tree = init_tree()
# 말단 직원 수 만큼 입력하기
for emps in range(employees-1, total_emp):
    #print("말단 직원 {}에게 업무 할당 시작(총 {}개 업무 줄 것)".format(emps, k), end=' ')
    emp_per_works = [*map(int,input().split())] # 직원 한 명에게 주어진 업무 (1차원 배열)
        
    tree[emps] = Node(emp_per_works)
    emp_total_works.append(emp_per_works)


# In[8]:


def get_work_left(emp_num):
    #print("{} 직원의 현재 업무 list : {}".format(emp_num, tree[emp_num].item), end=' / ')
    list_temp = tree[emp_num].item # 현재 직원의 수정 전 업무 복사
    
    if len(list_temp) == 0:
        list_temp = [0]  
    
    try: # 부하 직원이 있는 경우에만 작동
        next_work = tree[emp_num].left.item[0] # 왼쪽 직원이 처리한 업무 갖고오기
        list_temp.append(next_work) # 왼쪽 직원이 처리한 업무 추가
        
        if emp_num % 2 == 1:
            #print("!", end = ' ')
            del list_temp[0] # 이미 처리한 업무 삭제
            
        if len(list_temp) > 1 and list_temp[0] == 0:
            del list_temp[0]
            
    except: # 부하 직원이 없는 말단 직원인 경우에만 작동
        if emp_num % 2 == 1:
            del list_temp[0]
            
    tree[emp_num].item = list_temp
    #print("수정된 업무 list : {}".format(tree[emp_num].item))
    
    return tree[emp_num]


# In[9]:


def get_work_right(emp_num):
    #print("{} 직원의 현재 업무 list : {}".format(emp_num, tree[emp_num].item), end=' / ')
    list_temp = tree[emp_num].item # 현재 직원의 수정 전 업무 복사
    
    if len(list_temp) == 0:
        list_temp = [0]
    
    try: # 부하 직원이 있는 경우에만 작동
        next_work = tree[emp_num].right.item[0] # 오른쪽 직원이 처리한 업무 갖고오기
        list_temp.append(next_work) # 오른쪽 직원이 처리한 업무 추가
        
        if emp_num % 2 == 0:
            #print("!", end = ' ')
            del list_temp[0] # 이미 처리한 업무 삭제

        if len(list_temp) > 1 and list_temp[0] == 0:
            del list_temp[0]
            
    except: # 부하 직원이 없는 말단 직원인 경우에만 작동
        if emp_num % 2 == 0:
            del list_temp[0]
                    
    tree[emp_num].item = list_temp
    #print("수정된 업무 list : {}".format(tree[emp_num].item))
    
    return tree[emp_num]


# In[10]:


def finish_boss_work():
    #print(tree[0].item[0])
    if tree[0].item[0] != 0:
        del tree[0].item[0]
        
    if len(tree[0].item) == 0:
        tree[0].item = [0]
        
    return tree[0]


# In[11]:


def get_remove_zero(emp_num):
    list_temp = tree[emp_num].item
    #print(list_temp)
    if len(list_temp) > 1:
        while 0 in list_temp:
            list_temp.remove(0)
            
    if len(list_temp) == 0:
        list_temp = [0]

    #print(list_temp)
    tree[emp_num].item = list_temp
    return tree[emp_num]


# In[12]:


count = 0
count_prev = count
for days in range(2, r+1):
    tree = get_tree(tree)
    #print("\n#####\n")
    #print("day :", days)
    
    #print("오늘의 업무 확인")
    for emp_working in range(total_emp):
        tree[emp_working] = get_remove_zero(emp_working)
        #print("{} 직원의 현재 업무 : {}".format(emp_working, tree[emp_working].item))
        
    if days % 2 == 1: # 홀수 날에는 왼쪽 부하직원의 업무 처리
        #print("\n홀수 날에는 왼쪽 부하직원의 업무 처리")
        for emp_working in range(total_emp):
            tree[emp_working] = get_work_left(emp_working)

    elif days % 2 == 0: # 짝수 날에는 오른쪽 부하 직원의 업무 처리
        #print("\n짝수 날에는 오른쪽 부하 직원의 업무 처리")
        for emp_working in range(total_emp):
            tree[emp_working] = get_work_right(emp_working)

    # 처리한 업무 번호 구하기
    count += tree[0].item[0]
    #print("\n금일 부장님의 업무 처리 번호 : {}".format(tree[0].item))
    tree[0] = finish_boss_work()
    #print("완료된 업무 번호 총 합 : {}".format(count))
    #print()
    
    if count > 0:
        if count == count_prev:
            #print("더 이상 업무가 없습니다")
            break
    count_prev = count


# In[13]:


print(count)

