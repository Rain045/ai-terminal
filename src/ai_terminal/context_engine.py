import subprocess
import os
import platform

class ContextEngine:
    @staticmethod
    def get_system_info():
        info = {
            "os": platform.system(),
            "distro": platform.version(),
            "cwd": os.getcwd(),
            "docker_installed": False,
            "docker_containers": [],
            "conda_installed": False,
            "conda_envs": [],
            "conda_default_env": os.environ.get("CONDA_DEFAULT_ENV", "base"),
            "shell": os.environ.get("SHELL", "/bin/bash")
        }

        # Check Docker & Running Containers
        try:
            subprocess.run(["docker", "--version"], capture_output=True, check=True)
            info["docker_installed"] = True
            docker_ps = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
            if docker_ps.returncode == 0:
                info["docker_containers"] = docker_ps.stdout.strip().split("\n")
        except:
            pass

        # Check Conda & Envs
        try:
            subprocess.run(["conda", "--version"], capture_output=True, check=True)
            info["conda_installed"] = True
            conda_list = subprocess.run(["conda", "env", "list", "--json"], capture_output=True, text=True)
            if conda_list.returncode == 0:
                import json
                envs_data = json.loads(conda_list.stdout)
                # Conda envs are paths, we extract the names or folder names
                info["conda_envs"] = [os.path.basename(env) for env in envs_data.get("envs", [])]
        except:
            pass

        return info

    @staticmethod
    def format_context_for_llm():
        info = ContextEngine.get_system_info()
        context = (
            f"OS: {info['os']}, CWD: {info['cwd']}, Shell: {info['shell']}\n"
            f"Docker: {'Available' if info['docker_installed'] else 'No'}. "
            f"Active Containers: {', '.join(info['docker_containers']) if info['docker_containers'] else 'None'}\n"
            f"Conda: {'Available' if info['conda_installed'] else 'No'}. "
            f"Envs: {', '.join(info['conda_envs']) if info['conda_envs'] else 'None'}. "
            f"Current Env: {info['conda_default_env']}"
        )
        return context
