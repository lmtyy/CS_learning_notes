# `mv` 命令详解

`mv`（move）是 Linux/Unix 系统中用于**移动或重命名**文件和目录的核心命令。它比图形界面操作更高效，特别适合批量处理文件。

## 基本语法

```bash
mv [选项] 源文件/目录 目标文件/目录
mv [选项] 源文件1 源文件2 ... 目标目录
```

## 核心功能

### 1. 文件/目录重命名

```bash
mv oldname.txt newname.txt      # 文件重命名
mv old_dir/ new_dir/           # 目录重命名
```
- 不可以批量重命名

### 2. 移动文件/目录

```bash
mv file.txt /target/path/      # 移动文件到目录
mv dir1/ /new/path/            # 移动整个目录
```

### 3. 批量移动

```bash
mv *.jpg /images/              # 移动所有jpg文件
mv file1.txt file2.txt backup/ # 移动多个文件到目录
```

## 常用选项

| 选项 | 功能描述 |
|------|----------|
| `-i` | 交互模式（覆盖前确认） |
| `-n` | 禁止覆盖已存在文件 |
| `-v` | 显示详细操作信息 |
| `-u` | 只移动更新的文件（目标较旧或不存在时） |
| `-b` | 覆盖前创建备份（备份文件会加`~`后缀） |
| `-S` | 指定备份文件后缀（如 `-S .bak`） |
| `--strip-trailing-slashes` | 移除源参数末尾的斜杠 |

## 高级用法

### 1. 防止覆盖重要文件

```bash
mv -i important.txt existing.txt  # 覆盖前会询问
mv -n newfile.txt existing.txt   # 如果目标存在则不移动
```

### 2. 创建备份后再覆盖

```bash
mv -b file.txt existing.txt      # 生成existing.txt~
mv -S .bak file.txt existing.txt # 生成existing.txt.bak
```

### 3. 仅移动新文件

```bash
mv -u *.log /archive/           # 只移动比目标目录中更新的日志
```

### 4. 结合find批量移动

```bash
find . -name "*.tmp" -exec mv {} /tmp/ \;  # 移动所有临时文件
```

## 实际应用示例

1. **整理下载目录**：
```bash
mv ~/Downloads/*.mp4 ~/Videos/
mv ~/Downloads/*.jpg ~/Pictures/
```

2. **项目文件重构**：
```bash
mv src/old_module/ src/new_module/  # 重构目录结构
```

3. **备份配置文件**：
```bash
mv -bv /etc/nginx.conf /etc/nginx.conf.bak  # 备份后移动新文件
```

4. **批量添加前缀**：
```bash
for f in *.txt; do mv "$f" "archive_$f"; done
```

## 注意事项

1. **跨文件系统移动**：
   - 如果目标在不同文件系统，`mv`实际执行"复制+删除"操作
   - 大文件可能耗时较长

2. **权限要求**：
   - 需要对源文件有读权限，对目标目录有写权限
   - 系统文件通常需要`sudo`

3. **符号链接处理**：
   - 默认移动链接本身（不跟随链接）
   - 使用`-L`选项可跟随符号链接

4. **危险操作**：
   - `mv *`可能意外覆盖文件（建议先`ls`确认）
   - 没有回收站机制，覆盖后难以恢复

## 替代方案

1. **rsync**（更安全的移动/同步）：
```bash
rsync -av --remove-source-files src/ dest/
```

2. **mmv**（批量重命名）：
```bash
mmv '*.old' '#1.new'  # 批量修改后缀
```

3. **图形界面**：
   - Dolphin（KDE）
   - Nautilus（GNOME）
   - Thunar（XFCE）

`mv` 是Linux文件管理中最基础也最强大的命令之一，熟练掌握可以极大提升工作效率。记住：操作前先确认目标路径，重要文件做好备份！