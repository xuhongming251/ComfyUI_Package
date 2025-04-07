@echo off
REM Get the directory where this batch file is located
set "BASE_DIR=%~dp0"

REM Set the relative Python path
set "PYTHON_DIR=%BASE_DIR%python_embeded"

REM Add this directory and Scripts to the beginning of PATH
set "PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts;%PATH%"

echo.
echo ==================================================
echo Python environment has been set to:
echo      %PYTHON_DIR%
echo --------------------------------------------------
echo Python version:
python --version
echo --------------------------------------------------
echo Pip version:
pip --version
echo ==================================================
echo.

echo Common pip commands:
echo -----------------------------------------------
echo "  pip install <package>             <-- Install a package"
echo "  pip uninstall <package>           <-- Uninstall a package"
echo "  pip list                          <-- List installed packages"
echo "  pip show <package>                <-- Show package details"
echo "  pip freeze > requirements.txt     <-- Save env to file"
echo "  pip install -r requirements.txt   <-- Install from file"
echo -----------------------------------------------
echo Using common pip mirrors:
echo "  pip install <package> -i https://pypi.tuna.tsinghua.edu.cn/simple       <-- 清华大学"
echo "  pip install <package> -i https://mirrors.aliyun.com/pypi/simple         <-- 阿里云"
echo "  pip install <package> -i https://pypi.mirrors.ustc.edu.cn/simple        <-- 中国科学技术大学"
echo -----------------------------------------------
REM Open a new command prompt
cmd /k
