

# 1. Function no parameters and no return the result
def fn_no_args_and_no_return():
    print('This is a function without any arguments and no return any results.')

fn_no_args_and_no_return()

# 2. Function no parameters but return the result
def fn_no_args_and_return():
    return 'This is a function without any arguments but return the result'

result = fn_no_args_and_return()
print(fn_no_args_and_return())

# 3. Function with parameters args (arguments), kwargs (keyword arguments)
# 3.1 Function with only parameters (args) and no return any result
def fn_only_args_and_no_return(arg1 , arg2): # bat buoc phai 2 tham so
    print("arg1: " + arg1)
    print("arg2: " + arg2)

fn_only_args_and_no_return("test1", "test2") # tham so truyen vao theo thu tu
fn_only_args_and_no_return(arg1="test3", arg2="test4") # ko quan tam tham so truyen vao thu tu
fn_only_args_and_no_return(arg2="test5", arg1="test6") # ko quan tam tham so truyen vao thu tu

# 3.2 Function with only parameters (args) and return the result
def fn_only_args_and_return(arg1 , arg2): # bat buoc phai 2 tham so
    print("arg1: " + arg1)
    print("arg2: " + arg2)
    return arg1 + " : " + arg2

result1 = fn_only_args_and_return("test1", "test2")
print(result1)
result2 = fn_only_args_and_return(arg1="test3", arg2="test4")
print(result2)
result3 = fn_only_args_and_return(arg1="test5", arg2="test6")
print(result3)

# 3.3 Function with only parameters (args) and no return any results
def fn_only_args_with_star_sign_and_no_return(*args): # Co hoac ko co tham so truyen vao
    print(type(args))
    print(args)

fn_only_args_with_star_sign_and_no_return()
fn_only_args_with_star_sign_and_no_return("test1", "test2")

# 3.4 Function with only parameters (kwargs) and return the result
def fn_only_kwargs_and_no_return(arg1="default1" , arg2="default2"): # bat buoc phai 2 tham so
    print("arg1: " + arg1)
    print("arg2: " + arg2)

fn_only_kwargs_and_no_return()
fn_only_kwargs_and_no_return(arg1="test1", arg2="test2")
fn_only_kwargs_and_no_return(arg1="new test")

# 3.5 Function with only parameters (kwargs) and return the result
def fn_only_kwargs_and_return(arg1 , arg2): # bat buoc phai 2 tham so
    print("arg1: " + arg1)
    print("arg2: " + arg2)
    return arg1 + " : " + arg2

result1 = fn_only_kwargs_and_no_return()
print(result1)
result2 = fn_only_kwargs_and_no_return(arg1="test1", arg2="test2")
print(result2)
result3 = fn_only_kwargs_and_no_return(arg1="new test")
print(result3)

# 3.6 Function with only parameters (kwargs) and no return any results
def fn_only_kwargs_with_star_sign_and_no_return(**kwargs): # Co hoac ko co tham so truyen vao
    print(type(kwargs))
    print(kwargs)

fn_only_kwargs_with_star_sign_and_no_return()
fn_only_kwargs_with_star_sign_and_no_return(a=1, b=2, c=3)

# 4. Function with paramters and returned result
# 4.1 Function with only parameters (kwargs) and return the result
def fn_args_and_kwargs_with_star_sign_and_no_return(*args, **kwargs): # Co hoac ko co tham so truyen vao
    print(type(args))
    print(type(kwargs))

fn_args_and_kwargs_with_star_sign_and_no_return()
fn_args_and_kwargs_with_star_sign_and_no_return(1, 2, a=3, b=4)

# 4.2 Function with only parameters (kwargs) and return the result
def fn_args_and_kwargs_with_star_sign_and_return(*args, **kwargs): # Co hoac ko co tham so truyen vao
    print(type(args))
    print(type(kwargs))
    return (args, kwargs)

result1 = fn_args_and_kwargs_with_star_sign_and_return()
print(result1)
result2 = fn_args_and_kwargs_with_star_sign_and_return(3, 4, a=5, b=6)
print(result2)
