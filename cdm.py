
        else:
          crash
    except:
      writeFile = open(str(file_name)+'.csv', 'w', newline='')
      writer = _csv.writer(writeFile)
      data=__tostr__(data)
      writer.writerows(data)
      writeFile.close()
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
    writeFile.clos
