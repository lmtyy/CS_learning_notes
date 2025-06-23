在 C++ 中，输入输出（I/O）是与用户、文件或其他外部设备进行交互的重要部分。C++ 提供了丰富的功能来处理这些操作，主要通过标准库 `<iostream>` 和 `<fstream>` 来实现。以下是一些常用的输入输出操作，涵盖了控制台输入输出、文件读写以及格式化输出等常见任务。

### 1. **控制台输入输出**

控制台输入输出通常通过 `std::cin` 和 `std::cout` 来完成：

#### 输出到控制台：
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl; // 输出字符串并换行
    return 0;
}
```
- `std::cout` 是标准输出流，通常用于向控制台输出数据。
- `std::endl` 会输出换行符并刷新输出缓冲区。如果你只需要换行符，可以用 `"\n"` 替代。

#### 输入从控制台：
```cpp
#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;  // 从控制台输入一个整数
    std::cout << "You entered: " << num << std::endl;
    return 0;
}
```
- `std::cin` 是标准输入流，通常用于从控制台接收数据。
- `>>` 运算符用于将输入的值存储到变量中。

#### 输入多个数据：
```cpp
#include <iostream>

int main() {
    int a, b;
    std::cout << "Enter two numbers: ";
    std::cin >> a >> b;  // 输入两个整数
    std::cout << "Sum: " << a + b << std::endl;
    return 0;
}
```
- 可以一次性读取多个数据，`std::cin` 会根据空格、换行符等自动分隔输入项。

#### 检查输入有效性：
```cpp
#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    while (!(std::cin >> num)) {  // 检查输入是否有效
        std::cout << "Invalid input. Please enter a valid number: ";
        std::cin.clear();  // 清除输入错误标志
        std::cin.ignore(10000, '\n');  // 忽略当前行的剩余输入
    }
    std::cout << "You entered: " << num << std::endl;
    return 0;
}
```
- 使用 `std::cin.clear()` 清除输入错误标志。
- 使用 `std::cin.ignore()` 忽略当前行的内容。

### 2. **文件输入输出**

C++ 提供了 `<fstream>` 库来进行文件的读写操作。

#### 文件写入：
```cpp
#include <iostream>
#include <fstream>

int main() {
    std::ofstream outFile("example.txt");  // 打开文件用于写入
    if (outFile.is_open()) {
        outFile << "Hello, File!" << std::endl;  // 写入数据到文件
        outFile.close();  // 关闭文件
    } else {
        std::cerr << "Error opening file!" << std::endl;
    }
    return 0;
}
```
- `std::ofstream` 用于输出到文件。
- `outFile.is_open()` 检查文件是否成功打开。
- `outFile.close()` 关闭文件。

#### 文件读取：
```cpp
#include <iostream>
#include <fstream>

int main() {
    std::ifstream inFile("example.txt");  // 打开文件用于读取
    if (inFile.is_open()) {
        std::string line;
        while (getline(inFile, line)) {  // 逐行读取文件内容
            std::cout << line << std::endl;
        }
        inFile.close();  // 关闭文件
    } else {
        std::cerr << "Error opening file!" << std::endl;
    }
    return 0;
}
```
- `std::ifstream` 用于从文件读取数据。
- `std::getline()` 逐行读取文件内容。

#### 文件读写示例（同时进行输入和输出）：
```cpp
#include <iostream>
#include <fstream>

int main() {
    std::ifstream inFile("input.txt");
    std::ofstream outFile("output.txt");

    if (inFile.is_open() && outFile.is_open()) {
        std::string line;
        while (getline(inFile, line)) {
            outFile << line << std::endl;  // 将每行内容写入另一个文件
        }
        inFile.close();
        outFile.close();
    } else {
        std::cerr << "Error opening file!" << std::endl;
    }

    return 0;
}
```
- 同时操作输入输出文件。

### 3. **格式化输入输出**

C++ 允许你控制输出的格式，常见的格式化操作包括控制字段宽度、精度、填充字符等。

#### 设置输出宽度：
```cpp
#include <iostream>
#include <iomanip>  // 包含setw和setfill

int main() {
    int num = 42;
    std::cout << std::setw(10) << num << std::endl;  // 设置输出宽度为10
    return 0;
}
```
- `std::setw(int)` 设置输出字段的最小宽度。
- 它不会自动填充空白，可以使用 `std::setfill()` 来指定填充字符。

#### 设置浮点数精度：
```cpp
#include <iostream>
#include <iomanip>  // 包含setprecision

int main() {
    double pi = 3.141592653589793;
    std::cout << std::fixed << std::setprecision(2) << pi << std::endl;  // 输出3.14
    return 0;
}
```
- `std::setprecision(int)` 设置输出的数字的精度。
- `std::fixed` 输出固定小数点格式。

#### 设置填充字符：
```cpp
#include <iostream>
#include <iomanip>  // 包含setfill

int main() {
    int num = 42;
    std::cout << std::setfill('*') << std::setw(10) << num << std::endl;  // 用*填充输出
    return 0;
}
```
- `std::setfill(char)` 设置字段的填充字符。

#### 控制符：设置不同的输出格式
```cpp
#include <iostream>
#include <iomanip>

int main() {
    int num = 255;
    std::cout << std::hex << num << std::endl;  // 输出十六进制
    std::cout << std::oct << num << std::endl;  // 输出八进制
    std::cout << std::dec << num << std::endl;  // 输出十进制
    return 0;
}
```
- `std::hex`：十六进制格式输出。
- `std::oct`：八进制格式输出。
- `std::dec`：十进制格式输出。

### 4. **错误输出**

C++ 提供了 `std::cerr` 和 `std::clog` 来输出错误信息和日志信息。

#### 错误输出：
```cpp
#include <iostream>

int main() {
    std::cerr << "Error: Something went wrong!" << std::endl;  // 输出错误信息
    return 0;
}
```
- `std::cerr` 是无缓冲的错误输出流。
- `std::clog` 是带缓冲的日志输出流。

### 5. **同步与性能**

C++ 默认情况下 `std::cin` 和 `std::cout` 是与 C 的 `stdin` 和 `stdout` 流同步的。为了提高性能，可以禁用同步，但这会使得 C++ 的流与 C 的流分离：

```cpp
#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);  // 禁用同步
    std::cin.tie(nullptr);  // 解除 cin 和 cout 的绑定

    std::cout << "Hello, World!" << std::endl;

    return 0;
}
```
- 这样做通常会提高程序性能，但要注意，禁用同步后，C++ 流和 C 流的行为可能不再一致。

### 总结

C++ 提供了灵活且强大的输入输出操作，能够处理从控制台、文件、错误流等多种输入输出需求。常用操作包括：

- **控制台输入输出**：通过 `std::cin` 和 `std::cout`。
- **文件输入输出**：通过 `std::ifstream` 和 `std::ofstream`。
- **格式化输出**：通过 `std::setw`, `std::setfill`, `std::setprecision` 等控制输出格式。
- **错误输出**：通过 `std::cerr` 和 `std::clog` 输出错误或日志信息。
