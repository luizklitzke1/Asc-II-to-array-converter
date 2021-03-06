# ASC II .txt to Array Converter

Simple Python script to generate arrays based on ASCII art in text files

## Utilization

Add the files you would like to convert to the folder: #### txt_samples ####.

The converted files will be saved at: #### generated_arrays ####.

## Exemple

### Asc II art informed to the program

```
                             /T /I          
                              / |/ | .-~/    
                          T\ Y  I  |/  /  _  
         /T               | \I  |  I  Y.-~/  
        I l   /I       T\ |  |  l  |  T  /   
 __  | \l   \l  \I l __l  l   \   `  _. |    
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |    
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |    
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./    
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]     
^.___~"--._    ~-{  .-~ .  `\ Y . /    |     
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______     
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.  
              (_/ .  ~(   /'     "~"--,Y   -=b-. _) 
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  ) 
                 (_/ .   `  /     /       !       )/  
                  / / _.   '.   .':      /        ' 
                  ~(_/ .   /    _  `  .-<_      -Row
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\ 
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"               
```

### Output array

```
[
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', 'T', ' ', '/', 'I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|', '/', ' ', '|', ' ', '.', '-', '~', '/', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', '\\', ' ', 'Y', ' ', ' ', 'I', ' ', ' ', '|', '/', ' ', ' ', '/', ' ', ' ', '_', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '\\', 'I', ' ', ' ', '|', ' ', ' ', 'I', ' ', ' ', 'Y', '.', '-', '~', '/', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'I', ' ', 'l', ' ', ' ', ' ', '/', 'I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', '\\', ' ', '|', ' ', ' ', '|', ' ', ' ', 'l', ' ', ' ', '|', ' ', ' ', 'T', ' ', ' ', '/', ' ', ' ', ' '], 
[' ', '_', '_', ' ', ' ', '|', ' ', '\\', 'l', ' ', ' ', ' ', '\\', 'l', ' ', ' ', '\\', 'I', ' ', 'l', ' ', '_', '_', 'l', ' ', ' ', 'l', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '`', ' ', ' ', '_', '.', ' ', '|', ' ', ' ', ' ', ' '], 
[' ', '\\', ' ', '~', '-', 'l', ' ', ' ', '`', '\\', ' ', ' ', ' ', '`', '\\', ' ', ' ', '\\', ' ', ' ', '\\', '\\', ' ', '~', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '`', '.', ' ', '.', '-', '~', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '], 
[' ', ' ', '\\', ' ', ' ', ' ', '~', '-', '.', ' ', '"', '-', '.', ' ', ' ', '`', ' ', ' ', '\\', ' ', ' ', '^', '.', '_', ' ', '^', '.', ' ', '"', '-', '.', ' ', ' ', '/', ' ', ' ', '\\', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '], 
['.', '-', '-', '~', '-', '.', '_', ' ', ' ', '~', '-', ' ', ' ', '`', ' ', ' ', '_', ' ', ' ', '~', '-', '_', '.', '-', '"', '-', '.', '"', ' ', '.', '_', ' ', '/', '.', '_', ' ', '.', '"', ' ', '.', '/', ' ', ' ', ' ', ' '], 
[' ', '>', '-', '-', '.', ' ', ' ', '~', '-', '.', ' ', ' ', ' ', '.', '_', ' ', ' ', '~', '>', '-', '"', ' ', ' ', ' ', ' ', '"', '\\', '\\', ' ', ' ', ' ', '7', ' ', ' ', ' ', '7', ' ', ' ', ' ', ']', ' ', ' ', ' ', ' ', ' '], 
['^', '.', '_', '_', '_', '~', '"', '-', '-', '.', '_', ' ', ' ', ' ', ' ', '~', '-', '{', ' ', ' ', '.', '-', '~', ' ', '.', ' ', ' ', '`', '\\', ' ', 'Y', ' ', '.', ' ', '/', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '], 
[' ', '<', '_', '_', ' ', '~', '"', '-', '.', ' ', ' ', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '_', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', 'I', ' ', ' ', 'Y', ' ', ' ', ' ', ':', ' ', '|'], 
[' ', ' ', ' ', '^', '-', '.', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '(', '_', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '>', '.', '_', ':', ' ', ' ', ' ', '|', ' ', 'l', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', '^', '-', '-', '.', ',', '_', '_', '_', '.', '-', '~', '"', ' ', ' ', '/', '_', '/', ' ', ' ', ' ', '!', ' ', ' ', '`', '-', '.', '~', '"', '-', '-', 'l', '_', ' ', '/', ' ', ' ', ' ', ' ', ' ', '~', '"', '-', '.', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', '_', '/', ' ', '.', ' ', ' ', '~', '(', ' ', ' ', ' ', '/', "'", ' ', ' ', ' ', ' ', ' ', '"', '~', '"', '-', '-', ',', 'Y', ' ', ' ', ' ', '-', '=', 'b', '-', '.', ' ', '_', ')', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', '_', '/', ' ', '.', ' ', ' ', '\\', ' ', ' ', ':', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', 'l', ' ', ' ', ' ', ' ', ' ', ' ', 'c', '"', '~', 'o', ' ', '\\'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', '.', '^', ' ', ' ', ' ', '\\', '_', '.', '-', '~', '"', '~', '-', '-', '.', ' ', ' ', ')', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', '_', '/', ' ', '.', ' ', ' ', ' ', '`', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '/', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '/', ' ', '_', '.', ' ', ' ', ' ', "'", '.', ' ', ' ', ' ', '.', "'", ':', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', "'", ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '(', '_', '/', ' ', '.', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', '_', ' ', ' ', '`', ' ', ' ', '.', '-', '<', '_', ' ', ' ', ' ', ' ', ' ', ' ', '-', 'R', 'o', 'w'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '_', '/', ' ', '.', ' ', "'", ' ', '.', '-', '~', '"', ' ', '`', '.', ' ', ' ', '/', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', 'z', '=', '.'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '(', ' ', '/', ' ', ' ', ' ', "'", ' ', ' ', ':', ' ', ' ', ' ', '|', ' ', 'K', ' ', ' ', ' ', '"', '-', '.', '~', '-', '.', '_', '_', '_', '_', '_', '_', '/', '/'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', '-', ',', '.', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', 'I', '/', ' ', '\\', '_', ' ', ' ', ' ', ' ', '_', '_', '{', '-', '-', '-', '>', '.', '_', '(', '=', '=', '.'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '/', '(', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', '<', ' ', ' ', ' ', ' ', '~', '"', '~', '"', ' ', ' ', ' ', ' ', ' ', '/', '/'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', "'", ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ',', 'v', '=', '.', ' ', ' ', '(', '('], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', '^', '.', ' ', '/', ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', '"', ' ', ' ', '}', '_', '_', ' ', '/', '/', '=', '=', '=', '-', ' ', ' ', '`'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '/', ' ', "'", ' ', "'", ' ', ' ', '"', '-', '.', ',', '_', '_', ' ', '{', '-', '-', '-', '(', '=', '=', '-'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', '^', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ':', ' ', ' ', 'T', ' ', ' ', '~', '"', ' ', ' ', ' ', 'l', 'l'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '.', ' ', ' ', '.', ' ', ' ', '.', ' ', ':', ' ', '|', ' ', ':', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', '_', '/', ' ', ' ', '/', ' ', ' ', ' ', '|', ' ', '|', ' ', 'j', '-', '"', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '^'], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '-', '<', '_', '(', '_', '.', '^', '-', '~', '"', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 

]

```
