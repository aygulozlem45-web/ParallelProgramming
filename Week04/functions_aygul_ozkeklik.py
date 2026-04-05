custom_power = lambda x=0,/, e=1 : x ** e

def custom_equation(x: int = 0 , y: int = 0 , /, a: int = 1, b: int=1 , * , c: int = 1) -> float :
  return (x**a + y**b)/c

def fn_w_counter() -> (int, dict[str, int]):
  if not hasattr(fn_w_counter, "calls"):
    fn_w_counter.calls = 0
