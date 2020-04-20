#compiler designed for following hypothetical language
'''

int main()

begin

int Arr_name[size];

for i= num to expression do

var = Arr-name[var];

End

'''
import sys
tokens=['int','main','(',')','begin','end',';','[',']','for','=','to','do','+','-','*','/',]
print(tokens)

def error_handler(pointer):
    #yet to write the code
    print('hello')
    x=6
    return x


def tokenizer(program_string):
    program_string+='$'
    pointer=0
    lis=[] 
    while program_string[pointer] != "$":
        current_string=""
        if program_string[pointer].isalpha():
            current_string+=program_string[pointer]
            pointer+=1
            while program_string[pointer].isalnum() or program_string[pointer]=="_":
                current_string+=program_string[pointer]
                pointer+=1    
            if current_string in tokens:
                lis.append(tokens[tokens.index(current_string)])
            else:
                lis.append('id')    
        elif program_string[pointer].isnumeric():
            current_string+=program_string[pointer]
            pointer+=1
            dot_count=0
            while program_string[pointer].isnumeric() or program_string[pointer]==".":
                if program_string[pointer]==".":
                    dot_count+=1
                current_string+=program_string[pointer]
                pointer+=1
            if dot_count>1:
                x=error_handler(pointer)
                print('Error in Tokenizer Line No. : '+str(x)+' unidentified token '+current_string)
                exit()
            else:
                lis.append('num')
        else:
            if program_string[pointer]!=" " and program_string[pointer]!="\n":
                lis.append(tokens[tokens.index(program_string[pointer])])
                pointer+=1
            else:
                pointer+=1                             
    return lis

def main():
    if len(sys.argv) < 2:
        print("Compiler: No input file mentioned...\nUse Syntax cdproj.py <filename>")
        exit()
    program_string=open(sys.argv[1],'r').read() 
    print("\nProgram\n")
    print(program_string)
   
    token_list=tokenizer(program_string)
    print("\nTokens\n")
    print(token_list)



try:
    main()
except Exception as e:
    print("Compiler: Unkown compile time Exception occured..."+e)        