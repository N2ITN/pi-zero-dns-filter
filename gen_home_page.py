import subprocess

with open('home.html', 'w') as page:
    ip = subprocess.check_output("echo $IP", shell=True).decode('utf-8')
    router = subprocess.check_output("echo $ROUTER", shell=True).decode('utf-8')
    page.write('''
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">



<!-- Milligram CSS minified -->
<link rel="stylesheet" href="milligram/dist/milligram.min.css">

<!-- You should properly set the path from the main file. -->''')
    page.write("\n".join([
        '<html>', '<body>', '<label>Your router: </label>', '<t>', '<a href="',
        'http://', router, '">', router, '</a>', '<br>', '</t>', '<br>',
        '<label>Set your DNS to: </label>', '<t>', ip, '</t>', '<br>', '<br>',
        '<a href="', "/admin", '">', 'Pi-Hole dashboard ', '</a>', '</body>',
        '</html>'
    ]))
