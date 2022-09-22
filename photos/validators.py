import os                                                          

def isValidExtension(name):
    """ return true is the file extension is valid"""
    ext = os.path.splitext(name)[1]
    valid_extensions = ['.jpg', '.png']                                 
                                    
    if ext.lower() in valid_extensions:
        return True
    
    return False
    
def isValidSize(value):
    """ limit image size by 3mb """
    limit = 5 * 1024 * 1024
    is_valid = True
    
    if value > limit:
        return False
    return is_valid
