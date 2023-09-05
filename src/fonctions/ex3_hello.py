def hello_world(nom=None):
    if nom:
        print("Hello " + str(nom))
    else:
        print("Hello world")


if __name__ == "__main__":
    hello_world("toto")
    hello_world([1, 2, 3])
    hello_world()
