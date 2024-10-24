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
项目依赖 reflex 进行网页展示，安装所需的依赖：

```bash
# 安装 reflex
pip install reflex
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
python main.py
```
注释： 上述命令将会在本地启动一个 Streamlit 服务器，打开一个网页应用，你可以通过浏览器访问该应用。

### 6. 停止项目
当你不再需要运行项目时，可以通过以下命令关闭虚拟环境：

```bash
# 停止虚拟环境
deactivate
```
注释： deactivate 命令用于退出当前的虚拟环境。

### 7. reflex安装
为了确保这个应用能够作为基于 Web 的服务运行，需要进行相应的 Reflex 配置：

Reflex 是一个用于构建基于 Python 的全栈 Web 应用的框架，它能够让开发者在一个统一的 Python 环境中构建前后端应用，而不需要单独编写 API 来连接前端与后端。它具备高度的灵活性和丰富的 UI 组件库，使得开发复杂的 Web 应用更加轻松和高效。通过 Reflex，开发者可以使用 Python 编写整个应用的业务逻辑和界面，并且轻松与数据库、前端库等集成。

Reflex 提供了一整套从组件创建、样式定制到服务器端渲染的完整工具链，适用于构建各种应用，如数据可视化工具、AI 应用、管理面板等。

```bash
# 创建一个新的项目文件夹，并进入该目录
mkdir my_app_name
cd my_app_name

# 创建虚拟环境，以确保项目依赖和系统环境隔离
python -m venv venv

# 激活虚拟环境（Windows 平台使用此命令；Linux 和 macOS 平台使用 `source venv/bin/activate`）
venv\Scripts\activate

# 安装 Reflex 框架，通过 pip 来管理项目依赖
pip install reflex

# 初始化一个新的 Reflex 项目，此命令会创建项目所需的基础文件和目录
reflex init

# 运行 Reflex 项目，并输出调试日志（debug 模式有助于查看详细的运行信息）
python -m reflex run --loglevel debug
```
注释： my_reflex_template文件夹是一个可以完整运行的reflex最简洁项目，里面已经安装了reflex库，和reflex依赖的前端包，可以在此基础上建立自己的应用。
