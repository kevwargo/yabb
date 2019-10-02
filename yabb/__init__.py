import sys
from argparse import ArgumentParser


def snap(args):
    print(f'snapping {args}')

def send(args):
    print(f'sending {args}')

def restore(args):
    print(f'restoring {args}')


def main():
    cmds = {
        'snap': snap,
        'send': send,
        'restore': restore,
    }
    cmd_name = sys.argv[1]
    if cmd_name not in cmds:
        raise ValueError(f'Invalid command "{cmd_name}"')
    cmd = cmds[cmd_name]
    parser = ArgumentParser()
    parser.add_argument('-p', '--pool', default='/mnt/btrfs-pool')
    parser.add_argument('-b', '--backups-dir', default='/mnt/backups/volumes')
    parser.add_argument('all_volumes', nargs='*', default=['data', 'root'])
    ns = parser.parse_args(sys.argv[2:])
    cmd(ns)
