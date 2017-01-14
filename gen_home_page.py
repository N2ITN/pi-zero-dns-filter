
import subprocess

with open('home.html', 'w') as page:
    head = """<html>
    <body>"""

    middle = subprocess.check_output("echo $IP",shell=True)

    end = """</body>
    </html>"""
    page.write(head)
    page.write(middle)
    page.write(end)

