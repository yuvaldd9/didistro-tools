import argparse

from .boot import BootHandler


def main():
    parser = argparse.ArgumentParser(
        description="Toggle between rootfs partitions in cmdline.txt"
    )
    parser.add_argument(
        "action",
        choices=["toggle_rootfs", "get_current_rootfs"],
        help="Action to perform",
    )
    args = parser.parse_args()

    boot_handler = BootHandler()

    if args.action == "toggle_rootfs":
        boot_handler.toggle_rootfs()
    elif args.action == "get_current_rootfs":
        return boot_handler.toggle_rootfs()


if __name__ == "__main__":
    main()
