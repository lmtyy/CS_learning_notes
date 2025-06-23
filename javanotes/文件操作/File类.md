# Java File 类详解

File 类是 Java 中用于表示文件和目录路径名的抽象表示，它提供了丰富的文件系统操作功能。File 类位于 `java.io` 包中，既可以表示文件也可以表示目录。

## 1. File 类基本功能

### 构造方法

```java
// 通过路径名创建File对象
File(String pathname)

// 通过父路径和子路径创建
File(String parent, String child)

// 通过父File对象和子路径创建
File(File parent, String child)

// 通过URI创建
File(URI uri)
```

### 使用示例

```java
// 不同构造方法示例
File file1 = new File("test.txt");              // 相对路径
File file2 = new File("/usr/local/test.txt");  // 绝对路径
File file3 = new File("/usr/local", "test.txt");
File dir = new File("/usr/local");
File file4 = new File(dir, "test.txt");
```

## 2. 文件和目录操作

### 创建操作

```java
boolean createNewFile()   // 创建新文件(仅当不存在时)
boolean mkdir()          // 创建目录(仅一级)
boolean mkdirs()         // 创建目录(包括必要父目录)
```

### 删除操作

```java
boolean delete()         // 删除文件或空目录
void deleteOnExit()      // JVM退出时删除
```

### 重命名/移动

```java
boolean renameTo(File dest)  // 重命名或移动文件
```

### 判断方法

```java
boolean exists()         // 是否存在
boolean isFile()         // 是否是文件
boolean isDirectory()    // 是否是目录
boolean isHidden()       // 是否隐藏文件
boolean canRead()        // 是否可读
boolean canWrite()       // 是否可写
boolean canExecute()     // 是否可执行
```

### 获取信息

```java
String getName()         // 获取文件名
String getPath()         // 获取路径名
String getAbsolutePath() // 获取绝对路径
String getParent()       // 获取父目录路径
long length()           // 获取文件大小(字节)
long lastModified()     // 获取最后修改时间(毫秒)
```

## 3. 目录操作

### 列出目录内容

```java
String[] list()                         // 列出目录下的文件和子目录名
String[] list(FilenameFilter filter)    // 使用过滤器列出
File[] listFiles()                      // 列出目录下的File对象
File[] listFiles(FileFilter filter)     // 使用过滤器列出File对象
File[] listFiles(FilenameFilter filter) // 另一种过滤器形式
```

### 示例：递归列出目录所有文件

```java
public static void listAllFiles(File dir) {
    if (dir == null || !dir.exists()) {
        return;
    }
    if (dir.isFile()) {
        System.out.println(dir.getName());
        return;
    }
    for (File file : dir.listFiles()) {
        listAllFiles(file);
    }
}
```

## 4. 路径操作

### 路径相关方法

```java
String getAbsolutePath()     // 获取绝对路径
File getAbsoluteFile()       // 获取绝对路径的File对象
String getCanonicalPath()    // 获取规范路径(解析符号链接等)
File getCanonicalFile()      // 获取规范路径的File对象
```

### 路径分隔符常量

```java
File.separator       // 路径分隔符(如Unix的/或Windows的\)
File.separatorChar   // 同上，char类型
File.pathSeparator   // 多个路径间的分隔符(如;或:)
File.pathSeparatorChar
```

## 5. 文件过滤器

File 类支持两种过滤器接口：

### FilenameFilter 接口

```java
boolean accept(File dir, String name);
```

### FileFilter 接口

```java
boolean accept(File pathname);
```

### 使用示例

```java
// 列出所有.txt文件
File dir = new File("/path/to/dir");
File[] textFiles = dir.listFiles(new FilenameFilter() {
    @Override
    public boolean accept(File dir, String name) {
        return name.endsWith(".txt");
    }
});

// Java 8 Lambda表达式写法
File[] javaFiles = dir.listFiles((d, name) -> name.endsWith(".java"));
```

## 6. 临时文件操作

```java
// 创建临时文件
File tempFile = File.createTempFile("prefix", ".suffix");
File tempDirFile = File.createTempFile("prefix", ".suffix", new File("/tmp"));

// 设置退出时删除
tempFile.deleteOnExit();
```

## 7. 新旧API对比(Java 7+)

从Java 7开始，引入了新的NIO.2 API (`java.nio.file`包)，提供了更强大的文件操作功能：

| 功能         | 旧API (java.io.File) | 新API (java.nio.file.Path) |
|-------------|----------------------|---------------------------|
| 路径表示     | File                 | Path                      |
| 文件操作     | File方法             | Files工具类               |
| 符号链接处理 | 有限支持             | 完全支持                  |
| 文件属性访问 | 有限                 | 丰富                      |
| 性能         | 一般                 | 更优                      |

### 示例：新旧API对比

```java
// 旧API
File oldFile = new File("test.txt");
long size = oldFile.length();

// 新API
Path newPath = Paths.get("test.txt");
long newSize = Files.size(newPath);
```

尽管有了新的NIO.2 API，File类仍然被广泛使用，特别是在需要维护旧代码或简单文件操作的场景中。

## 8. 综合示例

```java
import java.io.File;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        // 创建File对象
        File file = new File("example.txt");
        
        try {
            // 创建新文件
            if (file.createNewFile()) {
                System.out.println("文件创建成功");
            } else {
                System.out.println("文件已存在");
            }
            
            // 文件信息
            System.out.println("文件名: " + file.getName());
            System.out.println("绝对路径: " + file.getAbsolutePath());
            System.out.println("文件大小: " + file.length() + " bytes");
            System.out.println("可读: " + file.canRead());
            System.out.println("可写: " + file.canWrite());
            
            // 删除文件
            if (file.delete()) {
                System.out.println("文件删除成功");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // 目录操作示例
        File dir = new File("mydir");
        if (dir.mkdir()) {
            System.out.println("目录创建成功");
            
            // 在目录中创建文件
            File newFile = new File(dir, "newfile.txt");
            try {
                newFile.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
            
            // 列出目录内容
            System.out.println("\n目录内容:");
            for (String f : dir.list()) {
                System.out.println(f);
            }
        }
    }
}
```

File类为Java程序提供了基本的文件和目录操作能力，虽然新的NIO.2 API提供了更多功能，但File类由于其简单易用，仍然是许多场景下的首选。