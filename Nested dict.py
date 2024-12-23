# how to adding key: values to the dictionary
#syntax of adding to the dictionary
#dict_name[key_name]=value
d={1:'a',2:'b',3:"c",4:'d'}
d[5],d[6]='e','f'
print(d)
#updating dictionary to value
a={1:"names",2:"classes",3:"subjects",4:"teachers"}
a[1]="students"
print(a)
# delete unwanted key from the dictionary
#syntax is
#del dict_name[key_name]
del a[1]
print(a)
#using nested-dict
mymovies = {
  "child1" : {
    "name" : "movie",
    "year" : 2023
  },
  "child2" : {
    "name" : "pushpa",
    "year" : 1986
  },
  "child3" : {
    "name" : "release",
    "year" : 2024
  }
}
print(mymovies)
