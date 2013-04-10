##########################
#  Python DLL Injection
##########################

import os
import sys

from ctypes import windll, byref, c_int, c_ulong

PAGE_READWRITE     = 0x04
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
VIRTUAL_MEM        = (0x1000 | 0x2000)

h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
load_library  = kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

def inject_dll(pid, dll_path, thread_id=0):
    ''' 
    Inject dll into remote process by process id 
    @param pid: The pid of the process to inject
    @param path: Path to the DLL to inject into the process 
    '''
    assert isinstance(pid, int)
    assert isinstance(thread_id, int)
    assert isinstance(dll_path, basestring)
    kernel32 = windll.kernel32
    h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if not h_process:
        raise RuntimeError("Couldn't acquire a handle to PID: %d" % pid)
    alloc_address = kernel32.VirtualAllocEx(h_process, 0, len(dll_path), VIRTUAL_MEM, PAGE_READWRITE)
    kernel32.WriteProcessMemory(h_process, alloc_address, dll_path, len(dll_path), byref(c_int(0)))
    thread_id = c_ulong(thread_id)
    return kernel32.CreateRemoteThread(h_process, None, 0, load_library, alloc_address, 0, byref(thread_id))
        
if __name__ == '__main__':
    pid      = raw_input("[?] Target Pid: ")
    dll_path = raw_input("[?] DLL Path: ")

    if inject_dll(int(pid), dll_path):
        print "[*] Remote thread successfully created"
    else:
        print "[!] Failed to create remote thread"
