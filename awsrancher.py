import sys
import os
import time
import requests
import argparse
import json


def get(url):
    r = requests.get(url, auth=(rancher_api_access_key, rancher_api_access_secret))
    r.raise_for_status()
    return r


def post(url, data):
    if data:
        r = requests.post(url, data=json.dumps(data), auth=(rancher_api_access_key, rancher_api_access_secret))
    else:
        r = requests.post(url, data="", auth=(rancher_api_access_key, rancher_api_access_secret))
    r.raise_for_status()
    return r.json()


def logar(mensagem):
    if mensagem:
        print(time.strftime("%Y-%m-%dT%H:%M:%S - ") + mensagem)
    else:
        print(time.strftime("%Y-%m-%dT%H:%M:%S"))
    return


def desativa():
    pass


def ativa():
    pass


def main():
    try:
        cron_start = os.environ["CRON_START"]
        cron_stop = os.environ["CRON_STOP"]
        rancher_url = os.environ["RANCHER_URL"]
        rancher_access_key = os.environ["RANCHER_ACCESS_KEY"]
        rancher_access_secret = os.environ["RANCHER_ACCESS_SECRET"]
        rancher_env = os.environ["RANCHER_ENV"]
    except KeyError:
        logar("Variaveis nao definidas!")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', action='store_const', dest='manage_hosts', const=True, default=False,
                        help='Manage hosts.')
    parser.add_argument('--services', action='store_const', dest='manage_services', const=True, default=False,
                        help='Manage Services.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    if args.manage_hosts:
        try:
            os.environ["RANCHER_HOSTS"]
        except KeyError:
            rancher_hosts = getRancherHosts()
        else:
            rancher_hosts = os.environ["RANCHER_HOSTS"]

    if args.manage_services:
        try:
            os.environ["RANCHER_SERVICES"]
        except KeyError:
            rancher_services = getRancherServices()
        else:
            rancher_services = os.environ["RANCHER_SERVICES"]


if __name__ == '__main__':
    main()
