# Java中的`throw`关键字

`throw`是Java中用于**主动抛出异常**的关键字，与`throws`不同，它不是声明可能抛出的异常，而是实际创建一个异常对象并将其抛出。

## 基本语法

```java
throw new 异常类型([错误信息]);
```

## 主要特点

1. **主动抛出异常**：用于在满足特定条件时主动中断程序正常流程
2. **可以抛出任何Throwable对象**：包括Exception和Error及其子类
3. **执行throw后，方法立即终止**（除非被捕获）

## 使用示例

### 基础用法

```java
public void checkAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("年龄不能为负数");
    }
    if (age < 18) {
        throw new ArithmeticException("未成年人禁止访问");
    }
    System.out.println("欢迎访问");
}
```

### 抛出自定义异常

```java
class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) {
        throw new InsufficientFundsException("余额不足，当前余额: " + balance);
    }
    balance -= amount;
}
```

### 重新抛出异常

```java
public void process() throws IOException {
    try {
        // 可能抛出IOException的代码
    } catch (IOException e) {
        System.err.println("处理过程中发生错误");
        throw e; // 重新抛出捕获的异常
    }
}
```

## 与`throws`的区别

| 特性        | throw                          | throws                         |
|------------|--------------------------------|--------------------------------|
| **作用**    | 主动抛出异常对象               | 声明方法可能抛出的异常类型      |
| **位置**    | 方法体内                       | 方法签名中                     |
| **数量**    | 一次只能抛出一个异常对象       | 可以声明多个异常类型           |
| **语法**    | `throw new Exception();`       | `throws Exception1, Exception2`|

## 最佳实践

1. **提供有意义的错误信息**：
   ```java
   // 不好的做法
   throw new Exception("错误发生");
   
   // 好的做法
   throw new IllegalArgumentException("参数userId不能为null或空字符串");
   ```

2. **选择合适的异常类型**：
   - 使用Java内置的标准异常（如IllegalArgumentException）
   - 或创建业务相关的自定义异常

3. **避免过度使用**：
   - 不要用异常处理常规控制流
   - 只在真正异常情况下使用

4. **保持异常不变性**：
   ```java
   try {
       // 某些操作
   } catch (SomeException e) {
       // 记录日志等
       throw new MyDomainException("业务处理失败", e); // 保留原始异常
   }
   ```

## 常见应用场景

1. 参数校验失败时
2. 业务规则违反时
3. 资源不可用时
4. 作为方法前置条件检查
5. 在catch块中转换异常类型

`throw`关键字是Java异常处理机制的核心部分，合理使用可以使代码更健壮，错误处理更清晰。