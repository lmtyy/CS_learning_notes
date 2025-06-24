# Java 中的 finally 从句详解

`finally` 是 Java 异常处理机制中的一个重要部分，它定义了无论是否发生异常都必须执行的代码块。

## 基本语法

```java
try {
    // 可能抛出异常的代码
} catch (ExceptionType e) {
    // 异常处理代码
} finally {
    // 无论是否发生异常都会执行的代码
}
```

## finally 的特点

1. **必定执行**：无论是否发生异常，finally 块中的代码都会执行
   - 即使 try 或 catch 中有 return 语句
   - 即使 try 或 catch 中抛出新的异常
   - 除非 JVM 退出（如 System.exit()）

2. **执行时机**：
   - 在 try 块正常结束后
   - 在 catch 块处理完异常后
   - 在 try/catch 中的 return 语句执行前

## 典型用途

1. **资源释放** - 最常见的用途

```java
FileInputStream fis = null;
try {
    fis = new FileInputStream("file.txt");
    // 使用文件流...
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fis != null) {
        try {
            fis.close();  // 确保文件流被关闭
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

2. **锁释放** - 确保锁被释放

```java
Lock lock = new ReentrantLock();
try {
    lock.lock();
    // 临界区代码...
} finally {
    lock.unlock();  // 确保锁被释放
}
```

## 特殊场景行为

1. **finally 与 return**

```java
public int testFinally() {
    try {
        return 1;
    } finally {
        return 2;  // 最终返回2，覆盖了try中的return
    }
}
```

2. **finally 中抛出异常**

```java
try {
    // 一些代码
} finally {
    throw new RuntimeException("finally中的异常");  // 会覆盖try/catch中的异常
}
```

## Java 7 改进：try-with-resources

Java 7 引入的 try-with-resources 语法可以替代大多数需要 finally 的场景：

```java
try (FileInputStream fis = new FileInputStream("file.txt");
     BufferedReader br = new BufferedReader(new InputStreamReader(fis))) {
    // 使用资源...
} catch (IOException e) {
    e.printStackTrace();
}
// 不需要显式finally块，资源会自动关闭
```

## 最佳实践

1. **保持 finally 块简洁**：只放必须执行的清理代码
2. **避免在 finally 中抛出异常**：会掩盖原始异常
3. **避免在 finally 中 return**：会覆盖 try/catch 中的返回值
4. **优先使用 try-with-resources**：比手动 finally 更安全简洁
5. **注意 null 检查**：在释放资源前检查是否为 null

finally 是确保资源安全和维护程序健壮性的重要机制，正确使用可以防止资源泄漏和其他清理问题。