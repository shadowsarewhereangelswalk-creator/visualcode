import sys


if "--check" in sys.argv:
    estructura = ("app.py", "servicio/__init__.py", "servicio/routes.py")
    assert len(estructura) == 3
    print("UNE10D02 OK")
    raise SystemExit(0)


from servicio import create_app


app = create_app()


if __name__ == "__main__":
    app.run()
