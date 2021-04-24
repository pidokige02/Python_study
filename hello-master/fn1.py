def fn():
	print("fn called")

def exp(x):
	return x ** 2

exp3 = exp(3)
print(exp3)

print(exp(9))

def get_fruits():
	return ['오렌지', '사과', '바나나']

print( get_fruits()[1] )

def get_name():
	return 'Kent', 'Beck'

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

name = get_name()
print( name, full_name('AAA', 'BBB') )


def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp) - 1])

var_param('AA', 'bbb', 'ccc')


def default_param(a, b = 'BBB'):
    print(a, b)

default_param('AAA')
default_param('AAA', 'bbbbbbbbbbb')
