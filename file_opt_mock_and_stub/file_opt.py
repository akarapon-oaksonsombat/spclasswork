import os
import os.path


def rm_when_lower(filename):
    # print(f"received filename => {filename}")
    if filename.isupper():
        # print(f"\"{filename}\" => is upper string")
        return
    # print(f"isFile => {os.path.isfile(filename)}")
    if os.path.isfile(filename):
        # print(f"remove filename => {filename}")
        os.remove(filename)

# if __name__ == '__main__':
#     fn = input('INPUT : ')
#     print(rm_when_lower(fn))
