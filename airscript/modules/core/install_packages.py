#!/usr/bin/env python3
import platform
from pathlib import Path
from shutil import rmtree
from typing import List, Union


from .constants import (AIRCRACK_PATH, BASE_PATH, COMPILATION_STEPS, DEBPKGS, MDK_PATH,
                        PIXIEWPS_PATH, REAVER_PATH)
from .shell_commands import Commands


class PackageHandler(Commands):
    """Detects package manager used by system and attempts to install dependencies."""

    def __init__(self) -> None:
        super().__init__()
        self.IS_WINDOWS: bool = (platform.system().lower() == "windows")
        self.display_output = False

    def __get_distro(self) -> bool:
        """Get the OS-release"""

        if not(self.IS_WINDOWS):
            with open(Path("/etc/os-release"), "r") as RELEASE_FILE:
                self.OS_RELEASE: Union[List[str], str] = RELEASE_FILE.read().split("\n")
            self.OS_RELEASE = sum([i.split("=") for i in self.OS_RELEASE], [])
            self.OS_RELEASE = self.OS_RELEASE[self.OS_RELEASE.index("ID") + 1].strip('"').lower()
            return True

        else:
            return False

    def manage(self, **package_mapping) -> Union[str, bool]:
        """Manage Packages."""
        result = []

        try:
            for name, actions in package_mapping.items():
                if self.valid_command(name):

                    for cmd in actions:
                        if not self.display_output:
                            result.append(self.check(cmd))

                        else:
                            self.run(cmd)
                            result.append(True)

                    else:
                        return min(result)

            else:
                return False

        except(KeyboardInterrupt):
            return False

    def compile(self, **dist_mapping) -> bool:
        """Compile source packages, discriminate based on os-release"""

        try:
            if self.__get_distro():
                for rel_actual_name, actions in dist_mapping.items():
                    if self.OS_RELEASE == rel_actual_name:
                        for compile_instruction in actions[1:]:
                            self.run(compile_instruction)
                        else:
                            return True
                else:
                    for actions in dist_mapping.values():
                        if self.valid_command(actions[0]):
                            for compile_instruction in actions[1:]:
                                self.run(compile_instruction)
                            else:
                                return True
                    else:
                        return False

            return False

        except(KeyboardInterrupt):
            return False


class PackageInstaller(PackageHandler):
    """Install the packages."""

    def __init__(self) -> None:
        super().__init__()

    def install(self, remove_prev=True) -> bool:
        try:
            check_paths: List[bool] = [AIRCRACK_PATH.exists(),
                                       MDK_PATH.exists(),
                                       PIXIEWPS_PATH.exists(),
                                       REAVER_PATH.exists()]

            if not self.manage(dpkg=[f"dpkg -s {DEBPKGS}"]):

                if remove_prev or not min(check_paths):
                    if BASE_PATH.exists():
                        rmtree(BASE_PATH)
                        BASE_PATH.mkdir(parents=True)

                self.display_output = True
                self.manage(apt=["apt update", f"apt install -y {DEBPKGS}"])

            if not BASE_PATH.exists():
                BASE_PATH.mkdir(parents=True)

            if not min(check_paths):
                self.compile(
                    ubuntu=COMPILATION_STEPS,
                    debian=COMPILATION_STEPS,
                    mint=COMPILATION_STEPS,
                    kali=COMPILATION_STEPS,
                    raspbian=COMPILATION_STEPS
                )

            return True

        except(Exception) as e:
            print(e)
            return False
