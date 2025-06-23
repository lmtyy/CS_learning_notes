# list
C++ 中的 `list` 是标准模板库（STL）中的一个容器类，位于 `<list>` 头文件中。它是一个双向链表（doubly-linked list），非常适合需要频繁在中间进行插入和删除操作的场景。与 `vector` 不同，`list` 的元素不是连续存储的，因此访问元素的速度较慢，但插入和删除操作效率更高。

以下是 `list` 的简介和常用操作：

---

## **特点**
1. **双向链表**：每个节点包含数据和前后指针。
2. **动态大小**：可以随时增加或减少大小。
3. **支持双向迭代**：支持 `bidirectional_iterator`，可以向前或向后遍历。
4. **高效插入和删除**：在任意位置插入和删除元素的时间复杂度为 \(O(1)\)（给定迭代器的情况下）。
5. **顺序访问**：不像 `vector` 那样支持随机访问，访问元素时需要从头开始逐步移动迭代器。

---

## **常用操作**

### **1. 声明和初始化**
```cpp
#include <iostream>
#include <list>

int main() {
    // 默认构造
    std::list<int> lst;

    // 使用初始化列表构造
    std::list<int> lst1 = {1, 2, 3, 4, 5};

    // 使用指定大小和初始值构造
    std::list<int> lst2(5, 10); // 5 个值为 10 的元素

    // 使用另一个容器构造
    std::list<int> lst3(lst1);

    return 0;
}
```

---

### **2. 常用成员函数**

#### **插入操作**
```cpp
lst.push_back(10);  // 在末尾插入
lst.push_front(20); // 在开头插入
lst.insert(it, 30); // 在迭代器 it 指向的位置插入 并返回新数据的迭代器
```

#### **删除操作**
```cpp
lst.pop_back();      // 删除末尾元素
lst.pop_front();     // 删除开头元素
lst.erase(it);       // 删除迭代器 it 指向的元素 返回被删除元素后紧跟的迭代器
lst.erase(it1, it2); // 删除 [it1, it2) 范围内的元素 返回下一个位置的迭代器
lst.clear();         // 清空整个列表
lst.remove(elem);    // 去除所有elem元素
```

#### **访问元素**
```cpp
lst.front(); // 返回第一个元素
lst.back();  // 返回最后一个元素
```

#### **遍历列表**
```cpp
for (auto it = lst.begin(); it != lst.end(); ++it) {
    std::cout << *it << " ";
}

// 使用范围循环
for (const auto &val : lst) {
    std::cout << val << " ";
}
```

#### **排序和反转**
```cpp
lst.sort();       // 对列表进行升序排序
lst.reverse();    // 反转列表的顺序
```

#### **合并和去重**
```cpp
std::list<int> lst2 = {3, 3, 4, 4, 5};
lst.merge(lst2);  // 合并 lst2 到 lst 中（lst 和 lst2 必须有序）
lst.unique();     // 去除连续重复的元素
```

#### **其他操作**
```cpp
lst.empty();       // 判断列表是否为空
lst.size();        // 返回列表中元素的个数
lst.resize(10);    // 调整列表大小为 10
lst.swap(lst2);    // 与另一个列表交换内容
```

---

### **示例代码**
```cpp
#include <iostream>
#include <list>

int main() {
    std::list<int> lst = {5, 2, 8, 1};

    // 插入和删除
    lst.push_back(10);
    lst.push_front(0);
    lst.erase(--lst.end());

    // 遍历
    for (auto val : lst) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 排序和反转
    lst.sort();
    lst.reverse();

    for (auto val : lst) {
        std::cout << val << " ";
    }

    return 0;
}
```

运行结果：
```
0 5 2 8 1 
8 5 2 0 
```

---

### **应用场景**
- 数据经常需要在中间进行插入或删除。
- 数据大小动态变化，不需要频繁随机访问。
- 需要合并、排序或去重的操作。

### **注意事项**
- 插入不会导致迭代器失效 但是删除时可能会

使用 `list` 时，应根据性能需求选择合适的容器（如 `vector` 或 `deque` 可能更适合随机访问频繁的场景）。