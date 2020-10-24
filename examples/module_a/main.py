from terrapy import Item, Plan

import a
import module_b


plan = Plan()

plan += Item("provider", "docker", host='"unix:///var/run/docker.sock"')
plan += Item("resource", "docker_container", "bar", image='"redis:latest"', name='"bar"')
plan += Item("module", "module_b", source='"./module_b"')

plan += Item("output", "container_bar_id", value="docker_container.bar.id")
