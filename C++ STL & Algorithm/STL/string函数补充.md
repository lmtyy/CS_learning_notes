在 C++ 中，`std::string` 类（位于 `<string>` 头文件中）提供了许多函数，用于处理字符串。以下是 C++ 标准库 `std::string` 中常见的函数和操作。

### 1. 构造函数
- **`std::string()`**: 默认构造函数，创建一个空字符串。
- **`std::string(const std::string& str)`**: 拷贝构造函数，创建一个新的字符串，内容与另一个字符串相同。
- **`std::string(const char* s)`**: 用 C 风格字符串构造字符串。
- **`std::string(std::string&& str)`**: 移动构造函数。

### 2. 操作字符串的函数
- **`str.size()` 或 `str.length()`**: 返回字符串的长度。
- **`str.empty()`**: 判断字符串是否为空。
- **`str.resize(size_t n)`**: 调整字符串大小。
- **`str.reserve(size_t n)`**: 预分配内存，用于减少重新分配的次数。
- **`str.clear()`**: 清空字符串。
- **`str.append(const std::string& str)` 或 `str += str`**: 向字符串追加内容。
- **`str.insert(size_t pos, const std::string& str)`**: 在指定位置插入字符串。
- **`str.erase(size_t pos, size_t len)`**: 删除字符串中的一部分。
- **`str.replace(size_t pos, size_t len, const std::string& str)`**: 替换字符串中的一部分。
- **`str.substr(size_t pos, size_t len)`**: 提取子字符串。

### 3. 查找和定位
- **`str.find(const std::string& str)`**: 返回第一次出现子字符串的位置，未找到返回 `std::string::npos`。
- **`str.rfind(const std::string& str)`**: 返回最后一次出现子字符串的位置。
- **`str.find_first_of(const std::string& str)`**: 查找任意一个字符出现在给定字符串中的位置。
- **`str.find_last_of(const std::string& str)`**: 查找最后一次出现任意字符的位置。
- **`str.find_first_not_of(const std::string& str)`**: 查找第一个不属于给定字符集的位置。
- **`str.find_last_not_of(const std::string& str)`**: 查找最后一个不属于给定字符集的位置。

### 4. 比较函数
- **`str == other`**: 比较两个字符串是否相等。
- **`str != other`**: 比较两个字符串是否不相等。
- **`str < other`**: 字典顺序比较两个字符串。
- **`str.compare(const std::string& other)`**: 返回 `0`（相等），`< 0`（小于），`> 0`（大于）根据字典顺序比较两个字符串。

### 5. 字符串内容操作
- **`str.c_str()`**: 返回 C 风格的字符串（`const char*`），即以 `\0` 结尾的字符数组。
- **`str.data()`**: 返回底层字符数组的指针（不一定以 `\0` 结尾，且不可修改）。
- **`str[0]` 或 `str.at(0)`**: 访问字符串中的单个字符。
- **`str.front()`**: 返回第一个字符。
- **`str.back()`**: 返回最后一个字符。

### 6. 转换函数
- **`std::stoi(const std::string& str)`**: 将字符串转换为整数。
- **`std::stol(const std::string& str)`**: 将字符串转换为长整数。
- **`std::stoll(const std::string& str)`**: 将字符串转换为长长整数。
- **`std::stof(const std::string& str)`**: 将字符串转换为浮点数。
- **`std::stod(const std::string& str)`**: 将字符串转换为双精度浮点数。
- **`std::to_string(T value)`**: 将其他类型转换为字符串。

### 7. 字符串流操作
- **`std::getline(std::istream& is, std::string& str)`**: 从输入流中读取一行内容，直到遇到换行符。
- **`std::stringstream`**: 使用字符串流进行格式化输入输出。

### 8. 其他函数
- **`std::string::npos`**: 一个常量，表示 "未找到" 的特殊值。
- **`str.swap(other)`**: 交换两个字符串的内容。
- **`std::string::shrink_to_fit()`**: 请求减少内存容量（根据实现，不一定能减少）。

### 示例代码
```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    
    // 获取字符串长度
    std::cout << "Length: " << str.size() << std::endl;
    
    // 查找子字符串
    size_t pos = str.find("World");
    if (pos != std::string::npos) {
        std::cout << "'World' found at position " << pos << std::endl;
    }
    
    // 字符串拼接
    str.append(" How are you?");
    std::cout << "Appended string: " << str << std::endl;
    
    // 提取子字符串
    std::string sub = str.substr(13, 5);
    std::cout << "Substring: " << sub << std::endl;
    
    // 转换为 C 风格字符串
    const char* cstr = str.c_str();
    std::cout << "C-style string: " << cstr << std::endl;
    
    return 0;
}
```

以上是 `std::string` 常用的一些函数和操作。如果你有其他具体问题，欢迎继续提问！