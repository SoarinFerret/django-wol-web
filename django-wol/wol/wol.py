from django.shortcuts import get_object_or_404
from .models import Computer
import os
import hashlib

# checks if provided hash matches system hash
def check_hash(pwd):
    sys_hash = os.environ.get('HASH')
    my_hash = hashlib.sha256(pwd.encode()).hexdigest()
    return sys_hash == my_hash
    

# always returns 0
def send_wol(computer_pk):
    c = get_object_or_404(Computer, pk=computer_pk)
    return os.system("wakeonlan " + c.mac_addr)

# Returns 0 if successful, 1 if it failed
def send_ping(computer_pk):
    c = get_object_or_404(Computer, pk=computer_pk)
    return os.system("ping -c 1 " + c.ip_addr)