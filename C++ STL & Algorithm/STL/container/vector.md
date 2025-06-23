# vector
在C++中，`vector` 是标准模板库（STL）中的一个动态数组容器类，定义在头文件 `<vector>` 中。它能够根据需要动态调整大小，支持随机访问，同时提供了高效的插入和删除操作。

以下是 `vector` 的简介和常用操作：

---

### **简介**
- **特点**：
  - **动态大小**：`vector` 会根据需要自动扩展或收缩。
  - **连续存储**：底层使用连续的内存空间，因此可以通过索引直接访问元素。
  - **高效的增删操作**：在尾部插入或删除元素效率较高，复杂度为 \(O(1)\)；在中间或开头进行插入删除操作时需要移动元素，复杂度为 \(O(n)\)。
  - **丰富的接口**：`vector` 提供许多成员函数以支持容器操作。

- **使用场景**：
  - 需要动态调整大小的数组。
  - 希望方便管理和操作数组元素。

---

### **常用操作**

#### 1. **引入头文件**
```cpp
#include <vector>
```

#### 2. **创建和初始化**
```cpp
std::vector<int> v1;                // 空vector
std::vector<int> v2(5);             // 包含5个元素，值为默认值0
std::vector<int> v3(5, 10);         // 包含5个元素，值为10
std::vector<int> v4{1, 2, 3, 4, 5}; // 使用列表初始化
std::vector<int> v5(v4);            // 拷贝构造
```

#### 3. **访问元素**
```cpp
v4[0];           // 通过下标访问（不进行边界检查）
v4.at(0);        // 使用 at() 访问（进行边界检查）
v4.front();      // 返回第一个元素
v4.back();       // 返回最后一个元素
```

#### 4. **修改元素**
```cpp
v4[1] = 20;         // 修改下标为1的元素
v4.push_back(6);    // 在尾部添加元素
v4.pop_back();      // 删除尾部元素
v4.assign(n, elem); // 覆盖原向量 添加n个elem
v4.swap(&vec);      // v4与vec互换元素
```

#### 5. **插入和删除**
```cpp
v4.insert(v4.begin() + 1, 99);      // 在位置1插入99
v4.insert(v4.end(), {7, 8, 9});     // 尾部插入多个元素
v4.erase(v4.begin() + 2);           // 删除下标为2的元素
v4.erase(v4.begin() + 1, v4.end()); // 删除指定范围的元素
v4.clear();                         // 清空所有元素
```

#### 6. **查询大小和容量**
```cpp
v4.size();       // 当前元素个数
v4.capacity();   // 当前分配的容量（不一定等于 size）
v4.empty();      // 检查是否为空
```

#### 7. **动态调整大小**
```cpp
v4.resize(10);     // 调整大小为10，默认填充0
v4.resize(10, 5);  // 调整大小为10，填充5
v4.reserve(20);    // 提前分配容量，避免频繁扩容
v4.shrink_to_fit(); // 释放多余的容量
```

#### 8. **排序与遍历**
```cpp
#include <algorithm>

// 排序
std::sort(v4.begin(), v4.end());   // 升序排序
std::sort(v4.rbegin(), v4.rend()); // 降序排序

// 遍历
for (int val : v4) {               // 范围for循环
    std::cout << val << " ";
}

for (auto it = v4.begin(); it != v4.end(); ++it) { // 迭代器遍历
    std::cout << *it << " ";
}
```

#### 9. **迭代器相关**
```cpp
auto it = v4.begin();  // 指向第一个元素
auto rit = v4.rbegin(); // 反向迭代器，指向最后一个元素
auto end = v4.end();    // 指向尾后元素
```

---

### **示例代码**
以下是一个综合示例：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // 初始化
    std::vector<int> v{5, 2, 8, 1};

    // 插入元素
    v.push_back(10);

    // 排序
    std::sort(v.begin(), v.end());

    // 遍历输出
    std::cout << "排序后：";
    for (const auto& val : v) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 删除元素
    v.erase(v.begin() + 1);

    // 打印大小
    std::cout << "大小：" << v.size() << ", 容量：" << v.capacity() << std::endl;

    return 0;
}
```

---

通过掌握这些操作，`vector` 可以极大简化动态数组的管理，是C++开发中不可或缺的工具之一。