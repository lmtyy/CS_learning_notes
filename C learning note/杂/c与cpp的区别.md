C 和 C++ 在基础语法上有很多相似之处，因为 C++ 是从 C 语言发展而来的，但 C++ 引入了许多增强的特性，特别是在面向对象编程（OOP）、类型安全、模板、异常处理等方面。下面我们详细比较 C 和 C++ 在基础语法上的差别：

---

### 1. **程序结构**

#### C 语言
在 C 语言中，程序通常是通过 `main()` 函数作为入口点。程序的结构非常简单，主要依赖过程化编程。

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

#### C++ 语言
C++ 继承了 C 语言的结构，但支持类（class）、对象（object）、构造函数（constructor）、析构函数（destructor）等面向对象编程的基本特性。在 C++ 中，程序的基本结构也可以从 `main()` 开始，但通常会涉及到类和对象的定义。

```cpp
#include <iostream>
using namespace std;

class MyClass {
public:
    void greet() {
        cout << "Hello, World!" << endl;
    }
};

int main() {
    MyClass obj;
    obj.greet();
    return 0;
}
```

### 2. **输入输出**

#### C 语言
在 C 语言中，输入输出通过 `stdio.h` 提供的 `printf` 和 `scanf` 函数来实现。

```c
#include <stdio.h>

int main() {
    int x;
    printf("Enter a number: ");
    scanf("%d", &x);
    printf("You entered: %d\n", x);
    return 0;
}
```

#### C++ 语言
C++ 引入了更为现代的输入输出流库，`iostream`，通过 `cin` 和 `cout` 实现输入输出。C++ 的流式输入输出支持类型安全、重载等特性。

```cpp
#include <iostream>
using namespace std;

int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;
    cout << "You entered: " << x << endl;
    return 0;
}
```

### 3. **函数声明和定义**

#### C 语言
在 C 语言中，函数声明需要指定返回类型和参数类型，且没有函数重载的机制。

```c
#include <stdio.h>

void greet();   // 函数声明

int main() {
    greet();
    return 0;
}

void greet() {   // 函数定义
    printf("Hello, World!\n");
}
```

#### C++ 语言
C++ 允许函数重载，即同名函数可以根据参数的不同类型或数量进行区分。

```cpp
#include <iostream>
using namespace std;

void greet() {
    cout << "Hello, World!" << endl;
}

void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

int main() {
    greet();
    greet("Alice");
    return 0;
}
```

### 4. **类型系统与类型安全**

#### C 语言
C 语言是一个相对简单的语言，其类型系统不如 C++ 强大。例如，C 语言没有 `class` 和 `struct` 之间的访问控制，不支持继承、多态等面向对象特性。

#### C++ 语言
C++ 提供了丰富的类型系统，支持 `class`、`struct`、继承、虚函数、多态、模板等面向对象和泛型编程的特性。例如，C++ 支持 `private`、`protected` 和 `public` 等访问控制符。

```cpp
#include <iostream>
using namespace std;

class MyClass {
private:
    int secret;

public:
    MyClass() : secret(42) {}
    void revealSecret() {
        cout << "The secret is: " << secret << endl;
    }
};

int main() {
    MyClass obj;
    obj.revealSecret();
    return 0;
}
```

### 5. **内存管理**

#### C 语言
在 C 中，内存管理主要通过 `malloc` 和 `free` 来进行。C 语言没有构造函数和析构函数，因此必须手动分配和释放内存。

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int* ptr = (int*)malloc(sizeof(int));  // 动态内存分配
    *ptr = 10;
    printf("%d\n", *ptr);
    free(ptr);  // 手动释放内存
    return 0;
}
```

#### C++ 语言
C++ 引入了 `new` 和 `delete` 操作符，用于动态内存分配和释放。此外，C++ 支持构造函数和析构函数，自动管理对象生命周期。

```cpp
#include <iostream>
using namespace std;

int main() {
    int* ptr = new int;  // 动态内存分配
    *ptr = 10;
    cout << *ptr << endl;
    delete ptr;  // 自动释放内存
    return 0;
}
```

### 6. **结构体（struct）和类（class）**

#### C 语言
在 C 中，`struct` 是唯一的一种复合数据类型，不能包含函数（方法）。

```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p = {10, 20};
    printf("Point: (%d, %d)\n", p.x, p.y);
    return 0;
}
```

#### C++ 语言
在 C++ 中，`struct` 仍然是一个数据容器，但 `class` 引入了访问控制、构造函数、析构函数等功能。`class` 默认是 `private`，而 `struct` 默认是 `public`。

```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y;

public:
    Point(int a, int b) : x(a), y(b) {}

    void display() {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p(10, 20);
    p.display();
    return 0;
}
```

### 7. **命名空间（namespace）**

#### C 语言
C 语言没有命名空间的概念，所有的符号（变量、函数、宏等）都在全局作用域中定义，容易发生命名冲突。

#### C++ 语言
C++ 引入了命名空间（`namespace`）的概念，用于避免命名冲突。命名空间可以封装函数、变量等符号。

```cpp
#include <iostream>
using namespace std;

namespace Math {
    int add(int a, int b) {
        return a + b;
    }
}

int main() {
    cout << "Sum: " << Math::add(3, 4) << endl;
    return 0;
}
```

### 8. **异常处理**

#### C 语言
C 语言本身没有内建的异常处理机制。错误处理通常通过返回值和 `errno` 来进行。

```c
#include <stdio.h>
#include <stdlib.h>

int divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero\n");
        return -1; // 错误处理
    }
    return a / b;
}

int main() {
    int result = divide(10, 0);
    if (result == -1) {
        // 错误处理
    }
    return 0;
}
```

#### C++ 语言
C++ 引入了异常处理机制，使用 `try`、`catch` 和 `throw` 关键字来处理异常。

```cpp
#include <iostream>
using namespace std;

int divide(int a, int b) {
    if (b == 0) {
        throw "Division by zero error";
    }
    return a / b;
}

int main() {
    try {
        int result = divide(10, 0);
        cout << "Result: " << result << endl;
    } catch (const char* msg) {
        cout << "Error: " << msg << endl;
    }
    return 0;
}
```

---

### 总结

C 和 C++ 在基础语法上有很多相似之处，但 C++ 引入了许多增强特性，如面向对象编程、类型安全、异常处理、模板、命名空间等。这些特性使得 C++ 在编写更复杂的程序时更加灵活和强大，但也增加了学习和使用的复杂性。

| 特性           | C 语言                                   | C++ 语言                               |
|----------------|------------------------------------------|----------------------------------------|
| 输入输出       | `printf` 和 `scanf`                      | `cout` 和 `cin`                        |
| 面向对象       | 不支持                                   | 支持类（class）、继承、多态、虚函数等 |
| 内存管理       | 使用 `malloc` 和 `free`                 | 使用 `new` 和 `delete`                |
| 函数重载       | 不支持                                   | 支持                                   |
| 异常处理

       | 不支持                                   | 支持 `try-catch`                       |
| 命名空间       | 不支持                                   | 支持                                   |
| 类型安全       | 较弱                                     | 较强，支持类型检查和重载             |

C++ 是 C 的超集，除了保留 C 的所有功能，还引入了许多新的特性，主要目的是支持更高效、更灵活的编程方式，尤其是在大型软件开发中。