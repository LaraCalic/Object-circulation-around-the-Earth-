#GlowScript 2.9 VPython
from vpython import *

# defining the set of constants in SI
# R_earth - radius of Earth [m], M_earth - mass of Earth [kg], gravitational constant [kg/m**3] 

R_earth=6.37e6
M_earth=5.972e24
G=6.67e-11

Earth=sphere(pos=vector(0,0,0), radius=R_earth, texture=textures.earth)

object=sphere(pos=vector(1.5*R_earth,0,0), radius=0.02*R_earth, make_trail=True)

# initial conditions: at initial position, at t=0,  initial velocity is v_0 = 4500 in x,y and z direction :(v0x, v0y, v0z)

t=0
dt=10
v0=4500
object.m=100
object.p=object.m*vector(v0,v0,0)
Earth.m=M_earth

while t<7000:
  rate(100)
  r=object.pos-Earth.pos
  F=-G*Earth.m*object.m*norm(r)/mag(r)**2
  object.p=object.p+F*dt
  object.pos=object.pos+object.p*dt/object.m
  t=t+dt
