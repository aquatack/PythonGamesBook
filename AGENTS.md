# AGENTS

## Scope

This note documents the pygbag + web packaging troubleshooting done for the hello game at:
- python-games/hello

## Problem Observed

Running pygbag produced a gray browser window that looked like the app was not starting.

## Root Causes Found

1. Browser user engagement gate (UME)
- The default launcher can wait for user interaction before fully starting media/runtime behavior.
- Result: page can appear stuck on a gray/loading screen until a click/touch.

2. BrowserFS script URL issue in generated template/runtime path
- In this environment, the generated launcher attempted a BrowserFS URL that did not resolve.
- This can prevent runtime initialization.

3. Pygbag invocation from wrong folder
- Running pygbag from repo root without pointing to app folder can fail (missing main.py in cwd).

## Fixes Applied

1. Web entrypoint changed to stable plain pygame async loop
- File: python-games/hello/main.py
- Reason: reliable startup path for pygbag wasm runtime.
- Key requirement: loop includes await asyncio.sleep(0).

2. Added clearer run instructions
- File: python-games/hello/README-web.md
- Use:
  /home/william/Code/PythonGamesBook/.venv/bin/pygbag --ume_block 0 .
- Run from app folder:
  /home/william/Code/PythonGamesBook/python-games/hello

3. Template/cache workaround for BrowserFS URL
- Patched cached template:
  python-games/hello/build/web-cache/27613e24ba16d44f2a5c88150c6d64e5.tmpl
- BrowserFS script set to:
  https://cdn.jsdelivr.net/npm/browserfs@1.4.3/dist/browserfs.min.js

## Important Notes

- build/ and build/web-cache are generated artifacts.
- If cache is removed, the BrowserFS template workaround may need to be re-applied.
- Running without --ume_block 0 may still require one click/touch to continue startup.

## Known Good Commands

From app folder:

cd /home/william/Code/PythonGamesBook/python-games/hello
/home/william/Code/PythonGamesBook/.venv/bin/pygbag --ume_block 0 .

Build only:

cd /home/william/Code/PythonGamesBook/python-games/hello
/home/william/Code/PythonGamesBook/.venv/bin/pygbag --build .

## Future Maintenance

If gray screen returns:

1. Confirm command includes --ume_block 0.
2. Hard refresh browser (Ctrl+Shift+R).
3. Verify BrowserFS script URL in generated build/web/index.html.
4. Verify app is launched from python-games/hello (or pass full path to pygbag).
5. Check in-browser logs and local server logs for 404s.
