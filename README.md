# 간단한 Docker Healthchecker

구현자 홍성민

## 작동법 
1. `ssh -i <private.pem> ubuntu@ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com`에 연결 
2. `cd healthcheck` 
3. `docker ps` 로 컨테이너 이름 확인
4. `python3 healthchecker.py --container-name <컨테이너 이름>  
5. 해당 컨테이너가 'Running' 이면 유지, 그 외 상태이면 'Restart' 시행
