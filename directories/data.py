from .config import PATH
import os


##### IMHO a serializer isnt neccesary for such a simple microservice(no models, no DBs) #####
##### So the conversion to JSON will be here #####


class DataObtaining():

    def __init__(self):
        self.data = {"data": []} # JSON dictionary


    def collect_properties(self): # File name & creation date
        content = os.listdir(PATH) # Get a list of files & folders
        for object in content:
            if os.path.isdir(os.path.join(PATH, object)): # check if obj is a folder
                file_type = "folder"
            elif os.path.isfile(os.path.join(PATH, object)): # check if obj is a file
                file_type = os.path.splitext(object)[1]
            if file_type == "": # if no type, make it undefined
                file_type = "undefined"
            creation_time = os.path.getmtime(os.path.join(PATH, object)) # get creation time
            self.data["data"].append({"name": object, "type": file_type, "time": creation_time}) # compose data to JSON


    def get_data(self): 
        return self.data #return JSON
    
obtain_data = DataObtaining() 
obtain_data.collect_properties()


