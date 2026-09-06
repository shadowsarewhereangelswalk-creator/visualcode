import sys


if "--check" in sys.argv:
    assert {"desarrollo", "pruebas", "produccion"} == set(("desarrollo", "pruebas", "produccion"))
    print("UNE10D03 OK")
    raise SystemExit(0)


from portal import create_app


app = create_app("desarrollo")


if __name__ == "__main__":
    app.run()
