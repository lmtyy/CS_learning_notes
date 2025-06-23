# Java Arrays 类常用操作详解

`java.util.Arrays` 类是 Java 中用于操作数组的实用工具类，提供了各种静态方法来处理数组。以下是 Arrays 类的常用操作分类详解：

## 一、数组排序

### 1. 基本类型数组排序
```java
int[] numbers = {3, 1, 4, 1, 5, 9};
Arrays.sort(numbers); // 升序排序
// 结果: [1, 1, 3, 4, 5, 9]

// 并行排序(大数据量性能更好)
int[] largeArray = new int[1000000];
Arrays.parallelSort(largeArray);
```

### 2. 对象数组排序
```java
String[] names = {"John", "Alice", "Bob"};
Arrays.sort(names); // 按自然顺序排序(字母顺序)
// 结果: ["Alice", "Bob", "John"]

// 使用自定义比较器
Arrays.sort(names, (a, b) -> b.compareTo(a)); // 降序排序
```

### 3. 部分范围排序
```java
int[] nums = {5, 2, 9, 1, 5, 6};
Arrays.sort(nums, 1, 4); // 对索引1到3(不包括4)的元素排序
// 结果: [5, 1, 2, 9, 5, 6]
```

## 二、数组搜索

### 1. 二分查找(必须先排序)
```java
int[] sorted = {1, 3, 5, 7, 9};
int index = Arrays.binarySearch(sorted, 5); // 返回2
int notFound = Arrays.binarySearch(sorted, 4); // 返回-3 (插入点为2+1)
```

### 2. 对象数组搜索
```java
String[] sortedNames = {"Alice", "Bob", "John"};
int pos = Arrays.binarySearch(sortedNames, "Bob"); // 1
```

## 三、数组比较

### 1. 判断数组相等
```java
int[] a1 = {1, 2, 3};
int[] a2 = {1, 2, 3};
boolean equal = Arrays.equals(a1, a2); // true

// 多维数组比较
int[][] m1 = {{1,2}, {3,4}};
int[][] m2 = {{1,2}, {3,4}};
boolean deepEqual = Arrays.deepEquals(m1, m2); // true
```

## 四、数组填充

### 1. 填充固定值
```java
int[] arr = new int[5];
Arrays.fill(arr, 10); // [10, 10, 10, 10, 10]

// 部分填充
Arrays.fill(arr, 1, 3, 20); // [10, 20, 20, 10, 10]
```

## 五、数组复制

### 1. 复制数组
```java
int[] original = {1, 2, 3};
int[] copy = Arrays.copyOf(original, original.length); // 完整复制
int[] truncated = Arrays.copyOf(original, 2); // [1, 2]
int[] extended = Arrays.copyOf(original, 5); // [1, 2, 3, 0, 0]

// 范围复制
int[] rangeCopy = Arrays.copyOfRange(original, 1, 3); // [2, 3]
```

## 六、数组转字符串

### 1. 数组内容可视化
```java
int[] nums = {1, 2, 3};
System.out.println(Arrays.toString(nums)); 
// 输出: [1, 2, 3]

// 多维数组
int[][] matrix = {{1,2}, {3,4}};
System.out.println(Arrays.deepToString(matrix));
// 输出: [[1, 2], [3, 4]]
```

## 七、数组转换为集合

### 1. 固定大小列表
```java
String[] names = {"Alice", "Bob"};
List<String> list = Arrays.asList(names);
// 注意: 返回的列表大小固定，不能添加/删除元素

// Java 8+ 流式处理
List<Integer> intList = Arrays.stream(new int[]{1,2,3})
                            .boxed()
                            .collect(Collectors.toList());
```

## 八、并行处理(Java 8+)

### 1. 并行数组操作
```java
int[] numbers = {1, 2, 3, 4, 5};

// 并行设置所有值
Arrays.parallelSetAll(numbers, i -> i * 2);
// 结果: [0, 2, 4, 6, 8]

// 并行前缀计算(累积和)
Arrays.parallelPrefix(numbers, (a, b) -> a + b);
// 结果: [0, 2, 6, 12, 20]
```

## 九、特殊比较方法

### 1. 比较和失配查找(Java 9+)
```java
int[] a = {1, 2, 3, 4};
int[] b = {1, 2, 4, 4};
int mismatch = Arrays.mismatch(a, b); // 返回2(第一个不匹配的索引)
int compare = Arrays.compare(a, b);   // 返回负数(a < b)
```

## 十、实际应用示例

### 1. 数组去重
```java
int[] withDuplicates = {1, 2, 3, 2, 1};
int[] distinct = Arrays.stream(withDuplicates)
                     .distinct()
                     .toArray();
// 结果: [1, 2, 3]
```

### 2. 数组统计
```java
int[] nums = {5, 2, 9, 1, 7};
IntSummaryStatistics stats = Arrays.stream(nums).summaryStatistics();
System.out.println("Max: " + stats.getMax());
System.out.println("Min: " + stats.getMin());
System.out.println("Avg: " + stats.getAverage());
```

### 3. 数组比较器
```java
String[] names = {"John", "Alice", "Bob"};
Arrays.sort(names, Arrays.compare(String::length, String::compareTo));
// 先按长度排序，长度相同按字母顺序
```

Arrays 类提供了丰富的方法来简化数组操作，合理使用这些方法可以大大提高开发效率并减少错误。对于大型数组，考虑使用并行方法(parallelSort, parallelPrefix等)来提高性能。