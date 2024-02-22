from cmath import asin, sin, sqrt


print("hello world")


print(3**1001)

#calcola la distanza tra oslo e vancouver
from math import asin
from math import cos
from math import sqrt
from math import sin
from math import radians




ϕ1,λ1 = radians (59.9) , radians (10.8)
ϕ2,λ2 = radians (49.3) , radians (-123.1)

r=6371
d= 2 *r *asin( sqrt(sin( 1/2*(ϕ2-ϕ1))**2+ cos(ϕ1) *cos(ϕ2)*sin( 1/2*(λ2-λ1))**2)) 
print(d)


