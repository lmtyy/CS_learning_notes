# 讲解 `TestDemo1` 和 `TestDemo2` 的区别

这两个类的主要区别在于它们实现迭代功能的方式不同，关键区别在于是否实现了 `Iterable` 接口。

## `TestDemo1` 分析

```java
class TestDemo1 {
    ArrayList<Product> ps = new ArrayList<Product>();
    public Iterator<Product> iterator() {
        return ps.iterator();
    }
}
```

特点：
1. 只是一个普通类，没有实现任何特定接口
2. 提供了 `iterator()` 方法，返回列表的迭代器
3. 不能直接用在增强 for 循环中（除非额外实现 `Iterable`）
4. 调用迭代功能需要显式调用 `iterator()` 方法

## `TestDemo2` 分析

```java
class TestDemo2 implements Iterable<Product> {
    ArrayList<Product> ps = new ArrayList<Product>();
    @Override
    public Iterator<Product> iterator() {
        return ps.iterator();
    }
}
```

特点：
1. 显式实现了 `Iterable<Product>` 接口
2. 同样提供了 `iterator()` 方法，返回列表的迭代器
3. 可以直接用在增强 for 循环中（因为实现了 `Iterable`）
4. 是 Java 集合框架的标准做法

## 主要区别

1. **接口实现**：
   - `TestDemo2` 实现了 `Iterable` 接口，而 `TestDemo1` 没有
   
2. **使用场景**：
   - `TestDemo2` 可以直接用于增强 for 循环：
     ```java
     for(Product p : new TestDemo2()) { ... }
     ```
   - `TestDemo1` 不能这样用，除非手动获取迭代器

3. **设计意图**：
   - `TestDemo2` 明确表示这是一个可迭代的集合类
   - `TestDemo1` 只是恰巧提供了迭代功能，但没有明确声明这一能力

4. **类型系统**：
   - `TestDemo2` 可以被识别为 `Iterable` 类型，可以用于需要 `Iterable` 参数的方法
   - `TestDemo1` 不能这样使用

## 最佳实践

在 Java 中，如果你想让你的类支持增强 for 循环或者希望明确表示你的类是可迭代的，应该实现 `Iterable` 接口（如 `TestDemo2` 的做法）。这是 Java 集合框架的标准模式。