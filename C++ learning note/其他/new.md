在C++中，`new` 操作符用于在**堆（Heap）**上动态分配内存。与在栈上分配内存（如局部变量）不同，使用 `new` 分配的内存需要手动释放，以避免内存泄漏。以下是 `new` 的基本用法及相关知识点。

## 1. `new` 的基本语法

### 1.1 分配单个对象

```cpp
类型* 指针变量 = new 类型;
```

**示例：**

```cpp
#include <iostream>

int main() {
    int* p = new int;    // 在堆上分配一个int
    *p = 10;             // 赋值
    std::cout << *p << std::endl; // 输出：10
    delete p;            // 释放内存
    return 0;
}
```

### 1.2 分配并初始化单个对象

```cpp
类型* 指针变量 = new 类型(构造参数);
```

**示例：**

```cpp
#include <iostream>
#include <string>

class Person {
public:
    std::string name;
    int age;

    Person(const std::string& n, int a) : name(n), age(a) {}
};

int main() {
    Person* p = new Person("Alice", 30);
    std::cout << p->name << " is " << p->age << " years old." << std::endl;
    delete p; // 释放内存
    return 0;
}
```

### 1.3 分配数组

```cpp
类型* 指针变量 = new 类型[数组大小];
```

**示例：**

```cpp
#include <iostream>

int main() {
    int* arr = new int[5]; // 在堆上分配一个包含5个int的数组
    for(int i = 0; i < 5; ++i) {
        arr[i] = i * 2;
    }
    for(int i = 0; i < 5; ++i) {
        std::cout << arr[i] << " "; // 输出：0 2 4 6 8
    }
    std::cout << std::endl;
    delete[] arr; // 释放数组内存
    return 0;
}
```

## 2. `delete` 的基本用法

与 `new` 相对应，`delete` 用于释放由 `new` 分配的内存。

### 2.1 释放单个对象

```cpp
delete 指针变量;
```

**示例：**

```cpp
int* p = new int(5);
// 使用 p
delete p; // 释放内存
p = nullptr; // 避免悬挂指针
```

### 2.2 释放数组

```cpp
delete[] 指针变量;
```

**示例：**

```cpp
int* arr = new int[10];
// 使用 arr
delete[] arr; // 释放数组内存
arr = nullptr; // 避免悬挂指针
```

## 3. 注意事项

### 3.1 内存泄漏

使用 `new` 分配的内存如果未使用 `delete` 释放，将导致内存泄漏。确保每一个 `new` 都有对应的 `delete`。

**示例：**

```cpp
void leakMemory() {
    int* p = new int(10);
    // 忘记 delete p; 会导致内存泄漏
}
```

### 3.2 避免重复释放

对同一个指针调用多次 `delete` 会导致未定义行为。释放后将指针置为 `nullptr` 可以避免这种情况。

**示例：**

```cpp
int* p = new int(10);
delete p;
p = nullptr; // 再次 delete p 就是安全的，因为 p 是 nullptr
```

### 3.3 异常处理

如果 `new` 无法分配内存，会抛出 `std::bad_alloc` 异常。可以使用 `try-catch` 块进行处理。

**示例：**

```cpp
#include <iostream>
#include <new> // 包含 std::bad_alloc

int main() {
    try {
        int* p = new int[1000000000000]; // 可能抛出异常
    }
    catch (const std::bad_alloc& e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
    }
    return 0;
}
```

## 4. `new` 与 `malloc` 的区别

虽然 `new` 和 `malloc` 都用于动态内存分配，但有以下区别：

- **类型安全**：`new` 返回指定类型的指针，无需类型转换；`malloc` 返回 `void*`，需要进行类型转换。
- **构造函数调用**：`new` 在分配内存后会调用对象的构造函数；`malloc` 仅分配内存，不调用构造函数。
- **异常处理**：`new` 分配失败时会抛出异常；`malloc` 返回 `nullptr`。
- **释放内存**：`new` 使用 `delete` 释放，`malloc` 使用 `free` 释放，二者不可混用。

**示例：**

```cpp
#include <iostream>
#include <cstdlib> // 包含 malloc 和 free

class MyClass {
public:
    MyClass() { std::cout << "Constructor called." << std::endl; }
    ~MyClass() { std::cout << "Destructor called." << std::endl; }
};

int main() {
    // 使用 new
    MyClass* obj1 = new MyClass();
    delete obj1;

    // 使用 malloc
    MyClass* obj2 = (MyClass*)malloc(sizeof(MyClass));
    if(obj2) {
        // 需要手动调用构造函数
        new(obj2) MyClass();
        // 需要手动调用析构函数
        obj2->~MyClass();
        free(obj2);
    }

    return 0;
}
```

## 5. C++11 及以后的智能指针

虽然 `new` 和 `delete` 是动态内存管理的基础，但现代C++推荐使用智能指针（如 `std::unique_ptr` 和 `std::shared_ptr`）来自动管理内存，避免手动 `delete` 带来的风险。

**示例：**

```cpp
#include <iostream>
#include <memory>

class MyClass {
public:
    MyClass() { std::cout << "Constructor called." << std::endl; }
    ~MyClass() { std::cout << "Destructor called." << std::endl; }
};

int main() {
    std::unique_ptr<MyClass> ptr1 = std::make_unique<MyClass>();
    // 无需手动 delete，超出作用域时自动释放

    std::shared_ptr<MyClass> ptr2 = std::make_shared<MyClass>();
    // 多个shared_ptr可以共享同一资源，引用计数为0时自动释放

    return 0;
}
```

**优势：**

- 自动内存管理，避免内存泄漏
- 异常安全
- 更简洁和安全的代码

## 6. 小结

- `new` 用于在堆上动态分配内存，适用于需要在运行时决定对象数量和生命周期的场景。
- 每一个 `new` 都应有对应的 `delete`，以防止内存泄漏。
- 使用智能指针（如 `std::unique_ptr` 和 `std::shared_ptr`）可以更安全地管理动态内存，推荐在现代C++中使用。
- 理解 `new` 与 `malloc` 的区别有助于更好地进行内存管理。

掌握 `new` 的基本用法对于编写高效和安全的C++程序至关重要。