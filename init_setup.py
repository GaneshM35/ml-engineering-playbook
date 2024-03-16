import os
import subprocess
import datetime

print(f"[{datetime.datetime.now()}]: START")

print(f"[{datetime.datetime.now()}]: creating env with python 3.10 version")

subprocess.run(["conda", "create", "--prefix", "./env", "python=3.10", "-y"], check=True)

print(f"[{datetime.datetime.now()}]: installing the dev requirements")

# For Windows
if os.name == 'nt':
    pip_executable = os.path.join(".", "env", "Scripts", "pip")
# For Linux and macOS
else:
    pip_executable = os.path.join(".", "env", "bin", "pip")

subprocess.run([pip_executable, "install", "-r", "requirements_dev.txt"], check=True)

print(f"[{datetime.datetime.now()}]: activating the environment")

# For Windows
if os.name == 'nt':
    activate_script = os.path.join(os.getenv('CONDA_PREFIX'), 'Scripts', 'activate')
    subprocess.run([activate_script, './env'], shell=True, check=True)
# For Linux and macOS
else:
    activate_script = os.path.join(os.getenv('CONDA_PREFIX'), 'bin', 'activate')
    subprocess.run(['source', activate_script, './env'], shell=True, check=True)

print(f"[{datetime.datetime.now()}]: END")