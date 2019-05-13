import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ui_index_file(host):
    f = host.file('/usr/share/bettercap/ui/index.html')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
