# Hoymiles Solar

[![Docker Repository on Quay](https://quay.io/repository/lagomes/hoymiles_notifications/status "Docker Repository on Quay")](https://quay.io/repository/lagomes/hoymiles_notifications)

### Run command

    docker run -it \
        --name notifications --rm \
        -e USUARIO='your username' \
        -e LINK='https://global.hoymiles.com/platform/login' \
        -e SENHA='your password' \
        -e CHAT_ID='your chat idd' \
        -e DEBUG=0 \
        -e TOKEN='your token of telegram bot' \
        quay.io/lagomes/hoymiles_notifications:main

#### For tests

    podman run -it --name hoymiles \
        --rm \
        -e USUARIO='your username' \
        -e LINK='https://global.hoymiles.com/platform/login' \
        -e SENHA='your password' \
        quay.io/lagomes/hoymiles:main


# References

* [bot API telegram](https://core.telegram.org/bots)
* [Lib python](https://python-telegram-bot.org/)