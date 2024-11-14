import os
import subprocess

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
# 获取当前脚本所在的目录
current_dir = os.path.dirname(current_script_path)

# 定义变量
python_executable = os.path.join(current_dir, "python.exe")
deps_dir = os.path.abspath(os.path.join(current_dir, "..", "comfyui_deps"))

# 检查Python可执行文件是否存在
if not os.path.isfile(python_executable):
    raise FileNotFoundError(f"The Python executable file {python_executable} does not exist.")

# 检查依赖目录是否存在
if not os.path.isdir(deps_dir):
    raise NotADirectoryError(f"The directory {deps_dir} does not exist.")

# 遍历依赖目录，查找所有.whl文件
for root, dirs, files in os.walk(deps_dir):
    for file in files:
        if file.endswith('.whl'):
            # 构建完整的文件路径
            whl_file_path = os.path.join(root, file)
            # 构建pip命令
            command = [python_executable, '-s', '-m', 'pip', 'install', '--no-index', '--find-links', deps_dir, whl_file_path]
            # 执行命令并捕获输出
            try:
                result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # 打印成功信息
                print(f"Installed: {file}")
                if result.stdout:
                    print(result.stdout.decode('utf-8'))
                if result.stderr:
                    print(result.stderr.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                # 打印错误信息
                print(f"Error installing {file}:")
                if e.stdout:
                    print(e.stdout.decode('utf-8'))
                if e.stderr:
                    print(e.stderr.decode('utf-8'))

print("All .whl files have been processed.")
