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

#list of tokens in the language
tokens=['int','main','(',')','begin','end',';','[',']','for','=','to','do','+','-','*','/',]
print(tokens)

#reference parsing table
parse_table={'0':{'int':'S 2','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'1','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'1':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'A','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'2':{'int':'NA','main':'S 3','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'3':{'int':'NA','main':'NA','(':'S 4',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'4':{'int':'NA','main':'NA','(':'NA',')':'S 5','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'5':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'S 6','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'6':{'int':'S 10','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 5',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'S 11','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'7','DEC':'8','ARRAY':'NA','F':'NA','FORL':'9','E':'NA','T':'NA','STMT':'NA'}
,
'7':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'S 12',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'8':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 2',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'S 11','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'13','E':'NA','T':'NA','STMT':'NA'}
,
'9':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 3',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'10':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 15','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'14','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'11':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 16','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'12':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'R 1','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'13':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 4',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'14':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'S 17','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'15':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'S 18',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'16':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'S 19','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'17':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 6',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'R 6','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'18':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'20','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'19':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'S 24','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA',')MT':'NA'}
,
'20':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'S 25','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'21':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'S 18',']':'R 15','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 15','+':'R 15','-':'R 15','*':'R 15','/':'R 15','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'22':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'R 16','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 16','+':'R 16','-':'R 16','*':'R 16','/':'R 16','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'23':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'R 17','id':'NA','[':'NA',']':'R 17','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 17','+':'R 17','-':'R 17','*':'R 17','/':'R 17','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'24':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'S 26','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'25':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'R 7','id':'NA','[':'NA',']':'R 7','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 7','+':'R 7','-':'R 7','*':'R 7','/':'R 7','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'26':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 26','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'37','FORL':'NA','E':'27','T':'28','STMT':'NA'}
,
'27':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'S 29','+':'S 30','-':'S 31','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'28':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 11','+':'R 11','-':'R 11','*':'S 32','/':'S 33','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'29':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 35','osb':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'34'}
,
'30':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'37','FORL':'NA','E':'NA','T':'36','STMT':'NA'}
,
'31':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'37','FORL':'NA','E':'NA','T':'38','STMT':'NA'}
,
'32':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'39','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'33':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'40','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'34':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'S 41','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'35':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'S 42','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'36':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 9','+':'R 9','-':'R 9','*':'S 32','/':'S 33','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'37':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','eq':'NA','to':'NA','do':'R 14','+':'R 14','-':'R 14','*':'R 14','/':'R 14','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'38':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 10','+':'R 10','-':'R 10','*':'S 32','/':'S 33','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'39':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 12','+':'R 12','-':'R 12','*':'R 12','/':'R 12','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'40':{'int':'S2','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'R 13','+':'R 13','-':'R 13','*':'R 13','/':'R 13','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'41':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'R 8',';':'NA','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'42':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'NA','id':'S 21','[':'NA',']':'NA','num':'S 22','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'23','F':'43','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
,
'43':{'int':'NA','main':'NA','(':'NA',')':'NA','begin':'NA','end':'NA',';':'R 18','id':'NA','[':'NA',']':'NA','num':'NA','for':'NA','=':'NA','to':'NA','do':'NA','+':'NA','-':'NA','*':'NA','/':'NA','$':'NA','S':'NA','CODE':'NA','DEC':'NA','ARRAY':'NA','F':'NA','FORL':'NA','E':'NA','T':'NA','STMT':'NA'}
}

# 2 * (number of elements in the grammar)
no_ele={'1':14,'2':2,'3':2,'4':4,'5':0,'6':6,'7':8,'8':18,'9':6,'10':6,'11':2,'12':6,'13':6,'14':2,'15':2,'16':2,'17':2,'18':6}

#grammar head (non-terminal)
gram_name={'1':'S','2':'CODE','3':'CODE','4':'CODE','5':'CODE','6':'DEC','7':'ARRAY','8':'FORL','9':'E','10':'E','11':'E','12':'T','13':'T','14':'T','15':'F','16':'F','17':'F','18':'STMT'}

#error handler
def error_handler(pointer):
    #yet to write the code
    print('hello')
    x=6
    return x

#tokenizer method
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

#syntax analyzer method
def syntax_analyser(token_list):
    top=0
    stack_token=['0']
    j=len(token_list)
    i=0
    while(i<j):
        x=parse_table[stack_token[top]][token_list[i]].split()
        if(x[0]=='S'):
            print('shift')
            stack_token.append(token_list[i])
            stack_token.append(x[1])
            top+=2
            i+=1
            print(stack_token)
        elif(x[0]=='R'):
            print('reduce')
            stack_token=stack_token[:(top-no_ele[x[1]])+1]
            top-=no_ele[x[1]]
            stack_token.append(gram_name[x[1]])
            top+=1
            stack_token.append(parse_table[stack_token[top-1]][stack_token[top]])
            top+=1
            print(stack_token)    
        elif(x[0]=='NA'):
            print("syntax error..!")
            exit()
        elif(x[0]=='A'):
            print("accepted..!\n")
            exit()
        else:
            break;        
                


        


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
    token_list.append('$')
    print("analysing syntax for the obtained tokens...")
    syntax_analyser(token_list)




try:
    main()
except Exception as e:
    print("Compiler: Unkown compile time Exception occured..."+e)        