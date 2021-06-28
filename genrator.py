# #def fab(n):
#  #   for i in range(n):
#   #      yield i**2
# a=[1,5,8,9]

# num = list(i**2 for i in a)
# b=list(num)
# #print(type(num))
# print(b)

my_num=[1,5,6,7]
# lambda_cube = lambda x,y: x+y
# print(lambda_cube(2,5))

a=list(map(lambda num:num**2,my_num))
print(a)