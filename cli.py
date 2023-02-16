import json
import os
import datetime
from pythonping import ping


root_dns = ( # in alphabetical order
    '198.41.0.4',
    '199.9.14.201',
    '192.33.4.12',
    '199.7.91.13',
    '192.203.230.10',
    '192.5.5.241',
    '192.112.36.4',
    '198.97.190.53',
    '192.36.148.17',
    '192.58.128.30',
    '193.0.14.129',
    '199.7.83.42',
    '202.12.27.33'
)


def speedtest(server_id):
    """
    Launch a speedtest and return the results
    :param server_id: the server id to use
    :return: a dict with the results (download, upload, ping)
    """
    st_results = json.loads('{}')
    try:
        st_infos = json.loads(os.popen('speedtest -s ' + server_id + ' -P 0 -f json').read())
        st_results['download'] = int(st_infos['download']['bandwidth']*0.000008)
        st_results['upload'] = int(st_infos['upload']['bandwidth']*0.000008)
        st_results['ping'] = st_infos['ping']['latency']
        return st_results
    except Exception as e:
        print(e)
        return None


def get_ping(host):
    """
    Get the ping of a host
    :param host: the host to ping
    :return: the average ping in ms
    """
    try:
        response_list = ping(host, size=40, count=10)
        return response_list.rtt_avg_ms
    except Exception as e:
        print(e)
        return None


def ping_root(dns_list):
    """
    Get the ping of a list of dns
    :param dns_list: the list of dns to ping
    :return: a dict with the dns as key and the ping as value
    """
    ping_results = json.loads('{}')
    for dns in dns_list:
        if get_ping(dns) >= 2000:
            delay = None
        else:
            delay = get_ping(dns)
        ping_results[dns] = delay
    return ping_results


def sum_results(st_r, ping_r):
    """
    Sum the results of speedtest and ping
    :param st_r: a dict with the results of speedtest
    :param ping_r: a dict with the results of ping
    :return: a dict with the results of speedtest and ping
    """
    results = json.loads('{}')
    results['timestamp'] = datetime.datetime.now().isoformat()
    results['speedtest'] = st_r
    results['ping'] = ping_r
    return results


if __name__ == '__main__':
    print(sum_results(speedtest('24215'), ping_root(root_dns)))
