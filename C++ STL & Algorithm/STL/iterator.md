# iterator
在 C++ 中，**迭代器（Iterator）** 是一种抽象工具，允许你遍历容器中的元素，同时不需要了解容器的底层实现。迭代器是 STL（标准模板库）的核心组件，广泛应用于容器的遍历、操作以及算法的输入。

以下是 C++ 中迭代器的详细介绍：

---

## **1. 迭代器的分类**

STL 中的迭代器分为五种类型，每种类型支持不同的操作：

| 迭代器类型         | 支持操作                           | 容器示例           |
|--------------------|------------------------------------|--------------------|
| **输入迭代器**      | 只读和单向遍历                      | 自定义输入流       |
| **输出迭代器**      | 只写和单向遍历                      | 自定义输出流       |
| **前向迭代器**      | 只读或只写，支持单向多次遍历          | `forward_list`    |
| **双向迭代器**      | 支持前后遍历                        | `list`, `set`      |
| **随机访问迭代器**   | 支持随机访问（+、-、索引访问）         | `vector`, `deque` |

---

## **2. 常见容器与迭代器类型**

| 容器           | 迭代器类型         |
|----------------|-------------------|
| `vector`       | 随机访问迭代器     |
| `deque`        | 随机访问迭代器     |
| `list`         | 双向迭代器         |
| `forward_list` | 前向迭代器         |
| `set`/`map`    | 双向迭代器         |
| `unordered_map`| 前向迭代器         |

---

## **3. 迭代器的基本操作**

### **(1) 常用方法**
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 定义迭代器
    std::vector<int>::iterator it;

    // 遍历元素
    for (it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " "; // 使用 * 解引用迭代器
    }
    std::cout << std::endl;

    // 使用 auto 简化写法
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

---

### **(2) 常用操作**

| 操作                     | 描述                                   |
|--------------------------|----------------------------------------|
| `begin()`                | 返回指向容器第一个元素的迭代器         |
| `end()`                  | 返回指向容器末尾后一个位置的迭代器     |
| `rbegin()` / `rend()`    | 返回逆向迭代器，用于反向遍历           |
| `cbegin()` / `cend()`    | 返回常量迭代器，不能修改元素           |
| `advance(it, n)`         | 将迭代器 `it` 向前移动 `n` 个位置      |
| `distance(it1, it2)`     | 返回 `it1` 和 `it2` 之间的距离         |

---

## **4. 示例操作**

### **(1) 遍历容器**
```cpp
#include <iostream>
#include <list>

int main() {
    std::list<int> lst = {10, 20, 30, 40};

    // 使用迭代器正向遍历
    for (auto it = lst.begin(); it != lst.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 使用反向迭代器遍历
    for (auto rit = lst.rbegin(); rit != lst.rend(); ++rit) {
        std::cout << *rit << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

输出：
```
10 20 30 40 
40 30 20 10 
```

---

### **(2) 插入和删除元素**
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 插入元素
    auto it = vec.begin() + 2;
    vec.insert(it, 10); // 在第三个位置插入 10

    // 删除元素
    vec.erase(vec.begin() + 1); // 删除第二个位置的元素

    for (const auto &val : vec) {
        std::cout << val << " ";
    }
    return 0;
}
```

输出：
```
1 10 3 4 5 
```

---

### **(3) 使用常量迭代器**
```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> s = {10, 20, 30};

    // 使用常量迭代器
    for (std::set<int>::const_iterator it = s.cbegin(); it != s.cend(); ++it) {
        std::cout << *it << " ";
    }

    return 0;
}
```

---

## **5. 迭代器的注意事项**

1. **失效问题（Iterator Invalidation）**：
   - `vector` 等动态数组容器在扩容或插入、删除操作时可能会导致迭代器失效。
     - 在动态数组扩容时 数组可能会整体搬迁 重新开辟内存
   - 对于 `list`、`set` 等基于链表的容器，插入或删除不会导致其他迭代器失效。

2. **常量迭代器**：
   - `const_iterator` 只能读取容器中的元素，不能修改其值。

3. **反向迭代器**：
   - `rbegin()` 和 `rend()` 用于反向遍历。
   - 注意：`rend()` 指向的是容器的第一个元素之前的位置。
4. **原理**
   - 就是**指针**

---

迭代器在 C++ 中非常灵活且高效，是容器操作的核心工具。通过理解不同类型的迭代器及其操作，可以更好地掌控 STL 容器的使用。