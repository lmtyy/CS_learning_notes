在 C 语言中，`math.h` 是一个标准库头文件，包含了许多数学计算函数。常用的函数主要包括基本的算术运算、三角函数、对数、指数函数等。下面是 `math.h` 库中一些常用函数的详细介绍：

### 1. **算术函数**
- `double fabs(double x);`
  - **功能**：计算 `x` 的绝对值。
  - **返回值**：返回 `x` 的绝对值。
  - **例子**：
    ```c
    #include <math.h>
    double result = fabs(-5.4);  // result = 5.4
    ```

- `double ceil(double x);`
  - **功能**：返回不小于 `x` 的最小整数值（向上取整）。
  - **返回值**：大于或等于 `x` 的最小整数值。
  - **例子**：
    ```c
    #include <math.h>
    double result = ceil(3.1);  // result = 4.0
    ```

- `double floor(double x);`
  - **功能**：返回不大于 `x` 的最大整数值（向下取整）。
  - **返回值**：小于或等于 `x` 的最大整数值。
  - **例子**：
    ```c
    #include <math.h>
    double result = floor(3.9);  // result = 3.0
    ```

- `double fmod(double x, double y);`
  - **功能**：返回 `x` 除以 `y` 的余数。
  - **返回值**：`x` 除以 `y` 的余数（即 `x - n * y`，其中 `n` 是最接近 `x / y` 的整数）。
  - **例子**：
    ```c
    #include <math.h>
    double result = fmod(5.5, 2.0);  // result = 1.5
    ```

### 2. **三角函数**
- `double sin(double x);`
  - **功能**：计算 `x` 的正弦值，`x` 以弧度为单位。
  - **返回值**：返回 `x` 的正弦值。
  - **例子**：
    ```c
    #include <math.h>
    double result = sin(M_PI / 2);  // result = 1.0
    ```

- `double cos(double x);`
  - **功能**：计算 `x` 的余弦值，`x` 以弧度为单位。
  - **返回值**：返回 `x` 的余弦值。
  - **例子**：
    ```c
    #include <math.h>
    double result = cos(M_PI);  // result = -1.0
    ```

- `double tan(double x);`
  - **功能**：计算 `x` 的正切值，`x` 以弧度为单位。
  - **返回值**：返回 `x` 的正切值。
  - **例子**：
    ```c
    #include <math.h>
    double result = tan(M_PI / 4);  // result = 1.0
    ```

- `double asin(double x);`
  - **功能**：计算 `x` 的反正弦值，返回结果以弧度为单位。
  - **返回值**：返回 `x` 的反正弦值。
  - **例子**：
    ```c
    #include <math.h>
    double result = asin(1.0);  // result = M_PI / 2
    ```

- `double acos(double x);`
  - **功能**：计算 `x` 的反余弦值，返回结果以弧度为单位。
  - **返回值**：返回 `x` 的反余弦值。
  - **例子**：
    ```c
    #include <math.h>
    double result = acos(0.5);  // result ≈ 1.0472 (π/3)
    ```

- `double atan(double x);`
  - **功能**：计算 `x` 的反正切值，返回结果以弧度为单位。
  - **返回值**：返回 `x` 的反正切值。
  - **例子**：
    ```c
    #include <math.h>
    double result = atan(1.0);  // result ≈ 0.7854 (π/4)
    ```

### 3. **指数与对数函数**
- `double exp(double x);`
  - **功能**：计算 `e` 的 `x` 次方（即 `e^x`）。
  - **返回值**：返回 `e^x` 的值。
  - **例子**：
    ```c
    #include <math.h>
    double result = exp(1.0);  // result ≈ 2.7183 (e)
    ```

- `double log(double x);`
  - **功能**：计算 `x` 的自然对数（以 `e` 为底）。
  - **返回值**：返回 `x` 的自然对数。
  - **例子**：
    ```c
    #include <math.h>
    double result = log(2.7183);  // result ≈ 1.0
    ```

- `double log10(double x);`
  - **功能**：计算 `x` 的以 10 为底的对数。
  - **返回值**：返回 `x` 的以 10 为底的对数。
  - **例子**：
    ```c
    #include <math.h>
    double result = log10(1000.0);  // result = 3.0
    ```

- `double pow(double x, double y);`
  - **功能**：计算 `x` 的 `y` 次方（即 `x^y`）。
  - **返回值**：返回 `x` 的 `y` 次方。
  - **例子**：
    ```c
    #include <math.h>
    double result = pow(2.0, 3.0);  // result = 8.0
    ```

- `double sqrt(double x);`
  - **功能**：计算 `x` 的平方根。
  - **返回值**：返回 `x` 的平方根。
  - **例子**：
    ```c
    #include <math.h>
    double result = sqrt(16.0);  // result = 4.0
    ```

### 4. **常量**
- `M_PI`：圆周率常量，约等于 3.141592653589793。
- `M_E`：自然对数的底数 `e`，约等于 2.718281828459045。
  
### 5. **其他函数**
- `double modf(double x, double *intpart);`
  - **功能**：将 `x` 拆分为整数部分和小数部分。
  - **返回值**：返回 `x` 的小数部分，将整数部分通过指针传递。
  - **例子**：
    ```c
    #include <math.h>
    double intpart;
    double fracpart = modf(5.75, &intpart);  // fracpart = 0.75, intpart = 5.0
    ```

这些函数大多处理浮点数，因此使用时需要注意类型的匹配。在使用这些函数时，通常需要 `#include <math.h>` 来包含该库。

希望这些介绍对你有帮助！如果有其他具体的函数或用法，随时可以问我。