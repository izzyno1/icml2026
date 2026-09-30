@echo off
setlocal
call "%~dp0project-env.cmd"
"%ICML_PROJECT%\.venv\Scripts\python.exe" -B -X utf8 %*
exit /b %ERRORLEVEL%
