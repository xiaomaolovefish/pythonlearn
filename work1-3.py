#encoding='utf-8'
#��ҵһ
#1
print 'name:ZhiPing Li'
#2
print 'h=a+b*c-d/e'
#3
print '..........\r',
print '555555555'
#4
print '..........\n 555555555'

#��ҵ��
weight=input('please input weight(kg):' )
height=input('please input height(m):' )
BMI=weight/(height*height)
if BMI < 18.5:
    print '����ƫ��'
if 18.5<= BMI < 24:
        print '��������'
if BMI >=24:
    print '����ƫ��'
    


#work3
import random
#�����˿����б�
items = [m+str(n)  for m in 'RBPD' for n in range(13)]
items.append('red Joker')
items.append('black Joker')
#ϴ��
random.shuffle(items)

def poker(items):
    A=random.sample(items,17)
    print(A)
    ret = list(set(items) ^ set(A))
    return(ret)
if __name__ == '__main__':
    ret = poker(items)
    retb = poker(ret)
    retc = poker(retb)
    print(retc)

