dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic_res = dict(dic1)
dic_res.update(dic2)
dic_res.update(dic3)
print(dic_res)