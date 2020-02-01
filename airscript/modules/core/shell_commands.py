#!/usr/bin/env python3
from base64 import b64decode
from subprocess import CalledProcessError, call, check_call, check_output
from sys import exit, stdout
from time import sleep
from typing import Any, Union

import requests


class Commands():

    def __init__(self) -> None:
        ...

    def capture(self, shell_cmd: str) -> Any:
        try:
            return check_output(shell_cmd, shell=True).decode().rstrip()

        except(CalledProcessError):
            return False

    def run(self, shell_cmd: str) -> None:
        call(shell_cmd, shell=True)

    def return_value(self, shell_cmd: str) -> Union[str, bool]:
        try:
            return not bool(check_call(f"{shell_cmd} 2>/dev/null >/dev/null", shell=True))

        except(CalledProcessError):
            return False

    def clear(self) -> None:
        self.run("clear || tput clear")

    def quit(self, exit_code: int = 0) -> None:
        exit(exit_code)

    def stdout_write(self, str_to_write: str) -> None:
        stdout.write(str_to_write)
        stdout.flush()

    def nm_active(self) -> bool:
        return self.capture(
            "systemctl is-active network-manager.service | tr -d [:space:]"
        ).lower().startswith("active")

    def nm_start(self) -> bool:
        if not self.nm_active():
            self.run("sudo systemctl restart NetworkManager.service")
            self.run("sudo systemctl restart wpa_supplicant.service")
            return True

        else:
            return False

    def nm_stop(self) -> bool:
        if self.nm_active():
            self.run("sudo systemctl stop NetworkManager.service")
            self.run("sudo systemctl stop wpa_supplicant.service")
            return True
        else:
            return False

    def wait(self, wait_time: Union[int, float]) -> None:
        sleep(wait_time)

    def conn_active(self) -> bool:
        try:
            requests.get("http://www.google.com")
            return True

        except(requests.exceptions.ConnectionError, Exception):
            return False

    def b64d(self, encoded_string: str) -> str:
        return b64decode(encoded_string.encode()).decode()

    def get_uname(self) -> str:
        return self.capture("id -un")

    def get_nodename(self) -> str:
        return self.capture("uname -n")

    def get_kernel(self) -> str:
        return self.capture("uname -r")

    def get_ruid(self) -> str:
        return self.capture("id -u")

    def get_iface_status(self, iface_name: str) -> str:
        return self.capture(f"iw {iface_name} info 2>/dev/null | grep -i type | cut -d ' ' -f 2")

    def get_iface_state(self, iface_name: str) -> str:
        return self.capture(f"cat /sys/class/net/{iface_name}/operstate")

    def get_process_name(self, proc_id: str) -> str:
        try:
            return self.capture(f"ps -p {proc_id} -o comm= 2>/dev/null")

        except(CalledProcessError):
            return "Unknown"
