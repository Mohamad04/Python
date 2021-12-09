# Cubic Root


def cubic_root(n):

  calculated_cube = "{:.0f}".format(n**(1/3) )
  cube = int(calculated_cube)

  if cube*cube*cube == n:
      output = "{0}, exact!".format(cube)
  else:
      output = "{0}, not exact with difference {1}".format(cube - 1 ,n-(cube-1)**3)

  return output


print( cubic_root(99)   )
print( cubic_root(2000) )
print( cubic_root(1000) )

# import numpy as np
# import math  

# def cubic_root(n):
#   cube = np.cbrt(n)
#   limit =  math.floor(cube)

#   if limit != cube:
#     output = "{0}, not exact with difference {1}".format(limit,n-pow(limit,3))
#   else:
#     output = "{0}, exact!".format(limit)
    

#   return output