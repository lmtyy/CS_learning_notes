当然！这里为你整理了最常用和实用的 Docker 命令，按照使用场景分类，方便你快速上手。

## 镜像相关命令

```bash
# 从仓库拉取镜像
docker pull nginx:latest

# 列出本地所有镜像
docker images

# 删除镜像
docker rmi nginx

# 强制删除镜像（即使有容器在使用）
docker rmi -f nginx
```

## 容器生命周期管理

```bash
# 运行容器（最常用）
docker run -d --name my-container -p 8080:80 nginx

# 运行容器的常用参数：
# -d : 后台运行
# --name : 为容器命名
# -p : 端口映射（主机端口:容器端口）
# -v : 数据卷挂载
# -e : 设置环境变量

# 启动已停止的容器
docker start my-container

# 停止运行中的容器
docker stop my-container

# 重启容器
docker restart my-container

# 暂停容器
docker pause my-container

# 恢复暂停的容器
docker unpause my-container
```

## 查看容器信息

```bash
# 查看正在运行的容器
docker ps

# 查看所有容器（包括已停止的）
docker ps -a

# 查看容器日志
docker logs my-container

# 实时查看日志
docker logs -f my-container

# 查看容器资源使用情况
docker stats

# 查看容器详细信息
docker inspect my-container
```

## 进入容器和执行命令

```bash
# 进入容器内部（交互式终端）
docker exec -it my-container /bin/bash

# 在容器内执行单个命令
docker exec my-container ls -l

# 进入容器的简化方式（某些镜像可用 sh）
docker exec -it my-container sh
```

## 删除容器

```bash
# 删除已停止的容器
docker rm my-container

# 强制删除运行中的容器
docker rm -f my-container

# 删除所有已停止的容器
docker container prune
```

## 构建镜像

```bash
# 使用当前目录的 Dockerfile 构建镜像
docker build -t my-app:1.0 .

# 指定 Dockerfile 路径构建
docker build -t my-app:1.0 -f /path/to/Dockerfile .
```

## 网络相关

```bash
# 查看网络列表
docker network ls

# 创建自定义网络
docker network create my-network

# 将容器连接到网络
docker network connect my-network my-container
```

## 数据卷管理

```bash
# 创建数据卷
docker volume create my-volume

# 列出数据卷
docker volume ls

# 删除未使用的数据卷
docker volume prune
```

## 实用技巧和组合命令

```bash
# 一键停止所有运行中的容器
docker stop $(docker ps -q)

# 一键删除所有已停止的容器
docker rm $(docker ps -aq)

# 清理所有未使用的镜像、容器、网络
docker system prune

# 强制清理（包括未使用的数据卷）
docker system prune -a --volumes
```

## 最常用的命令组合示例

```bash
# 典型开发环境启动命令
docker run -d \
  --name my-webapp \
  -p 8080:80 \
  -v $(pwd):/app \
  -e ENV=development \
  nginx:latest

# 进入 MySQL 容器
docker exec -it mysql-container mysql -u root -p
```

记住这些核心命令，你就能应对 80% 的日常 Docker 使用场景了！建议先从 `docker run`、`docker ps`、`docker exec`、`docker logs` 这几个最常用的命令开始练习。