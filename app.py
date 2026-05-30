"""
J.A.R.V.I.S — Double Clap Workspace Launcher
=============================================
Double clap → launches your workspace automatically.
Customize WORKSPACE_TASKS to open whatever you want.

Install: pip install pyaudio numpy
Run:     python jarvis.py
"""

import pyaudio, numpy as np, time, os, platform

# ── Config ───────────────────────────────────────────────
THRESHOLD  = 3000    # peak amplitude to count as clap (lower = more sensitive)
MIN_DELAY  = 0.2     # min seconds between claps  (filters echo)
MAX_DELAY  = 1.0     # max seconds between claps  (longer = reset)
CHUNK      = 1024
RATE       = 44100
PAUSE_AFTER = 10     # seconds to pause listening after launch (prevent music triggers)

# ── OS helper ────────────────────────────────────────────
IS_MAC  = platform.system() == "Darwin"
IS_WIN  = platform.system() == "Windows"

def open_url(url):
    if IS_MAC:  os.system(f"open '{url}'")
    elif IS_WIN: os.system(f"start {url}")
    else:        os.system(f"xdg-open '{url}'")

def open_app(app):
    if IS_MAC:  os.system(f"open -a '{app}'")
    elif IS_WIN: os.system(f"start {app}")
    else:        os.system(f"{app} &")

def notify(msg):
    if IS_MAC:  os.system(f"osascript -e 'display notification \"{msg}\" with title \"J.A.R.V.I.S\"'")
    elif IS_WIN: print(f"[JARVIS] {msg}")   # use win10toast if you want popups on Windows
    else:        os.system(f"notify-send 'J.A.R.V.I.S' '{msg}'")

# ── Workspace Tasks ──────────────────────────────────────
# Add / remove / reorder tasks freely. Each is a (label, callable) tuple.
WORKSPACE_TASKS = [
    ("Opening Google",          lambda: open_url("https://www.google.com")),
    ("Opening Gmail",           lambda: open_url("https://mail.google.com")),
    ("Opening GitHub",          lambda: open_url("https://github.com")),
    ("Opening YouTube Music",   lambda: open_url("https://music.youtube.com")),
    ("Opening VS Code",         lambda: open_app("Visual Studio Code")),
]

def launch_workspace():
    print("\n" + "═"*45)
    print("  ⚡  J.A.R.V.I.S  WORKSPACE PROTOCOL ACTIVE")
    print("═"*45)
    notify("Workspace launching...")
    for label, task in WORKSPACE_TASKS:
        print(f"  ▶  {label}...")
        try:    task()
        except Exception as e: print(f"     ⚠ Failed: {e}")
        time.sleep(0.6)
    print("═"*45)
    print(f"  ✅  All done! Pausing mic for {PAUSE_AFTER}s...\n")
    notify("Workspace ready!")
    time.sleep(PAUSE_AFTER)

# ── Audio Setup ──────────────────────────────────────────
def make_stream():
    p = pyaudio.PyAudio()
    s = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
               input=True, frames_per_buffer=CHUNK)
    return p, s

def peak(data):
    return np.abs(np.frombuffer(data, dtype=np.int16)).max()

# ── Clap Detection ───────────────────────────────────────
def listen():
    p, stream = make_stream()
    last_clap, count = 0, 0

    print("\n╔══════════════════════════════════════════╗")
    print("║   J.A.R.V.I.S  —  Clap Detector Active  ║")
    print("║   👏 Double clap to launch workspace     ║")
    print("║   Ctrl+C to stop                         ║")
    print("╚══════════════════════════════════════════╝\n")

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if peak(data) <= THRESHOLD:
                continue

            now   = time.time()
            delta = now - last_clap

            if delta > MIN_DELAY:
                count      = count + 1 if delta < MAX_DELAY else 1
                last_clap  = now
                bar        = "█" * count + "░" * (2 - min(count, 2))
                print(f"  👏  Clap {count}/2  [{bar}]")

                if count == 2:
                    launch_workspace()
                    count = 0

    except KeyboardInterrupt:
        print("\n  👋  Shutting down J.A.R.V.I.S...\n")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

# ── Entry ─────────────────────────────────────────────────
if __name__ == "__main__":
    listen()