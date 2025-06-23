`string.h` 是 C 标准库中的一个头文件，包含了用于处理字符串的各种函数。这些函数操作字符串（以 null 终止的字符数组），提供了许多常见的字符串操作，如复制、连接、查找、比较等。

以下是 `string.h` 中常用的函数及其详细参数和返回值：

### 1. `strlen`
```c
size_t strlen(const char *str);
```
- **参数**:  
  - `str`: 一个指向以 null 终止的字符串的指针。
  
- **返回值**:  
  - 返回字符串的长度（不包括终止的 null 字符）。

---

### 2. `strcmp`
```c
int strcmp(const char *str1, const char *str2);
```
- **参数**:  
  - `str1`, `str2`: 需要比较的两个字符串。
  
- **返回值**:  
  - 如果 `str1` 小于 `str2`，返回负数；  
  - 如果 `str1` 等于 `str2`，返回 0；  
  - 如果 `str1` 大于 `str2`，返回正数。

---

### 3. `strncmp`
```c
int strncmp(const char *str1, const char *str2, size_t n);
```
- **参数**:  
  - `str1`, `str2`: 需要比较的两个字符串。  
  - `n`: 最多比较的字符数。
  
- **返回值**:  
  - 如果 `str1` 小于 `str2`，返回负数；  
  - 如果 `str1` 等于 `str2`，返回 0；  
  - 如果 `str1` 大于 `str2`，返回正数；  
  - 如果比较的前 `n` 个字符相同，返回 0。

---

### 4. `strcpy`
```c
char *strcpy(char *dest, const char *src);
```
- **参数**:  
  - `dest`: 目标字符串，必须有足够的空间存放源字符串。
  - `src`: 源字符串，必须是以 null 终止的。
  
- **返回值**:  
  - 返回指向目标字符串 `dest` 的指针。

---

### 5. `strncpy`
```c
char *strncpy(char *dest, const char *src, size_t n);
```
- **参数**:  
  - `dest`: 目标字符串。
  - `src`: 源字符串。
  - `n`: 最多复制的字符数。
  
- **返回值**:  
  - 返回目标字符串 `dest` 的指针。

- **注意**: 如果 `src` 长度小于 `n`，目标字符串 `dest` 会用 null 字符填充。

---

### 6. `strcat`
```c
char *strcat(char *dest, const char *src);
```
- **参数**:  
  - `dest`: 目标字符串，必须有足够的空间来存放 `src` 字符串。
  - `src`: 要连接到目标字符串 `dest` 的字符串。
  
- **返回值**:  
  - 返回指向目标字符串 `dest` 的指针。

---

### 7. `strncat`
```c
char *strncat(char *dest, const char *src, size_t n);
```
- **参数**:  
  - `dest`: 目标字符串。
  - `src`: 要追加的源字符串。
  - `n`: 最多追加的字符数。
  
- **返回值**:  
  - 返回指向目标字符串 `dest` 的指针。

---

### 8. `strchr`
```c
char *strchr(const char *str, int c);
```
- **参数**:  
  - `str`: 指向字符串的指针。
  - `c`: 要查找的字符（作为整数传递）。
  
- **返回值**:  
  - 返回指向第一次出现字符 `c` 的位置的指针；如果没有找到，返回 `NULL`。

---

### 9. `strrchr`
```c
char *strrchr(const char *str, int c);
```
- **参数**:  
  - `str`: 指向字符串的指针。
  - `c`: 要查找的字符（作为整数传递）。
  
- **返回值**:  
  - 返回指向最后一次出现字符 `c` 的位置的指针；如果没有找到，返回 `NULL`。

---

### 10. `strstr`
```c
char *strstr(const char *haystack, const char *needle);
```
- **参数**:  
  - `haystack`: 被搜索的字符串。
  - `needle`: 要查找的子字符串。
  
- **返回值**:  
  - 如果找到了子字符串 `needle`，返回指向子字符串首次出现的位置的指针；否则返回 `NULL`。

---

### 11. `strtok`
```c
char *strtok(char *str, const char *delim);
```
- **参数**:  
  - `str`: 被分割的字符串，第一次调用时传入待分割的字符串，之后为 `NULL`（继续分割同一字符串）。  
  - `delim`: 包含分隔符的字符串，分隔符是 `delim` 中的任意字符。
  
- **返回值**:  
  - 返回指向当前分割出来的子字符串的指针。如果没有更多的子字符串，返回 `NULL`。

---

### 12. `memset`
```c
void *memset(void *ptr, int value, size_t num);
```
- **参数**:  
  - `ptr`: 指向要设置值的内存块的指针。
  - `value`: 要填充的值（会被转换为 `unsigned char`）。
  - `num`: 要填充的字节数。
  
- **返回值**:  
  - 返回指向内存块 `ptr` 的指针。

---

### 13. `memcpy`
```c
void *memcpy(void *dest, const void *src, size_t n);
```
- **参数**:  
  - `dest`: 目标内存地址。
  - `src`: 源内存地址。
  - `n`: 要复制的字节数。
  
- **返回值**:  
  - 返回指向目标内存的指针 `dest`。

---

### 14. `memcmp`
```c
int memcmp(const void *ptr1, const void *ptr2, size_t num);
```
- **参数**:  
  - `ptr1`, `ptr2`: 要比较的内存块。
  - `num`: 要比较的字节数。
  
- **返回值**:  
  - 如果内存块 `ptr1` 小于 `ptr2`，返回负值；  
  - 如果相等，返回 0；  
  - 如果 `ptr1` 大于 `ptr2`，返回正值。

---

### 15. `memmove`
```c
void *memmove(void *dest, const void *src, size_t n);
```
- **参数**:  
  - `dest`: 目标内存地址。
  - `src`: 源内存地址。
  - `n`: 要移动的字节数。
  
- **返回值**:  
  - 返回指向目标内存的指针 `dest`。

- **注意**: 与 `memcpy` 不同，`memmove` 可以处理源和目标内存块重叠的情况。

---

### 16. `strdup`
```c
char *strdup(const char *str);
```
- **参数**:  
  - `str`: 要复制的字符串。
  
- **返回值**:  
  - 返回指向新分配的内存块的指针，内存块包含源字符串的副本。如果内存分配失败，返回 `NULL`。

---

### 17. `strspn`
```c
size_t strspn(const char *str1, const char *str2);
```
- **参数**:  
  - `str1`: 待扫描的字符串。
  - `str2`: 包含允许字符的字符串。
  
- **返回值**:  
  - 返回 `str1` 中从开头开始连续包含在 `str2` 中的字符数。

---

### 18. `strcspn`
```c
size_t strcspn(const char *str1, const char *str2);
```
- **参数**:  
  - `str1`: 待扫描的字符串。
  - `str2`: 包含不允许字符的字符串。
  
- **返回值**:  
  - 返回 `str1` 中从开头开始扫描直到遇到 `str2` 中任何字符的位置（即不允许字符的第一个位置）。

---

### 19. `strpbrk`
```c
char *strpbrk(const char *str1, const char *str2);
```
- **参数**:  
  - `str1`: 待扫描的字符串。
  - `str2`: 包含匹配字符的字符串。
  
- **返回值**:  
  - 返回指

向 `str1` 中第一个匹配 `str2` 中字符的指针；如果没有匹配，返回 `NULL`。

---

### 20. `strtok_r`
```c
char *strtok_r(char *str, const char *delim, char **saveptr);
```
- **参数**:  
  - `str`: 被分割的字符串（第一次调用时提供，后续调用传递 `NULL`）。  
  - `delim`: 分隔符的字符串。
  - `saveptr`: 用于保存字符串的位置指针。
  
- **返回值**:  
  - 返回分割出的子字符串的指针；如果没有更多子字符串，返回 `NULL`。

---

这些是 `string.h` 库中的常用函数和它们的参数、返回值说明。希望对你有所帮助！