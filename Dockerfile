# 基础镜像使用 Python 官方镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8000

# 使用 Gunicorn 启动 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:server"]
