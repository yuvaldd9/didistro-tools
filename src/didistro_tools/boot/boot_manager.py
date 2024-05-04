"""
Boot handler is responsible on the board booting options
"""

import logging

from pathlib import Path


KERNEL_CMDLINE_FILE = Path("/boot/cmdline.txt")
ROOTFS_1 = str(Path("/dev/disk/by-label/rootfs1").resolve())
ROOTFS_2 = str(Path("/dev/disk/by-label/rootfs2").resolve())
TOGGLE_MAPPING = {ROOTFS_1: ROOTFS_2, ROOTFS_2: ROOTFS_1}


class BootHandler:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("BootHandler")

        self._get_kernel_cmd()
        self._get_current_rootfs()

    def _get_kernel_cmd(self):
        """Read the kernel command"""

        with open(KERNEL_CMDLINE_FILE, "r") as kernel_cmd_file:
            self.kernel_cmd = kernel_cmd_file.read()

    def _get_current_rootfs(self) -> str:
        """Get the current rootfs"""
        self._get_kernel_cmd()
        self.current_rootfs = ROOTFS_1 if ROOTFS_1 in self.kernel_cmd else ROOTFS_2

    def toggle_rootfs(self):
        """Toggle between rootfs1 and rootfs2"""

        self._get_current_rootfs()
        self.kernel_cmd = self.kernel_cmd.replace(
            self.current_rootfs, TOGGLE_MAPPING[self.current_rootfs]
        )

        # Write the modified contents back to the file
        with open(KERNEL_CMDLINE_FILE, "w") as kernel_cmd_file:
            kernel_cmd_file.write(self.kernel_cmd)

        self.logger.info(
            f"Rootfs toggled from {self.current_rootfs} to {TOGGLE_MAPPING[self.current_rootfs]}"
        )
