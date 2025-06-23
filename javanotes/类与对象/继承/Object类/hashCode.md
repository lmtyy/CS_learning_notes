# Java中的hashCode

hashCode是Java中Object类的一个方法，它返回对象的哈希码值（一个整数）。哈希码主要用于哈希表数据结构（如HashMap、HashSet等）中，用于快速定位对象。

## 基本概念

1. **定义**：`public native int hashCode();`
   - 是一个native方法，通常基于对象的内存地址或其他因素实现
   - 默认实现通常返回对象内部地址的整数表示

2. **作用**：
   - 提高哈希表（如HashMap、HashSet）的性能
   - 用于快速确定对象在哈希表中的存储位置

## hashCode的重要约定

Java对hashCode方法有三个重要约定：

1. **一致性**：在对象未被修改的情况下，多次调用hashCode()应返回相同的值
2. **相等性**：如果两个对象通过equals()方法相等，那么它们的hashCode必须相同
3. **不等性**：如果两个对象不相等，它们的hashCode不一定不同（但不同可以提升哈希表性能）

## 重写hashCode的准则

当重写equals()方法时，通常也需要重写hashCode()方法以保持上述约定。常用方法：

```java
@Override
public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + (field1 == null ? 0 : field1.hashCode());
    result = prime * result + (field2 == null ? 0 : field2.hashCode());
    return result;
}
```

## 示例

```java
public class Person {
    private String name;
    private int age;
    
    @Override
    public int hashCode() {
        int result = 17;
        result = 31 * result + name.hashCode();
        result = 31 * result + age;
        return result;
    }
    
    @Override
    public boolean equals(Object obj) {
        // equals实现
    }
}
```

## 为什么使用31作为乘数

1. 31是一个奇素数，可以减少哈希冲突
2. 31可以用移位和减法优化：`31 * i == (i << 5) - i`
3. 经验表明31能很好地分散哈希值

## 实际应用

在HashMap中，hashCode用于确定桶(bucket)的位置：

```java
// HashMap中的简化实现
int index = (hash & 0x7FFFFFFF) % table.length;
```

良好的hashCode实现能减少哈希冲突，提高集合类的性能。