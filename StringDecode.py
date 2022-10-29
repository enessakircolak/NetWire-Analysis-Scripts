my_dict = {"i":'l',"9":'p',"o":'6',"c":'b',"L":"N","-":"H","u":'U',"E":'G',"V":'b',"a":'D',"f":'x'
,"p":'.',"G":'1',"H":"k","Z":'y',"e":'j',"n":'g',"I":'h',"y":'0',"3":'-',"h":'2',"O":'4',"t":'9',
"7":'q',"N":'3',"k":'z',"C":'a',"X":'i',"w":'k',"l":'m',"2":"v","s":'p',"r":'R',"Q":'u',"R":'n',
"P":'C',"Q":'u',"0":'r',"d":'e',"5":'t',"z":'V',"6":'s',"4":'i',"W":'o',"U":'W',"S":'d',"g":'w',
"F":'M',"Y":'c',"8":'f',"M":'S',"T":'O',"_":'F',"q":'T',"r":'R',"D":'A',"j":'E'}
a = input()
c=0
text=""
for i in a:
    try:
        print(my_dict[i])
        text=text+my_dict[i]
    except KeyError:
        print("["+a[c]+"]")
        text=text+a[c] 
    c=c+1
text_file = open("C:\cozum.txt", "a")
text_file.writelines(a + " = " + text+"\n")
text_file.close()



