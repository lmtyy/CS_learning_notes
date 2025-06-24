# 迭代器的 `hasNext()` 和 `next()` 方法对迭代器位置的影响

在 Java 迭代器（`Iterator`）中，这两个方法的行为不同：

## `hasNext()` 方法
- **不会移动迭代器**
- 仅检查是否还有更多元素可供遍历
- 是一个无副作用的查询方法
- 示例：
  ```java
  Iterator<String> it = list.iterator();
  while(it.hasNext()) {  // 只是检查，不移动位置
      String item = it.next();  // 实际移动位置
  }
  ```

## `next()` 方法
- **会移动迭代器**到下一个元素
- 返回当前元素并将迭代器位置向前移动
- 如果调用时没有下一个元素会抛出 `NoSuchElementException`
- 示例：
  ```java
  Iterator<String> it = list.iterator();
  String first = it.next();  // 移动到第一个元素
  String second = it.next(); // 移动到第二个元素
  ```

## 典型使用模式
```java
List<String> list = Arrays.asList("A", "B", "C");
Iterator<String> iterator = list.iterator();

while(iterator.hasNext()) {  // 检查但不移动
    String element = iterator.next();  // 获取并移动
    System.out.println(element);
}
```

## 重要区别
| 方法       | 移动迭代器位置 | 可能抛出异常       | 主要用途               |
|------------|----------------|--------------------|------------------------|
| `hasNext()` | 否             | 无                 | 检查是否还有元素       |
| `next()`    | 是             | `NoSuchElementException` | 获取元素并前进到下一个 |

因此，在迭代过程中，`next()` 是实际导致迭代器位置移动的方法，而 `hasNext()` 只是进行安全检查。