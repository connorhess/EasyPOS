@echo off
echo Starting.........

pyinstaller -w -F -i "Till.ico" login.py

echo Done

echo renaming

rename C:\Users\conno\OneDrive\Desktop\Shop\dist\login.py "EasyPOS V0.1.1"

echo ====================================
echo ================Done================
echo ====================================

set /p DUMMY=Hit ENTER to continue...



