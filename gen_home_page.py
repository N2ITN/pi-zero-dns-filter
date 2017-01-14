import subprocess

with open('home.html', 'w') as page:
    ip = 'http://' + subprocess.check_output(
        "echo $IP", shell=True).decode('utf-8')
    router =  subprocess.check_output(
        "echo $ROUTER", shell=True).decode('utf-8')

    page.write("\n".join([
        '<html>', '<body>', '<label>Your router: </label>',  '<t>',
        '<a href="','http://', router, '">', router, '</a>', '<br>','</t>', '<br>',
        '<label>Set your DNS to: </label>', '<t>', ip, '</t>', '<br>',
        '<br>', '<a href="', "/admin", '">', 'Pi-Hole dashboard ', '</a>',
        '</body>', '</html>'
    ]))
