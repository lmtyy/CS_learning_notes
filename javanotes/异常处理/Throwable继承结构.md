# Throwable 的继承结构

Throwable 是 Java 异常处理机制中最顶层的类，所有错误和异常都继承自它。以下是完整的继承结构：

```
java.lang.Throwable (实现 Serializable 接口)
├── java.lang.Error (错误，通常不可恢复)
│   ├── VirtualMachineError (虚拟机错误)
│   │   ├── OutOfMemoryError (内存溢出错误)
│   │   ├── StackOverflowError (栈溢出错误)
│   │   └── InternalError (虚拟机内部错误)
│   ├── AssertionError (断言失败错误)
│   ├── LinkageError (链接错误)
│   │   ├── NoClassDefFoundError (类定义未找到错误)
│   │   └── IncompatibleClassChangeError (不兼容类变化错误)
│   └── ...
│
└── java.lang.Exception (异常，可处理)
    ├── RuntimeException (运行时异常/非检查异常)
    │   ├── NullPointerException (空指针异常)
    │   ├── IndexOutOfBoundsException (索引越界异常)
    │   │   ├── ArrayIndexOutOfBoundsException (数组越界异常)
    │   │   └── StringIndexOutOfBoundsException (字符串越界异常)
    │   ├── ClassCastException (类转换异常)
    │   ├── IllegalArgumentException (非法参数异常)
    │   │   └── NumberFormatException (数字格式异常)
    │   ├── IllegalStateException (非法状态异常)
    │   └── ...
    │
    └── 其他 Exception (检查异常)
        ├── IOException (IO异常)
        │   ├── FileNotFoundException (文件未找到异常)
        │   ├── EOFException (文件结束异常)
        │   └── ...
        ├── SQLException (SQL异常)
        ├── InterruptedException (中断异常)
        ├── CloneNotSupportedException (克隆不支持异常)
        └── ...
```

## 关键特点

1. **Throwable** 是所有错误和异常的基类
   - 包含获取异常信息的常用方法：
     ```java
     String getMessage()  // 获取详细消息
     String toString()    // 获取简短描述
     void printStackTrace() // 打印调用栈轨迹
     ```

2. **Error** 表示严重问题，应用程序通常无法恢复
   - 如 `OutOfMemoryError`、`StackOverflowError`
   - 通常不应捕获处理

3. **Exception** 表示应用程序可以处理的异常
   - **RuntimeException**：非检查异常，由程序逻辑错误导致
   - 其他Exception：检查异常，必须处理

## 自定义异常

创建自定义异常时通常继承 `Exception` 或 `RuntimeException`：

```java
// 检查型异常
public class MyCheckedException extends Exception {
    public MyCheckedException(String message) {
        super(message);
    }
}

// 非检查型异常
public class MyUncheckedException extends RuntimeException {
    public MyUncheckedException(String message) {
        super(message);
    }
}
```

理解 Throwable 的继承结构有助于正确选择要捕获和处理的异常类型，以及设计合理的异常处理策略。