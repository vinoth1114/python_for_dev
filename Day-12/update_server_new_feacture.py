def update_server_config(file_path,key,value):
    key_found = False
    with open(file_path,'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
                key_found = True
            else:
                file.write(line)
    if not key_found:
        print(f"The {key} is not avaiable in the {file_path} fill")
def main():
    file_path = input("Enter The file Path: ")
    key = input("Enter The Key Here: ")
    value = input("Enter The Value Here: ")
    update_server_config(file_path,key,value)

if __name__=='__main__':
    main()