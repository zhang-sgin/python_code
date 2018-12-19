# with open('quota') as f_quota:
#     z = 0
#     for i in f_quota:
#         f_quota_line = i.strip().split('a')
#         # print(f_quota_line,type(f_quota_line))
#         for i in f_quota_line:
#             i=int
#             print(i,type(i))
#             z= z + i
#         print(z,type(z))


import re
nums = []
with open('quota', 'r') as f:
    for s in re.findall(r'\d+', f.read()):
        nums.append(float(s))
print(sum(nums))