#  concatenate following dictionaries to create a new one. 

dic1={1:10,
      2:20} 
dic2={3:30,
      4:40} 
dic3={5:50,
      6:60} 

# using | operator 
dic = dic1 | dic2 | dic3
print(dic)

# using update 
dic = {}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)
print(dic)

# using dictionary unpacking **
dic = {**dic1,**dic2,**dic3}
print(dic)