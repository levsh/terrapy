from terrapy import Item, Plan


def test_item():
    item = Item("provider")
    assert item.type == "provider"
    assert item.args == ()
    assert item.kwds == {}
    assert item.items == ()
    assert item.format() == "provider {\n}"

    item = Item("provider", "docker")
    assert item.type == "provider"
    assert item.args == ("docker",)
    assert item.kwds == {}
    assert item.items == ()
    assert item.format() == 'provider "docker" {\n}'

    item = Item("provider", "docker", host='"unix:///var/run/docker.sock"')
    assert item.type == "provider"
    assert item.args == ("docker",)
    assert item.kwds == {"host": '"unix:///var/run/docker.sock"'}
    assert item.items == ()
    assert item.format() == 'provider "docker" {\n  host = "unix:///var/run/docker.sock"\n}'

    backend_item = Item(
        "backend", "consul", address='"demo.consul.io"', scheme='"https"', path='"example_app/terraform_state"'
    )
    item = Item(
        "terraform",
        backend_item,
        required_version='">= 0.13"',
    )
    assert item.type == "terraform"
    assert item.args == ()
    assert item.kwds == {"required_version": '">= 0.13"'}
    assert item.items == (backend_item,)
    assert item.format() == (
        """terraform {\n"""
        """  backend "consul" {\n"""
        """    address = "demo.consul.io"\n"""
        """    scheme = "https"\n"""
        """    path = "example_app/terraform_state"\n"""
        """  }\n"""
        """  required_version = ">= 0.13"\n"""
        """}"""
    )


def test_plan():
    plan = Plan()
    assert plan.items == []
    assert plan.modules == []
    assert plan.format() == ""

    plan = Plan()
    provider = Item("provider", "docker", host='"unix:///var/run/docker.sock"')
    resource = Item("resource", "docker_container", "foo", image='"redis:latest"', name='"foo"')
    module = Item("module", "module_a", source='"./module_a"')

    plan += provider
    assert plan.items == [provider]
    assert plan.modules == []

    plan += resource
    assert plan.items == [provider, resource]
    assert plan.modules == []

    plan += module
    assert plan.items == [provider, resource, module]
    assert plan.modules == [module]

    assert plan.format() == (
        """provider "docker" {\n"""
        """  host = "unix:///var/run/docker.sock"\n"""
        """}\n\n"""
        """resource "docker_container" "foo" {\n"""
        """  image = "redis:latest"\n"""
        """  name = "foo"\n"""
        """}\n\n"""
        """module "module_a" {\n"""
        """  source = "./module_a"\n"""
        """}"""
    )
