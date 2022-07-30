# Notificacoes

## Run Local
### define variables 
    export USUARIO='your username'
    export LINK='https://global.hoymiles.com/platform/login'
    export SENHA='your password'
    export CHAT_ID=-660131018
    export TOKEN='1111111111:AAFxLoSSPIVOqZo-39o6UiLK9sMGlmWu4TA'

### Run
    python notifications.py

## Docker

### Build
    buildah build -t solarmanpv:v1 
### Run container from localhost
    podman run -it --name notifications --rm -e USUARIO='your username' -e LINK='https://global.hoymiles.com/platform/login' -e SENHA='your password' -e CHAT_ID=-660131018 -e TOKEN='111111111:AAFxLoSSPIVOqZo-39o6UiLK9sMGlmWu4TA' localhost/solarmanpv:v1
### Run container from repository 
    podman run -it --name notifications --rm -e USUARIO='your username' -e LINK='https://global.hoymiles.com/platform/login' -e SENHA='your password' -e CHAT_ID=-660131018 -e TOKEN='111111111:AAFxLoSSPIVOqZo-39o6UiLK9sMGlmWu4TA' quay.io/lagomes/solarman_notifications:main
