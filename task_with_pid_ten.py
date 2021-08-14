import psutil
from psutil import AccessDenied

name = "python.exe"

for proc in psutil.process_iter():
    try:
        if proc.name() == name:
            print(proc)
    except (PermissionError, AccessDenied):
        print("error")

"""
print()
error
psutil.Process(pid=8584, name='python.exe', status='running', started='22:59:11')
error
"""

