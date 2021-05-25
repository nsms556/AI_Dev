# [Monthly Project 1]

## 서버
  - Nvidia Jetson Nano Dev Kit
    - Ubuntu 18.04
    - Miniforge3-aarch64 (Anaconda)

## 파이썬 환경
  - `python venv` 대신 아나콘다 가상환경을 사용
    - ~/miniforge3/envs/mon1

  - conda install로 uwsgi 설치 실패
    - `pip install uwsgi`

  - django
    - djangorestframework

## uWSGI
  - 파일 변경시 재실행 필요
  - http vs socket
    - uwsgi 단독 실행시 http 사용
    - nginx 연동 시 socket과 소켓 파일 사용
  - ini
    - home : 파이썬 가상환경 위치
    - chdir : 프로젝트 최상위 경로 (manage.py가 존재하는 폴더)
    - module : wsgi.py 모듈
      - django.core.wsgi:get_wsgi_application() : 자동으로 처리
    - processes : 프로세스 수
    - vacuum : 종료시 생성된 파일 삭제 여부
    - daemonize : log 파일 경로
      -  백그라운드 실행시 설정
    - socket : 통신에 사용할 소켓 파일 (Nginx 사용시 필요)
      - 소켓 파일 대신 ip_address:port 사용 가능
      - chmod-socket : 소켓 파일의 권한 설정
    - master : master 프로세스로 실행
    - ``` ini
      [uwsgi]
      uid = jetson
      base = /home/%(uid)/workspace/monthly1
  
      home= /home/%(uid)/miniforge3/envs/mon1
      virtualenv = /home/%(uid)/miniforge3/envs/mon1
  
      chdir=%(base)
      module = django.core.wsgi:get_wsgi_application()
      env = DJANGO_SETTINGS_MODULE=monthly1.settings
  
      master=True
      processes = 1
  
      daemonize=%(base)/django.log
  
      # nginx
      socket = %(base)/uwsgi.sock
      chmod-socket=666
  
      # uwsgi
      #http = 192.168.0.21:5001
  
      vacuum=True
      ```
  - 추후에 시스템 전역 실행으로 변경
    - ini파일을 `/etc/uwsgi/sites`로 이동
    - service 등록 및 실행
      - `/etc/systemd/system/uwsgi.service`
      - ```
        [Unit]
        Description=uWSGI Emperor service
        
        [Service]
        ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
        Restart=on-failure
        KillSignal=SIGQUIT
        Type=notify
        NotifyAccess=all
        StandardError=syslog
        
        [Install]
        WantedBy=multi-user.target
        ```

## Nginx
  - `apt install nginx`
  - sites-available에 설정 파일 추가
    - ```
      upstream django {
          server unix:<uwsgi에서 설정한 소켓 파일 경로>
      }
      
      server {
              listen <port>;
              server_name <ip_address>;
      
              location = /favicon.ico { access_log off;       log_not_found off; }
      
              location /static/ {
                      root <static 폴더 위치>;
              }
      
              location / {
                  include         /etc/nginx/uwsgi_params;
                  uwsgi_pass      django;
              }
      }
      ```
  - sites-enabled에 심볼릭 링크로 위의 파일 추가
  - nginx 문법 검사
    - `sudo nginx -t`
  - 설정 완료 후 nginx 서비스 재실행
    - `sudo systemctl restart nginx`
    