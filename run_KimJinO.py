#from class_KimJinO import add1 as ad
import class_KimJinO as CK
a = CK.add1()
a.getPredict(5)

c = CK.add3()
c.getPredict3(4,3)

import pickle

###pickle 저장1
pickle.dump(a,open("./emp1.pkl","wb"))
print('dump pickle')

###pickle이 제대로 저장되었나 확인
a_1=pickle.load(open('./emp1.pkl','rb'))
print('load pickle')

a_1.getPredict(7)

##pickle 저장3
pickle.dump(c,open('./emp3.pkl','wb'))

c_1=pickle.load(open('./emp3.pkl','rb'))

c_1.getPredict3(3,3)