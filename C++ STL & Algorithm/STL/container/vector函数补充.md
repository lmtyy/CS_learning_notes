在 C++ 中，`std::vector` 是一种动态数组容器，定义在头文件 `<vector>` 中。它提供了灵活的数组操作功能，支持动态调整大小、高效的随机访问等。

以下是 `std::vector` 的所有主要成员函数和功能分类：

---

### **1. 构造与析构**
1. **默认构造**：  
   `vector()`  
   创建一个空的 `vector`。

2. **指定大小构造**：  
   `vector(size_type count)`  
   创建一个包含 `count` 个默认值的元素的 `vector`。

3. **初始化列表构造**：  
   `vector(std::initializer_list<T> init)`  
   使用初始化列表构造 `vector`。

4. **范围构造**：  
   `vector(InputIt first, InputIt last)`  
   从范围 `[first, last)` 中的元素构造 `vector`。

5. **拷贝构造**：  
   `vector(const vector &other)`  
   从另一个 `vector` 拷贝构造。

6. **移动构造**：  
   `vector(vector &&other)`  
   从另一个 `vector` 移动构造（高效转移资源）。

---

### **2. 赋值操作**
1. `vector& operator=(const vector &other)`  
   拷贝赋值。

2. `vector& operator=(vector &&other)`  
   移动赋值。

3. `vector& operator=(std::initializer_list<T> ilist)`  
   使用初始化列表赋值。

---

### **3. 迭代器**
1. `iterator begin()` / `const_iterator begin() const`  
   返回指向第一个元素的迭代器。

2. `iterator end()` / `const_iterator end() const`  
   返回指向容器末尾之后位置的迭代器。

3. `reverse_iterator rbegin()` / `const_reverse_iterator rbegin() const`  
   返回指向最后一个元素的反向迭代器。

4. `reverse_iterator rend()` / `const_reverse_iterator rend() const`  
   返回指向反向迭代器之前的位置。

5. `const_iterator cbegin() const` / `const_iterator cend() const`  
   返回 `const` 版本的 `begin()` 和 `end()`。

6. `const_reverse_iterator crbegin() const` / `const_reverse_iterator crend() const`  
   返回 `const` 版本的 `rbegin()` 和 `rend()`。

---

### **4. 容量管理**
1. `size_type size() const`  
   返回当前元素数量。

2. `size_type max_size() const`  
   返回容器理论上的最大大小。

3. `void resize(size_type count)`  
   调整容器大小为 `count`，若增加则用默认值填充。

4. `size_type capacity() const`  
   返回当前分配的容量（不一定等于 `size()`）。

5. `bool empty() const`  
   检查容器是否为空。

6. `void reserve(size_type new_cap)`  
   预留至少 `new_cap` 的存储空间，避免频繁重新分配内存。

7. `void shrink_to_fit()`  
   减小容量，使之等于当前大小。

---

### **5. 元素访问**
1. `reference operator[](size_type pos)` / `const_reference operator[](size_type pos) const`  
   访问指定位置的元素。

2. `reference at(size_type pos)` / `const_reference at(size_type pos) const`  
   访问指定位置的元素，带边界检查。

3. `reference front()` / `const_reference front() const`  
   返回第一个元素的引用。

4. `reference back()` / `const_reference back() const`  
   返回最后一个元素的引用。

5. `T* data()` / `const T* data() const`  
   返回底层数组的指针。

---

### **6. 修改操作**
1. `void assign(size_type count, const T &value)`  
   用 `count` 个值 `value` 替换当前内容。

2. `void assign(InputIt first, InputIt last)`  
   使用迭代器范围赋值。

3. `void assign(std::initializer_list<T> ilist)`  
   使用初始化列表赋值。

4. `void push_back(const T &value)`  
   在末尾添加元素 `value`。

5. `void push_back(T &&value)`  
   在末尾添加右值引用元素。

6. `void pop_back()`  
   移除最后一个元素。

7. `iterator insert(const_iterator pos, const T &value)`  
   在指定位置插入元素 `value`。

8. `iterator insert(const_iterator pos, T &&value)`  
   在指定位置插入右值引用元素。

9. `iterator insert(const_iterator pos, size_type count, const T &value)`  
   在指定位置插入 `count` 个值为 `value` 的元素。

10. `iterator insert(const_iterator pos, InputIt first, InputIt last)`  
    在指定位置插入范围 `[first, last)` 的元素。

11. `iterator insert(const_iterator pos, std::initializer_list<T> ilist)`  
    在指定位置插入初始化列表。

12. `iterator erase(const_iterator pos)`  
    移除指定位置的元素。

13. `iterator erase(const_iterator first, const_iterator last)`  
    移除指定范围的元素。

14. `void clear()`  
    移除所有元素。

15. `void emplace_back(Args&&... args)`  
    原地构造一个新元素，并添加到末尾。

16. `iterator emplace(const_iterator pos, Args&&... args)`  
    原地构造一个新元素，并插入到指定位置。

17. `void swap(vector &other)`  
    交换两个 `vector` 的内容。

---

### **7. 比较操作**
1. `bool operator==(const vector &lhs, const vector &rhs)`  
   按元素逐个比较，判断是否相等。

2. `bool operator!=(const vector &lhs, const vector &rhs)`  
   检查是否不相等。

3. `bool operator<(const vector &lhs, const vector &rhs)`  
   按字典顺序比较。

4. `bool operator<=(const vector &lhs, const vector &rhs)`  
   检查是否小于等于。

5. `bool operator>(const vector &lhs, const vector &rhs)`  
   检查是否大于。

6. `bool operator>=(const vector &lhs, const vector &rhs)`  
   检查是否大于等于。

---

### **示例代码**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {1, 2, 3, 4};

    // 添加元素
    vec.push_back(5);
    vec.emplace_back(6);

    // 遍历元素
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    // 删除元素
    vec.pop_back();
    vec.erase(vec.begin() + 1);

    // 插入元素
    vec.insert(vec.begin(), 10);

    // 显示结果
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

---

### **复杂度分析**
- **随机访问**：\( O(1) \)
- **插入或删除末尾元素**：\( O(1) \) 平均
- **插入或删除中间元素**：\( O(n) \) 最坏
- **动态扩容**：\( O(n) \) 最坏，但摊销复杂度为 \( O(1) \)

`std::vector` 是动态数组操作的核心容器，适用于大多数普通场景。