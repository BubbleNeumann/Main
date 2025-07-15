
import ctypes
import sys
import os


INJ_BIN_PATH = 'bin'
inj_bin = None

addr = 0  # where to inj TODO

# linux consts
PTRACE_ATTACH = 16
PTRACE_DETACH = 17
PTRACE_POKETEXT = 4

libc = ctypes.CDLL('libc.so.6')

def main():

    # print('injector')

    # TODO get the oldest python pid

    # pid = int(input('pid='))
    #
    #
    # # now we need to get the address for this pid??
    #
    # with open(INJ_BIN_PATH, 'rb') as f:
    #     inj_bin = f.read()
    #
    # # attach to proc
    # libc.ptrace(PTRACE_ATTACH, pid, None, None)
    #


if __name__ == '__main__':
    print('injector started')
    main()

