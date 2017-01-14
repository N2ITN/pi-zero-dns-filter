import subprocess

with open('home.html', 'w') as page:
    ip = 'http://' + subprocess.check_output("echo $IP", shell=True).decode('utf-8')
    router = 'http://' +  subprocess.check_output("echo $ROUTER", shell=True).decode('utf-8')

    page.write("\n".join([
        '<html>', '<body>', '<label>Your network: </label>', '<t>', '<a href="',
        ip, '">', ip, '</a>', '</t>', '<br>', '<label>Your router: </label>',
        '<t>', '<a href="', router, '">', router, '</a>', '</t>', '<br>',
        '<a href="', "/admin", '">', 'Pi-Hole dashboard ', '</a>', '</body>', '</html>'
    ]))
