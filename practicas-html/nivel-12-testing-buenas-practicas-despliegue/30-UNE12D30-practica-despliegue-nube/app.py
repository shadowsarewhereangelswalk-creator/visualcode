import os
import sys

PRACTICA = "UNE12D30"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D30"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from wsgi import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "10000")),
        debug=False,
    )
