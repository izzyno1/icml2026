@echo off
setlocal
call "%~dp0project-env.cmd"
"%ICML_PROJECT%\.tools\git\cmd\git.exe" %*
exit /b %ERRORLEVEL%
