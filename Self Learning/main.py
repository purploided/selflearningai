# self learning ai that remembers you
# please, im sleep deprived
# ~nicolas

# 21/11/21
# it seems ive been livestreaming the development on tiktok
# LMAO
# ~nicolas

import subprocess
import os
from subprocess import run

startupQuestion = input("""Hey! I'm Jarad, right now, we are just setting me up.
Question, would you mind to uh, paste the folder address of 'Neural Network' here?
Please check the github for a tutorial on how to get the folder address
> """)

print("""Starting...
""")

os.chdir(f'{startupQuestion}')
run('python neural.py')