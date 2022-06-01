command = "G()(al)"

def interpret(command):
    answer = ""
    for i in range(len(command)):
        if command[i] == "(" and command[i +1] == ")":
            answer += "o"
        elif command[i] == "G":
            answer += "G"
        elif command[i] == "(" and command[i +1] == "a":
            answer += "al"
            
    return answer

print(interpret(command))