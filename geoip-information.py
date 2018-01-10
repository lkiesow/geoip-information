import pygeoip
pygeoip.GeoIP('/usr/share/GeoIP/GeoLiteCity.dat')
g = pygeoip.GeoIP('/usr/share/GeoIP/GeoLiteCity.dat')
with open('ip.dat', 'r') as f:
    # Print header
    t = ('ip',
         'latitude',
         'longitude',
         'country_code',
         'postal_code',
         'city',
         'country_name',
         'continent')
    print(u'%s,%s,%s,%s,%s,"%s","%s",%s' % t)

    # Print data
    while True:
        ip = f.readline()
        if not ip:
            break
        r = g.record_by_addr(ip.rstrip('\n'))
        if not r:
            continue
        t = (ip.rstrip('\n'),
             r['latitude'],
             r['longitude'],
             r['country_code'],
             r['postal_code'],
             r['city'],
             r['country_name'],
             r['continent'])
        print(u'%s,%s,%s,%s,%s,"%s","%s",%s' % t)
