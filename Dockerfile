# 使用官方 Python 基础镜像，根据需要选择适合的 Python 版本
FROM python:3.9-slim

# 设置工作目录为 /app，所有的命令都会在这个目录下执行
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录中
COPY . /app

# 安装 requirements.txt 中列出的所有依赖
# 使用 --no-cache-dir 标志可以避免在 Docker 层中存储不必要的缓存
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn 将监听的端口，确保这个端口与 Gunicorn 配置中的端口相匹配
EXPOSE 5000

# 启动 Gunicorn 服务器，'-c' 参数指定 Gunicorn 的配置文件
# 'demo:server' 指定了 Gunicorn 应当寻找的模块名和应用实例名
CMD ["gunicorn", "-c", "gunicorn_config.py", "demo:app"]
