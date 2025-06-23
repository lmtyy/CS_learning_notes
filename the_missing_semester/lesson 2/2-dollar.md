在Linux Shell中，`$` 符号是核心符号之一，用途广泛，主要用于**变量引用、命令替换、算术运算、特殊参数**等场景。以下是 `$` 符号的详细用法及示例：

---

## **1. 变量引用**
### **基础用法**
- 用 `$` 引用已定义的变量：
  ```bash
  name="Alice"
  echo $name        # 输出: Alice
  echo ${name}      # 推荐使用{}明确变量边界
  ```

### **变量默认值**
- `${var:-default}`：如果 `var` 未定义或为空，则使用默认值：
  ```bash
  echo ${username:-"guest"}  # 如果username未定义，输出"guest"
  ```
- `${var:=default}`：如果 `var` 未定义或为空，则赋值默认值并返回：
  ```bash
  echo ${count:=0}  # 如果count未定义，赋值为0并输出
  ```
- `${var:?error}`：如果 `var` 未定义或为空，报错并退出：
  ```bash
  echo ${path:?"Error: path is not set"}  # 如果path未定义，报错退出
  ```
- `${var:+value}`：如果 `var` 已定义且非空，则返回 `value`：
  ```bash
  echo ${DEBUG:+1}  # 如果DEBUG已定义且非空，输出1
  ```

---

## **2. 命令替换**
### **`$()` 或反引号 `` ` ``**
- 执行命令并替换为输出：
  ```bash
  echo "Today is $(date)"    # 输出: Today is [当前日期]
  echo "Files: `ls`"         # 旧式写法（推荐用$()）
  ```

---

## **3. 算术运算**
### **`$(( ))`**
- 进行整数运算：
  ```bash
  echo $(( 5 + 3 ))       # 输出: 8
  x=10
  echo $(( x * 2 ))       # 输出: 20
  ```

### **`let` 命令**
- 类似 `$(( ))`，但直接修改变量：
  ```bash
  let "y = x + 5"         # y = x + 5
  ```

---

## **4. 特殊变量**
### **脚本参数**
- `$0`：脚本名称
- `$1, $2, ..., $9`：第1-9个参数
- `$#`：参数个数
- `$@` 和 `$*`：所有参数（`"$@"` 保持参数独立性，`"$*"` 合并为一个字符串）
  ```bash
  ./script.sh arg1 arg2
  echo $0      # 输出: ./script.sh
  echo $1      # 输出: arg1
  echo $#      # 输出: 2
  ```

### **进程状态**
- `$?`：上一条命令的退出状态（`0`=成功，非`0`=失败）
  ```bash
  ls /nonexistent
  echo $?      # 输出非0（表示失败）
  ```
- `$$`：当前Shell的进程ID（PID）
- `$!`：最后一个后台进程的PID
  ```bash
  sleep 10 &
  echo $!      # 输出后台sleep的PID
  ```

---

## **5. 字符串操作**
### **子字符串提取**
- `${var:start:length}`：
  ```bash
  str="HelloWorld"
  echo ${str:0:5}    # 输出: Hello
  ```

### **字符串替换**
- `${var/pattern/replacement}`（仅替换第一个匹配）：
  ```bash
  path="/home/user/file.txt"
  echo ${path/file/doc}   # 输出: /home/user/doc.txt
  ```
- `${var//pattern/replacement}`（替换所有匹配）：
  ```bash
  str="a-b-c"
  echo ${str//-/ }    # 输出: a b c
  ```

### **字符串删除**
- `${var#pattern}`：删除**最短**匹配前缀：
  ```bash
  file="backup.tar.gz"
  echo ${file#*.}     # 输出: tar.gz
  ```
- `${var##pattern}`：删除**最长**匹配前缀：
  ```bash
  echo ${file##*.}    # 输出: gz
  ```
- `${var%pattern}`：删除**最短**匹配后缀：
  ```bash
  echo ${file%.*}     # 输出: backup.tar
  ```
- `${var%%pattern}`：删除**最长**匹配后缀：
  ```bash
  echo ${file%%.*}    # 输出: backup
  ```

---

## **6. 数组操作**
### **索引数组**
- `${array[index]}`：
  ```bash
  fruits=("apple" "banana" "cherry")
  echo ${fruits[1]}   # 输出: banana
  ```
- `${#array[@]}`：数组长度：
  ```bash
  echo ${#fruits[@]}  # 输出: 3
  ```

### **关联数组（Bash 4+）**
- 需先 `declare -A`：
  ```bash
  declare -A colors
  colors["red"]="#FF0000"
  echo ${colors["red"]}  # 输出: #FF0000
  ```

---

## **7. 其他用法**
### **当前Shell的选项**
- `$-`：显示当前Shell的选项标志：
  ```bash
  echo $-    # 输出类似: himBHs
  ```

### **随机数**
- `$RANDOM`：生成随机数（0-32767）：
  ```bash
  echo $RANDOM
  ```

---

## **总结**
| 语法 | 用途 | 示例 |
|------|------|------|
| `$var` | 引用变量 | `echo $PATH` |
| `${var}` | 明确变量边界 | `echo ${var}_log` |
| `$(cmd)` | 命令替换 | `echo $(date)` |
| `$(( ))` | 算术运算 | `echo $(( 5 + 3 ))` |
| `$0, $1, $#` | 脚本参数 | `echo $1` |
| `$?` | 上一条命令的退出状态 | `echo $?` |
| `${var:-default}` | 变量默认值 | `echo ${name:-"guest"}` |
| `${var/old/new}` | 字符串替换 | `echo ${str/ /_}` |
| `${var:start:len}` | 子字符串提取 | `echo ${str:0:5}` |

掌握 `$` 的用法可以极大提升Shell脚本编写的灵活性和效率！