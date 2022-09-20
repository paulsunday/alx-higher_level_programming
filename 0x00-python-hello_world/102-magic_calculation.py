import dis

def magic_calculation(a, b):
    return (len(a), len(b))

dis.dis(magic_calculation(a,b))
