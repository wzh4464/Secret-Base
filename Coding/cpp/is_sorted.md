---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# 理解 C++ 中的 std::is_sorted

## 简介

`std::is_sorted` 是 STL 算法库中用于检查一个元素范围是否有序的函数。它在 C++11 中引入，定义在 `<algorithm>` 头文件中。

## 函数签名

```cpp
// (1) 使用默认的 operator< 进行比较
template <class ForwardIt>
bool is_sorted(ForwardIt first, ForwardIt last);

// (2) 使用自定义比较函数
template <class ForwardIt, class Compare>
bool is_sorted(ForwardIt first, ForwardIt last, Compare comp);
```

## 比较函数的要求

用于 `is_sorted` 的比较函数必须建立严格弱序（strict weak ordering）。这意味着它必须满足以下性质：

1. **不自反性**：`comp(x, x)` 必须为 false
2. **反对称性**：如果 `comp(x, y)` 为 true，那么 `comp(y, x)` 必须为 false
3. **传递性**：如果 `comp(x, y)` 和 `comp(y, z)` 为 true，那么 `comp(x, z)` 必须为 true

### 常见错误

1. 使用 `<=` 而不是 `<`：

```cpp
// 错误
is_sorted(v.begin(), v.end(), [](int a, int b) { return a <= b; });

// 正确
is_sorted(v.begin(), v.end(), [](int a, int b) { return a < b; });
```

2. 不满足传递性：

```cpp
// 错误：浮点数比较破坏了传递性
is_sorted(v.begin(), v.end(), [](double a, double b) { 
    return std::abs(a - b) < 0.0001 || a < b; 
});

// 正确
is_sorted(v.begin(), v.end(), [](double a, double b) { return a < b; });
```

## Grid Challenge 示例

在 grid challenge 问题中，正确使用 `is_sorted` 的方式如下：

```cpp
bool isColumnSorted(const vector<string>& grid, size_t col) {
    return is_sorted(grid.begin(), grid.end(),
        [col](const string& a, const string& b) {
            return a[col] < b[col];  // 使用 < 确保严格弱序
        });
}

string gridChallenge(vector<string> grid) {
    if (grid.empty()) return "YES";
    
    // 对每行排序
    for(auto& row : grid) {
        sort(row.begin(), row.end());
    }
    
    // 检查每列是否有序
    for(size_t col = 0; col < grid[0].size(); col++) {
        if (!isColumnSorted(grid, col)) {
            return "NO";
        }
    }
    
    return "YES";
}
```

## 性能考虑

- 时间复杂度：O(n)，其中 n 是范围中的元素个数
- 空间复杂度：O(1)

## 最佳实践

1. 在比较函数中始终使用 `<` 而不是 `<=`
2. 确保比较函数的一致性和传递性
3. 如果需要找出排序在哪里被破坏，考虑使用 `std::is_sorted_until`
4. 测试边界情况，特别是使用自定义比较器时

## 常见用例

1. 验证排序结果：

```cpp
vector<int> v = {1, 2, 3, 4, 5};
assert(is_sorted(v.begin(), v.end()));
```

2. 自定义对象排序：

```cpp
struct Person {
    string name;
    int age;
};

vector<Person> people;
bool isSortedByAge = is_sorted(people.begin(), people.end(),
    [](const Person& a, const Person& b) { return a.age < b.age; });
```

3. 部分范围检查：

```cpp
// 检查前半部分是否有序
bool firstHalfSorted = is_sorted(v.begin(), v.begin() + v.size()/2);
```

## 调试技巧

当 `is_sorted` 返回意外结果时：

1. 打印序列以验证输入
2. 单独测试比较函数
3. 检查边界情况，如空范围
4. 验证比较函数是否维持严格弱序
5. 使用 `is_sorted_until` 找出排序在哪里被破坏

重要提示：正确实现的比较函数对于 `is_sorted` 的正常工作至关重要。始终确保它建立严格弱序。
