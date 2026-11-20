"""Functions and reusable checks

Time: 7 minutes
Goal: Write a reusable function with inputs and a return value.

Explanation:
def creates a function. Parameters receive caller inputs; limit_ms has a default. return sends a value back to the caller. Keyword arguments make optional settings readable. Keeping the check independent of printing makes it reusable in pytest.

Expected result:
True, False, False.

Try it:
Call the function at exactly 800 ms. Change the default to 1000 and predict which calls change.
"""

def is_acceptable(status_code, response_ms, limit_ms=800):
    return status_code == 200 and response_ms <= limit_ms

def gen_fib(r=10):
    fib=[]
    try:
        r = int(r)
    except Exception:
        raise Exception("invalid range")

    a,b=0,1

    for _ in range(1,r):
        fib.append(a)
        a,b = b,a+b
    return fib


def gen_fib1(r=10):
    fib=[]
    try:
        r = int(r)
    except Exception as e:
        print(e)
        return fib
    a,b=0,1

    for _ in range(1,r):
        fib.append(a)
        a,b = b,a+b
    return fib

def call_gen_fib1(r):
    gen_fib1(r)


if __name__=="__main__":
    print(is_acceptable(200, 600))
    print(is_acceptable(500, 100))
    print(is_acceptable(200, 600, limit_ms=500))
    print(gen_fib(5))
    print(gen_fib(10))
    try:
        print(gen_fib("Hello World"))
    except Exception as e:
        print(e)

    print(call_gen_fib1("Hello World"))
