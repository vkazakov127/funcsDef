# Function with default parameters
def print_params(a=1, b='Urban', c=True):
    print(a, b, c)
print('------- Function with default parameters')
print_params(a=100)
print_params(a='Apple')
print_params(c=('Butter', 'Milk', 'Cheese'))
print_params(b=25)
print_params(c=[1,2,3])
# ---------------------------
# Unpacking parameters
values_list = [365, 'Potato', ('Urban', 130, 'University')]
values_dict = {'a':'Bulgaria','b':3.14,'c':True}
print('------- Unpacking values_list')
print_params(*values_list)
print('------- Unpacking values_dict')
print_params(**values_dict)
# ---------------------------
# Unpacking and separate parameters
values_list_2 = [7, 'May']
print('------- Unpacking values_list_2')
print_params(*values_list_2, 42)