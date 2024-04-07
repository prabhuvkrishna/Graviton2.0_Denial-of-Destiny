import pickle 
 
# Create a sample data 
data = {'TIME_DIFF': 0.000001,'Length': 114} 
 
# Open a file in binary write mode 
with open('data.pkl', 'wb') as file: 
    # Serialize the data and write it to the file 
    pickle.dump(data,file)
