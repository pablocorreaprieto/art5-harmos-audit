"""Test helper only: shortens the retry sleeps of generate.py (5 to 160 s) so that stress runs finish.
Loaded through PYTHONPATH by n1_run.py when --fast is given. The budget logic does not depend on the duration of a sleep."""
import os
import time

_real = time.sleep


def _fast(s):
    _real(min(s, float(os.environ.get("FAST_SLEEP_MAX", "0.02"))))


time.sleep = _fast
