import subprocess

def run():
    output = subprocess.check_output("ipconfig", shell=True).decode()
    return {'type': 'ipconfig', 'data': output}
