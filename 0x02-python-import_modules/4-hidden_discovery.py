#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for names in dir(hidden_4):
        if name.start("_"):
            break
        else:
            print("{}".formant(name))
