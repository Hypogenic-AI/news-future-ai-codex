import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    env = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
    }

    with (out_dir / "env.json").open("w", encoding="utf-8") as f:
        json.dump(env, f, indent=2)


if __name__ == "__main__":
    main()
