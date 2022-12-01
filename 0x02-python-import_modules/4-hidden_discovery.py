#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4):
        if s.startswith("_"):
            h = 1
        else:
            print(s)
