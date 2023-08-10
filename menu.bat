@echo off
setlocal

:menu
echo 1. Open video2imgs/start.bat
echo 2. Open img2ascii/start.bat
set /p choice=Select number (1/2): 

if "%choice%"=="1" (
    cd video2imgs
    start start.bat
) else if "%choice%"=="2" (
    cd img2ascii
    start start.bat
) else (
    echo Wrong Answer!
    goto menu
)

endlocal
