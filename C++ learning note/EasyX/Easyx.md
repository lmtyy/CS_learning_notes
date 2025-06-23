### 〇、包含头文件
1. `#include<easyx.h>` 最新（包括了之前旧的不建议使用的）
2. `#include<graphics.h>` 之前旧的

### 一、窗口设置和坐标体系
1. 创建一个图形窗口（宽度 * 高度）：
   1. `initgraph(int width, int height, int flag = 0);`
   2. flag有宏：
      1. `EX_SHOWCONSOLE == 1` 显示原本黑窗口（这个函数另有一个窗口）
      2. `EX_NOCLOSE == 2`
      3. `EX_NOMINIMIZE == 4`
      4. `EX_DBLCLKS == 8` 支持鼠标的双击event
      5. 若要包含多种状态 则用位或运算 `|`
2. 设置窗口的背景颜色：
   1. `setbkcolor(...);`
      1. 括号内填入宏：用RED GREEN BLUE等
      2. 也可以用三原色宏：`RGB(...)` 括号内填入三原色值
3. 用设置的背景颜色填充整个窗口：
   1. `cleardevice();` 无参数
4. 坐标体系：左上角为原点 向右为x轴 向下为y轴

### 二、基本图形绘制
1. 绘制一个点：
   1. `putpixel(x, y, color);` (x, y)为点的位置 color为颜色
2. 绘制一条线：
   1. `line(x1, y1, x2, y2);` 从 (x1, y1) 到 (x2, y2)
   2. 设置线条颜色：`setlinecolor();` 括号里用宏
   3. 设置线条样式：`srtlinestyle(style, thickness);` style用宏 thickness是线条粗细 用int
3. 绘制一个矩形：
   1. `rectangle(left, top, right, bottom);` 矩形的左上角和右下角 就是`x1,y1,x2,y2`
      - 默认是一个框 没有内部填充
   2. 绘制一个填充矩形：`fillrectangle(x1, y1, x2, y2);` 一个框加内部填充 填充默认白色
   3. 无边框填充矩形：`solidrecctangle(the same);` 没有边框的
   4. 设置填充颜色：`setfillcolor(color);` color为参数
4. 绘制一个圆角矩形：
   1. `roundrect(the same, width, height);` 圆角圆的水平直径和垂直直径
   2. 同理 有：`fillroundrect();` `solidroundrect();`
5. 绘制圆形：
   1. `circle(x, y, radius);` 半径
   2. 同理 有：`fillcircle();` `solidcircle();`
6. 绘制椭圆：
   1. `ellipse(x1, y1, x2, y2);` 和矩形一样 椭圆内接矩形
   2. 同理
- 还有很多 用时自行查找
- 注意：在使用`setfillcolor();`时 要注意它作用的范围




