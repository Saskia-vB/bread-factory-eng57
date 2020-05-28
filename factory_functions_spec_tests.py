# define the tests before we code the functions
from factory_functions import *

# make_dough()
## test 1 - make_dough()
print("When make_dough is called with 'water' and 'flour' it should return 'dough'")
print(make_dough('water','flour')=='dough')
print('got:', make_dough('water','flour'))

## test 2 - make_dough()
print("When make_dough is called with 'water' and 'cement' it should return 'not dough'")
print(make_dough('water','cement')== 'not dough')
print('got:', make_dough('water','cement'))

# bake_bread()
## test 1 - bake_bread()
print("When make_dough is 'baked' it should return 'bread baked'")
print(bake_bread('baked')=='bread baked')
print('got:', bake_bread('baked'))

## test 2 - bake_bread()
print("When make_dough is 'not baked' it should return 'bread not baked'")
print(bake_bread('not baked')=='bread not baked')
print('got:', bake_bread('not baked'))



# wholewheat - effective use of factory and new markets
## test 1 - wholewheat
print("When wholewheat is called with 'water' and 'wholewheat flour' it should return 'factory downtime more effective and new markets'")
print(wholewheat('water','wholewheat flour')=='factory downtime more effective and new markets')
print('got:', wholewheat('water', 'wholewheat flour'))

## test 2 - wholewheat
print("When wholewheat is called with 'water' and 'flour' it should return  'factory downtime not more effective and no new markets'")
print(wholewheat('water','flour')=='factory downtime not more effective and no new markets')
print('got:', wholewheat('water', 'flour'))



# wholewheat_sell - sell to niche clients
## test 1 - sell to niche clients
print("When wholewheat is 'baked' it should return 'sell to niche clients'")
print(wholewheat_sell('baked')=='sell to niche clients')
print('got:', wholewheat_sell('baked'))

## test 2 - sell to niche clients
print("When wholewheat is 'not baked' it should return 'cannot sell to niche clients'")
print(wholewheat_sell('not baked')=='cannot sell to niche clients')
print('got:', wholewheat_sell('not baked'))