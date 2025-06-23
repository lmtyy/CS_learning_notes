是的，**`catch` 块可以同时捕获检查型异常（Checked Exception）和非检查型异常（Unchecked Exception）**，只要它们的类型不同，并且符合 Java 异常处理机制的要求。  

---

## **1. 检查型异常 vs. 非检查型异常**
| 类型 | 特点 | 示例 |
|------|------|------|
| **检查型异常（Checked）** | 必须显式处理（`try-catch` 或 `throws`） | `IOException`, `SQLException` |
| **非检查型异常（Unchecked）** | 不强制处理，通常是程序逻辑错误 | `NullPointerException`, `ArrayIndexOutOfBoundsException` |

---

## **2. `catch` 捕获不同类型异常**
Java 允许一个 `try` 块后跟多个 `catch` 块，每个 `catch` 可以捕获不同类型的异常（包括检查型和非检查型）。  

### **示例代码**
```java
import java.io.*;

public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            // 可能抛出检查型异常（IOException）
            BufferedReader reader = new BufferedReader(new FileReader("file.txt"));
            String line = reader.readLine();

            // 可能抛出非检查型异常（NullPointerException）
            String str = null;
            System.out.println(str.length());

        } catch (IOException e) {  // 捕获检查型异常
            System.err.println("文件读取失败: " + e.getMessage());

        } catch (NullPointerException e) {  // 捕获非检查型异常
            System.err.println("空指针异常: " + e.getMessage());

        } catch (Exception e) {  // 通用捕获（可选，通常放最后）
            System.err.println("其他异常: " + e.getMessage());
        }
    }
}
```

### **输出示例**
- 如果 `file.txt` 不存在 → 触发 `IOException`。
- 如果文件存在但 `str` 为 `null` → 触发 `NullPointerException`。

---

## **3. 关键注意事项**
### **（1）`catch` 块的顺序**
- **子类异常在前，父类异常在后**（否则子类异常会被父类 `catch` 捕获，导致编译错误）。  
  ```java
  try {
      // ...
  } catch (NullPointerException e) {  // 子类
      System.out.println("空指针异常");
  } catch (Exception e) {  // 父类
      System.out.println("通用异常");
  }
  ```
  **❌ 错误写法**（编译失败）：
  ```java
  try {
      // ...
  } catch (Exception e) {  // 父类在前，无法捕获子类异常
      System.out.println("通用异常");
  } catch (NullPointerException e) {  // 子类在后，永远不会执行
      System.out.println("空指针异常");
  }
  ```

### **（2）`catch` 可以同时捕获检查型和非检查型异常**
- **检查型异常**（如 `IOException`）必须显式处理（`try-catch` 或 `throws`）。  
- **非检查型异常**（如 `NullPointerException`）可以捕获，但不是必须的。  

### **（3）`Exception` 是所有异常的父类**
- 如果 `catch (Exception e)` 放在最前面，它会捕获所有异常（包括 `RuntimeException`），通常不建议这样做，除非是日志记录或通用错误处理。

---

## **4. 最佳实践**
- **按需捕获**：只捕获你能处理的异常，避免 `catch (Exception e)` 滥用。  
- **日志记录**：在 `catch` 块中记录异常（如 `e.printStackTrace()` 或使用日志框架）。  
- **资源释放**：使用 `try-with-resources` 或 `finally` 确保资源关闭。  

### **改进版（推荐）**
```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
    System.out.println(line);
} catch (IOException e) {
    System.err.println("文件错误: " + e.getMessage());
} catch (NullPointerException e) {
    System.err.println("空指针错误: " + e.getMessage());
}
```

---

## **5. 总结**
| 问题 | 答案 |
|------|------|
| **`catch` 能否同时捕获检查型和非检查型异常？** | ✅ 可以 |
| **`catch` 块的顺序要求？** | 子类在前，父类在后 |
| **非检查型异常必须捕获吗？** | ❌ 不是必须的，但可以捕获 |
| **`Exception` 能捕获所有异常吗？** | ✅ 能，但通常不建议滥用 |

**结论**：合理使用 `catch` 块可以同时处理检查型和非检查型异常，但要注意捕获顺序和异常处理逻辑！ 🚀