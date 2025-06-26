# Java StringBuilder 类详解

`StringBuilder` 是 Java 中一个可变的字符序列，用于高效地进行字符串操作。与不可变的 `String` 类相比，`StringBuilder` 在频繁修改字符串时性能更高。

## 1. 为什么需要 StringBuilder

- **String 的不可变性**：每次修改 String 都会创建新对象，效率低
- **StringBuilder 的可变性**：内部维护可变字符数组，直接修改而不创建新对象
- **性能优势**：在大量字符串拼接操作时，StringBuilder 比 String 的 "+" 操作快很多

## 2. 主要构造方法

```java
// 构造一个初始容量为16的空StringBuilder
StringBuilder sb1 = new StringBuilder();

// 构造指定初始容量的StringBuilder
StringBuilder sb2 = new StringBuilder(50);

// 构造包含指定字符串内容的StringBuilder
StringBuilder sb3 = new StringBuilder("Hello");
```

## 3. 核心方法

### 追加内容 (append)

```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" ").append("World"); // Hello World
sb.append(123); // Hello World123
```

支持追加各种类型：`String`, `char`, `int`, `double`, `boolean`, `Object` 等

### 插入内容 (insert)

```java
StringBuilder sb = new StringBuilder("HelloWorld");
sb.insert(5, " "); // 在索引5处插入空格 → "Hello World"
```

### 删除内容 (delete)

```java
StringBuilder sb = new StringBuilder("HelloWorld");
sb.delete(5, 10); // 删除索引5-9 → "Hello"
```

### 替换内容 (replace)

```java
StringBuilder sb = new StringBuilder("HelloWorld");
sb.replace(5, 10, " Java"); // Hello Java
```

### 反转字符串 (reverse)

```java
StringBuilder sb = new StringBuilder("Hello");
sb.reverse(); // olleH
```

### 其他实用方法

```java
// 获取长度
int len = sb.length();

// 获取当前容量
int capacity = sb.capacity();

// 设置长度
sb.setLength(10);

// 确保最小容量
sb.ensureCapacity(100);

// 获取指定位置的字符
char ch = sb.charAt(2);

// 设置指定位置的字符
sb.setCharAt(2, 'X');

// 删除指定位置的字符
sb.deleteCharAt(2);
```

## 4. 性能特点

- **非线程安全**：StringBuilder 不是线程安全的，但在单线程环境下性能更好
- **自动扩容**：当容量不足时，会自动扩容（通常是当前容量的2倍+2）
- **最佳实践**：预估所需容量初始化，避免频繁扩容

## 5. 与 StringBuffer 的比较

| 特性          | StringBuilder | StringBuffer |
|-------------|--------------|--------------|
| 线程安全       | 否            | 是           |
| 性能          | 更高          | 稍低         |
| 引入版本       | Java 5        | Java 1.0     |

## 6. 使用示例

```java
public class StringBuilderExample {
    public static void main(String[] args) {
        // 创建StringBuilder
        StringBuilder sb = new StringBuilder();
        
        // 链式调用
        sb.append("Java")
          .append(" ")
          .append("Programming")
          .append(" ")
          .append(2023);
        
        System.out.println(sb.toString()); // Java Programming 2023
        
        // 插入内容
        sb.insert(5, "Awesome ");
        System.out.println(sb.toString()); // Java Awesome Programming 2023
        
        // 替换内容
        sb.replace(20, 31, "Language");
        System.out.println(sb.toString()); // Java Awesome Language 2023
        
        // 反转
        sb.reverse();
        System.out.println(sb.toString()); // 3202 egaugnaL emosewA avaJ
    }
}
```

## 7. 最佳实践

1. **在循环中使用 StringBuilder**：避免在循环中使用 String 的 "+" 操作
   ```java
   // 不好的做法
   String result = "";
   for (int i = 0; i < 100; i++) {
       result += i; // 每次循环创建新String对象
   }
   
   // 好的做法
   StringBuilder sb = new StringBuilder();
   for (int i = 0; i < 100; i++) {
       sb.append(i);
   }
   ```

2. **预估初始容量**：减少扩容次数
   ```java
   StringBuilder sb = new StringBuilder(1024); // 预估大容量
   ```

3. **复用 StringBuilder**：对于频繁操作，可以清空后复用
   ```java
   sb.setLength(0); // 清空内容，保留容量
   ```

StringBuilder 是 Java 中处理可变字符串的高效工具，特别适合需要频繁修改字符串内容的场景。