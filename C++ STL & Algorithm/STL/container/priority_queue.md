# priority_queue

### **优先队列（Priority Queue）简介**

**优先队列（Priority Queue）** 是一种特殊的队列，它的特点是每个元素都有一个 **优先级**，并且 **优先级高的元素先被移除**。与普通队列不同，普通队列遵循 **先进先出**（FIFO）的规则，而优先队列遵循 **优先级高的元素优先出队** 的规则，类似于医院的急诊队列，高优先级的病人会优先接受治疗。

### **优先队列的特点**

- **优先级**：每个元素都关联有一个优先级，优先级高的元素比优先级低的元素先出队。
- **非固定顺序**：元素在队列中的位置取决于其优先级，而非插入顺序。
- **堆（Heap）实现**：优先队列通常使用 **堆**（特别是 **二叉堆**）来实现，这样可以在 \(O(\log n)\) 时间内插入和删除元素。

### **常见的优先队列类型**

1. **最大优先队列**：
   - 最大优先队列保证每次出队时返回具有最大优先级的元素。
   - 适用于按优先级从高到低处理任务的场景。

2. **最小优先队列**：
   - 最小优先队列保证每次出队时返回具有最小优先级的元素。
   - 适用于按优先级从低到高处理任务的场景。

### **优先队列的常用操作**

- **`push(value, priority)`**：将具有指定优先级的元素插入到队列中。
- **`pop()`**：移除优先级最高的元素（出队操作）。
- **`top()`**：返回优先级最高的元素，但不移除它。
- **`empty()`**：检查队列是否为空。
- **`size()`**：获取队列中的元素数量。

### **C++ 中的 `priority_queue`**

C++ 标准库提供了一个名为 **`priority_queue`** 的容器适配器，默认实现是 **最大优先队列**，即优先级较大的元素先出队。其底层实现通常是 **最大堆（max-heap）**。

#### **头文件**
```cpp
#include <queue>
```

#### **常用操作**
| **函数/方法**       | **作用**                                                      |
|---------------------|---------------------------------------------------------------|
| `push(value)`       | 将元素插入队列，并根据其优先级进行排序。                    |
| `pop()`             | 移除优先级最高的元素。                                       |
| `top()`             | 获取优先级最高的元素，但不移除它。                          |
| `empty()`           | 判断队列是否为空。                                           |
| `size()`            | 获取队列中元素的数量。                                       |

#### **优先队列的实现方式**

C++ 中的 **`priority_queue`** 默认使用 **`vector`** 作为底层容器，且使用 **最大堆**（max-heap）来实现。你可以通过更改底层容器或自定义比较函数来实现 **最小堆**（min-heap）。

---

### **最大优先队列（默认）示例**

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> pq;

    // 入队（根据优先级自动排序）
    pq.push(10);
    pq.push(20);
    pq.push(15);

    // 查看优先队列中的元素，优先级高的元素先出队
    cout << "队头元素: " << pq.top() << endl; // 输出 20（最大值）

    pq.pop(); // 移除最大元素（20）
    cout << "队头元素（弹出后）: " << pq.top() << endl; // 输出 15

    return 0;
}
```

在这个示例中，`priority_queue<int>` 默认是一个最大优先队列（即堆中最大值在队头），每次出队时返回最大值。

---

### **最小优先队列示例**

如果需要实现 **最小优先队列**（即堆中最小值在队头），可以通过自定义比较函数来改变默认的排序方式。

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    // 使用 greater<int> 实现最小优先队列
    priority_queue<int, vector<int>, greater<int>> pq;

    // 入队（根据优先级自动排序）
    pq.push(10);
    pq.push(20);
    pq.push(15);

    // 查看优先队列中的元素，优先级最低的元素先出队
    cout << "队头元素: " << pq.top() << endl; // 输出 10（最小值）

    pq.pop(); // 移除最小元素（10）
    cout << "队头元素（弹出后）: " << pq.top() << endl; // 输出 15

    return 0;
}
```

在这个示例中，`priority_queue<int, vector<int>, greater<int>>` 使得队列成为最小优先队列，每次出队时返回最小值。

---

### **`priority_queue` 的常见应用**

1. **任务调度**：
   - 根据任务的优先级执行任务。高优先级的任务会被优先处理。

2. **Dijkstra 算法**：
   - 在图的最短路径算法（如 Dijkstra）中，用优先队列来管理当前的最短路径。

3. **合并多个有序链表**：
   - 在合并多个有序链表时，使用优先队列来持续获取当前最小的元素。

4. **模拟并发任务**：
   - 在并发编程中，可以用优先队列来处理具有不同优先级的任务。

5. **贪心算法**：
   - 优先队列常用于贪心算法中，例如在 Huffman 编码中选择最小权值的元素进行合并。

---

### **总结**

- **优先队列（Priority Queue）** 是一种特殊的队列，它按照元素的优先级来处理元素，而不是按照元素的插入顺序。
- C++ 中的 **`priority_queue`** 默认实现是 **最大优先队列**，你可以通过更改比较函数来实现 **最小优先队列**。
- 优先队列在许多场景中非常有用，如任务调度、图算法、合并有序数据等。

在 **优先队列（Priority Queue）** 中，元素 **不必是数字**。可以是任何可以比较大小的对象或数据类型。优先队列的关键是元素之间有一个明确的优先级关系，因此你可以将任意类型的对象插入优先队列，只要你提供了合适的比较规则。

---

### **自定义比较函数**

在 C++ 中，`priority_queue` 默认使用 **`operator<`** 来比较元素，这对于数字类型（如 `int`、`double` 等）是有效的。但对于自定义类型的元素，你需要自定义比较规则，以指定哪些元素具有更高的优先级。

### **示例 1：优先队列中的字符串**

你可以将 **字符串** 插入到优先队列中，并且可以根据字典顺序（默认的比较方式）对它们进行排序：

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    priority_queue<string> pq;

    pq.push("banana");
    pq.push("apple");
    pq.push("cherry");

    // 按照字典顺序输出
    while (!pq.empty()) {
        cout << pq.top() << " ";
        pq.pop();
    }
    // 输出：cherry banana apple

    return 0;
}
```

在这个示例中，`priority_queue<string>` 默认按字典顺序（即按字母顺序从大到小）排列字符串。

---

### **示例 2：自定义对象作为优先队列元素**

你还可以将 **自定义类** 的对象放入优先队列中，并通过自定义比较函数来定义优先级。例如，我们可以定义一个包含 `priority` 和 `name` 的结构体，按 `priority` 对其进行排序：

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

struct Task {
    int priority;
    string name;

    Task(int p, string n) : priority(p), name(n) {}

    // 自定义比较函数：优先级越高，越先出队
    bool operator<(const Task& t) const {
        return priority < t.priority;  // 最大优先队列（优先级大的排在前面）
    }
};

int main() {
    priority_queue<Task> pq;

    pq.push(Task(5, "Task 1"));
    pq.push(Task(1, "Task 2"));
    pq.push(Task(3, "Task 3"));

    // 按优先级顺序输出
    while (!pq.empty()) {
        cout << pq.top().name << " (Priority: " << pq.top().priority << ")" << endl;
        pq.pop();
    }
    // 输出：
    // Task 1 (Priority: 5)
    // Task 3 (Priority: 3)
    // Task 2 (Priority: 1)

    return 0;
}
```

在这个示例中，我们定义了一个 `Task` 结构体，其中包含了一个 `priority` 和 `name`。然后通过重载 `<` 运算符来指定如何比较 `Task` 对象的优先级。通过这种方式，`priority_queue` 会根据任务的优先级进行排序。

---

### **自定义最小优先队列**

如果需要 **最小优先队列**，可以使用自定义的比较器，确保最小优先级的元素先出队。比如，我们可以使用 `greater<T>` 来表示元素的优先级按从小到大的顺序排列：

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

struct Task {
    int priority;
    string name;

    Task(int p, string n) : priority(p), name(n) {}

    // 自定义比较函数：优先级越低，越先出队
    bool operator>(const Task& t) const {
        return priority > t.priority;  // 最小优先队列
    }
};

int main() {
    // 使用 greater 来实现最小优先队列
    priority_queue<Task, vector<Task>, greater<Task>> pq;

    pq.push(Task(5, "Task 1"));
    pq.push(Task(1, "Task 2"));
    pq.push(Task(3, "Task 3"));

    // 按优先级顺序输出（从最小到最大）
    while (!pq.empty()) {
        cout << pq.top().name << " (Priority: " << pq.top().priority << ")" << endl;
        pq.pop();
    }
    // 输出：
    // Task 2 (Priority: 1)
    // Task 3 (Priority: 3)
    // Task 1 (Priority: 5)

    return 0;
}
```

在此示例中，`greater<Task>` 确保优先级较低的任务先出队，从而实现最小优先队列。

---

### **总结**

- **优先队列** 中的元素不必是数字，可以是任何类型，只要这个类型支持比较操作。
- **自定义比较规则**：你可以通过重载比较运算符（如 `<`、`>`）或提供自定义的比较函数来控制优先级的排序方式。
- 适用于字符串、结构体、类等各种类型的元素，只要可以比较优先级。

优先队列的灵活性允许它处理多种复杂的数据类型，只要能为这些类型定义合理的排序规则。