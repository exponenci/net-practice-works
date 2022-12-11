import argparse
import subprocess
import sys


def is_ping_ok(host, mtu_value, strict=True):
    # the only place, where some error can be arisen;
    # so, if we have some, we will notify user about error and exit
    ping_res = subprocess.run(
        ['ping', host, '-c', '1', '-M', 'do', '-s', str(mtu_value)],
        stdout=subprocess.PIPE, # to keep stdout of callee process clear
        stderr=subprocess.PIPE, # to keep stderr of callee process clear
    )
    if strict:        
        if ping_res.returncode != 0 and ping_res.returncode != 1:
            print('Some error happened while pinging host')
            sys.exit(0)
        return ping_res.returncode == 0
    return ping_res.returncode


def main():
    # parse host
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='host, to which path we are going to find MTU', type=str)
    host = parser.parse_args().host

    # check whether given host is valid and do we have access to ICMP
    rc = is_ping_ok(host, 1, strict=False)
    if rc == 127:
        print('Has no access to ICMP')
        return
    elif rc > 0:
        print('Are you sure you provided valid host?')
        return

    # find MTU by bin search
    left, right = 1, 1501 - 28
    while left + 1 < right:
        mtu = (left + right) // 2
        if is_ping_ok(host, mtu):
            left = mtu
        else:
            right = mtu
    print(f'MTU: {left + 28}')


if __name__ == '__main__':
    main()
