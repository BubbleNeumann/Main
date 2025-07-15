import subprocess


if __name__ == '__main__':
    subprocess.run(('python3', 'main.py'), check=True, capture_output=True)
    subprocess.run(('python3', 'injector.py'), check=True, capture_output=True)

