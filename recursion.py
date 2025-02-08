def fibonacci(num):
    assert num>=0 and int(num) == num,"The numbers should be a postivie whole number."
    if num in [0,1]:
        return num
    else:
      return fibonacci(num-1) + fibonacci(num-2)   

print(fibonacci(10))
# result is 89 thus the fibonacci of position 10 is 89.