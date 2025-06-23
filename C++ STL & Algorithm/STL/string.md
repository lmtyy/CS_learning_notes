以下是 C++ 中 `std::string` 的详细函数说明，包括**参数**和**返回值**的完整解释。它是标准库的一部分，定义在 `<string>` 头文件中。

---

## **1. 构造函数**
### (1) 默认构造函数  
```cpp
std::string();
```
- **作用**：创建一个空字符串。
- **参数**：无。
- **返回值**：无。

---

### (2) 从 C 风格字符串构造  
```cpp
std::string(const char* s);
std::string(const char* s, size_type n);
```
- **作用**：
  - 第一种形式：用以 `\0` 结尾的字符数组构造字符串。
  - 第二种形式：用 `s` 指向的前 `n` 个字符构造字符串。
- **参数**：
  - `s`：指向字符数组的指针。
  - `n`：要使用的字符数量。
- **返回值**：无。

---

### (3) 拷贝构造函数  
```cpp
std::string(const std::string& other);
```
- **作用**：从已有字符串 `other` 复制构造。
- **参数**：`other` 是另一个 `std::string` 对象。
- **返回值**：无。

---

### (4) 重复字符构造  
```cpp
std::string(size_type n, char c);
```
- **作用**：构造一个包含 `n` 个字符 `c` 的字符串。
- **参数**：
  - `n`：字符的数量。
  - `c`：重复的字符。
- **返回值**：无。

---

### (5) 范围构造  
```cpp
template <class InputIterator>
std::string(InputIterator first, InputIterator last);
```
- **作用**：从迭代器范围 `[first, last)` 构造字符串。
- **参数**：
  - `first`：范围的起始迭代器。
  - `last`：范围的结束迭代器。
- **返回值**：无。

---

### (6) 初始化列表构造  
```cpp
std::string(std::initializer_list<char> ilist);
```
- **作用**：使用初始化列表构造字符串。
- **参数**：`ilist` 是字符的初始化列表。
- **返回值**：无。

---

## **2. 容量操作**
### (1) `size` 和 `length`  
```cpp
size_type size() const noexcept;
size_type length() const noexcept;
```
- **作用**：返回字符串中字符的数量。
- **参数**：无。
- **返回值**：字符串的长度。

---

### (2) `empty`  
```cpp
bool empty() const noexcept;
```
- **作用**：检查字符串是否为空。
- **参数**：无。
- **返回值**：
  - `true`：字符串为空。
  - `false`：字符串非空。

---

### (3) `capacity`  
```cpp
size_type capacity() const noexcept;
```
- **作用**：返回字符串当前分配的存储空间大小（以字符为单位）。
- **参数**：无。
- **返回值**：当前分配的容量。

---

### (4) `resize`  
```cpp
void resize(size_type n);
void resize(size_type n, char c);
```
- **作用**：
  - 第一种形式：调整字符串大小为 `n`，不足的部分填充默认字符。
  - 第二种形式：不足部分填充字符 `c`。
- **参数**：
  - `n`：目标大小。
  - `c`：填充的字符。
- **返回值**：无。

---

### (5) `reserve`  
```cpp
void reserve(size_type n);
```
- **作用**：为字符串预留至少 `n` 个字符的存储空间。
- **参数**：`n` 是要预留的容量。
- **返回值**：无。

---

### (6) `shrink_to_fit`  
```cpp
void shrink_to_fit();
```
- **作用**：减少字符串容量以适应当前大小。
- **参数**：无。
- **返回值**：无。

---

## **3. 元素访问**
### (1) `operator[]`  
```cpp
char& operator[](size_type pos);
const char& operator[](size_type pos) const;
```
- **作用**：访问指定位置的字符。
- **参数**：`pos` 是要访问的位置（从 0 开始）。
- **返回值**：引用所访问的字符。

---

### (2) `at`  
```cpp
char& at(size_type pos);
const char& at(size_type pos) const;
```
- **作用**：访问指定位置的字符，带边界检查。
- **参数**：`pos` 是要访问的位置。
- **返回值**：引用所访问的字符。
- **异常**：如果 `pos` 超出范围，会抛出 `std::out_of_range` 异常。

---

### (3) `front` 和 `back`  
```cpp
char& front();
const char& front() const;
char& back();
const char& back() const;
```
- **作用**：
  - `front`：返回字符串第一个字符的引用。
  - `back`：返回字符串最后一个字符的引用。
- **参数**：无。
- **返回值**：引用对应的字符。

---

### (4) `data` 和 `c_str`  
```cpp
const char* data() const noexcept;
const char* c_str() const noexcept;
```
- **作用**：
  - `data`：返回字符串底层存储的字符数组指针。
  - `c_str`：返回以 `\0` 结尾的 C 风格字符串。
- **参数**：无。
- **返回值**：指向字符数组的指针。

---

## **4. 修改操作**
### (1) `append`  
```cpp
std::string& append(const std::string& str);
std::string& append(const char* s, size_type n);
std::string& append(size_type n, char c);
```
- **作用**：在字符串末尾追加内容。
- **参数**：
  - `str`：要追加的字符串。
  - `s`：指向字符数组的指针。
  - `n`：字符数量。
  - `c`：要追加的字符。
- **返回值**：引用自身。

---

### (2) `insert`  
```cpp
std::string& insert(size_type pos, const std::string& str);
std::string& insert(size_type pos, size_type n, char c);
```
- **作用**：在指定位置插入内容。
- **参数**：
  - `pos`：插入位置。
  - `str`：要插入的字符串。
  - `n`：字符数量。
  - `c`：要插入的字符。
- **返回值**：引用自身。

---

### (3) `erase`  
```cpp
std::string& erase(size_type pos = 0, size_type n = npos);
```
- **作用**：从指定位置开始删除 `n` 个字符。
- **参数**：
  - `pos`：删除的起始位置。
  - `n`：要删除的字符数量。
- **返回值**：引用自身。

---

### (4) `replace`  
```cpp
std::string& replace(size_type pos, size_type len, const std::string& str);
```
- **作用**：将从 `pos` 开始的 `len` 个字符替换为字符串 `str`。
- **参数**：
  - `pos`：起始位置。
  - `len`：要替换的字符数量。
  - `str`：替换内容。
- **返回值**：引用自身。

---

### (5) `substr`  
```cpp
std::string substr(size_type pos = 0, size_type len = npos) const;
```
- **作用**：返回从 `pos` 开始、长度为 `len` 的子字符串。
- **参数**：
  - `pos`：起始位置。
  - `len`：子字符串长度。
- **返回值**：子字符串。

---

## 示例代码
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hello";
    s.append(" world");
    cout << s << endl;  // 输出 "hello world"

    s.replace(6, 5, "C++");
    cout << s << endl;  // 输出 "hello C++"

    string sub = s.substr(6, 3);
    cout << sub << endl; // 输出 "C++"

    return 0;
}
```

通过这些详细说明，您可以更好地理解和使用 `std::string`。