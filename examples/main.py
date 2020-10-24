from terrapy import Item, Plan

import module_a


plan = Plan()

plan += Item(
    "terraform",
    required_version='">= 0.13"',
)

plan += Item("variable", "image", type="string", default='"redis"')

plan += Item(
    "variable",
    "test_variable",
    type="list(object({one=number, two=number}))",
    default=[{"one": 1, "two": 2}],
)

plan += Item("provider", "docker", host='"unix:///var/run/docker.sock"')
plan += Item("resource", "docker_container", "foo", image="var.image", name='"foo"')
plan += Item("module", "module_a", source='"./module_a"')

plan += Item("output", "container_foo_id", value="docker_container.foo.id")
plan += Item("output", "container_bar_id", value="module.module_a.container_bar_id")
