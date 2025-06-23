# stack

C++ 提供了一个标准模板库（STL）中的 **`stack`** 容器，它是一个简单、易用的栈实现。以下是对 **`stack`** 库的全面介绍。

---

### **`stack` 简介**
`std::stack` 是一个 **后进先出**（LIFO）的容器适配器，封装了底层的顺序容器（如 `vector`、`deque` 或 `list`），只暴露与栈相关的接口。

- **头文件**:  
  ```cpp
  #include <stack>
  ```
- **命名空间**:  
  ```cpp
  using namespace std;
  ```

---

### **`stack` 的常用操作**

以下是 `stack` 提供的核心接口和功能：

| **函数/方法**       | **作用**                                                             |
|---------------------|----------------------------------------------------------------------|
| `push(value)`       | 向栈顶添加元素。                                                    |
| `pop()`             | 移除栈顶元素（不返回其值）。                                        |
| `top()`             | 获取栈顶元素（不移除）。                                            |
| `empty()`           | 检查栈是否为空，返回 `true` 或 `false`。                            |
| `size()`            | 返回栈中元素的数量。                                                |
| `emplace(args...)`  | 在栈顶直接构造元素（避免临时对象的开销，C++11 引入）。              |
| `swap(otherStack)`  | 交换当前栈与另一个栈的内容（时间复杂度为 \(O(1)\)）。              |

---

### **`stack` 示例代码**

#### **基本用法**
```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;

    // 入栈
    s.push(10);
    s.push(20);
    s.push(30);

    // 栈的基本信息
    cout << "栈顶元素: " << s.top() << endl; // 输出 30
    cout << "栈的大小: " << s.size() << endl; // 输出 3

    // 出栈
    s.pop();
    cout << "栈顶元素（弹出后）: " << s.top() << endl; // 输出 20

    // 判断栈是否为空
    if (s.empty()) {
        cout << "栈为空" << endl;
    } else {
        cout << "栈不为空" << endl; // 输出 "栈不为空"
    }

    return 0;
}
```

#### **使用 `emplace`**
`emplace` 在栈顶直接构造对象，效率更高。

```cpp
#include <iostream>
#include <stack>
using namespace std;

struct Point {
    int x, y;
    Point(int a, int b) : x(a), y(b) {}
};

int main() {
    stack<Point> s;

    // 使用 emplace 构造元素
    s.emplace(1, 2);
    s.emplace(3, 4);

    // 查看栈顶元素
    Point topPoint = s.top();
    cout << "栈顶元素: (" << topPoint.x << ", " << topPoint.y << ")" << endl; // 输出 (3, 4)

    return 0;
}
```

---

### **底层容器**
`std::stack` 是一个 **容器适配器**，默认使用 **`std::deque`** 作为底层容器，但可以通过模板参数指定其他顺序容器，例如 `std::vector` 或 `std::list`。

#### **使用 `vector` 作为底层容器**
```cpp
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
    // 使用 vector 作为底层容器
    stack<int, vector<int>> s;

    s.push(1);
    s.push(2);
    s.push(3);

    while (!s.empty()) {
        cout << s.top() << " "; // 输出 3 2 1
        s.pop();
    }

    return 0;
}
```

---

### **完整操作示例**
以下代码展示了栈的各种操作：
```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<string> s;

    // 入栈
    s.push("apple");
    s.push("banana");
    s.push("cherry");

    // 获取栈顶元素
    cout << "栈顶: " << s.top() << endl; // 输出 cherry

    // 获取栈的大小
    cout << "栈大小: " << s.size() << endl; // 输出 3

    // 弹出元素
    s.pop();
    cout << "栈顶（弹出后）: " << s.top() << endl; // 输出 banana

    // 判断是否为空
    cout << "栈是否为空: " << (s.empty() ? "是" : "否") << endl; // 输出 否

    // 交换两个栈
    stack<string> s2;
    s2.push("x");
    s2.push("y");

    s.swap(s2);
    cout << "交换后栈顶: " << s.top() << endl; // 输出 y

    return 0;
}
```

---

### **常见问题与注意事项**

1. **只能访问栈顶元素**：
   - `stack` 只提供对栈顶元素的访问，不允许遍历或随机访问底层元素。

2. **性能考虑**：
   - 默认底层容器是 `deque`，可以根据需求替换为 `vector` 或 `list`。
   - `deque` 适合频繁的入栈和出栈操作，`vector` 可能在大规模数据时表现更好。

3. **不是线程安全**：
   - `std::stack` 不提供线程安全性，如果需要多线程操作，请使用同步机制。

4. **不提供迭代器:**
   - 不允许遍历

---

### **栈的常见应用**
1. **括号匹配**：
   - 判断括号是否匹配。
2. **表达式求值**：
   - 中缀表达式转后缀表达式的计算。
3. **深度优先搜索（DFS）**：
   - 用栈模拟递归。
4. **函数调用栈**：
   - 系统调用中的调用栈管理。

通过 `stack` 容器，我们可以高效实现许多基于 **后进先出** 特性的问题。