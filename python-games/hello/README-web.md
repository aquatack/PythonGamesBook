# Run this Pygame Zero game on the web with pygbag

## 1) Run locally with Pygame Zero (desktop)

```bash
cd /home/william/Code/PythonGamesBook/python-games/hello
/home/william/Code/PythonGamesBook/.venv/bin/pgzrun main.py
```

## 2) Package + serve with pygbag (web)

```bash
cd /home/william/Code/PythonGamesBook/python-games/hello
/home/william/Code/PythonGamesBook/.venv/bin/pygbag --ume_block 0 .
```

Then open:

- http://localhost:8000

If you run without `--ume_block 0`, a gray loading page may remain until you click/touch the page once.

## 3) Build only (no local web server)

```bash
cd /home/william/Code/PythonGamesBook/python-games/hello
/home/william/Code/PythonGamesBook/.venv/bin/pygbag --build .
```

The web output is generated under the build folder created in this game directory.
