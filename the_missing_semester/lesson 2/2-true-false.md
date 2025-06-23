在 Linux Shell 中，`true` 和 `false` 是两个特殊的命令（或称为“内置常量”），用于表示逻辑上的 **真（成功）** 和 **假（失败）**。它们通常用于条件判断、循环控制或函数返回值。

---

## **1. 基本概念**
| 命令   | 退出状态码 | 说明                     |
|--------|------------|--------------------------|
| `true` | `0`        | 表示逻辑真（成功）。      |
| `false`| `1`        | 表示逻辑假（失败）。      |

- **退出状态码（Exit Status）**：
  - 在 Shell 中，`0` 表示成功，非 `0` 表示失败。
  - `true` 直接返回 `0`，`false` 直接返回 `1`。

---

## **2. 常见用途**
### **(1) 条件判断**
```bash
if true; then
    echo "This will always run."
fi

if false; then
    echo "This will never run."
else
    echo "This will run because false returns 1."
fi
```

### **(2) 循环控制**
- **无限循环（`while true`）**：
  ```bash
  while true; do
      echo "Running forever..."
      sleep 1
  done
  ```
- **直到成功（`until false`）**：
  ```bash
  until false; do
      echo "This runs once, then exits."
      break
  done
  ```

### **(3) 函数返回值**
```bash
is_ok() {
    if [ "$1" = "yes" ]; then
        true  # 返回 0（成功）
    else
        false # 返回 1（失败）
    fi
}

is_ok "yes" && echo "Success" || echo "Failure"
```

### **(4) 占位符**
- 在脚本中暂时占位，避免语法错误：
  ```bash
  if [ -f "/tmp/file" ]; then
      true  # 文件存在，暂时不处理
  else
      echo "File missing."
  fi
  ```

---

## **3. 与 `:`（冒号命令）的区别**
- `:` 是一个 Shell 内置命令，**不做任何操作**，但返回 `0`（类似 `true`）。
- 用途：
  - 充当空操作（NOP）。
  - 用于变量默认值（`${var:=default}`）的占位。
  ```bash
  : ${USER:="guest"}  # 如果 USER 未定义，赋值为 "guest"
  ```

---

## **4. 实现原理**
- `true` 和 `false` 通常是 Shell 的 **内置命令**（`type true` 可查看）。
- 也可以直接使用 `/bin/true` 和 `/bin/false`（部分系统提供独立二进制文件）。

---

## **5. 示例：结合 `&&` 和 `||`**
```bash
true && echo "This runs"   # 前一条命令成功（0），执行后续命令
false || echo "This runs"  # 前一条命令失败（非0），执行后续命令
```

---

## **6. 注意事项**
- `true` 和 `false` **不是布尔值**，而是命令，需通过 `$?` 获取返回值：
  ```bash
  false
  echo $?  # 输出 1
  ```
- 在算术比较中，`0` 为真，非 `0` 为假（与其他编程语言相反）：
  ```bash
  if (( 0 )); then
      echo "This is false in arithmetic context."
  fi
  ```

---

## **总结**
| 场景               | 推荐命令       | 作用                          |
|--------------------|---------------|-------------------------------|
| 表示逻辑真         | `true`        | 返回 `0`（成功）              |
| 表示逻辑假         | `false`       | 返回 `1`（失败）              |
| 空操作             | `:`           | 返回 `0`，不做任何操作        |
| 无限循环           | `while true`  | 持续运行直到手动中断          |
| 条件占位           | `true`/`false`| 保持语法完整性                |

`true` 和 `false` 是 Shell 脚本中简单但强大的工具，常用于控制流程或占位逻辑！