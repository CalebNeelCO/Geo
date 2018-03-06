%~d1
cd "%~p1"

echo start "" http://127.0.0.1:5000/
python.exe test.py
pause
echo call cmd