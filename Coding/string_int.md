---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# 字符串与整数转换

## C++

1. 字符串转整数：

```cpp
// string to int
string str = "123";
int num1 = std::stoi(str);        // throws std::invalid_argument 或 std::out_of_range
int num2 = std::atoi(str.c_str());  // 不安全，失败返回0
int num3;
std::istringstream(str) >> num3;   // 失败设置failbit

// string to long
long num4 = std::stol(str);       // string to long
long long num5 = std::stoll(str); // string to long long
```

2. 整数转字符串：

```cpp
int num = 123;
// to string
string str1 = std::to_string(num);
string str2 = std::format("{}", num);  // C++20

// 使用字符串流
std::ostringstream oss;
oss << num;
string str3 = oss.str();
```

## Python

1. 字符串转整数：

```python
# string to int
str_num = "123"
num1 = int(str_num)         # 基本转换
num2 = int(str_num, base=10)  # 指定进制
num3 = int("7b", base=16)     # 十六进制转换

# 异常处理
try:
    num = int("abc")
except ValueError:
    print("转换失败")
```

2. 整数转字符串：

```python
num = 123
# to string
str1 = str(num)           # 基本转换
str2 = f"{num}"          # f-string
str3 = "{}".format(num)  # format方法
str4 = hex(num)          # 转16进制字符串 '0x7b'
str5 = oct(num)          # 转8进制字符串  '0o173'
str6 = bin(num)          # 转2进制字符串  '0b1111011'
```

## 主要区别

1. 错误处理：
   - C++: 使用异常或返回值检查
   - Python: 主要使用异常处理

2. 进制转换：
   - C++: 需要使用 `std::stoi` 的第二个参数或使用 `std::stringstream`
   - Python: 使用 `int()` 的 `base` 参数或专门的函数（`hex()`, `oct()`, `bin()`）

3. 格式化：
   - C++: 使用 `to_string`、`stringstream` 或 C++20 的 `format`
   - Python: 提供多种方式：`str()`、f-string、`.format()`

4. 类型安全：
   - C++: 需要注意异常处理和溢出检查
   - Python: 整数没有大小限制，但需要注意 ValueError

5. 使用便利性：
   - C++: 相对复杂，需要更多错误处理
   - Python: 简单直观，内置类型转换函数

记住要根据具体需求选择合适的转换方法，特别是在处理错误情况和特殊格式时。
