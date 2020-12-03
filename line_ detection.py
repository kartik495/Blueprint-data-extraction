import cv2

def get_lines(location):
    
    image=cv2.imread(location,0)
    #read image
    edges = cv2.Canny(gray,50,150,apertureSize = 3) 
      
    # This returns an array of r and theta values 
    lines = cv2.HoughLines(edges,1,np.pi/180, 200) 
    line_list=[]  
    # The below for loop runs till r and theta values  
    # are in the range of the 2d array 
    for r,theta in lines[0]: 
          
        # Stores the value of cos(theta) in a 
        a = np.cos(theta) 
      
        # Stores the value of sin(theta) in b 
        b = np.sin(theta) 
          
        # x0 stores the value rcos(theta) 
        x0 = a*r 
          
        # y0 stores the value rsin(theta) 
        y0 = b*r 
          
        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
        x1 = int(x0 + 1000*(-b)) 
          
        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
        y1 = int(y0 + 1000*(a)) 
      
        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
        x2 = int(x0 - 1000*(-b)) 
          
        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
        y2 = int(y0 - 1000*(a))

        line_list.append(x1,y1,x2,y2)
    return line_list
        
         
        
