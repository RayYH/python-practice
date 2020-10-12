import subprocess


def run_bash(bash_command):
    try:
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            output = output.decode('utf8').strip()
        if error:
            error = error.decode('utf8').strip()
    except FileNotFoundError:
        output = None
        error = 'bash command not found'
    return {'output': output, 'error': error}
