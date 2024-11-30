@echo off
setlocal

:: Set ComfyUI root directory path (without the main.py part)
set comfyui_root_path=D:\ComfyUI

:: Build the full path to main.py and custom_nodes directory
set main_script_path=%comfyui_root_path%\main.py
set custom_nodes_dir=%comfyui_root_path%\custom_nodes

:: Output paths for confirmation
echo Main script path: %main_script_path%
echo Custom nodes directory: %custom_nodes_dir%

:: Modify the first line of python3xx._pth to set it to comfyui_root_path
(
    setlocal enabledelayedexpansion
    set first_line=%comfyui_root_path%
    set first_line_done=false
    for /f "delims=" %%A in (.\python_embeded\python312._pth) do (
        if not !first_line_done! == true (
            echo !first_line!
            set first_line_done=true
        ) else (
            echo %%A
        )
    )
) > .\python_embeded\python312._pth.tmp
move /y .\python_embeded\python312._pth.tmp .\python_embeded\python312._pth


:: Run the disable_nodes.py script with the custom nodes directory
.\python_embeded\python.exe .\python_embeded\disable_nodes.py --config ".\enable_nodes.json" --disable-config ".\disable_nodes.json" --custom-nodes-dir "%custom_nodes_dir%"

:: Run the main.py script
.\python_embeded\python.exe -s "%main_script_path%" --disable-metadata --windows-standalone-build

:: Pause to keep the command prompt open
pause
