@echo off
echo Starting.........

pyinstaller -w --name "EasyPOS" "C:/Users/conno/OneDrive/Documents/GitHub/EasyPOS/login.py"

echo Compiling

"C:\Program Files (x86)\Inno Setup 6\iscc" "C:\Users\conno\OneDrive\Documents\GitHub\EasyPOS\Update\EasyPOS.iss"

echo ====================================
echo ================Done================
echo ====================================

set /p DUMMY=Hit ENTER to continue...

