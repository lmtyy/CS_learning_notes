# `rm` 命令详解：Linux 文件删除指南

`rm` (remove) 是 Linux/Unix 系统中用于删除文件和目录的核心命令，功能强大但需要谨慎使用，因为删除的文件通常无法恢复。

## 基本用法

### 1. 删除单个文件
```bash
rm filename.txt
```

### 2. 删除多个文件
```bash
rm file1.txt file2.txt file3.txt
```

### 3. 使用通配符删除
```bash
rm *.tmp       # 删除所有.tmp后缀文件
rm project_*   # 删除所有以project_开头的文件
```

## 重要选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-i` | 交互式删除，每次删除前询问 | `rm -i *.log` |
| `-f` | 强制删除，忽略不存在的文件和警告 | `rm -f tempfile` |
| `-r` 或 `-R` | 递归删除目录及其内容 | `rm -r old_directory` |
| `-v` | 显示详细操作信息 | `rm -v *.bak` |
| `--no-preserve-root` | 允许删除根目录/(危险!) | `rm -rf --no-preserve-root /` |

## 危险操作警告

1. **永远不要执行**：
```bash
rm -rf /      # 删除系统所有文件(现代系统有保护)
rm -rf *      # 删除当前目录所有内容
rm -rf .*     # 删除所有隐藏文件(包括配置文件)
```

2. 替代安全做法：
```bash
# 先列出要删除的文件确认
ls *.tmp
# 确认无误后再删除
rm *.tmp
```

## 实用技巧

1. **安全删除模式** (推荐日常使用)：
```bash
alias rm='rm -i'   # 添加到~/.bashrc永久生效
```

2. **删除空目录** (更安全的替代方案)：
```bash
rmdir empty_dir/   # 只能删除空目录
```

3. **找回被删文件** (仅限ext3/4文件系统)：
```bash
# 需要立即卸载分区并尝试恢复
debugfs /dev/sdX
> lsdel
> dump <inode> /recovery/path
```

## 最佳实践

1. 删除前先备份重要数据
2. 使用`-i`选项进行交互式删除
3. 对目录操作时先使用`ls`查看内容
4. 考虑使用`trash-cli`等回收站工具替代直接删除

记住：在Linux中，删除操作是即时的，没有回收站概念(除非使用特殊工具)，因此使用`rm`命令时需要格外小心！