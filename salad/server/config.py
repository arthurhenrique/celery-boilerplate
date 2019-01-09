# -*- coding: utf-8 -*-

import os

server_ip = str(os.environ["REMOTE_ADDR"])

data = {
    "flower": {"port": "5555"},
    "rabbitmq": {
        "protocol": "amqp",
        "user": "guest",
        "pwd": "guest",
        "ip": server_ip,
        "port": "5672",
    },
}
