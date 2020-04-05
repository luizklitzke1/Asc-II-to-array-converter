
def convert_txt_to_array(name):

    print(f"txt_samples/{name}.txt")

    with open(f"txt_samples/{name}.txt", "r") as file:
    
    
        print(f"Lendo o arquivo: {file.name}")
        
        lines = file.readlines()
        
        lines_array = []
        
        for line in lines:
            
            new_line = []
            
            for character in line:
                
                if character != "\n":
                    new_line.append(character)
                
            lines_array.append(new_line)
         
        print(f"Amount of lines: {len(lines_array)}")    
        
    return lines_array 

def view_array(array):
    
    for line in array:
        print(''.join(map(str, line))) 
    
def generate_txt(array, name):

    txt_array = open(f"generated_arrays/{name}_array.txt", "w")  
    
    txt_array.write("[\n")
    
    for line in array:
        txt_array.write(f"{line}, \n")
    
    txt_array.write("\n]")
    
    txt_array.close()
 
def generate_txt2(array, name):

    txt_array = open(f"generated_arrays/{name}_array2.txt", "w")  
    
    txt_array.write("[")

    for line in array:
        txt_array.write(f"{line}")
    
    txt_array.write("]")
    
    txt_array.close()  
        
if __name__ == "__main__":    
    
    name = str(input("Inform the name of the .txt file to be converted: "))
    
    array = convert_txt_to_array(name)
    
    view_array(array)

    generate_txt(array, name)
    
    
    