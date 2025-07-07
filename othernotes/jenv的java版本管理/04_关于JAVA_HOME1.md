## 📌 什么是 `JAVA_HOME`？

### 1. 基本概念
- **定义**：一个指向 JDK 安装目录的环境变量
- **用途**：告诉系统和开发工具（如 Maven/Gradle/IDE）在哪里找到 Java 开发环境
- **典型路径示例**：
  ```bash
  # macOS
  /Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
  
  # Linux
  /usr/lib/jvm/java-21-openjdk
  
  # Windows
  C:\Program Files\Java\jdk-21
  ```

### 2. 核心作用
| 场景 | 说明 |
|------|------|
| **编译/运行** | `javac`、`java` 等命令依赖该路径 |
| **构建工具** | Maven/Gradle 根据它定位 JDK |
| **IDE 配置** | IntelliJ/VSCode 自动检测或手动指定 |
| **服务器部署** | Tomcat/Jenkins 等需要知道 Java 位置 |

### 3. 与 `jenv` 的关系
- **自动管理**：  
  当使用 `jenv` 时，它会自动动态设置 `JAVA_HOME`（无需手动配置）
  ```bash
  # 查看 jenv 当前管理的 JAVA_HOME
  echo $JAVA_HOME
  # 输出示例：/Users/you/.jenv/versions/21.0.7
  ```

- **手动覆盖**（不推荐）：  
  如果在 `.zshrc` 中手动设置了 `JAVA_HOME`，会与 `jenv` 冲突

### 4. 如何正确检查
```bash
# 方法1：通过 jenv 获取
jenv javahome

# 方法2：macOS 专用命令
/usr/libexec/java_home

# 方法3：通用环境变量
echo $JAVA_HOME
```

### 5. 特殊情况处理
**需要手动设置的情况**：
- 某些老旧工具强制要求 `JAVA_HOME`
- 不使用 `jenv` 时

**解决方案**（临时）：
```bash
# 在终端临时设置（仅当前会话有效）
export JAVA_HOME=$(jenv javahome)
```

### 6. 重要原则
1. **优先级**：  
   `jenv` 管理的版本 > 手动设置的 `JAVA_HOME` > 系统默认

2. **验证顺序**：
   ```bash
   which java      # 应指向 jenv shim
   java -version   # 检查实际版本
   echo $JAVA_HOME # 应与 jenv 版本一致
   ```

---

## 🚨 常见问题
**Q：为什么设置了 `jenv` 但 `JAVA_HOME` 为空？**  
A：确保 `eval "$(jenv init -)"` 已正确执行，或尝试重启终端。

**Q：需要同时安装 JRE 吗？**  
A：现代 JDK 已包含 JRE，无需单独安装。

**Q：IDE 不识别 jenv 管理的版本？**  
A：在 IDE 中手动指定路径为：  
`~/.jenv/versions/你的版本号`
