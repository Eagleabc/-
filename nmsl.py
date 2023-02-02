#！/usr/bin/env python3
#mac系统调用编译器

from Crypto.Cipher import AES
import time
import random
import codecs

a=random.randint(99999,999999)

def add_to_16(value):#补齐16
    value=value.encode("utf-8")
    while len(value) % 16 != 0:
        value += b'\0'
    return value  # 返回bytes

def add_to_16text(value):#补齐
    value=value.encode("gb2312")
    while len(value) % 16 != 0:
        value += b'\0'
    return value  # 返回bytes

def ifprime(m):#素数检测
    for i in range(2,int(m**(1/2))+1):
        if m % i == 0:
            return False
            break
    return True

while True:#生成随机素数，提供参考
    egg_p=random.randint(99,999999)
    if ifprime(egg_p)==True:
        break
       
print("请输入双方商定的素数p（尽可能大）  例如：",egg_p)#协商p与g,确定key
g=int(input())
p=int(input("请输入双方商定好的素数g（不用很大，10以内即可，如2，3，5，7，11，13，17......）"))
x=(p**a)%g
print("q=",x)
print("请告知对方生成数q")
q=int(input("请输入对方告知的生成数q"))
key=(q**a)%g

key=str(key)#密钥转化为字符串
key=add_to_16(key)#key补全部分
#print("debug",key)

aes = AES.new(key, AES.MODE_ECB)#加密函数创建

while True:#选择加密/解密部分及其代码
    type=str(input("加密还是解密 加密：0  解密：1 关闭软件：2"))
    if type !="0" and type != "1" and type != "2":
        print("请重新输入")
    elif type == "2":
        break
    elif type == "0":
        text=str(input("输入明文"))
        length=len(text.encode("utf-8"))
        text=add_to_16(text)
        secret = aes.encrypt(text)
        print("加密为：",secret,"长度：",length)
    elif type == "1":
        secret_other=bytes(input("输入密文")[2:-1],"utf-8")
        length_other=int(input("长度"))
        secret_other=codecs.escape_decode(secret_other, "hex-escape")
        #print("debug用，不用管",secret_other[0])
        #print("debug用，不用管",secret_other[0]==secret)
        text_other = aes.decrypt(secret_other[0])
        text_other=text_other[0:length_other]
        text_other=text_other.decode("utf-8","ignore")
        print("解密为",text_other)

print("感谢使用，10秒后自动关闭")
time.sleep(10)
    





