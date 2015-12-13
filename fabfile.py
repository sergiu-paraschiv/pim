from fabric.api import *

env.hosts = ['pi@192.168.1.104']

def deploy():
    code_path = '/media/pi/Extern/work/pim'
    with cd(code_path):
        run('git pull')
