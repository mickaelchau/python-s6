dic1={1:10, 4:40}
dic2={3:30, 2:20}

dic_res = dict(dic1)
dic_res.update(dic2)

print(sorted(dic_res.items(), key = lambda x:x[0]))

