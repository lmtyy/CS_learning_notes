# `getClass()` 和 `getName()` 的区别

在 Java 中，`getClass()` 和 `getName()` 都是与类信息相关的方法，但它们的功能和使用场景有显著区别：

## 1. `getClass()`

**定义**：`Object` 类的方法，所有 Java 对象都继承此方法  
**返回类型**：`Class<?>` 对象  
**作用**：返回对象的运行时类信息  
**特点**：
- 是一个实例方法，需要通过对象调用
- 返回的是完整的类元数据（Class 对象）
- 可以进一步获取类的各种信息（方法、字段、注解等）

```java
String str = "Hello";
Class<?> clazz = str.getClass();  // 返回 String 的 Class 对象
```

## 2. `getName()`

**定义**：`Class` 类的方法  
**返回类型**：`String`  
**作用**：返回类/接口/数组/基本类型的全限定名  
**特点**：
- 是 Class 对象的方法
- 返回的是字符串形式的类名
- 有多个变体方法：
  - `getSimpleName()`：不包含包名
  - `getCanonicalName()`：规范名称
  - `getTypeName()`：JDK 8 新增

```java
Class<?> clazz = String.class;
String name = clazz.getName();  // 返回 "java.lang.String"
```

## 对比表格

| 特性                | getClass()                     | getName()                     |
|---------------------|-------------------------------|-------------------------------|
| **所属类**          | Object                        | Class                         |
| **调用方式**        | 对象实例调用                  | Class 对象调用                |
| **返回类型**        | Class<?>                      | String                        |
| **典型返回值**      | class java.lang.String        | "java.lang.String"            |
| **是否包含包名**    | 是（通过 toString() 显示）    | 是                            |
| **主要用途**        | 获取类元数据                  | 获取类名字符串                |

## 使用示例

```java
public class Test {
    public static void main(String[] args) {
        String str = "Example";
        
        // getClass() 使用
        Class<?> strClass = str.getClass();
        System.out.println(strClass);  // 输出: class java.lang.String
        
        // getName() 使用
        System.out.println(strClass.getName());      // java.lang.String
        System.out.println(strClass.getSimpleName()); // String
        System.out.println(strClass.getTypeName());   // java.lang.String
        
        // 基本类型
        System.out.println(int.class.getName());      // int
    }
}
```

## 关键区别总结

1. **层次不同**：
   - `getClass()` 是对象→类
   - `getName()` 是类→名字符串

2. **信息量不同**：
   - `Class` 对象包含完整的类信息（方法、字段等）
   - `getName()` 只返回名称字符串

3. **使用场景**：
   - 需要反射操作时用 `getClass()`
   - 只需要类名时用 `getName()`

理解这两个方法的区别对于Java反射机制和日志记录等场景非常重要。