# =============================================================================
# # file 1
# 
# file = open('ALP_2patternA.txt','r')
# file2= file.readlines()
# Pi,Qi,P, Q, R, Ri=[],[],[], [], [], []
# 
# for i in range(0, len(file2)-1):
#     P.append(file2[i].rstrip())
#     Q.append(file2[i+1].rstrip())
#     Pi.append(int(P[i],2))
#     Qi.append(int(Q[i],2))
#     if(Qi[i] != 0):
#         Ri.append((6^Pi[i])%Qi[i])
#     else:
#         Ri.append(0)
#     
# 
# 
# for i in range(0, len(Ri)-1):
#     R.append(bin(Ri[i])[2:].zfill(16))
#     
#   
# filew = open('p3_group_x_dmem_A.txt','w')
# for i in range(0, len(R)):
#     filew.write(R[i])
#     filew.write('\n')
#     print(R[i])
# 
# file.close()  
# filew.close()
# 
# # file 2
# 
# file = open('ALP_3patternB.txt','r')
# file2= file.readlines()
# Pi,Qi,P, Q, R, Ri=[],[],[], [], [], []
# 
# for i in range(0, len(file2)-1):
#     P.append(file2[i].rstrip())
#     Q.append(file2[i+1].rstrip())
#     Pi.append(int(P[i],2))
#     Qi.append(int(Q[i],2))
#     if(Qi[i] != 0):
#         Ri.append((6^Pi[i])%Qi[i])
#     else:
#         Ri.append(0)
#     
# 
# 
# for i in range(0, len(Ri)-1):
#     R.append(bin(Ri[i])[2:].zfill(16))
#     
#   
# filew = open('p3_group_x_dmem_B.txt','w')
# for i in range(0, len(R)):
#     filew.write(R[i])
#     filew.write('\n')
#     print(R[i])
# 
# file.close()  
# filew.close()
# 
# =============================================================================
# =============================================================================
# 
# # file 3
# 
# file = open('ALP_4patternC.txt','r')
# file2= file.readlines()
# Pi,Qi,P, Q, R, Ri=[],[],[], [], [], []
# 
# for i in range(0, len(file2)-1):
#     P.append(file2[i].rstrip())
#     Q.append(file2[i+1].rstrip())
#     Pi.append(int(P[i],2))
#     Qi.append(int(Q[i],2))
#     if(Qi[i] != 0):
#         Ri.append((6^Pi[i])%Qi[i])
#     else:
#         Ri.append(0)
#     
# 
# 
# for i in range(0, len(Ri)-1):
#     R.append(bin(Ri[i])[2:].zfill(16))
#     
#   
# filew = open('p3_group_x_dmem_C.txt','w')
# for i in range(0, len(R)):
#     filew.write(R[i])
#     filew.write('\n')
#     print(R[i])
# 
# file.close()  
# filew.close()
# 
# 
# 
# # file 4
# 
# file = open('ALP_5patternD.txt','r')
# file2= file.readlines()
# Pi,Qi,P, Q, R, Ri=[],[],[], [], [], []
# 
# for i in range(0, len(file2)-1):
#     P.append(file2[i].rstrip())
#     Q.append(file2[i+1].rstrip())
#     Pi.append(int(P[i],2))
#     Qi.append(int(Q[i],2))
#     if(Qi[i] != 0):
#         Ri.append((6^Pi[i])%Qi[i])
#     else:
#         Ri.append(0)
#     
# 
# 
# for i in range(0, len(Ri)-1):
#     R.append(bin(Ri[i])[2:].zfill(16))
#     
#   
# filew = open('p3_group_x_dmem_D.txt','w')
# for i in range(0, len(R)):
#     filew.write(R[i])
#     filew.write('\n')
#     print(R[i])
# 
# file.close()  
# filew.close()
# 
# =============================================================================
#Assume everything is equal to zero at first

setval1 = set()                   # A new empty set
setval1.add("00")                # Add a single member
setval1.update(["11", "10"])  
setval1 |= set(["10", "11"]) 
if "cat" in setval1:              # Membership test
  setval1.remove("00")
setval1.discard("101")    
print(setval1)
for item in setval1:              # Iteration AKA for each element
  print(item)
print("Item count:", len(setval1)) 
#1stitem = setval1[0]            
isempty = len(setval1) == 0      
setval1 = {"00011", "1111"}       
#setval1 = {}                    
setval1 = set(["01010", "00011"])     
setval2 = set(["10101", "00011"])
setval3 = setval1 & setval2             # Intersection
setval4 = setval1 | setval2             # Union
setval5 = setval1 - setval3             # Set difference
setval6 = setval1 ^ setval2             # Symmetric difference
issubset = setval1 <= setval2        # Subset test
issuperset = setval1 >= setval2      # Superset test
setval7 = setval1.copy()             # A shallow copy
setval7.remove("00011")
print(setval7.pop())              
setval8 = setval1.copy()
setval8.clear()                   
setval9 = {x for x in range(10) if x % 2} # Set comprehension; since Python 2.7
#print(setval1, setval2, setval3, setval4, setval5, setval6, setval7, setval8, setval9, issubset, issuperset)
filew = open('p3_group_x_p1_imem.txt','w')
s1=str(setval1).split('{')
s1=s1[1].split('}')
s1=s1[0].split(',')
s2=str(setval2).split('{')
s2=s2[1].split('}')
s2=s2[0].split(',')

filew.write(s1[0])
filew.write(s1[1])
filew.close()
filew = open('p3_group_x_p2_imem.txt','w')

filew.write(s2[0])
filew.write(s2[1])

filew.close()
