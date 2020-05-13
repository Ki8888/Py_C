import pickle
favorite_color={"lion","yellow","kitty","red"}
favorite_color_load=pickle.dump(favorite_color, open("save.pkl","wb"))

import pickle
pidcke.dump(emp1,open('./emp1.pkl','wb'))
print('dump.pickle')
emp_1pkl=pickle.load(open('./emp1.pkl','rb'))
print('load pickle')
emp1_pkl.displayEmployee()