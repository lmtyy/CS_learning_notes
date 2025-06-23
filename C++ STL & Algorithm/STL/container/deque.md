# deque

在 C++ 中，`std::deque` 是双端队列，位于头文件 `<deque>` 中。它支持高效地在两端进行插入和删除操作，同时提供随机访问功能。以下是 `std::deque` 的常用操作：

---

### 1. **引入头文件与声明**
```cpp
#include <deque>
#include <iostream>

std::deque<int> dq;  // 声明一个整型双端队列
```

---

### 2. **常用操作**

#### 插入
- **`push_back(val)`**: 在队列尾部插入元素。
- **`push_front(val)`**: 在队列头部插入元素。

```cpp
dq.push_back(10);    // 队列: [10]
dq.push_front(20);   // 队列: [20, 10]
```

#### 删除
- **`pop_back()`**: 移除队列尾部的元素。
- **`pop_front()`**: 移除队列头部的元素。

```cpp
dq.pop_back();       // 队列: [20]
dq.pop_front();      // 队列: []
```

#### 访问元素
- **`front()`**: 返回队列头部元素。
- **`back()`**: 返回队列尾部元素。
- **`operator[]`** 或 **`at(index)`**: 按索引访问元素。

```cpp
dq.push_back(10);
dq.push_back(20);
std::cout << dq.front() << std::endl;  // 输出: 10
std::cout << dq.back() << std::endl;   // 输出: 20
std::cout << dq[1] << std::endl;       // 输出: 20
std::cout << dq.at(1) << std::endl;    // 输出: 20
```

---

### 3. **容量操作**
- **`empty()`**: 检查队列是否为空。
- **`size()`**: 返回队列中元素的数量。
- **`resize(n, val)`**: 调整队列大小，多余部分用 `val` 填充。

```cpp
std::cout << dq.empty() << std::endl;  // 输出: 0 (false)
std::cout << dq.size() << std::endl;   // 输出: 2
dq.resize(5, 42);                      // 队列: [10, 20, 42, 42, 42]
```

---

### 4. **插入与删除指定位置**
- **`insert(pos, val)`**: 在指定位置插入元素。
- **`erase(pos)`**: 删除指定位置的元素。
- **`clear()`**: 清空队列。

```cpp
auto it = dq.begin();      // 迭代器指向第一个元素
dq.insert(it + 1, 15);     // 队列: [10, 15, 20, 42, 42, 42]
dq.erase(it + 1);          // 队列: [10, 20, 42, 42, 42]
dq.clear();                // 队列为空
```

---

### 5. **迭代器操作**
- **`begin()`**: 返回指向队列首元素的迭代器。
- **`end()`**: 返回指向队列尾元素后一位置的迭代器。
- **`rbegin()` 和 `rend()`**: 返回反向迭代器。

```cpp
for (auto it = dq.begin(); it != dq.end(); ++it) {
    std::cout << *it << " ";
}
```

---

### 6. **双端操作的应用场景**
由于 `std::deque` 支持高效的双端插入和删除操作，常用于如下场景：
- 队列和栈操作。
- 滑动窗口问题。
- 数据需要频繁在两端操作的情形。

---

`std::deque` 是一个灵活的数据结构，结合其接口可轻松实现多种算法。
- deque和vector的操作基本一样 就多了操作头部的两个函数
- deque元素地址**不完全连续**