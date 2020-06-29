@echo off
echo Starting.........

pyinstaller -c -F --name "EasyPOS" "C:/Users/conno/OneDrive/Documents/GitHub/EasyPOS/login.py"

echo ====================================
echo ================Done================
echo ====================================

set /p DUMMY=Hit ENTER to continue...

