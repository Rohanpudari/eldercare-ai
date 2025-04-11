import subprocess

def ask_phi(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "phi", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"
