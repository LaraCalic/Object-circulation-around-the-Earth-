from vpython import *

G=6.67e-11 
M_earth=5.972e24  
R_earth=6.371e6 
h=400e3 

r=R_earth+h
omega=sqrt(G*M_earth/r**3)
T=2*pi/omega
print("Orbital Period = ",T," seconds = ", T/60," minutes")


tgraph=graph(title='T = f(r)', xtitle="Orbital Radius [m]", ytitle="Orbital Period [h]", width=550, height=550)
f1=gcurve(color=color.red)


dr=100e3

while r<10*R_earth:
  omega=sqrt(G*M_earth/r**3)
  T=2*pi/omega
  f1.plot(r,T/3600)
  r=r+dr