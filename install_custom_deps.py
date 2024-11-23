import os
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_header(text):
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + f" {text} ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)

def print_message(text):
    print(Fore.BLUE + Style.BRIGHT + text)

def print_error(text):
    print(Fore.RED + Style.BRIGHT + f"ERROR: {text}")

def check_python_environment():
    python_executable = "./python_embeded/python.exe"
    if not os.path.exists(python_executable):
        print_error("Python executable not found in the python_embeded directory.")
        print_message("Please ensure that Python is properly installed in this directory.")
        input(Fore.YELLOW + "Press Enter to exit...")
        exit(1)

def install_package(package_input, mirror_url=None):
    command = [r".\python_embeded\python.exe", "-m", "pip", "install", package_input]
    if mirror_url:
        command.extend(["-i", mirror_url])
    
    with open("installation.log", "a") as log_file:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
            log_file.write(line)
    
    return_code = process.wait()
    if return_code != 0:
        print_error("An error occurred during installation. Check installation.log for details.")
        input(Fore.YELLOW + "Press Enter to continue...")

def check_package_installed(package_name):
    command = [r".\python_embeded\python.exe", "-m", "pip", "show", package_name]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        print_error(f"Package '{package_name}' is not installed or an error occurred.")
    else:
        print_message(f"Details for package '{package_name}':")
        print(process.stdout)

def uninstall_package(package_name):
    command = [r".\python_embeded\python.exe", "-m", "pip", "uninstall", "-y", package_name]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        print_error(f"Failed to uninstall package '{package_name}'.")
    else:
        print_message(f"Package '{package_name}' has been successfully uninstalled.")
        print(process.stdout)

def main_menu():
    print_header("Python Package Management Tool For Current ComfyUI")
    check_python_environment()
    
    while True:
        print_message("\nChoose an option:\n")
        print(Fore.CYAN + "1. Install a package")
        print(Fore.CYAN + "2. Check if a package is installed")
        print(Fore.CYAN + "3. Uninstall a package")
        print(Fore.CYAN + "4. Exit")
        choice = input(Fore.GREEN + "> ").strip()
        
        if choice == '1':
            print_message("Input the package name and version (or type 'exit' to quit)\nIf no version is specified, the latest version will be installed\nPlease enter the package name and version (e.g., requests==2.28.1).")
            package_input = input(Fore.GREEN + "> ").strip()
            if package_input.lower() == 'exit':
                continue
            
            print_message("Please choose a source:")
            print(Fore.CYAN + "1. Official PyPI")
            print(Fore.CYAN + "2. USTC (University of Science and Technology of China)")
            print(Fore.CYAN + "3. TUNA (Tsinghua University)")
            print(Fore.CYAN + "4. Aliyun (Alibaba Cloud)")
            
            while True:
                source_choice = input(Fore.GREEN + "Enter the number of your choice (1/2/3/4): ").strip()
                if source_choice == "1":
                    install_package(package_input)  # Official PyPI
                    break
                elif source_choice == "2":
                    install_package(package_input, "https://pypi.mirrors.ustc.edu.cn/simple/")
                    break
                elif source_choice == "3":
                    install_package(package_input, "https://pypi.tuna.tsinghua.edu.cn/simple/")
                    break
                elif source_choice == "4":
                    install_package(package_input, "https://mirrors.aliyun.com/pypi/simple/")
                    break
                else:
                    print_error("Invalid choice, please try again.")
        
        elif choice == '2':
            package_name = input(Fore.GREEN + "Enter the name of the package to check: ").strip()
            check_package_installed(package_name)
        
        elif choice == '3':
            package_name = input(Fore.GREEN + "Enter the name of the package to uninstall: ").strip()
            uninstall_package(package_name)
        
        elif choice == '4':
            print_message("Exiting...")
            break
        
        else:
            print_error("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
