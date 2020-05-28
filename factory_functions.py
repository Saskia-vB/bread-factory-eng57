
def make_dough(ingredient1, ingredient2):
    # when given water and flour
        # return dough
    # else I want to return not dough
    print(ingredient1)
    if ingredient1 == 'water' and ingredient2 == 'flour':
        return 'dough'
    else:
        return 'not dough'


def bake_bread(dough):
    # when dough is baked
        #return bread baked
    #else return break not baked
    if dough=='baked':
        return 'bread baked'
    else:
        return 'bread not baked'



def wholewheat(ingredient1, ingredient2):
    # when given water and wholewheat flour
        # return wholewheat dough
    # else I want to return not wholewheat dough
    if ingredient1== 'water' and ingredient2=='wholewheat flour':
        return 'factory downtime more effective and new markets'
    else:
        return 'factory downtime not more effective and no new markets'

def wholewheat_sell(dough):
    # when dough baked
        # return sell to niche clients
    # else I want to return cannot sell to niche clients
    if dough=='baked':
        return 'sell to niche clients'
    else:
        return 'cannot sell to niche clients'
