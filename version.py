import os
import sys
VERSION = sys.argv[2]
SEMANTIC_TYPE = sys.argv[1]
v = VERSION.split('.')
lol_string = ''
if SEMANTIC_TYPE == 'major':
    print('major......!')
    vs = int(v[0])
    vs += 1
    v[0] = vs
    v[1]= 0
    v[2]= 0
    lol_string = '.'.join(map(str, v))
elif SEMANTIC_TYPE == 'minor':
    print ('minor......!')
    vs = int(v[1])
    vs += 1
    v[1] = vs
    v[2] = 0
    lol_string = '.'.join(map(str, v))
else:
    print ('patch......!')
    vs = int(v[2])
    vs += 1
    v[2] = vs
    lol_string = '.'.join(map(str, v))

print('final_version', lol_string)
with open('.env', 'w') as writer:
     writer.write(f'export VERSION="{lol_string}"')
