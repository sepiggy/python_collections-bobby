from collections import namedtuple

# namedtuple 的应用: 将 user 表的数据全部取出然后加一个列
User = namedtuple('User', ['name', 'age', 'height', 'edu'])

user_tuple = ('bobby', 29, 175)
user_dict = {
    'name': 'bobby',
    'age': 29,
    'height': 175,
}

# 向 namedtuple 传参可以使用 tuple 和 dict 两种方式
#  user = User(*user_tuple, 'master')
user = User(**user_dict, edu='master')
print(user.age, user.name, user.height, user.edu)

# 转为 dict
user_info_dict = user._asdict()
print(user_info_dict)
