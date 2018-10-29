
# def fun1(n):
#     for i,m in n.items():
#         m = str(m)
#         if len(m) > 2:
#             n[i] = m[0:2]
#     print(n)
dic = {'name':'fanfan','sex':'boy'}
# fun1(dic)

for i,m in dic.items():
    if len(m) > 2:
        dic[i]=m[0:2]
    print(dic)