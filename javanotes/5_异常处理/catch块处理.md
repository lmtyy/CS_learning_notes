# Java catch 块中的异常处理内容

在 catch 块中，你应该编写能够适当处理异常的代码。以下是 catch 块中常见的处理方式和最佳实践：

## 1. 记录日志（最常见做法）

```java
try {
    // 业务代码
} catch (IOException e) {
    logger.error("文件操作失败: " + e.getMessage(), e);
}
```

**最佳实践**：
- 使用专业的日志框架（如SLF4J+Logback）
- 记录完整的异常堆栈（包括cause）
- 添加上下文信息（如操作的文件名、用户ID等）

## 2. 抛出业务异常（异常转换）

```java
try {
    // 数据库操作
} catch (SQLException e) {
    throw new BusinessException("数据库操作失败", e);
}
```

**适用场景**：
- 将底层技术异常转换为业务层异常
- 隐藏技术细节，暴露业务相关错误信息

## 3. 返回默认值或替代结果

```java
public String readConfig(String key) {
    try {
        return configStore.read(key);
    } catch (ConfigNotFoundException e) {
        return DEFAULT_VALUES.get(key); // 返回默认值
    }
}
```

**适用场景**：
- 当异常情况有合理的默认处理方式时
- 不影响核心业务流程的次要操作

## 4. 重试机制

```java
int retries = 3;
while (retries > 0) {
    try {
        return remoteService.call();
    } catch (TimeoutException e) {
        retries--;
        if (retries == 0) {
            throw new ServiceUnavailableException("服务不可用", e);
        }
        Thread.sleep(1000); // 延迟后重试
    }
}
```

## 5. 资源清理和回滚

```java
Connection conn = null;
try {
    conn = getConnection();
    // 业务操作
} catch (SQLException e) {
    if (conn != null) {
        try {
            conn.rollback(); // 事务回滚
        } catch (SQLException rollbackEx) {
            logger.error("回滚失败", rollbackEx);
        }
    }
    throw new DataAccessException("数据库操作失败", e);
} finally {
    closeQuietly(conn); // 资源释放
}
```

## 6. 用户友好的错误提示

```java
try {
    processUserRequest(request);
} catch (InvalidInputException e) {
    showUserAlert("输入无效: " + e.getUserFriendlyMessage());
    return ErrorResponse.withMessage(e.getUserFriendlyMessage());
}
```

## 7. 组合处理（常见模式）

```java
try {
    // 业务代码
} catch (BusinessException e) {
    // 已知业务异常，直接抛出
    throw e;
} catch (TechnicalException e) {
    // 技术异常，记录后转换
    logger.error("技术异常", e);
    throw new ServiceException("服务暂时不可用");
} catch (Exception e) {
    // 未知异常，记录后包装
    logger.error("未知异常", e);
    throw new SystemException("系统错误");
}
```

## 应该避免的做法

1. **空的catch块**（静默吞掉异常）：
   ```java
   try {
       doSomething();
   } catch (Exception e) {
       // 绝对不要这样做！
   }
   ```

2. **仅打印堆栈跟踪**（生产环境无效）：
   ```java
   catch (Exception e) {
       e.printStackTrace(); // 生产环境看不到控制台输出
   }
   ```

3. **过于宽泛的异常捕获**：
   ```java
   catch (Exception e) { // 太宽泛
       // ...
   }
   ```

## 最佳实践总结

1. **针对性捕获**：捕获最具体的异常类型
2. **完整记录**：记录异常和上下文信息
3. **合理处理**：根据异常类型选择适当处理方式
4. **资源安全**：确保资源被正确释放
5. **用户友好**：向最终用户提供有意义的错误信息
6. **异常转换**：将底层异常转换为高层抽象

记住：catch块的目的是"处理"异常，而不仅仅是"捕获"异常。应该根据具体业务场景决定如何处理每种异常情况。