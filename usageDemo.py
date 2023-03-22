# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:23:22 2023

@author: Josef Tausendschön
"""

import keras
import numpy as np
import matplotlib.pyplot as plt

from keras.models import model_from_json

"""------------------------define network to load------------------------------"""

opti  = keras.optimizers.Adam         # the optimizer must be specified, however has no influence
loss  = 'mean_absolute_error'
alpha = 0.0005

file0 = '0_DNN_2D_grav_fiveMarker/0_keras_3HiddLayer_2D_grav_fiveMarker_structure.json'
file1 = '0_DNN_2D_grav_fiveMarker/1_keras_3HiddLayer_2D_grav_fiveMarker_weights.h5'

fileMax = '0_DNN_2D_grav_fiveMarker/2_keras_3HiddLayer_2D_grav_fiveMarker_xmax.txt'
fileMin = '0_DNN_2D_grav_fiveMarker/3_keras_3HiddLayer_2D_grav_fiveMarker_xmin.txt'

max_ = np.loadtxt(fileMax)
min_ = np.loadtxt(fileMin)

phiSmax = 0.64
ut      = 0.8562
""" ########################################################################## """

"""------------------------load and compile model------------------------------"""    

json_file         = open(file0,'r')                         # open json file
loaded_model_json = json_file.read()                        # read json file
json_file.close()                                           # close json file

loaded_model = model_from_json(loaded_model_json)           # load structure of .json file

loaded_model.load_weights(file1)                            # load weights of .h5 file

loaded_model.compile(loss=loss, optimizer=opti(lr=alpha))   # compile loaded model
""" ########################################################################## """

"""--------------------------load demo data------------------------------------"""

fileX = 'demoData/0_demoDataset2D_fiveMarker_grav_X_test.csv'
fileY = 'demoData/1_demoDataset2D_grav_y_test.csv'     

X = np.loadtxt(fileX) 
y_target = np.loadtxt(fileY) 

X_in = np.empty_like(X)

X_in[:,0]  = 1/X[:,0]
X_in[:,1:] = X[:,1:]

"""---------------------------normalize input----------------------------------"""

def knownMinMaxScalerAdjList(X_test_list,xmax,xmin):
    
    X_norm_list = np.empty_like(X_test_list)
        
    for col,(max_,min_) in enumerate(zip(xmax,xmin)):
                
        X_norm_list[:,col] = 2*(X_test_list[:,col]-min_)/(max_-min_)-1
            
    return X_norm_list

X_inN = knownMinMaxScalerAdjList(X_in,max_,min_)

"""------------------predict values and make parity plot-----------------------"""

y_pred = loaded_model.predict(X_inN)

xL  = np.arange(-0.4, 0.05, 1e-3)
yL  = np.arange(-0.4, 0.05, 1e-3)

plt.figure()
plt.plot(y_target,y_pred,'ro')
plt.plot(xL,yL,'k--')
plt.ylabel('prediction')
plt.xlabel('target')






