# Java `final` 关键字详解

`final` 是 Java 中一个非常重要的关键字，它可以用于修饰类、方法和变量，具有不同的语义。下面是全面的知识点总结：

## 一、`final` 修饰不同元素的含义

| 修饰目标 | 作用 | 示例 |
|---------|------|------|
| **类** | 表示该类不能被继承 | `final class String {...}` |
| **方法** | 表示该方法不能被子类重写 | `public final void method() {...}` |
| **变量** | 表示该变量只能被赋值一次 | `final int MAX_VALUE = 100;` |

## 二、`final` 修饰变量（最常用）

### 1. 基本类型变量
```java
final int MAX_AGE = 120;
// MAX_AGE = 150;  // 编译错误，不能重新赋值
```

### 2. 引用类型变量
```java
final List<String> names = new ArrayList<>();
names.add("Alice");  // 可以修改内容
// names = new LinkedList<>();  // 编译错误，不能重新赋值
```

### 3. 三种变量类型
- **实例变量**：必须在声明时、构造器或初始化块中赋值
- **静态变量**：必须在声明时或静态初始化块中赋值
- **局部变量**：只需要在使用前赋值即可

## 三、`final` 修饰方法

### 特点：
- 不能被子类重写
- 可以被重载（同名不同参数）
- 可以提高方法调用效率（早期Java版本）

```java
class Parent {
    public final void show() {
        System.out.println("Parent show");
    }
}

class Child extends Parent {
    // @Override public void show() {}  // 编译错误
}
```

## 四、`final` 修饰类

### 特点：
- 类不能被继承
- **所有方法隐式final**（因为不能被继承）
- 常用于工具类、安全敏感类

```java
final class UtilityClass {
    // 工具方法...
}
// class SubClass extends UtilityClass {}  // 编译错误
```

## 五、`final` 的高级用法

### 1. final 参数
```java
void process(final int param) {
    // param = 10;  // 编译错误
}
```

### 2. final 与不可变对象
```java
public final class ImmutablePoint {
    private final int x;
    private final int y;
    
    public ImmutablePoint(int x, int y) {
        this.x = x;
        this.y = y;
    }
    // 只有getter，没有setter
}
```

### 3. final 与多线程
- final 变量可以安全发布（不需要额外同步）
- 适用于构建线程安全对象

## 六、`final` 的常见面试问题

1. final、finally、finalize的区别？
2. 为什么String类被设计为final？
3. final变量一定是线程安全的吗？
4. final方法能被重载吗？
5. 如何创建一个不可变类？

## 七、最佳实践

1. 将不会改变的常量声明为final
2. 设计API时，考虑哪些方法应该禁止重写
3. 安全敏感类应该声明为final
4. 局部变量如果不需要修改，尽量用final修饰（提高可读性）

`final`关键字是Java实现不变性(immutability)和安全性的重要工具，合理使用可以使代码更健壮、更安全。