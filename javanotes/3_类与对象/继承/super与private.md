在 Java 中，**`super` 关键字不能用来调用父类的私有方法（`private` 方法）**，因为私有方法只能在声明它们的类内部访问，子类无法直接访问父类的私有成员（包括方法和字段）。  

### 关键点：
1. **`private` 方法的访问限制**：
   - `private` 方法是类私有的，只能在**定义它的类内部**访问，子类无法继承或直接调用。
   - `super` 只能访问父类的**非私有成员**（`public`、`protected` 或默认访问权限的方法）。

2. **`super` 的作用**：
   - 用于调用父类的**可继承方法**（非 `private`）。
   - 常用于方法重写（`@Override`）时，调用父类的实现。

---

### 示例验证：
#### ❌ 错误示例：尝试用 `super` 调用父类私有方法（编译错误）
```java
class Parent {
    private void privateMethod() {
        System.out.println("Parent's private method");
    }
}

class Child extends Parent {
    public void callParentPrivateMethod() {
        super.privateMethod(); // ❌ 编译错误：'privateMethod()' has private access in 'Parent'
    }
}
```

#### ✅ 正确示例：调用父类 `protected` 或 `public` 方法
```java
class Parent {
    protected void protectedMethod() {
        System.out.println("Parent's protected method");
    }
}

class Child extends Parent {
    @Override
    protected void protectedMethod() {
        super.protectedMethod(); // ✅ 合法：调用父类的 protected 方法
    }
}
```

---

### 如何间接访问父类私有方法？
如果必须调用父类的私有方法，可以通过以下方式（但违反封装原则，不推荐）：
1. **改为 `protected` 或 `public` 方法**（推荐）。  
2. **使用反射（Reflection）**（破坏封装性，慎用）：
   ```java
   import java.lang.reflect.Method;

   class Parent {
       private void privateMethod() {
           System.out.println("Parent's private method");
       }
   }

   class Child extends Parent {
       public void callPrivateMethod() throws Exception {
           Method method = Parent.class.getDeclaredMethod("privateMethod");
           method.setAccessible(true); // 强制访问私有方法
           method.invoke(this);       // 调用
       }
   }
   ```

---

### 总结：
| 关键字 | 能否调用父类私有方法 | 原因 |
|--------|---------------------|------|
| `super` | ❌ 不能 | `private` 方法对子类不可见 |
| 反射    | ✅ 能（不推荐） | 绕过访问控制，破坏封装 |

**最佳实践**：  
- 如果子类需要调用父类的某个方法，应该将其声明为 `protected` 或 `public`，而不是 `private`。  
- 避免使用反射调用私有方法，除非绝对必要（如框架开发）。