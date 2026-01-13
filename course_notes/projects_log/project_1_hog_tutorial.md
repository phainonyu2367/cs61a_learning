## assert(断言)

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。

```
assert expression
```
等价于
```
if not expression:
    raise AssertionError
```

```
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
```

## *parameters
在python中，我们调用的时候可以使用`*parameters`来传入实参，这个符号会将传递进来的数据打包成一个tuple

`**`会打包成一个字典
```
def myprint(**params):
   print(params)
myprint(x=1, y=2, z=3) # 输出: {'x': 1, 'y': 2, 'z': 3}
```

## nonlocal
相当于c++中的extern