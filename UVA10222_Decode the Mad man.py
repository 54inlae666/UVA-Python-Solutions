import sys

if __name__ == "__main__":

    KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

    lines = sys.stdin.read().splitlines()

    for line in lines:
        
        line = line.rstrip('\r\n')
        
        result = []

        for char in line.lower():
            
            if char in KEYBOARD:
                idx = KEYBOARD.index(char)
                result.append(KEYBOARD[idx-2])
            else:
                result.append(char)
        
        print("".join(result))


