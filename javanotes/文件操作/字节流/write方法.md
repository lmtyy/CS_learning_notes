在 Java 中，**字节流的 `write()` 方法** 用于将数据写入输出流（如文件、网络等），它是 `OutputStream` 类及其子类的核心方法。与 `read()` 类似，`write()` 也有多种形式，且写入后指针会自动后移。下面详细讲解它的用法和注意事项。

---

## **1. `OutputStream` 中的 `write()` 方法**
`OutputStream` 是字节输出流的抽象基类，定义了 3 种 `write()` 方法：

### **(1) `void write(int b)`**
- **功能**：写入 **单个字节**（低 8 位，高 24 位被忽略）。
- **示例**：
  ```java
  OutputStream os = new FileOutputStream("output.txt");
  os.write(65); // 写入 'A' (ASCII 65)
  os.close();
  ```

### **(2) `void write(byte[] b)`**
- **功能**：写入整个字节数组 `b`。
- **示例**：
  ```java
  byte[] data = {72, 101, 108, 108, 111}; // "Hello" 的 ASCII 码
  OutputStream os = new FileOutputStream("output.txt");
  os.write(data); // 写入整个数组
  os.close();
  ```

### **(3) `void write(byte[] b, int off, int len)`**
- **功能**：从数组 `b` 的 `off` 位置开始，写入 `len` 个字节。
- **示例**：
  ```java
  byte[] data = {72, 101, 108, 108, 111}; // "Hello"
  OutputStream os = new FileOutputStream("output.txt");
  os.write(data, 1, 3); // 写入 "ell" (从索引 1 开始，取 3 字节)
  os.close();
  ```

---

## **2. 文件指针的移动**
- **每次 `write()` 后，文件指针会自动向后移动写入的字节数**：
  - `write(int b)` → 移动 **1 字节**。
  - `write(byte[] b)` → 移动 `b.length` 字节。
  - `write(byte[] b, int off, int len)` → 移动 `len` 字节。
- **示例**：
  ```java
  OutputStream os = new FileOutputStream("output.txt");
  os.write(65);       // 写入 'A'，指针移动到第 2 字节
  os.write(new byte[]{66, 67}); // 写入 'BC'，指针移动到第 4 字节
  os.close();
  ```

---

## **3. 常见子类的 `write()` 方法**
| 类名 | 说明 |
|------|------|
| `FileOutputStream` | 写入文件 |
| `ByteArrayOutputStream` | 写入内存字节数组 |
| `BufferedOutputStream` | 带缓冲的写入，提高性能 |
| `ObjectOutputStream` | 写入序列化对象 |

---

## **4. 注意事项**
### **(1) 必须关闭流或使用 try-with-resources**
```java
// ✅ 推荐方式（自动关闭）
try (OutputStream os = new FileOutputStream("output.txt")) {
    os.write("Hello".getBytes());
} // 自动调用 os.close()
```
如果不关闭流，可能导致：
- **数据未完全写入**（缓冲区的数据可能未刷新）。
- **文件句柄泄漏**（影响系统资源）。

### **(2) 缓冲写入提高性能**
单字节写入 (`write(int b)`) 效率低，建议：
- 使用 `BufferedOutputStream` 包装：
  ```java
  try (OutputStream os = new BufferedOutputStream(new FileOutputStream("output.txt"))) {
      os.write("Hello".getBytes());
  }
  ```
- 或直接写入字节数组：
  ```java
  byte[] data = "Hello".getBytes();
  os.write(data); // 比逐字节写入快
  ```

### **(3) 覆盖 vs. 追加模式**
- **默认覆盖文件**：
  ```java
  new FileOutputStream("output.txt"); // 如果文件存在，内容会被清空
  ```
- **追加模式（`append=true`）**：
  ```java
  new FileOutputStream("output.txt", true); // 新内容追加到文件末尾
  ```

### **(4) 异常处理**
`write()` 可能抛出 `IOException`，需捕获或声明抛出：
```java
try {
    OutputStream os = new FileOutputStream("output.txt");
    os.write(65);
    os.close();
} catch (IOException e) {
    e.printStackTrace();
}
```

---

## **5. 完整示例**
```java
import java.io.*;

public class WriteExample {
    public static void main(String[] args) {
        try (OutputStream os = new FileOutputStream("output.txt", true)) {
            // 写入单个字节
            os.write(72); // 'H'
            
            // 写入字节数组
            byte[] data = "ello".getBytes();
            os.write(data);
            
            // 写入部分数组
            os.write("\nWorld".getBytes(), 1, 4); // "orld"
            
            System.out.println("写入完成！");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
**输出文件内容**：
```
Hello
orld
```

---

## **6. 总结**
| 方法 | 说明 |
|------|------|
| `write(int b)` | 写入单个字节 |
| `write(byte[] b)` | 写入整个字节数组 |
| `write(byte[] b, int off, int len)` | 写入数组的一部分 |
| **指针移动** | 每次 `write()` 后自动后移 |
| **性能优化** | 使用缓冲流 (`BufferedOutputStream`) |
| **关闭流** | 必须调用 `close()` 或使用 try-with-resources |

如果有更具体的需求（如网络流、对象序列化等），可以进一步探讨！