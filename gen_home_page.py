
import subprocess

with open('home.html', 'w'):
    head = """<html>
    <body>"""

    middle = subprocess.check_output("echo $IP",shell=True)

    end = """</body>
    </html>"""
    w.write(head)
    w.write(middle)
    w.write(end)
    
