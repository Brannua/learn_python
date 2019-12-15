# Learn python3 笔记

### 基本数据类型

- Number
  - int
  - float
  - bool 布尔类型: 表示真、假
    - True
    - False
  - complex 复数: 数字+j
    - eg. 复数36表示为 --> 36j
- str 字符串
  - 单引号
  - 双引号
  - 三引号( 三个单引号或者三个双引号适用于多行字符串 )
    - 两种多行输入的方式
    > 利用转义字符 \ 或使用三引号
    ```
    1. 'hello world\
        hello world\
        hello world'
    2. '''
        hello world
        hello world
        hello world
       '''
    ```

```
int(True) --> 1
int(False) --> 0
bool(1) --> True
bool(0) --> False
```

- 可以被bool()方法转化为False的有
  - 任何进制、任何精度的数字0
  - 空字符串、空列表[]、空元组{}
  - None

```
1/2 --> 0.5
1//2 --> 0
2/2 --> 1.0 --> type(2/2) --> float
2//2 --> 1 --> type(2//2) --> int
```
- tips
  - / 是除法,结果是float
  - // 是在除法的基础上做一步向下取整,结果是int

### 进制的表示和转换

```
2进制的2 --> 0b10
2进制的3 --> 0b11
8进制的8 --> 0o10
8进制的9 --> 0o11
16进制的16 --> 0x10
16进制的17 --> 0x11
```
```
@param 传入任何进制的数
@binary 返回的数是param的2进制表示
bin(param): binary
```
```
@param 传入任何进制的数
@binary 返回的数是param的8进制表示
oct(param): octonary
```
```
@param 传入任何进制的数
@binary 返回的数是param的10进制表示
int(param): integer
```
```
@param 传入任何进制的数
@binary 返回的数是param的16进制表示
hex(param): hexadecimal
```

### 普通字符串与原始字符串

- r + 普通字符串 == 原始字符串

```
'C:\\north\\northeast' == r'C:\north\northeast'
```

### 字符串的运算

```
"hello" * 3 == "hellohellohello"

"hello world"[0:5] == "hello"
"hello world"[0:-1] == "hello worl"
"hello world"[6:] == "world"
"hello world"[-5:] == "world"
```
