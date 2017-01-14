import os 
os.seteuid(1000)
with open("local_networks.txt", 'r') as ln:
    localNetworks = (ln.readlines()[0]).split(',')[1:-1]
    localNetworks = [
        n for n in (i.strip()[10:-1] for i in localNetworks) if len(n) > 0
    ]

localNetworks = ([
    ''.join(["<option value=", '"', i, '"', ">", i, "</option>"])
    for i in localNetworks
])

with open("app.html", 'r') as original:
    with open('app_new.html', 'w') as new:
        for line in original.readlines():
            new.write(line)
            if '<select name="network">' in line:
                for x in localNetworks:
                    new.write(x)
                    new.write('\n')
                    
os.seteuid(0)