import os

os.system('pip install numpy-1.9.3+mkl-cp34-none-win32.whl')
os.system('pip install -r requirements.txt')
os.system('python manage.py db upgrade')
