with open("local_networks.txt", 'w') as ln:
    ln.write(
        '[Cell(ssid=NETGEAR03), Cell(ssid=HOME-3F92), Cell(ssid=:)), Cell(ssid=Sarah_Palin), Cell(ssid=WildFrontier), Cell(ssid=xfinitywifi), Cell(ssid=), Cell(ssid=youngHotTake_), Cell(ssid=Nicoooooleeeeee), Cell(ssid=Steelhead), Cell(ssid=C-H), Cell(ssid=DIRECT-roku-153-0E314F), Cell(ssid=Lakota7), Cell(ssid=Bemer_2GEXT), Cell(ssid=), Cell(ssid=CookieMonster), Cell(ssid=NETGEAR71)]'
    )

import ast
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
            if '<input type="text" name="network" />' in line:
                for x in localNetworks:
                    new.write(x)
                    new.write('\n')
                    