
def converter_txt_para_array(name):

    print(f"txt_samples/{name}.txt")

    with open(f"txt_samples/{name}.txt", "r") as arquivo:
    
    
        print(f"Lendo o arquivo: {arquivo.name}")
        
        linhas = arquivo.readlines()
        
        array_linhas = []
        
        for linha in linhas:
            
            nova_linha = []
            
            for caracter in linha:
                
                if caracter != "\n":
                    nova_linha.append(caracter)
                
            array_linhas.append(nova_linha)
         
        print(f"Quantidade de linhas: {len(array_linhas)}")    
        
    return array_linhas 

def visualizar_array_montado(array):
    
    for linha in array:
        print(''.join(map(str, linha))) 
    
def gerar_txt_array(array, name):

    txt_array = open(f"generated_arrays/{name}_array.txt", "w")  
    
    txt_array.write("[\n")
    
    for linha in array:
        txt_array.write(f"{linha}, \n")
    
    txt_array.write("\n]")
    
    txt_array.close()
 
def gerar_txt_array2(array, name):

    txt_array = open(f"generated_arrays/{name}_array2.txt", "w")  
    
    txt_array.write("[")

    for linha in array:
        txt_array.write(f"{linha}")
    
    txt_array.write("]")
    
    txt_array.close()  
        
if __name__ == "__main__":    
    
    name = str(input("Informe o nome do arquivo .txt a ser convertido: "))
    
    array = converter_txt_para_array(name)
    
    visualizar_array_montado(array)

    gerar_txt_array(array, name)
    
    
    