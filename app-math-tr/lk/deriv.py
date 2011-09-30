import numpy as np
import scipy.signal as si
from PIL import Image

def deriv(im1, im2):
    fx = si.convolve2d(im1, 0.25 * np.array([[-1., 1.],[-1., 1.]])) + \
        si.convolve2d(im2, 0.25 * np.array([[-1., 1.],[-1., 1.]]) )    
    fy = si.convolve2d(im1, 0.25 * np.array([[-1., -1.],[1., 1.]])) + \
        si.convolve2d(im2, 0.25 * np.array([[-1., -1.],[1., 1.]]) )    
    ft = si.convolve2d(im1, 0.25 * np.ones((2,2))) + \
        si.convolve2d(im2, -0.25 * np.ones((2,2)))
                
    fx = fx[0:fx.shape[0]-1, 0:fx.shape[1]-1]    
    fy = fy[0:fy.shape[0]-1, 0:fy.shape[1]-1];
    ft = ft[0:ft.shape[0]-1, 0:ft.shape[1]-1];
    return fx, fy, ft
    
if __name__ == "__main__": 
    im1 = np.asarray(Image.open('flow1-bw-0.png'))
    im2 = np.asarray(Image.open("flow2-bw-0.png"))
    fx, fy, ft = deriv(im1, im2)

    
    
