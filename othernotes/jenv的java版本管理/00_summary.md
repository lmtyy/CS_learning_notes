## 📚 jenv 使用指南总结

### 1. 核心概念
- **作用**：轻量级 Java 版本管理工具（类似 nvm/pyenv）
- **特点**：
  - 不安装 JDK，只管理现有安装
  - 通过 shims 机制动态切换版本
  - 支持全局/项目级/临时会话三级配置

### 2. 安装配置
```bash
# 通过 Homebrew 安装
brew install jenv

# 添加到 Shell 配置（~/.zshrc 或 ~/.bashrc）
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"
```

### 3. 常用命令
| 命令 | 作用 |
|------|------|
| `jenv versions` | 查看所有可用版本 |
| `jenv global <version>` | 设置全局默认版本 |
| `jenv local <version>` | 设置项目级版本（生成 .java-version 文件） |
| `jenv shell <version>` | 设置当前会话临时版本 |
| `jenv add <jdk-path>` | 注册新 JDK 到 jenv |
| `jenv which java` | 查看当前 Java 实际路径 |

### 4. 版本管理流程
1. **注册 JDK**：
   ```bash
   # Homebrew 安装的 JDK
   jenv add /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
   
   # 手动下载的 JDK
   jenv add /Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
   ```

2. **设置默认版本**：
   ```bash
   jenv global 21.0.7  # 推荐使用完整版本号
   ```

3. **项目级配置**：
   ```bash
   cd my-project
   jenv local 17.0.15  # 生成 .java-version 文件
   ```

### 5. 优先级规则
```text
jenv shell > 项目目录 .java-version > jenv global > system
```

### 6. 最佳实践
- **团队协作**：将 `.java-version` 文件加入版本控制
- **IDE 集成**：
  - VS Code：通过 `java.configuration.runtimes` 配置
  - IntelliJ：手动添加 `~/.jenv/versions/` 下的 JDK
- **构建工具**：
  ```xml
  <!-- Maven 示例 -->
  <maven.compiler.source>17</maven.compiler.source>
  <maven.compiler.target>17</maven.compiler.target>
  ```

### 7. 故障排查
```bash
# 检查 PATH 优先级
echo $PATH | tr ':' '\n'

# 验证实际调用路径
which java  # 应显示 ~/.jenv/shims/java

# 重新初始化
eval "$(jenv init -)"
```

### 8. 典型工作流
```bash
# 创建新项目
mkdir my-app && cd my-app

# 设置项目版本
jenv local 21.0.7

# 初始化项目（自动使用 JDK 21）
mvn archetype:generate  # 或 gradle init
```

---

## 📝 注意事项
1. 避免手动配置 `JAVA_HOME`，让 jenv 自动管理
2. 推荐使用完整版本号（如 `17.0.15`）而非通用别名（如 `17`）
3. 通过 `jenv which java` 确认实际调用的 JDK 路径

---

这个总结涵盖了安装、配置、日常使用和问题排查的所有关键点，你可以将其保存为 `jenv-cheatsheet.md` 随时查阅。