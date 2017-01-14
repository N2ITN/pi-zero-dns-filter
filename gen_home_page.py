import subprocess


with open('home.html', 'w') as page:
    ip = str(subprocess.check_output("echo $IP", shell=True))
    router = str(subprocess.check_output("echo $ROUTER", shell=True))
    router = str(subprocess.check_output("""netstat -nr | awk '$1 == "0.0.0.0"{print$2}'""")

    page.write("\n".join([
        '<html>', '<body>', '<label>Your network: </label>', '<t>', ip, '</t>', '<br>',
        '<label>Your router: </label>', '<t>', router, '</t>', '</body>',
        '</html>'
    ]))
