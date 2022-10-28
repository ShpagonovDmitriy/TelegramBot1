@echo off

call %~dp0Telegram_Bot1\venv\Scripts\activate

cd %~dp0Telegram_Bot1

set TOKEN = 5778655169:AAF2nRy3Dp8J8OfDxZ_Mmx8PXvCGFyZ4oSE

python bot_telegram.py

pause