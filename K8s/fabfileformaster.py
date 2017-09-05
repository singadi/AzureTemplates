#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

vm0 = "{elbpublicdns}:8022"
vm0PiP = "10.0.0.4"
totalnodes = {nodeschosen}   
env.hosts = [vm0]
        
def deployall():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/etc_kubernetes_config' -o /etc/kubernetes/config""")
    sudo("""sed -i "s#{masterprivateip}#%s#g" /etc/kubernetes/config""" %vm0PiP)
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/etc_etcd_etcd.conf' -o /etc/etcd/etcd.conf""")
    sudo("""bash make-ca-cert.sh "%s" "IP:%s,IP:10.254.0.1,DNS:kubernetes,DNS:kubernetes.default,DNS:kubernetes.default.svc,DNS:kubernetes.default.svc.cluster.local""" %(vm0PiP,vm0PiP))
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/etc_kubernetes_apiserver' -o /etc/kubernetes/apiserver""")
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/etc_kubernetes_controller-manager' -o /etc/kubernetes/controller-manager""")
    try:
        sudo("init 6")
    except:
        print("This was fine just restarted the system.")