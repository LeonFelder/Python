evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""
titulo, resumen = evaluar.split('resumen: ')
if len(titulo.strip('título: ').split()) <= 10:
    print('título Ok')
else:
    print('título demasiado largo')
oraciones = [0,0,0,0]
for elem in resumen.split('.'):
    if len(elem.split()) < 13:
        oraciones[0] += 1
    elif len(elem.split()) < 18:
        oraciones[1] += 1
    elif len(elem.split()) < 26:
        oraciones[2] += 1
    else:
        oraciones[3] += 1
print(f"""Cantidad de oraciones fáciles de leer: {oraciones[0]}, aceptables para leer: {oraciones[1]}, dificil de leer: {oraciones[2]}, muy difícil de leer:
{oraciones[3]}""")