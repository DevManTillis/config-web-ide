#!/usr/bin/env python3
import os


def list_dir_contents(parent_dir, subdir=str()):
    state     = parent_dir + "/" + subdir
    contents  = os.listdir(parent_dir + "/" + subdir)
    file_data = {"contents": contents, "state": state}
    return file_data

print("PLAYBOOKS")
print(list_dir_contents("playbooks"))
print()

print("PYTHON_LIBS")
print(list_dir_contents("python_libs"))
print()

print("LOGS")
print(list_dir_contents("logs"))
print()

print("INVENTORY")
print(list_dir_contents("inventory"))
print()

print("CONFIG_SETS")
print(list_dir_contents("config_sets"))
print()

print("ANSIBLE_CFG")
print(list_dir_contents("ansible_cfg"))
print()

print("ROLES")
print(list_dir_contents("roles", "sample-role-1/tasks"))