import sys
import math
import numpy
import numpy.matlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.transforms as mtransforms
import matplotlib.ticker as ticker

in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &(frags['start'] <= start) &(frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &(frags['start'] <= end) &(frags['end'] > end))[0][0]] + 1

miniscore_data1 = 0
miniscore_data2 = 0
length = end_bin - start_bin -1
matrix1= numpy.matlib.zeros(shape = (length,length))
matrix2= numpy.matlib.zeros(shape = (length,length))


for i in range(len(data1)):
	if data1[i][0] < end_bin:
		if data1[i][0] > start_bin:
			if data1[i][1] < end_bin:
				if data1[i][1]> start_bin:
					F1 = data1[i][0] - start_bin -1
					F2 = data1[i][1] - start_bin -1
                    #square matrix
					matrix1[F1,F2] = math.log(data1[i][2],2) #Log-transform the scores 
					matrix1[F2,F1] = math.log(data1[i][2],2) #Log-transform the scores 
					if matrix1[F2,F1] < miniscore_data1:
						miniscore_data1 = matrix1[F2,F1]
					else: 
						miniscore_data1 = miniscore_data1
matrix1 = matrix1 - miniscore_data1

for i in range(len(data2)):
	if data2[i][0] < end_bin:
		if data2[i][0] > start_bin:
			if data2[i][1] < end_bin:
				if data2[i][1]> start_bin:
					F1 = data2[i][0] - start_bin -1
					F2 = data2[i][1] - start_bin -1
                    #square matrix
					matrix2[F1,F2] = math.log(data2[i][2],2) #Log-transform the scores 
					matrix2[F2,F1] = math.log(data2[i][2],2) #Log-transform the scores 
					if matrix2[F2,F1] < miniscore_data2:
						miniscore_data2 = matrix2[F2,F1]
					else: 
						miniscore_data2 = miniscore_data2
matrix2 = matrix2 - miniscore_data2



fig,(ax1,ax2,ax3) = plt.subplots(1,3)
dd = ax1.imshow(matrix1, cmap = "magma", vmin = -15, vmax = 0)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("DDCTCF")
d = ax2.imshow(matrix2, cmap = "magma", vmin = -15, vmax = 0)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title("DCTCF")

cb = plt.colorbar(dd, ax = [ax1,ax2], label = "Normalized read counts",fraction = 0.02, pad = 0.04, location = 'left')
tick_locator_0 = ticker.MaxNLocator(nbins=7)
cb.locaor = tick_locator_0
cb.update_ticks()


def remove_dd_bg(mat):
     N = mat.shape[0]
     mat2 = numpy.copy(mat)
     for i in range(N):
         bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
         mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
         if i > 0:
             mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
     return mat2
     
def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
    
    
decom = smooth_matrix(remove_dd_bg(matrix2)) - smooth_matrix(remove_dd_bg(matrix1))
norm1 = colors.CenteredNorm()
diff = ax3.imshow(decom, norm = norm1, cmap = "seismic")
ax3.set_title("difference plot")
ax3.set_xticks([])
ax3.set_yticks([])
cb1 = plt.colorbar(diff, ax = ax3, label = "log2 ratio", fraction = 0.05, pad = 0.05, location = 'right')
tick_locator = ticker.MaxNLocator(nbins=7)
cb1.locaor = tick_locator
cb1.set_ticks([-1.5, -1, -0.5, 0, 0.5, 1,1.5])
cb1.update_ticks()
plt.show()



#part3
# I run this in a different script but I copy them this place

import sys
import math
import numpy
import numpy.matlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors

matrix40000 = sys.argv[1]
data = numpy.loadtxt(matrix40000, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
#print(data)
start_bin = 54878
end_bin = 54951
matrix =  numpy.matlib.zeros(shape = (74,74))
miniscore = 0
for i in range(len(data)):
	if data[i][0] < 54952:
		if data[i][0] > 54877:
			if data[i][1] < 54952:
				if data[i][1]> 54877:
					F1 = data[i][0] - start_bin
					F2 = data[i][1] - start_bin
					matrix[F1,F2] = math.log(data[i][2],2)
					matrix[F2,F1] = math.log(data[i][2],2)
					if matrix[F2,F1] < miniscore:
						miniscore = matrix[F2,F1]
					else: 
						miniscore = miniscore
matrix = matrix - miniscore

#print(matrix)
score = []
postion = []
for i in range(5, 70):
	up = numpy.mean(matrix[(i - 5):i, i:(i + 5)])
	down = numpy.mean(matrix[(i-5):i, (i-5):i])
	score.append(up/2 + down/2)
	postion.append(i+start_bin)
    
#print(score)
#print(position)

fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
pl = ax[0].imshow(-matrix, cmap = "magma")
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_title("score for 40kb resolution")
ax[0].axis('off')
ax[1].set_xlim(54878,54951)
ax[1].set_xticks([54878,54951])
ax[1].set_xticklabels([10400000,13400000])
ax[1].scatter(postion,score)
plt.show()
