import csv as _csv
def __tostr__(lists,lvl=0):
  lvl+=1
  newlist=[]
  if type(lists) == list or type(lists) == set:
    newlist = [__tostr__(n,lvl) for n in lists]
  else:
    if lvl == 2:
      newlist=[(str(lists),str(type(lists)).replace("<class '","").replace("'>",""))]
    else:
      newlist=(str(lists),str(type(lists)).replace("<class '","").replace("'>",""))
  return newlist 
def __tolist__(strs):
  try:
    strs=eval(strs)
  except:
    pass
  if type(strs) == list:
    newval = [__tolist__(n) for n in strs]
  else:
    vals=eval(str(strs))
    newval=eval(vals[1])(vals[0])
  return newval
"""
use cdm.new() or cdm.add() or cdm.read()
new(data,file_name) 'creates a new file or overwrites exsisting files
'data' is a list or array of variables
'file_name' is the name of the file to be made or edited


add(data,file_name) 'opens a csv file and adds data
'data' is a list or array of variables
'file_name' is the name of the file to be made or edited


read(file_name) 'reads a csv file and returns the data
'file_name' is the name of the file to be made or edited
Example:
read("test")
"""
def new(data,file_name):
    """
new(data,file_name) 'creates a new file or overwrites exsisting files
'data' is a list or array of variables
'file_name' is the name of the file to be made or edited

new.prompt if True 'new()' will ask user if they want to overwrite 
new.prompt is True by defult

new.overwrite if True overwrite an exsisting file without prompting user
new.overwrite is False by defult

new.normal if False data and type will be saved and whe data type will remain when read
new.normal if True data will be saved and all data will be set to string
new.normal is False by defult

Example:
data=[[1,2,3],[4,5,6]]
new(data,"test")
"""
    try:
      if new.overwrite == True:
        crash
      elif new.overwrite == False:
        if new.prompt == True:        
          dum=open(str(file_name)+'.csv', 'r', newline='')
          confirm=input(str(file_name)+" already exists.\nDo you want to overwrite (Y or N):")
          if confirm.lower() == "y" or confirm.lower() == "yes":
            crash
          else:
            print("Overwrite canceled")
        else:
          crash
    except:
      if new.normal==True:
        writeFile = open(str(file_name)+'.csv', 'w', newline='')
        writer = _csv.writer(writeFile)
        writer.writerows(data)
        writeFile.close()
      else:  
        writeFile = open(str(file_name)+'.csv', 'w', newline='')
        writer = _csv.writer(writeFile)
        data=__tostr__(data)
        writer.writerows(data)
        writeFile.close()
new.normal=False
new.overwrite=False
new.prompt=True
def add(data,file_name):
    """
add(data,file_name) 'opens a csv file and adds data
'data' is a list or array of variables
'file_name' is the name of the file to be made or edited
Example:
data=[[1,2,3],[4,5,6]]
add(data,"test")"""
    writeFile = open(str(file_name)+'.csv', 'a', newline='')
    data=__tostr__(data)
    writer = _csv.writer(writeFile)
    writer.writerows(data)
    writeFile.close()
def read(file_name):
    """
read(file_name) 'reads a csv file and returns the data
'file_name' is the name of the file to be made or edited
Example:
read("test")"""
    readFile = open(str(file_name)+'.csv', 'r', newline='')
    readr = list(_csv.reader(readFile))
    try:
      ret=__tolist__(readr)
    except:
      ret=readr
    return ret
