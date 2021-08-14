import psutil


p = psutil.Process(pid = 12676)
p.terminate()

"""
12676 was Steam's pid and it was closed
"""
