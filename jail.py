# Jerónimo Uc Matthew Emiliano 

from difflib import SequenceMatcher
import subprocess
import re
import os

def run_cmd(cmd, get_output=True, timeout=35, stop_on_error=True):
    """Run cmd logging input and output"""
    output = ""
    try:
        if get_output:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
            output, err = p.communicate(timeout=timeout)
        else:
            subprocess.check_call(cmd, stderr=subprocess.STDOUT, shell=True, timeout=timeout)
    except subprocess.CalledProcessError as e:
        if stop_on_error:
            print(f"Failed cmd: {e.returncode}")
    except Exception as e:
        if stop_on_error:
            print(f"Error: {str(e)}")
    return output

def check(test_str):
    # Basado en la terminal: solo permite caracteres dentro de [.aclist- ]
    pattern = r'^[.acflst\s]*$'
    if re.match(pattern, test_str):
        return True
    return False
