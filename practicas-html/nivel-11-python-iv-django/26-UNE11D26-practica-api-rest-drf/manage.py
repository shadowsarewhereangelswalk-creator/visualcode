import os
import sys


PRACTICA = "UNE11D26"


if "--check" in sys.argv:
    assert PRACTICA.startswith("UNE11D")
    assert len(PRACTICA) == 8
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

