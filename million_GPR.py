import numpy as np
import csv
output = []
b=[]
f = open( 'SongCSV.csv', 'rU' )
for line in f:
    cells = line.split( "," )
    output.append( ( cells[ 0 ],cells[ 11 ],cells[ 13 ],cells[ 14 ],cells[ 18 ],cells[ 19 ], ) )
#    output.append(cells)   
    
f.close()
print output[0]
song = np.array(output)
n,d = song.shape
for i in range(1,n):
    b.append(np.float64(song[i]))

song = np.array(b) # final array with columns in the following order Song number, Key Tempo, Time Signature, Energy, Loudness
song_features = song[:,1:]
song_num = song[:,0]
#a = input('Enter songer index:')
#print song_num[a]

#-------------------- step 1 (take in value of particular songs from KMT kernel)
KMT_val = K(x,y) #take the value of KMT kernel related to two given songs

#-------------------- step 2 (find alpha)
delta_matrix = np.corrcoef(x,y) #correlation matrix which shows us the correlation between two matrices and also the correlation with itself
delta = delta_matrix[0,1] # take only the the correlation values between two matrics x and y
sigma = 1 # for now I dont know the value of sigma which is the noise
sum1  = (sigma^2)*delta
alpha = 1/(KMT_val + sum1)

#--------------------- step 3 (find preferance for that particular song)

f_star = alpha * KMT_val

if (f_star > 0.5):
    print('To the play list')
else:
    print('Discard')