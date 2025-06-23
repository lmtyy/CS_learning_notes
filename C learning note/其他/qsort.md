`qsort` 是 C 标准库中的一个函数，用于对数组进行快速排序。它定义在 `<stdlib.h>` 头文件中。`qsort` 函数非常灵活，可以对任意类型的数组进行排序，只要提供一个比较函数来定义排序顺序。

以下是 `qsort` 函数的原型：

```c
void qsort(void *base, size_t num, size_t size, int (*compar)(const void *, const void *));
```

参数说明：
- `base`：指向要排序的数组的指针。
- `num`：数组中元素的数量。
- `size`：数组中每个元素的大小（以字节为单位）。
- `compar`：指向一个比较函数的指针，该函数用于确定数组元素的排序顺序。

比较函数 `compar` 的原型如下：

```c
int compar(const void *a, const void *b);
```

该函数应返回一个整数，表示：
- 小于 0：`a` 应该在 `b` 之前。
- 等于 0：`a` 和 `b` 相等（排序中位置不变）。
- 大于 0：`a` 应该在 `b` 之后。

下面是一个示例，演示如何使用 `qsort` 对整数数组进行升序排序：

```c
#include <stdio.h>
#include <stdlib.h>

// 比较函数，用于整数升序排序
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {5, 2, 9, 1, 5, 6};
    size_t arr_size = sizeof(arr) / sizeof(arr[0]);

    // 使用 qsort 对数组进行排序
    qsort(arr, arr_size, sizeof(int), compare);

    // 打印排序后的数组
    for (size_t i = 0; i < arr_size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```

在这个示例中，`compare` 函数将两个整数指针转换为 `int` 指针，然后解引用它们以获取整数值，并返回它们的差值。`qsort` 函数使用这个比较函数来确定数组元素的排序顺序。

对于其他类型的数据（如结构体），你需要提供一个适当的比较函数，并确保在 `qsort` 调用中正确设置 `size` 参数。例如，对于一个包含多个字段的结构体数组，你可能需要根据某个特定字段进行排序。