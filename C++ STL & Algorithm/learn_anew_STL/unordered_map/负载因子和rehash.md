# 理解 unordered_map 中的 rehash 和负载因子

在 C++ 的 `unordered_map` 中，**rehash** 和 **负载因子(load factor)** 是两个密切相关的核心概念，它们直接影响哈希表的性能和内存使用。下面我将详细解释这两个概念及其相互关系。

## 1. 负载因子 (Load Factor)

### 1.1 基本定义

负载因子是衡量哈希表拥挤程度的指标，计算公式为：

```
负载因子 = 元素数量 / 桶数量
```

例如：
- 一个有 10 个桶的 unordered_map 存储了 7 个元素，负载因子 = 7/10 = 0.7
- 当插入更多元素使总数达到 14 时，负载因子 = 14/10 = 1.4

### 1.2 负载因子的意义

- **性能指标**：负载因子越高，冲突概率越大，性能可能下降
- **扩容触发**：当负载因子超过 `max_load_factor` 时会触发 rehash

### 1.3 相关操作

```cpp
std::unordered_map<std::string, int> map;

// 获取当前负载因子
float current_lf = map.load_factor();
std::cout << "当前负载因子: " << current_lf << std::endl;

// 获取/设置最大负载因子（默认通常为1.0）
float max_lf = map.max_load_factor();
std::cout << "最大负载因子: " << max_lf << std::endl;

map.max_load_factor(0.75f);  // 设置为0.75
```

## 2. rehash 操作

### 2.1 基本概念

rehash 是哈希表为适应数据增长而进行的内部重组过程，包括：

1. 分配一个新的更大的桶数组
2. 重新计算所有元素的哈希值和新桶位置
3. 将元素迁移到新桶中
4. 释放旧桶数组内存

### 2.2 触发条件

rehash 会在以下情况自动发生：
- 插入元素后 `size() / bucket_count() > max_load_factor`
- 调用 `reserve()` 或 `rehash()` 时

### 2.3 rehash 的影响

- **优点**：减少冲突，提高性能
- **代价**：耗时操作（所有元素需要重新哈希和移动）
- **副作用**：使所有迭代器、指针和引用失效

### 2.4 相关操作

```cpp
// 确保哈希表至少有100个桶
map.rehash(100);

// 确保哈希表能容纳至少100个元素而不需要rehash
map.reserve(100);  // 等价于 rehash(ceil(100 / max_load_factor))

// 强制缩减桶数量（但不保证一定会缩减）
map.rehash(0);
```

## 3. rehash 和负载因子的关系

### 3.1 自动 rehash 过程

当插入新元素导致 `load_factor() > max_load_factor()` 时：

1. 计算新桶数量（通常至少是当前桶数量的两倍）
2. 执行 rehash 操作
3. 新负载因子 ≈ 元素数量 / 新桶数量

### 3.2 示例

```cpp
std::unordered_map<int, int> map;
map.max_load_factor(1.0f);  // 设置最大负载因子为1.0

// 初始状态
std::cout << "初始桶数: " << map.bucket_count() << std::endl;  // 可能是1

map.insert({1, 10});
std::cout << "插入1个元素后桶数: " << map.bucket_count() << std::endl;

// 持续插入直到触发rehash
for (int i = 2; i <= 10; ++i) {
    map.insert({i, i*10});
    if (map.bucket_count() > prev_bucket_count) {
        std::cout << "在插入" << i << "后触发rehash，新桶数: " 
                  << map.bucket_count() << std::endl;
    }
}
```

## 4. 性能考虑

### 4.1 负载因子选择

- **较低负载因子**（如0.5）：
  - 内存使用较多
  - 冲突较少，性能较好
- **较高负载因子**（如1.0）：
  - 内存使用较少
  - 冲突较多，性能可能下降

### 4.2 rehash 优化策略

1. **预先分配**：
   ```cpp
   // 预先分配足够空间避免多次rehash
   std::unordered_map<int, int> big_map;
   big_map.reserve(10000);
   ```

2. **选择合适的 max_load_factor**：
   ```cpp
   // 对于查询密集型应用，设置较低负载因子
   map.max_load_factor(0.7f);
   ```

3. **批量插入后手动rehash**：
   ```cpp
   // 批量插入大量数据
   for (int i = 0; i < 100000; ++i) {
       map.insert({i, i*10});
   }
   // 最后手动rehash优化内存
   map.rehash(0);
   ```

## 5. 实际示例分析

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

void printMapStats(const std::unordered_map<int, int>& map) {
    std::cout << "元素数: " << map.size() 
              << " | 桶数: " << map.bucket_count()
              << " | 负载因子: " << map.load_factor()
              << " | 最大负载因子: " << map.max_load_factor()
              << std::endl;
}

int main() {
    std::unordered_map<int, int> map;
    
    std::cout << "初始状态:\n";
    printMapStats(map);
    
    // 设置最大负载因子为0.7
    map.max_load_factor(0.7f);
    
    std::cout << "\n开始插入元素...\n";
    for (int i = 1; i <= 20; ++i) {
        map[i] = i * 10;
        std::cout << "插入 " << i << " 后: ";
        printMapStats(map);
        
        // 检测是否发生了rehash
        static size_t last_bucket_count = map.bucket_count();
        if (map.bucket_count() != last_bucket_count) {
            std::cout << "  --> 发生了rehash!\n";
            last_bucket_count = map.bucket_count();
        }
    }
    
    // 手动触发rehash
    std::cout << "\n执行手动rehash(50)...\n";
    map.rehash(50);
    printMapStats(map);
    
    // 尝试缩减
    std::cout << "\n尝试rehash(0)...\n";
    map.rehash(0);  // 请求缩减，但实现可能忽略
    printMapStats(map);
    
    return 0;
}
```

可能的输出示例：
```
初始状态:
元素数: 0 | 桶数: 1 | 负载因子: 0 | 最大负载因子: 1

开始插入元素...
插入 1 后: 元素数: 1 | 桶数: 1 | 负载因子: 1 | 最大负载因子: 0.7
  --> 发生了rehash!
插入 2 后: 元素数: 2 | 桶数: 3 | 负载因子: 0.666667 | 最大负载因子: 0.7
插入 3 后: 元素数: 3 | 桶数: 3 | 负载因子: 1 | 最大负载因子: 0.7
  --> 发生了rehash!
插入 4 后: 元素数: 4 | 桶数: 7 | 负载因子: 0.571429 | 最大负载因子: 0.7
...
插入 8 后: 元素数: 8 | 桶数: 7 | 负载因子: 1.14286 | 最大负载因子: 0.7
  --> 发生了rehash!
插入 9 后: 元素数: 9 | 桶数: 17 | 负载因子: 0.529412 | 最大负载因子: 0.7
...

执行手动rehash(50)...
元素数: 20 | 桶数: 53 | 负载因子: 0.377358 | 最大负载因子: 0.7

尝试rehash(0)...
元素数: 20 | 桶数: 53 | 负载因子: 0.377358 | 最大负载因子: 0.7
```

## 6. 关键总结

1. **负载因子**：
   - 衡量哈希表"拥挤程度"的指标
   - 计算公式：元素数量 / 桶数量
   - 可通过 `max_load_factor()` 设置阈值

2. **rehash**：
   - 哈希表扩容和重组的过程
   - 自动触发条件：`load_factor() > max_load_factor()`
   - 可手动触发：`rehash()` 或 `reserve()`

3. **性能优化**：
   - 预分配足够空间 (`reserve()`) 避免多次rehash
   - 根据应用特点调整 `max_load_factor`
   - 批量插入后考虑手动 `rehash(0)` 优化内存

理解这两个概念可以帮助你更好地控制和优化 `unordered_map` 的性能表现，特别是在处理大量数据时。