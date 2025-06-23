学习Java面向对象编程时，了解其与C++的语法差异能帮助你更快上手。以下是两者在面向对象语法上的主要区别：

### 1. 类与对象
- **C++**:
  ```cpp
  class MyClass {
  public:
      int myVar;
      void myMethod() {
          // 方法实现
      }
  };
  ```
- **Java**:
  ```java
  public class MyClass {
      public int myVar;
      public void myMethod() {
          // 方法实现
      }
  }
  ```
  **区别**:
  - Java中类默认是`public`，C++中默认是`private`。
  - Java方法默认是`public`，C++中默认是`private`。

### 2. 访问控制
- **C++**:
  ```cpp
  class MyClass {
  private:
      int privateVar;
  protected:
      int protectedVar;
  public:
      int publicVar;
  };
  ```
- **Java**:
  ```java
  public class MyClass {
      private int privateVar;
      protected int protectedVar;
      public int publicVar;
  }
  ```
  **区别**:
  - Java的访问控制符与C++类似，但Java没有`friend`关键字。

### 3. 继承
- **C++**:
  ```cpp
  class Base {
  public:
      void baseMethod() {}
  };
  class Derived : public Base {
  public:
      void derivedMethod() {}
  };
  ```
- **Java**:
  ```java
  public class Base {
      public void baseMethod() {}
  }
  public class Derived extends Base {
      public void derivedMethod() {}
  }
  ```
  **区别**:
  - Java使用`extends`关键字，C++使用冒号`:`。
  - Java不支持多继承，但可通过接口实现类似功能。

### 4. 多态
- **C++**:
  ```cpp
  class Base {
  public:
      virtual void myMethod() {
          // 基类实现
      }
  };
  class Derived : public Base {
  public:
      void myMethod() override {
          // 派生类实现
      }
  };
  ```
- **Java**:
  ```java
  public class Base {
      public void myMethod() {
          // 基类实现
      }
  }
  public class Derived extends Base {
      @Override
      public void myMethod() {
          // 派生类实现
      }
  }
  ```
  **区别**:
  - Java默认支持多态，C++需要`virtual`关键字。
  - Java使用`@Override`注解，C++使用`override`关键字。

### 5. 接口
- **C++**:
  C++没有接口，但可通过纯虚函数模拟：
  ```cpp
  class MyInterface {
  public:
      virtual void myMethod() = 0;
  };
  ```
- **Java**:
  ```java
  public interface MyInterface {
      void myMethod();
  }
  public class MyClass implements MyInterface {
      @Override
      public void myMethod() {
          // 实现
      }
  }
  ```
  **区别**:
  - Java有专门的`interface`关键字，C++通过纯虚函数模拟。

### 6. 内存管理
- **C++**:
  ```cpp
  MyClass* obj = new MyClass();
  delete obj;
  ```
- **Java**:
  ```java
  MyClass obj = new MyClass();
  // 不需要手动释放内存
  ```
  **区别**:
  - Java有垃圾回收机制，无需手动释放内存。

### 7. 异常处理
- **C++**:
  ```cpp
  try {
      // 可能抛出异常的代码
  } catch (MyException& e) {
      // 处理异常
  }
  ```
- **Java**:
  ```java
  try {
      // 可能抛出异常的代码
  } catch (MyException e) {
      // 处理异常
  }
  ```
  **区别**:
  - Java的异常处理与C++类似，但Java要求捕获或声明所有受检异常。

### 8. 标准库
- **C++**:
  ```cpp
  #include <iostream>
  int main() {
      std::cout << "Hello, World!" << std::endl;
      return 0;
  }
  ```
- **Java**:
  ```java
  public class Main {
      public static void main(String[] args) {
          System.out.println("Hello, World!");
      }
  }
  ```
  **区别**:
  - Java使用`System.out.println`，C++使用`std::cout`。

### 9. 文件结构
- **C++**:
  - 头文件（`.h`）和源文件（`.cpp`）分开。
- **Java**:
  - 每个类一个文件，文件名与类名一致。

### 10. 包与命名空间
- **C++**:
  ```cpp
  namespace MyNamespace {
      class MyClass {};
  }
  ```
- **Java**:
  ```java
  package mypackage;
  public class MyClass {}
  ```
  **区别**:
  - Java使用`package`，C++使用`namespace`。

### 总结
- Java更简洁，垃圾回收机制减轻了内存管理负担。
- Java不支持多继承，但接口提供了类似功能。
- Java的异常处理更严格，要求处理所有受检异常。

掌握这些区别后，你能更快适应Java的面向对象编程。