# terrapy
Python to Terraform converter

Create main.py file
```python
from terrapy import Item, Plan

plan = Plan()

plan += Item(
    "terraform",
    required_version='">= 0.13"',
)

plan += Item(
    "variable",
    "test_variable",
    type="list(object({one=number, two=number}))",
    default=[{"one": 1, "two": 2}],
)

plan += Item("provider", "docker", host='"unix:///var/run/docker.sock"')
plan += Item("resource", "docker_container", "foo", image='"redis"', name='"foo"')
plan += Item("module", "module_a", source='"./module_a"')

plan += Item("output", "container_foo_id", value="docker_container.foo.id")
```
Then run
```
$ terrapy generate -u
$ terraform validate
```

```
$ terrapy generate -h
usage: terrapy generate [-h] [-u] [DIR]

Generate terraform plans

positional arguments:
  DIR            directory with root main.py (default: current directory)

optional arguments:
  -h, --help     show this help message and exit
  -u, --upgrade  run 'terraform 0.13upgrade' command for each module
```
