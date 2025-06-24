在 Java 中，**`Throwable` 是一个类（class）**，而不是接口（interface）。它是 Java 异常处理体系的**根类**，所有错误（`Error`）和异常（`Exception`）都继承自 `Throwable`。

---

### **关键点说明**
1. **`Throwable` 是类，不是接口**  
   - 定义在 `java.lang` 包中，是 Java 异常和错误的顶层父类。
   - 直接子类包括：
     - **`Error`**（严重错误，如 `OutOfMemoryError`，通常程序无法恢复）。
     - **`Exception`**（可检查异常，如 `IOException`，必须处理或声明抛出）。

2. **继承关系示例**
   ```java
   // Throwable 的继承体系
   class Throwable { ... }
   class Exception extends Throwable { ... }
   class IOException extends Exception { ... }
   class Error extends Throwable { ... }
   class OutOfMemoryError extends Error { ... }
   ```

3. **`Throwable` 的核心方法**  
   - `getMessage()`：获取异常信息。
   - `printStackTrace()`：打印异常堆栈跟踪。
   - `getCause()`：返回引发当前异常的根源（链式异常）。

---

### **为什么 `Throwable` 是类而不是接口？**
- **需要状态和方法实现**：异常类通常包含错误信息、堆栈跟踪等状态，并提供方法（如 `printStackTrace()`），这些必须通过类实现。
- **类型系统统一性**：所有异常和错误需共享公共行为（如捕获机制 `catch (Throwable t)`），类继承能更好地满足这一需求。

---

### **常见误区**
- **误区**：“`Throwable` 是接口，因为异常可以被 `catch`？”  
  **纠正**：能被 `catch` 捕获的是类实例（如 `Exception`），而接口不能实例化。`Throwable` 作为类，其子类对象才能被抛出或捕获。

---

### **总结**
`Throwable` 是 Java 异常处理的**基类**，`Error` 和 `Exception` 均继承自它。它的类设计（而非接口）确保了异常体系的状态存储、方法实现和类型统一性。