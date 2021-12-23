import os 
import subprocess
import argparse

def check_status(container_name: str):
    process = subprocess.Popen(['docker', 'container', 'inspect', container_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    grep = subprocess.Popen(['grep', 'Status'], stdin=process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdout.close()
    out, err = grep.communicate()
    status = out.strip().decode('utf8').strip(',')
    
    if status == '"Status": "running"':
        print("Running")
    else:
        print(f"Container {container_name} 이 작동하고 있지 않습니다. 재시작 합니다.")
        restart_container(container_name)
        print("재시작 완료")


def restart_container(container_name: str):
    print(f"Restart Container {container_name}")
    process = subprocess.Popen(['docker', 'restart', container_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="container name")
    parser.add_argument('--container-name', type=str, help="컨테이너 이름을 입력하고 해당 컨테이너의 건강을 확인하세요!")
    args = parser.parse_args()
    container_name = args.container_name
    check_status(container_name)



