#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import platform
import sys

from python_hosts.hosts import Hosts, HostsEntry


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs='+', required=True,
                        help='IP address like 127.0.0.1')
    parser.add_argument('-n', nargs='*', required=True,
                        help='domain name and alias like www.example.com example.com')

    # no input means show me the help
    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def write_hosts(ip_address, domain_name, alias_name):
    if platform.system() == 'Windows':
        hosts_path="C:\\Windows\\System32\\drivers\\etc\\hosts"
    else:
        hosts_path="/etc/hosts"

    hosts = Hosts(path=hosts_path)
    hosts.remove_all_matching(name=domain_name)
    new_entry = HostsEntry(entry_type='ipv4', address=ip_address, names=[domain_name, alias_name])
    hosts.add([new_entry])
    hosts.write()


if __name__ == '__main__':
    filename = "hosts"
    arg = parse_input()
    # print(arg.p)
    ip_address = arg.p[0]
    domain_name = arg.n[0]
    alias_name = arg.n[1]

    try:
      write_hosts(ip_address, domain_name, alias_name)
    except Exception as e:
        print("Error Write to  Hosts", e)
    else:
        print("Domain name added")
