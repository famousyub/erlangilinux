

import os
import re

from statistics import *

import datetime







__version__ = 'v1.0.0'









rep_log = input("entre path ")




nom_log = ""
list_log_all = os.listdir(rep_log)
list_log2g = []
list_log5g = []
list_log1 = []
list_log2 = []



        



class Application:
    def __init__(self) -> None:
        self.rep_log = rep_log
        #"C:\\Users\\g702306\Desktop\\testy000\\myapptelnet\\log"

        self.nom_log = ""
        self.list_log_all = os.listdir(rep_log)
        self.list_log2g = []
        self.list_log5g = []
        self.list_log1 = []
        self.list_log2 = []
        self.dctsave= {}
        self.dtexcel={}
        self.resd= []
        
        self.step = ["Step"]
        self.mes = ["Mesure"]
        self.uni = ["Unité"]
        self.min = ["Min"]
        self.max = ["Max"]
        self.it = ["IT"]
        self.mesmin = ["Mesure min"]
        self.moy = ["Moyenne"]
        self.mesmax = ["Mesure max"]
        self.eten = ["Etendue"]
        self.ic = ["IC"]
        self.cp = ["CP"]
        self.cpk = ["CPK"]
        self.res = ["Résultat"]
        self.steps = ["","Step"]
        self.mess = ["","Mesures"]
        
    
    def  startextract(self):
        
        for i in range(len(self.list_log_all)):        #Classification des logs selon leurs types
            ch = self.list_log_all[i]
            c = "5G"
            c2 = "2G"
            if c2 in self.list_log_all[i]:
                self.list_log2g.append(ch)
            elif c in list_log_all[i]:
                self.list_log5g.append(ch)
            else:
                with open(self.rep_log + "//" + self.list_log_all[i]) as log:
                    log.seek(0, os.SEEK_END)
                    if log.tell() > 31000:
                        self.list_log1.append(self.list_log_all[i])
                    else:
                        self.list_log2.append(self.list_log_all[i])
        
        
        for i in range(len(self.list_log2g)):                     #Extractions des steps et mesures
            if self.list_log2g[i][-8] == "F":
                i += 1
            else:
                with open(self.rep_log + "//" + self.list_log2g[i]) as log:
                    for line in log:
                        z = re.findall("\_\_", line)
                        mm = ''
                        if z:
                            ch = line
                            st = ''
                            for i in range(len(ch)):
                                if ch[i] == '_' and ch[i + 1] == '_':
                                    break
                                else:
                                    st = st + ch[i]
                        x = re.findall("\(\s", line)
                        y = re.findall("\,\s\d", line)
                        if x or y:
                            ch = line
                           # print(line.split(' ')[0])
                            fg = line.split(' ')[0]
                            
                            t = len(ch) - 2
                            if ch[t] != '.':
                                mm = line
                                self.step.append(st)
                                m = mm.split()
                                self.mes.append(m[0])
                                self.uni.append(m[3])
                                self.dctsave[fg]= ''
                                self.dtexcel[fg] ='' 
                                
                                
                                  
                                
                                #import time 
                                #print(m)
                                #time.sleep(2)
                                #os.system("cls")
                                if len(m) == 6:
                                    mi = re.findall("\,\)", m[5])
                                    print(mi)
                                    import time 
                               
                                    if mi:
                                        
                                        mini = ''
                                        r = len(m[5])
                                        for i in range(r - 2):
                                            strr = m[5]
                                            mini = mini + strr[i]
                                        self.min.append(mini)
                                        self.max.append('')
                                    else:
                                        self.min.append('')
                                        maxi = ''
                                        r = len(m[5])
                                        for i in range(r - 1):
                                            strr = m[5]
                                            maxi = maxi + strr[i]
                                        self.max.append(maxi)
                                else:
                                    r = len(m[5])
                                    mini = ''
                                    for i in range(r - 1):
                                        strr = m[5]
                                        mini = mini + strr[i]
                                    self.min.append(mini)
                                    maxi = ''
                                    r = len(m[6])
                                    for i in range(r - 1):
                                        strr = m[6]
                                        maxi = maxi + strr[i]
                                    self.max.append(maxi)
                    
                break
        i = 0
        col = []
        col.append(self.step)
        col.append(self.mes)
        self.dctsave["step"] = self.step[1:]
        
        for nom_log2g in self.list_log2g:                    #Extraction des valeurs, unités, minimum et maximum
            val = [nom_log2g[:11]]
            with open(self.rep_log + "//" + nom_log2g) as log:
                for line in log:
                    x = re.findall("\(\s", line)
                    y = re.findall("\,\s\d", line)
                    if x or y:
                        ch = line
                        t = len(ch) - 2
                        if ch[t] != '.':
                            mm = line
                            m = mm.split()
                            val.append(m[2])
                            self.dctsave[m[0]] = m[2]
                            self.dtexcel[m[0]] =  m[2] 
                            print ()
                            
                            
                             
            col.append(val)
            col.append(self.uni)
            col.append(self.min)
            col.append(self.max)
            self.dctsave['min'] = self.min 
            self.dctsave["max"]  =self.max
            self.dctsave["val"] =val
            self.dctsave['groupe'] =c2
            self.dctsave['uni'] =self.uni
        for i in range(1, len(self.min)):
            if self.max[i] == "" or self.min[i] == "":
                self.it.append("infini")
            else:
                x = float(self.max[i]) - float(self.min[i])
                self.it.append(x)
        col.append(self.it)
        for i in range(2, len(col)-4):
            for j in range(1, len(col[i])):
                if len(self.mesmin) < j+1:
                    self.mesmin.append(float(col[i][j]))
                else:
                    if float(self.mesmin[j]) > float(col[i][j]):
                        self.mesmin[j] = col[i][j]
        col.append(self.mesmin)
        
        for i in range(1, len(self.step)):
            moyy = 0
            coef = 0
            for j in range(2, len(col)-5):
                if len(col[j]) >= i+1:
                    moyy = float(col[j][i]) + moyy
                    coef += 1
            moyy = moyy / coef
            self.moy.append(round(moyy,2))
        col.append(self.moy)
        for i in range(2, len(col)-6):
            for j in range(1, len(col[i])):
                if len(self.mesmax) < j+1:
                    self.mesmax.append(float(col[i][j]))
                else:
                    if float(self.mesmax[j]) < float(col[i][j]):
                        self.mesmax[j] = col[i][j]
        col.append(self.mesmax)
        for i in range(1,len(self.mesmax)):
            self.eten.append(round(float(self.mesmax[i])-float(self.mesmin[i]),2))
        col.append(self.eten)
        for i in range(1, len(self.moy)):
            lis = []
            for j in range(2, len(col)-8):
                if len(col[j]) >= i+1:
                    lis.append(float(col[j][i]))
                    print(lis)
                    self.dctsave ["lis"] =lis 
                    
            if len(lis) > 2 :
                self.ic.append(round(stdev(lis),2))
        col.append(self.ic)
        for i in range(1, len(self.it)):
            print(len(self.ic))
            if self.it[i] == 'infini' and    len(self.ic)>1  :
                if self.ic[i] == 0:
                    self.cp.append("ERREUR")
            else:
                if len(self.ic ) > 2:
                    _eqcp = 6*self.ic[i]
                    self.cp.append(round(float(self.it[i])/(_eqcp),2))
                if self.it[i] == 'infini':
                    self.cp.append('ERREUR')
                else :
                    self.cp.append(round(float(self.it[i])/(6),2))
                
        col.append(self.cp)
        for i in range(1, len(self.min)):
            pass 
            
        for i in range(1,len(self.cpk)):
            if self.cpk[i] == "ERREUR":
                self.res.append("ERREUR")
            else:
                if float(self.cpk[i]) < 1.33:
                    self.res.append("INSUFFISANT")
                elif 1.33 < float(self.cpk[i]) < 1.67:
                    self.res.append("ACCEPTABLE")
                elif 1.67 < float(self.cpk[i]) < 2:
                    self.res.append("SATISFAISANT")
                else:
                    self.res.append("EXCELLENT")
        col.append(self.res)

        colt = []
        steps = ["","Step"]
        mess = ["","Mesures"]
        for i in range(len(self. list_log2g)):              #Extraction des steps
            if self.list_log2g[i][-8] == "F":
                i += 1
            else:
                with open(self.rep_log + "//" + self.list_log2g[i]) as log:
                    for line in log:
                        z = re.findall("\_\_", line)
                        mm = ''
                        if z:
                            ch = line
                            st = ''
                            for i in range(len(ch)):
                                if ch[i] == '_' and ch[i + 1] == '_':
                                    break
                                else:
                                    st = st + ch[i]
                            self.steps.append(st)
                            self.mess.append("Time")
                            self.steps.append(st)
                            self.mess.append("Retry")
                break
        self.steps.append("Flow Run Time")
        colt.append(steps)
        colt.append(mess)
        
        print(colt)
        
        for i in (list_log2g):                    #Extraction du FlowRunTime,temps et retry correspondants au steps
            colo =[i[:11]]
            if i[-8] == "F":
                colo.append("Failed")
            else:
                colo.append("Passed")
            with open(rep_log + "//" + i) as log:
                for line in log:
                    z = re.findall("\_\_", line)
                    if z:
                        ret = ''
                        time = ''
                        ch = line
                        st = ''
                        for i in range(len(ch)):
                            if ch[i] == '_' and ch[i + 1] == '_':
                                break
                            else:
                                st = st + ch[i]
                    x = re.findall("\-\-\>",line)
                    if x:
                        m = line.split()
                        if len(m) < 6:
                            ret = m[4]
                        else:
                            ret = m[5]
                    if line.__contains__("Test Time"):
                        m = line.split()
                        time = m[3] + m[4]
                        colo.append(time)
                        colo.append((ret))
                    if line.__contains__("Flow Run Time"):
                        m = line.split()
                        frt = m[3]+ m[4]
                        colo.append(frt)
                colt.append(colo)
        try:
            if len(colt[0]) > len(colt[2]):
                for i in range(0,4):
                    del colt[0][32]
                    del colt[1][32]
        except:
            pass
        x = datetime.datetime.now()
        
        date_time = x.strftime("%m_%d_%Y_%H_%M_%S")
    
    def affiche_dict(self):
        
        
        valur = self.dctsave['val']
        print(len(valur))
        
        mes = self.dctsave
        
        print(len(mes))
        print(mes)
        
        return self.dctsave
    
    
    
    def write_to_text(self,filename):
        dfNom = []
       
        print("moinnnn")
       
        min_ = self.dctsave['min'][1]
        print(min_)
        
        max_ = self.dctsave['max'][1]
        
        print("maxxx")
        print (  )
       
        with  open(filename , "w+") as f :
            df = """Nom ;status ;duree ;mesure ;limiteInferieure ;limiteSuperieure ;libelle ;unite ;groupe ;commentaire"""
            
            
            
            
            
         
            f.write("\n")
            
          
            #f.write(data_)
            f.write("\n")
            
            
            l = 1
            #appl=AppliNom()
            #durees , noms=appl.extract_time("R2326905450-27092023161006_2G_PASS.txt")
            #min', 'max', 'val', 'groupe', 'uni', 'lis'
            dct = {}
            
            
          
            
            for k1, v1 in self.dctsave.items() :
                if  k1 !="min"  or  k1!="max" or k1 !="" or k1!="Nom" or k1!="val" or  k1 !="groupe"  or  k1!="uni" or k1!="lis" :
                    dct[k1] =v1
                else  :
                    pass 
            print(self.dtexcel) 
            import time  
            time.sleep(20)   
            
            
           
          
            self.resd = [0 for _ in range(len(self.dctsave.keys()))]
            #print(self.step)
            df_ =set(self.step)
            for k, v in self.dctsave.items() :
                
                uni = 'db'
                if  k !="min"  or  k!="max" or k !="" or k!="Nom" or k!="val":
                    
                   
                    h = self.dctsave['uni']
                    
                    hh =[m for m in h  if m.isalpha() or m.isalnum()]
                    # if k == 'uni' :
                    #     for t in v:
                    #         if  t.lower() in  ['db' , 'dbm','ppm','mhz','dbc']  and  t not in ['%' ,'Unit' ,'('  ]   :
                    #             uni = v 
                    #             print(uni)
                    print(hh) 
                              
                    min_ = "infinity"  if min_ ==  "" else min_ 
                    max_ ="infinity" if max_ =='' else max_ 
                    
                    #nom_ =  dfNom[l] if  l <= (len(dfNom)-1) else dfNom[0]
                    
                    nummintest =  self.dctsave['min'][l] if  self.dctsave['min'][l]!="" else "infinity"
                    nummaxtext =self.dctsave['max'][l]  if self.dctsave['max'][l]!="" else "infinity"
                    res_ = [0,1,2]
                    x = datetime.datetime.now()
                    
                    date_time = x.strftime("%m_%d_%Y_%H_%M_%S")
                    
                    #g=type(v) != type('list')
                    #print(g)
                    # if g ==True:
                    #     if type(nummaxtext) is type('float') and  type(nummaxtext) is type('float') and  self.dctsave['min'][l] != "infinity" and type(v) != type('list'):
                    #         if  float(v)   > float(nummaxtext)  and float(v) <  float(nummaxtext) :
                    #             self.resd[l] =0
                    #     elif type(nummaxtext) is type('float') and  nummaxtext ==  'infinity' :
                    #         self.resd[l] = 0
                    #     else :
                    #         self.resd[l] = 1
                            
                            
                    
                    data_ = f"{self.dctsave['step'][l] + '_' + k } ;0 ; {date_time} ;  {v} ;{self.dctsave['min'][l]} ;{self.dctsave['max'][l]} ;{k} ; {hh[l]}   ; ''"
                    
                
                    
                    
                
                        
                    f.write(data_ + "\n")  
                    l+=1   
                    
                    
                    
       
        
        
        
            
            



class AppliNom :
    def __init__(self) -> None:
        self.Nom = ''
        self.rep =rep_log
        self.lstduree = []
        self.nom = []
        
    def extract_time(self,filename):
        
        with open(f"{self.rep}/{filename}",'r+') as f:
            realine = f.readline()
            while realine :
                if 'Test Time = ' in  realine :
                    duree = realine.split("=")[1]
                    self.lstduree.append(duree)
                
                if '.TEST_VERIFY' in realine :
                    self.nom.append(realine)
                
                realine  =f.readline()
        inse_ =''
        with open('duree.txt' , 'w+') as g :
            for d in self.lstduree :
                
                g.write(str(d))
        with open('nomm.txt','w+') as s :
            for _i in  self.nom:
                inse_ =  str(_i).split("______")[0]
                s.write(inse_)
                s.write("\n")
                
                
                        
    
        return self.lstduree , self.nom       
                
                
                 
            
        
        











    







