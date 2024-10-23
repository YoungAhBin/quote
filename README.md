# quote 项目说明

本项目主要用于定制化产品的报价功能，通过集成不同产品的报价模块，提供自动化报价服务。

# 本地部署与运行

请按照以下步骤在本地部署并运行本项目：

### 1. 克隆项目
确保你已经从代码仓库克隆了本项目的代码。

### 2. 创建并激活虚拟环境
首先，进入项目目录，然后创建 Python 虚拟环境并激活它：

```bash
# 进入项目目录
cd C:\Users\传防科电脑\Desktop\quote-main

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境（Windows 平台）
venv\Scripts\activate
```
注释： 虚拟环境的作用是将项目所需的依赖与全局环境隔离开来，防止冲突。
如果你使用的是其他操作系统，请根据操作系统的虚拟环境激活命令修改上述命令。

### 3. 安装依赖
项目依赖 Streamlit 进行网页展示，安装所需的依赖：

```bash
# 安装 Streamlit
pip install streamlit
```

### 4. 安装 Swarm 依赖模块
项目使用了 Swarm 模块来进行某些核心功能的处理。需要切换到 Swarm 的目录并安装它（需下载 Swarm 模块到本地进行安装）：

```bash
# 进入 Swarm 模块目录
cd "C:\Users\传防科电脑\Desktop\swarm-main"

# 安装 Swarm 模块
pip install .
```

### 5. 运行项目
安装完所有依赖后，返回到 quote-main 目录并启动项目：

```bash
# 切换回 quote-main 目录
cd "C:\Users\传防科电脑\Desktop\quote-main"

# 启动应用
run main.py
```
注释： 上述命令将会在本地启动一个 Streamlit 服务器，打开一个网页应用，你可以通过浏览器访问该应用。

### 6. 停止项目
当你不再需要运行项目时，可以通过以下命令关闭虚拟环境：

```bash
# 停止虚拟环境
deactivate
```
注释： deactivate 命令用于退出当前的虚拟环境。
