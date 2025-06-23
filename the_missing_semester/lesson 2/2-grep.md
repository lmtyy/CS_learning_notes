# `grep` 命令详解

`grep` (Global Regular Expression Print) 是 Linux/Unix 系统中强大的**文本搜索工具**，用于在文件或输入流中查找匹配特定模式的行。

## 基本语法

```bash
grep [选项] "模式" [文件...]
```

## 核心功能

### 1. 基础文本搜索

```bash
grep "error" log.txt       # 在log.txt中搜索包含"error"的行
grep -i "warning" file.log # 忽略大小写搜索"warning"
```

### 2. 正则表达式搜索

```bash
grep "^start" file.txt     # 搜索以"start"开头的行
grep "end$" file.txt       # 搜索以"end"结尾的行
grep "a.*b" file.txt       # 搜索包含a后面跟着b的行
```

### 3. 文件内容筛选

```bash
grep -v "success" data.txt # 显示不包含"success"的行
grep -c "pattern" file     # 统计匹配行数
grep -n "text" file        # 显示匹配行及其行号
```

## 常用选项

| 选项 | 功能描述 |
|------|----------|
| `-i` | 忽略大小写 |
| `-v` | 反向匹配（显示不匹配的行） |
| `-r` | 递归搜索目录 |
| `-l` | 只显示包含匹配项的文件名 |
| `-L` | 只显示不包含匹配项的文件名 |
| `-w` | 全词匹配 |
| `-A n` | 显示匹配行及其后n行 |
| `-B n` | 显示匹配行及其前n行 |
| `-C n` | 显示匹配行及其前后各n行 |
| `-E` | 使用扩展正则表达式（等同于egrep） |
| `-F` | 按字面字符串匹配（快速模式） |
| `--color` | 高亮显示匹配内容 |

## 高级用法

### 1. 递归搜索目录

```bash
grep -r "function" /path/to/code  # 递归搜索代码目录
```

### 2. 多模式搜索

```bash
grep -e "error" -e "fail" log.txt # 搜索error或fail
grep "pattern1\|pattern2" file    # 使用或条件
```

### 3. 结合管道使用

```bash
ps aux | grep "nginx"      # 查找nginx进程
cat access.log | grep "404" # 筛选404错误
```

### 4. 上下文显示

```bash
grep -A 2 -B 2 "exception" log.txt # 显示异常上下文
```

### 5. 只显示匹配部分

```bash
grep -o "user_[0-9]\+" data.txt # 只输出user_123这类匹配项
```

## 实用示例

1. 查找配置文件中的有效配置（非注释行）：
```bash
grep -v "^#" /etc/nginx/nginx.conf | grep -v "^$"
```

2. 统计代码中特定函数调用次数：
```bash
grep -r "function_name" ./src/ | wc -l
```

3. 查找日志中的错误并显示时间戳：
```bash
grep -E "ERROR|WARN" app.log | grep -o "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}"
```

4. 检查系统开放端口：
```bash
netstat -tulnp | grep -E "0.0.0.0|:::"
```

## 性能优化技巧

1. 对大文件使用 `-m` 限制匹配数量：
```bash
grep -m 100 "pattern" huge.log # 找到100个匹配就停止
```

2. 使用 `-F` 加速固定字符串搜索：
```bash
grep -F "static_string" file.txt
```

3. 排除特定目录（结合find）：
```bash
find . -name "*.py" -not -path "./venv/*" -exec grep "import" {} +
```

## 注意事项

1. 特殊字符需要转义：
```bash
grep "3\.14" file.txt # 搜索"3.14"而不是"314"
```

2. 默认使用基础正则表达式，复杂模式建议用 `-E`：
```bash
grep -E "pattern1|pattern2" file.txt
```

3. 二进制文件可能显示乱码，可加 `-a` 选项：
```bash
grep -a "text" binary.file
```

## 替代工具

1. `ack` - 专为代码搜索优化
2. `ag` (The Silver Searcher) - 更快的递归搜索
3. `rg` (ripgrep) - 现代高效替代品

`grep` 是Linux系统管理中最常用的命令之一，熟练掌握可以极大提高文本处理效率。