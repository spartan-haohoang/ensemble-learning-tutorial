#!/usr/bin/env python3
"""
Script to run Jupyter notebook programmatically
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_notebook(notebook_path: str, port: int = 8888, ip: str = "0.0.0.0") -> None:
    """Run Jupyter Lab with the specified notebook"""
    
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        sys.exit(1)
    
    print(f"🚀 Starting Jupyter Lab...")
    print(f"📓 Notebook: {notebook_path}")
    print(f"🌐 URL: http://{ip}:{port}")
    print(f"🔑 No authentication required")
    print("")
    print("Press Ctrl+C to stop the server")
    
    try:
        cmd = [
            "jupyter", "lab",
            "--ip", ip,
            "--port", str(port),
            "--no-browser",
            "--allow-root",
            "--NotebookApp.token=''",
            "--NotebookApp.password=''"
        ]
        
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down Jupyter Lab...")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Jupyter Lab: {e}")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Jupyter notebook")
    parser.add_argument(
        "--notebook", 
        default="ensembles.ipynb",
        help="Path to the notebook file (default: ensembles.ipynb)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8888,
        help="Port to run Jupyter on (default: 8888)"
    )
    parser.add_argument(
        "--ip", 
        default="0.0.0.0",
        help="IP address to bind to (default: 0.0.0.0)"
    )
    
    args = parser.parse_args()
    
    run_notebook(args.notebook, args.port, args.ip)


if __name__ == "__main__":
    main()
