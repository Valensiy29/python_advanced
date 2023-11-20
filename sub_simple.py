import shlex
import subprocess
import requests
def subproces():
    command = """curl -i -H "Accept: application/json" -X GET
https://api.ipify.org?format=json"""
    args = shlex.split(command)
    run_proc = subprocess.Popen(args)
    for i in args:
        if i.startswith('http'):
            res = requests.get(i).text
            print(res.strip())
    print(run_proc)

if __name__ == '__main__':
    res = subproces()