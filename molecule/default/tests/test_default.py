import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_inspec_binary_exists(host):
    assert host.file('/usr/bin/inspec').exists


def test_inspec_binary_file(host):
    assert host.file('/usr/bin/inspec').is_file


def test_inspec_binary_which(host):
    assert host.check_output('which inspec') == '/usr/bin/inspec'
