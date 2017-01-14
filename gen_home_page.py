import subprocess

with open('home.html', 'w') as page:
    ip = subprocess.check_output("echo $IP", shell=True).decode('utf-8')
    router = subprocess.check_output("echo $ROUTER", shell=True).decode('utf-8')

    page.write("\n".join([
        '<html>', '<body>', '<label>Your network: </label>', '<t>', ip, '</t>',
        '<br>', '<label>Your router: </label>', '<t>', router, '</t>',
        '</body>', '</html>'
    ]))
