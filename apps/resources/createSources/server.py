import requests

from resources.serializers.server import SaltServerSerializer


def check_ip_city(ip, timeout=10):
    # Taobao ip api: http://ip.taobao.com/service/getIpInfo.php?ip=8.8.8.8
    # Sina ip api: http://int.dpool.sina.com.cn/iplookup/iplookup.php?ip=8.8.8.8&format=json

    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
    try:
        r = requests.get(url, timeout=timeout)
    except:
        r = None
    city = False
    if r and r.status_code == 200:
        try:
            data = r.json()
            if not isinstance(data, int) and data['code'] == 0:
                country = data['data']['country']
                _city = data['data']['city']
                if country == 'XX':
                    city = False
                else:
                    city = True
        except ValueError:
            pass
    return city

def get_inner_public_Ips(ips):
    innerIps = []
    publicIps = []

    for ip in ips:
        if ip == '127.0.0.1':
            continue
        elif check_ip_city(ip):
            publicIps.append(ip)
        else:
            innerIps.append(ip)
    return innerIps, publicIps

def saveServer(instance):
    data = {}
    data['provider'] = None
    data['id'] = instance['uuid']
    data['saltID'] = instance['id']
    data['planform'] = instance['kernel']
    data['os'] = '{} {} {}'.format(instance['os'],'.'.join(str(x) for x in instance['osrelease_info']), instance['osarch'])
    data['cpu_model'] = instance['cpu_model']
    data['cpu_arch'] = instance['cpuarch']
    data['cpu_count'] = instance['num_cpus']
    data['ram'] = {'physical': instance['mem_total'], 'swap': instance['swap_total']}
    data['hostname'] = instance['host']
    data['innerIps'], data['publicIps'] = get_inner_public_Ips(instance['ipv4'])
    if data['innerIps']:
        data['_IP'] = data['innerIps'][0]
    elif data['publicIps']:
        data['_IP'] = data['publicIps'][0]
    else:
        data['_IP'] = None

    serializer = SaltServerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return serializer.errors

