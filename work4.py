#encoding='utf-8'
#python 2.7.12
#��ҵ4
import random
n = input('please input people:' )
total = input('please input total:' )
money=total*100
length=money-n+1

#���������
def get_num(length,n):
  redpack=[random.randint(1, length) for i in range(n)]
  #print redpack
  return(redpack)


if __name__ == '__main__':
  
  redpack = get_num(length,n)
  act_money = sum(redpack)
  #�Ƚ������֮�����ܽ���Ƿ����
  while act_money != money :
    #����ȣ�ִ��ѭ��
    redpack = get_num(length,n)
    act_money = sum(redpack)
    if act_money == money :
      #��ȴ�ӡ�����
      print(redpack)
      print(sum(redpack))
      for item in redpack :
        #����������
        pack = item/float(100)
        pack='%.2f' %pack
        print pack
        #��ӡ���������ÿ�����ú�����
  




