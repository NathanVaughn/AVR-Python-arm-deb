import os
import platform
import subprocess
import sys

packages = [
    "libpython3.10-minimal",
    "libpython3.10-stdlib",
    "python3.10-distutils",
    "python3.10-lib2to3",
    "python3.10-minimal",
    "python3.10",
]

dist_dir = os.path.join(os.getcwd(), "dist")
os.makedirs(dist_dir, exist_ok=True)

if platform.machine() not in {"AMD64", "x86_64"}:
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--privileged",
            "multiarch/qemu-user-static",
            "--reset",
            "-p",
            "yes",
        ]
    )

subprocess.run(
    [
        "docker",
        "run",
        "--rm",
        "-it",
        "--platform",
        "linux/arm64",
        "-v",
        f"{dist_dir}:/output/",
        "ghcr.io/bellflight/avr/visual:2023-06-03-20-14-33",
        "/bin/bash",
        "-c",
        "cd /output/ && apt-get update -y && apt-get install -y dpkg-repack"
        + " ".join(f"&& dpkg-repack {pkg}" for pkg in packages),
    ],
    stdout=sys.stdout,
    stderr=sys.stderr,
)
