@echo off
setlocal
cd /d "%~dp0"
echo OpenReview official API login and bounded paper download.
echo Enter credentials only in this local window. Both prompts are hidden.
echo No browser cookies or credential files are read. No secrets are saved.
echo Up to 4 PDFs for 3 selected papers; this is not a full-corpus download.
call "%~dp0tools\python-project.cmd" "%~dp0tools\openreview_session.py" --run
echo.
echo Finished. The local receipt records success or a sanitized failure.
pause
