### **Homebrew 简明指南：macOS/Linux 的终极包管理器**  

#### **1. 什么是 Homebrew？**  
Homebrew 是 macOS（和 Linux）上的**开源包管理工具**，用于快速安装、更新和管理开发者工具、命令行程序及应用程序。它通过简单的命令自动化软件安装过程，省去手动下载、配置的麻烦。  

---

#### **2. 为什么选择 Homebrew？**  
✅ **一键安装**：一条命令即可安装软件（如 Python、Git、Node.js）。  
✅ **自动处理依赖**：无需手动解决库依赖问题。  
✅ **集中管理**：所有软件安装在独立目录（如 `/opt/homebrew`），与系统自带软件隔离，避免冲突。  
✅ **丰富的软件库**：支持数千个开源工具和主流应用（如 VS Code、Chrome）。  
✅ **跨平台**：macOS 和 Linux 通用（Linux 版称为 **Linuxbrew**）。  

---

#### **3. 安装 Homebrew**  
##### **macOS 安装命令**（复制到终端执行）：  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```  
- **Apple Silicon（M1/M2/M3 Mac）**：默认安装到 `/opt/homebrew`。  
- **Intel Mac**：默认安装到 `/usr/local`。  

安装完成后，按提示将以下行添加到 `~/.zshrc` 或 `~/.bash_profile`：  
```bash
export PATH=/opt/homebrew/bin:$PATH  # Apple Silicon 用户
# 或
export PATH=/usr/local/bin:$PATH     # Intel 用户
```  
运行 `source ~/.zshrc` 生效。  

##### **Linux 安装命令**：  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```  
默认路径为 `/home/linuxbrew/.linuxbrew`。  

---

#### **4. 基础使用命令**  
| 命令 | 作用 | 示例 |
|------|------|------|
| `brew install <包名>` | 安装软件 | `brew install python` |
| `brew uninstall <包名>` | 卸载软件 | `brew uninstall node` |
| `brew update` | 更新 Homebrew 自身 | - |
| `brew upgrade` | 升级所有已安装软件 | - |
| `brew list` | 查看已安装的软件 | - |
| `brew search <关键词>` | 搜索软件包 | `brew search mysql` |
| `brew info <包名>` | 查看软件信息 | `brew info git` |
| `brew install --cask <应用名>` | 安装图形应用（如 VS Code） | `brew install --cask google-chrome` |

---

#### **5. 常见问题**  
❓ **安装路径不对？**  
- Apple Silicon Mac：`/opt/homebrew`  
- Intel Mac：`/usr/local`  
- 通过 `brew --prefix` 查看当前路径。  

❓ **命令未找到（`command not found`）？**  
检查 `PATH` 是否包含 Homebrew 的路径（参考上文环境变量配置）。  

❓ **软件安装失败？**  
运行 `brew doctor` 诊断问题，或尝试更新 Homebrew：  
```bash
brew update && brew upgrade
```

---

#### **6. 进阶技巧**  
- **清理旧版本软件**：`brew cleanup`  
- **查看依赖关系**：`brew deps <包名>`  
- **使用国内镜像加速**（如中科大源）：  
  ```bash
  export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"
  export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"
  ```

---

#### **7. 总结**  
Homebrew 是开发者必备工具，能极大提升效率。无论是安装开发环境（如 Java、Python）还是日常应用（如 Slack、Spotify），只需一行命令！  

尝试安装你的第一个软件吧：  
```bash
brew install wget && brew install --cask visual-studio-code
```  
🚀 **Enjoy Coding!**