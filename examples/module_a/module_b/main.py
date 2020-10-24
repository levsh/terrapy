from terrapy import Item, Plan

import b


plan = Plan()

plan += Item("provider", "docker", host='"unix:///var/run/docker.sock"')
plan += Item("resource", "docker_container", "zzz", image='"redis:latest"', name='"zzz"')
