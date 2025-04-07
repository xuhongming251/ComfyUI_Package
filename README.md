
# ComfyUI 运行环境离线安装包

## 解决的问题
1. 安装过程联网失败问题。
2. 环境依赖冲突问题。
3. 多环境共享一个ComfyUI目录。
4. 管理不同环境的依赖安装，可放在不同目录。

## 方案
1. 提供所有依赖的离线whl文件。
2. 提供内嵌的python环境，不影响其它环境，不受其它环境影响。
3. 可完全离线进行安装依赖。
4. 可再次重装。
5. 提供一键安装脚本。
6. 提供只启用哪些节点配置，快速启动ComfyUI。
7. 提供自定义安装节点依赖的脚本。

## 使用场景
1. 第一次使用ComfyUI，不想下载巨大整合包，可使用这个最小依赖包。
2. 本地ComfyUI环境搞坏了，想重新整个环境，但是不想重新下载节点和下载配置模型路径。
3. 多环境共享一个ComfyUI目录，比如一个新的torch 和 python环境，为了提速或者兼容某些节点的特殊环境需求。
4. 想自己发布自己的ComfyUI整合包，拷贝到哪里都可以使用。


## 使用方式

1. `https://huggingface.co/xuminglong/ComfyUI_PKG/tree/main` 下载zip包。
2. 第一次使用，双击执行`1、Offline Install ComfyUI Dependencies.bat`，安装当前环境依赖和`pip.exe`。
3. 用文本编辑器打开`2、Start ComfyUI.bat`, 把路径`D:\ComfyUI`修改为自己本地的`ComfyUI`目录，如果没有，通过`git clone https://github.com/comfyanonymous/ComfyUI.git`进行拉取。
4. 配置`enable_nodes.json`文件，配置上要启用的节点，节点名称可在`custom_nodes`文件夹内查看，要启用的节点，把目录名拷贝到`enable_nodes.json`中，要符合json格式。
5. 双击`2、Start ComfyUI.bat`, 启动`ComfyUI`。
6. 启动后，会自动打开浏览器`ComfyUI`页面。
7. 自定义安装依赖的方式：
   1. 第一种方式通过`ComfyUI-Manager`.
   2. 第二种方式通过`3、Install Custom Dependencies.bat`脚本按照指引进行安装，可选择切换不同源进行安装。
   3. 第三种方式是通过`4、Enter Current Python Env.bat`进入当前python环境后，通过pip命令进行安装。