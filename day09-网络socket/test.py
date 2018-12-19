with open('quota') as f_quota:
    z = 0
    for i in f_quota:
        f_quota_line = i.strip().split('|')
        print(f_quota_line,type(f_quota_line))
        for i in f_quota_line:
            z+=int(i)
        print(z)