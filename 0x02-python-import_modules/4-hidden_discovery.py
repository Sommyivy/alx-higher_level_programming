#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4):
        h = s.startswith('_')
        if s != h:
            print(s)
