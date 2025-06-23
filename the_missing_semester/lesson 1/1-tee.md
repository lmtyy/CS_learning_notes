# **`tee` 命令详解：同时输出到屏幕和文件**

`tee` 是 Linux/Unix 系统中一个非常实用的命令，它的核心功能是 **“分流”数据**：既将数据输出到屏幕（stdout），又同时写入一个或多个文件。它的名字来源于管道中的 T 型分流器（类似三通管）。

---

## **1. 基本语法**
```bash
command | tee [选项] 文件名
```
- **输入**：从管道（`|`）接收前一个命令的输出。
- **输出**：
  - 默认显示到屏幕（stdout）
  - 同时写入指定文件

---

## **2. 核心功能**
### **(1) 同时显示并保存输出**
```bash
ls -l | tee filelist.txt
```
- **效果**：
  - 终端会显示 `ls -l` 的结果（就像直接运行 `ls -l`）。
  - 同时将结果保存到 `filelist.txt`。

### **(2) 追加内容到文件（不覆盖）**
```bash
echo "New line" | tee -a log.txt
```
- `-a` 选项表示追加（Append），不加则会覆盖原文件。

### **(3) 写入多个文件**
```bash
dmesg | tee file1.txt file2.txt
```
- 将输出同时保存到 `file1.txt` 和 `file2.txt`。

---

## **3. 高级用法**
### **(1) 配合 sudo 写入受保护文件**
```bash
echo "127.0.0.1 example.com" | sudo tee -a /etc/hosts
```
- 普通用户无法直接修改 `/etc/hosts`，但通过 `sudo tee` 可以绕过权限限制。

### **(2) 忽略中断信号（`-i`）**
```bash
ping example.com | tee -i ping.log
```
- `-i` 选项让 `tee` 忽略中断信号（即使按 `Ctrl+C`，已写入的数据也不会丢失）。

### **(3) 与 `xargs` 结合批量操作**
```bash
find . -name "*.txt" | tee files.txt | xargs rm
```
- 先记录被删除的文件列表到 `files.txt`，再执行删除。

---

## **4. 典型使用场景**
| 场景 | 命令示例 | 说明 |
|------|----------|------|
| **保存日志并实时查看** | `tail -f /var/log/syslog \| tee syslog_copy.txt` | 动态跟踪日志并备份 |
| **调试脚本输出** | `./script.sh \| tee debug.log` | 同时查看和记录脚本输出 |
| **多次复用命令结果** | `apt list --upgradable \| tee upgrades.txt \| wc -l` | 既保存列表又统计数量 |
| **安全写入系统文件** | `echo "new config" \| sudo tee /etc/config.cfg` | 避免直接重定向的权限问题 |

---

## **5. 与纯重定向的区别**
| 方法 | 屏幕显示 | 文件写入 | 权限要求 |
|------|----------|----------|----------|
| `command > file` | ❌ 无输出 | ✅ 覆盖写入 | 需文件写权限 |
| `command \| tee file` | ✅ 有输出 | ✅ 默认覆盖写入 | 需文件写权限 |
| `sudo command > file` | ❌ 无输出 | ❌ 可能失败（权限问题） | 需 root 权限 |
| `command \| sudo tee file` | ✅ 有输出 | ✅ 成功写入 | 只需 sudo 权限 |

---

## **6. 总结**
- **`tee` 的核心价值**：**“一箭双雕”**——既看结果又存文件。
- **必记选项**：
  - `-a`：追加模式（不覆盖）
  - `-i`：忽略中断信号
- **经典组合**：
  - `sudo + tee`：安全写入系统文件
  - `tee + xargs`：记录后再处理数据

这个小工具在日志收集、调试、系统管理时非常有用，是 Linux 高手工具箱里的必备品！ 🔧