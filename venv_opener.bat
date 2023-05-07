@echo off
mode 120, 40
title Venv Opener
color 3
:inicio
echo venv opener batch made by d3vh4n5.com.ar
echo.
echo    ==============================================
echo                       MENU
echo    ==============================================
echo.
echo                Seleccione una Opcion
echo.
echo        1. Ambiente django1 + proyecto
echo        2. Ambiente django2 + proyecto
echo        3. Ambiente python practicas + VSC
echo        4. Abrir React practicas en VSC + YT
echo        5. Abrir Visual Studio Code nuevo
echo        6. Abrir chat gpt
echo        s. Salir
echo.
echo    =============================================
echo.
echo.
set /p menu=Select option = 

if "%menu%"=="1" goto op1
if "%menu%"=="2" goto op2
if "%menu%"=="3" goto op3
if "%menu%"=="4" goto op4
if "%menu%"=="5" goto op5
if "%menu%"=="6" goto op6
if "%menu%"=="s" goto salir
echo Opcion invalida
echo Presione una tecla para volver al menu
pause>null
cls
goto inicio

:op1
cls
cmd /c code C:\Repositorios\Practicas\django\miproyecto
cmd /k C:\Repositorios\Practicas\django\miproyectodjangovenv\Scripts\activate

:op2
cls
cmd /c code C:\Repositorios\django
cmd /k D:\Envs\p2django\Scripts\activate

:op3
cls
cmd /c code C:\Users\Hans\Desktop\Python
cmd /k C:\Users\Hans\Desktop\Python\Practicando\venv\ejemplo_codo\Scripts\activate

:op4
cls
echo Abriendo navegador en el menu de seleccion de la clase
start https://www.youtube.com/playlist?list=PLyBd7TyyK5mrLI6lQ8D3HLED0gEAHYHMs
echo Abriendo Visual Studio Code con el proyecto de practicas de React
cmd /c code C:\Repositorios\React\helloworld
cls
goto inicio

:op5
cls
cmd /c code .
cls
goto inicio

:op6
cls
echo.
start https://chat.openai.com/
echo Presione una tecla para volver al menu
pause>null
cls
goto inicio

:salir
cls&exit