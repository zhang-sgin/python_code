import traceback

def f1():
    ret = 123
    int('saasd')
    return ret


def run():
    try:
    
        f1()
        
    except Exception as e:
        
        ret = traceback.format_exc()
        print(type(ret))


run()
