# URL（统一资源定位符）详解

URL（Uniform Resource Locator，统一资源定位符）是互联网上用于**定位和访问资源**的标准地址格式。它是URI（统一资源标识符）的最常见形式。

## 1. URL的基本结构

一个完整的URL通常由以下几部分组成：

```
  https://www.example.com:8080/path/to/resource?query=string#fragment
  \___/   \_____________/\__/\_______________/\_________/ \_______/
    |           |         |         |              |          |
  协议      主机名      端口号      路径          查询参数    片段标识
(scheme)   (host)     (port)    (path)         (query)     (fragment)
```

## 2. URL各组成部分详解

### (1) 协议（Scheme）
- 指定访问资源使用的协议
- 常见协议：
  - `http`：超文本传输协议
  - `https`：安全的HTTP协议
  - `ftp`：文件传输协议
  - `mailto`：电子邮件地址
  - `file`：本地文件

### (2) 主机名（Host）
- 资源所在服务器的主机名或IP地址
- 可以是：
  - 域名（如 `www.example.com`）
  - IP地址（如 `192.168.1.1`）

### (3) 端口号（Port，可选）
- 指定服务器监听的端口
- 默认端口：
  - HTTP：80
  - HTTPS：443
- 示例：`:8080`

### (4) 路径（Path）
- 指定服务器上资源的具体位置
- 示例：`/path/to/resource`

### (5) 查询字符串（Query，可选）
- 以`?`开头，包含传递给服务器的参数
- 格式：`key1=value1&key2=value2`
- 示例：`?id=123&lang=en`

### (6) 片段标识（Fragment，可选）
- 以`#`开头，指定资源内的特定部分
- 通常用于HTML文档锚点
- 示例：`#section2`

## 3. URL编码

由于URL只能使用特定字符集（ASCII），其他字符需要编码：

- 空格编码为 `%20`
- 中文编码示例：
  - "中国" → `%E4%B8%AD%E5%9B%BD`
- 在Java中可使用`URLEncoder.encode()`

## 4. 绝对URL vs 相对URL

| 类型 | 示例 | 说明 |
|------|------|------|
| **绝对URL** | `https://example.com/img/logo.png` | 包含完整路径 |
| **相对URL** | `../img/logo.png` | 相对于当前页面位置 |

## 5. URL的实际应用示例

```java
// Java中解析URL
try {
    URL url = new URL("https://www.example.com:8080/search?q=java#results");
    
    System.out.println("协议: " + url.getProtocol());  // https
    System.out.println("主机: " + url.getHost());     // www.example.com
    System.out.println("端口: " + url.getPort());     // 8080
    System.out.println("路径: " + url.getPath());     // /search
    System.out.println("查询: " + url.getQuery());    // q=java
    System.out.println("片段: " + url.getRef());      // results
    
} catch (MalformedURLException e) {
    e.printStackTrace();
}
```

## 6. URL与URI的区别

- **URI**（统一资源标识符）：标识资源的更广泛概念
- **URL**：URI的子集，不仅标识资源还提供访问方式
- **URN**（统一资源名称）：另一种URI，只命名不定位（如`urn:isbn:0451450523`）

URL是互联网的基础构建块，理解其结构和编码规则对Web开发至关重要。