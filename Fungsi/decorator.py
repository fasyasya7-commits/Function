def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

# Menggunakan decorator pada fungsi dengan simbol @
@my_decorator
def say_hello(name):
    print("halo, selamat belajar Python!")


#Memanggil fungsi yang telah didekorasi
say_hello("Alice")