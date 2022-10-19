#%% -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:09:08 2022

@author: galac
"""
#%%###################
"""
packages
"""
#
# Basic 
import numpy as np
#
# Plotting
import matplotlib.pyplot as plt
#
# Animation
from matplotlib import animation
#
# Gui
"""
Variables
"""
#
#
AU          = 1.495e8              # earth sun distance (converts units to Km)
AU_meter    = 1.495e11             # earth sun distance (converts units to m)
daysec      = 24.0*60*60           # seconds of a day
#
#
# Mass (kg)##############################
G           = 6.672e-11   # Gravitatoinal constant, "Big G"
Mb          = 4.0e30      # black hole
Ms          = 1.9891e30   # Mass of Sun
Mmer        = 0.3301e24   # Mass of Mercury
Mv          = 4.8673e24   # Mass of Venus
Me          = 5.9722e24   # Mass of Earth        
Mm          = 0.64169e24  # Mass of Mars
Mj          = 1898.13e24  # Mass of Jupiter
Msat        = 568.32e24   # Mass of Saturn
Mu          = 86.811e24   # Mass of Uranas
Mn          = 102.409e24  # Mass on Neptune
Mp          = 0.01303e24  # Mass of Pluto

Mc          = 6.39e20     # unknown comet  
#########################################
#
# Eccentricity###########################
e_me = 0.20563069
e_v  = 0.00677323
e_e  = 0.01671022
e_m  = 0.09341233
e_j  = 0.04839266
e_s  = 0.05415060
e_u  = 0.04716771
e_n  = 0.00858587
e_p  = 0.24880766
#########################################
#
# Semi-Major Axis (10**6 km or 10**9 m) ##################
a_me = 57.909*10**6   # Mercury semi-major axis in km
a_v  = 108.210*10**6  # Venus semi-major axis in km
a_e  = 149.598*10**6  # Eartrh semi-major axis in km
a_m  = 227.956*10**6  # Mars semi-major axis in km
a_j  = 778.479*10**6  # Jupite semi-major axis in km
a_s  = 1432.041*10**6 # Saturn semi-major axis in km
a_u  = 2867.043*10**6 # Uranus semi-major axis in km
a_n  = 4514.953*10**6 # Neptune semi-major axis in km
a_p  = 5869.656*10**6 # Pluto semi-major axis in km
#########################################
#
# Radius at Aphelion(10**6 km or 10**9 m) ################
r_a_me = 69.818*10**6    # Mercury radius at aphelion in km
r_a_v  = 108.941*10**6   # Venus radius at aphelion in km
r_a_e  = 152.100*10**6   # Earth radius at aphelion in km
r_a_m  = 249.261*10**6   # Mars radius at aphelion in km
r_a_j  = 816.363*10**6   # Jupiter radius at aphelion in km
r_a_s  = 1506.527*10**6  # Saturn radius at aphelion in km
r_a_u  = 3001.390*10**6  # Uranus radius at aphelion in km
r_a_n  = 4558.857*10**6  # Neptune radius at aphelion in km
r_a_p  = 7304.326*10**6  # Pluto radius at aphelion in km
#######################################
#
# Velocities at Aphelion (m/s) ##################
mer_ap_v = 38857.8268475       # Mercury velocity at aphelion
v_ap_v   = 34784.739777796     # Venus velocity at aphelion
e_ap_v   = 29290.666788604     # Earth velocity at aphelion
m_ap_v   = 21969.61279616      # Mars velocity at aphelion
j_ap_v   = 12436.025618165     # Jupiter velocity at aphelion
sat_ap_v = 9138.3725336002     # Saturn velocity at aphelion
u_ap_v   = 6491.9276204985     # Uranus velocity at aphelion
n_ap_v   = 5369.1611683257     # Neptune velocity at aphelion
p_ap_v   = 3705.1522236097     # Pluto velocity at aphelion
#################################################


commet_v    = 7000

gravconst_mer = G*Mmer*Ms
gravconst_v   = G*Mv*Ms
gravconst_e = G*Me*Ms
gravconst_m = G*Mm*Ms
gravconst_c = G*Mc*Ms
gravconst_j   = G*Mj*Ms
gravconst_sat = G*Msat*Ms
gravconst_u   = G*Mu*Ms
gravconst_n   = G*Mn*Ms
gravconst_p   = G*Mp*Ms



#%%###################
"""
Settings
"""
#
# setup the starting conditions
#
# Mercury
xmer,ymer,zmer     = 0.4668426*AU,0,0
xvmer,yvmer,zvmer  = 0,mer_ap_v,0
#
# Venus
xv,yv,zv           = 0.7282314594*AU,0,0
xvv,yvv,zvv        = 0,v_ap_v,0
#
# Earth
xe,ye,ze           = 1.0167*AU,0,0
xve,yve,zve        = 0,e_ap_v,0
#
# Mars
xm,ym,zm           = 1.666*AU,0,0
xvm,yvm,zvm        = 0,m_ap_v,0
#
# Jupiter
xj,yj,zj           = 5.46062*AU,0,0
xvj,yvj,zvj        = 0,j_ap_v,0
#
# Saturn
xsat,ysat,zsat     = 10.0771*AU,0,0
xvsat,yvsat,zvsat  = 0,sat_ap_v,0
#
# Uranas
xu,yu,zu           = 20.0762*AU,0,0
xvu,yvu,zvu        = 0,u_ap_v,0
#
# Neptune
xn,yn,zn           = 30.494*AU,0,0
xvn,yvn,zvn        = 0,n_ap_v,0
#
# Pluto
xp,yp,zp           = 48.8584*AU,0,0
xvp,yvp,zvp        = 0,p_ap_v,0
#
# comet
xc,yc,zc    = 2*AU,0,0
xvc,yvc,zvc = 0,commet_v,3000
#
# sun
xs,ys,zs    = 0,0,0
xvs,yvs,zvs = 0,0,0

t           = 0.0
dt          = 1*daysec # every frame move this time

#
# Define Position Matrix
xslist,yslist,zslist       = [],[],[] #Sun
xmerlist,ymerlist,zmerlist = [],[],[] #Mercury
xvlist,yvlist,zvlist       = [],[],[] #Venus
xelist,yelist,zelist       = [],[],[] #Earth
xmlist,ymlist,zmlist       = [],[],[] #Mars
xjlist,yjlist,zjlist       = [],[],[] #Jupiter 
xsatlist,ysatlist,zsatlist = [],[],[] #Saturn
xulist,yulist,zulist       = [],[],[] #Uranus
xnlist,ynlist,znlist       = [],[],[] #Neptune
xplist,yplist,zplist       = [],[],[] #Pluto


xclist,yclist,zclist = [],[],[]  # Comet

#%%##################
"""
Main
"""
# start simulation
while t<5*365*daysec:
    
    ################ Mercury #############
    # compute G force on Mercury
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rx_me,ry_me,rz_me = xmer - xs, ymer - ys, zmer - zs
    modr3_me = (rx_me**2+ry_me**2+rz_me**2)**1.5
    fx_me = -gravconst_mer*rx_me/modr3_me
    fy_me = -gravconst_mer*ry_me/modr3_me
    fz_me = -gravconst_mer*rz_me/modr3_me
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvmer += fx_me*dt/Mmer
    yvmer += fy_me*dt/Mmer
    zvmer += fz_me*dt/Mmer
    
    # update position
    xmer += xvmer*dt
    ymer += yvmer*dt 
    zmer += zvmer*dt
    
    # save the position in list
    xmerlist.append(xmer)
    ymerlist.append(ymer)
    zmerlist.append(zmer)
    
    ################ Venus #############
    # compute G force on Venus
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rxv,ryv,rzv = xv - xs, yv - ys, zv - zs
    modr3_v = (rxv**2+ryv**2+rzv**2)**1.5
    fx_v = -gravconst_v*rxv/modr3_v
    fy_v = -gravconst_v*ryv/modr3_v
    fz_v = -gravconst_v*rzv/modr3_v
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvv += fx_v*dt/Mv
    yvv += fy_v*dt/Mv
    zvv += fz_v*dt/Mv
    
    # update position
    xv += xvv*dt
    yv += yvv*dt 
    zv += zvv*dt
    
    # save the position in list
    xvlist.append(xv)
    yvlist.append(yv)
    zvlist.append(zv)
    
    ################ earth #############
    # compute G force on earth
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rx,ry,rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx**2+ry**2+rz**2)**1.5
    fx_e = -gravconst_e*rx/modr3_e
    fy_e = -gravconst_e*ry/modr3_e
    fz_e = -gravconst_e*rz/modr3_e
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xve += fx_e*dt/Me
    yve += fy_e*dt/Me
    zve += fz_e*dt/Me
    
    # update position
    xe += xve*dt
    ye += yve*dt 
    ze += zve*dt
    
    # save the position in list
    xelist.append(xe)
    yelist.append(ye)
    zelist.append(ze)
    
    ################ Mars ##############
    # compute G force on mars
    rx_m,ry_m,rz_m = xm - xs, ym - ys, zm - zs
    modr3_m = (rx_m**2+ry_m**2+rz_m**2)**1.5
    fx_m = -gravconst_m*rx_m/modr3_m
    fy_m = -gravconst_m*ry_m/modr3_m
    fz_m = -gravconst_m*rz_m/modr3_m
    
    xvm += fx_m*dt/Mm
    yvm += fy_m*dt/Mm
    zvm += fz_m*dt/Mm
    
    # update position
    xm += xvm*dt
    ym += yvm*dt
    zm += zvm*dt
    
    # add to list
    xmlist.append(xm)
    ymlist.append(ym)
    zmlist.append(zm)
    
    ################ Jupiter #############
    # compute G force on Jupiter
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rxj,ryj,rzj = xj - xs, yj - ys, zj - zs
    modr3_j = (rxj**2+ryj**2+rzj**2)**1.5
    fx_j = -gravconst_j*rxj/modr3_j
    fy_j = -gravconst_j*ryj/modr3_j
    fz_j = -gravconst_j*rzj/modr3_j
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvj += fx_j*dt/Mj
    yvj += fy_j*dt/Mj
    zvj += fz_j*dt/Mj
    
    # update position
    xj += xvj*dt
    yj += yvj*dt 
    zj += zvj*dt
    
    # save the position in list
    xjlist.append(xj)
    yjlist.append(yj)
    zjlist.append(zj)
    
    ################ Saturn #############
    # compute G force on Saturn
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rx_sa,ry_sa,rz_sa = xsat - xs, ysat - ys, zsat - zs
    modr3_sa = (rx_sa**2+ry_sa**2+rz_sa**2)**1.5
    fx_sa = -gravconst_sat*rx_sa/modr3_sa
    fy_sa = -gravconst_sat*ry_sa/modr3_sa
    fz_sa = -gravconst_sat*rz_sa/modr3_sa
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvsat += fx_sa*dt/Msat
    yvsat += fy_sa*dt/Msat
    zvsat += fz_sa*dt/Msat
    
    # update position
    xsat += xvsat*dt
    ysat += yvsat*dt 
    zsat += zvsat*dt
    
    # save the position in list
    xsatlist.append(xsat)
    ysatlist.append(ysat)
    zsatlist.append(zsat)
    
    ################ Uranus #############
    # compute G force on Uranus
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rxu,ryu,rzu = xu - xs, yu - ys, zu - zs
    modr3_u = (rxu**2+ryu**2+rzu**2)**1.5
    fx_u = -gravconst_u*rxu/modr3_u
    fy_u = -gravconst_u*ryu/modr3_u
    fz_u = -gravconst_u*rzu/modr3_u
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvu += fx_u*dt/Mu
    yvu += fy_u*dt/Mu
    zvu += fz_u*dt/Mu
    
    # update position
    xu += xvu*dt
    yu += yvu*dt 
    zu += zvu*dt
    
    # save the position in list
    xulist.append(xu)
    yulist.append(yu)
    zulist.append(zu)
    
    ################ Neptune #############
    # compute G force on Neptune
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rxn,ryn,rzn = xn - xs, yn - ys, zn - zs
    modr3_n = (rxn**2+ryn**2+rzn**2)**1.5
    fx_n = -gravconst_n*rxn/modr3_n
    fy_n = -gravconst_n*ryn/modr3_n
    fz_n = -gravconst_n*rzn/modr3_n
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvn += fx_n*dt/Mn
    yvn += fy_n*dt/Mn
    zvn += fz_n*dt/Mn
    
    # update position
    xn += xvn*dt
    yn += yvn*dt 
    zn += zvn*dt
    
    # save the position in list
    xnlist.append(xn)
    ynlist.append(yn)
    znlist.append(zn)
    
    ################ Pluto?? #############
    # compute G force on Pluto
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rxp,ryp,rzp = xp - xs, yp - ys, zp - zs
    modr3_p = (rxp**2+ryp**2+rzp**2)**1.5
    fx_p = -gravconst_p*rxp/modr3_p
    fy_p = -gravconst_p*ryp/modr3_p
    fz_p = -gravconst_p*rzp/modr3_p
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvp += fx_p*dt/Mp
    yvp += fy_p*dt/Mp
    zvp += fz_p*dt/Mp
    
    # update position
    xp += xvp*dt
    yp += yvp*dt 
    zp += zvp*dt
    
    # save the position in list
    xplist.append(xp)
    yplist.append(yp)
    zplist.append(zp)
    
 
    
    ################ comet/satallite? ##############
    # compute G force on comet
    rx_c,ry_c,rz_c = xc - xs, yc - ys, zc - zs
    modr3_c = (rx_c**2+ry_c**2+rz_c**2)**1.5
    fx_c = -gravconst_c*rx_c/modr3_c
    fy_c = -gravconst_c*ry_c/modr3_c
    fz_c = -gravconst_c*rz_c/modr3_c
    
    xvc += fx_c*dt/Mc
    yvc += fy_c*dt/Mc
    zvc += fz_c*dt/Mc
    
    # update position
    xc += xvc*dt
    yc += yvc*dt 
    zc += zvc*dt
    
    # add to list
    xclist.append(xc)
    yclist.append(yc)
    zclist.append(zc)

    ################ the sun ###########
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvs += -(fx_e+fx_m)*dt/Ms
    yvs += -(fy_e+fy_m)*dt/Ms
    zvs += -(fz_e+fz_m)*dt/Ms
    
    # update position
    xs += xvs*dt
    ys += yvs*dt 
    zs += zvs*dt
    xslist.append(xs)
    yslist.append(ys)
    zslist.append(zs)
    
    # update dt
    t +=dt

print('data ready')
#print(xalist,yalist)

#%%
'''
Plot
'''

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.axis('auto')

axis_size = 5.5
ax.set_xlim(-axis_size*AU,axis_size*AU)
ax.set_ylim(-axis_size*AU,axis_size*AU)
ax.set_zlim(-axis_size*AU,axis_size*AU)

# ax.set_aspect('auto')
# ax.grid()

###############
## data sets ##
###############
#
datadict = {}
dataset_s  = [xslist,yslist,zslist]        #Sun
dataset_me = [xmerlist,ymerlist,zmerlist]  #Mercury
dataset_v  = [xvlist,yvlist,zvlist]        #Venus
dataset_e  = [xelist,yelist,zelist]        #Earth
dataset_m  = [xmlist,ymlist,zmlist]        #Mars
dataset_j  = [xjlist,yjlist,zjlist]        #Jupiter 
dataset_sa = [xsatlist,ysatlist,zsatlist]  #Saturn
dataset_u  = [xulist,yulist,zulist]        #Uranus
dataset_n  = [xnlist,ynlist,znlist]        #Neptune
dataset_p  = [xplist,yplist,zplist]        #Pluto
dataset_c  = [xclist,yclist,zclist]        #comet
datadict['s']  = dataset_s
datadict['me'] = dataset_me
datadict['v']  = dataset_v 
datadict['e']  = dataset_e
datadict['m']  = dataset_m
datadict['j']  = dataset_j
datadict['sa'] = dataset_sa 
datadict['u']  = dataset_u
datadict['n']  = dataset_n
datadict['p']  = dataset_p


datadict['c']  = dataset_c


##########################
## Plot visual settings ##
##########################
#
vis_dict = {}
# sun
line_s,     = ax.plot([0],[0],[0],'-g',lw=1)
point_s,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s      = ax.text(AU,0,0,'Sun')
vis_dict['s'] = [line_s,point_s,text_s]
#
# Mercury
line_me,     = ax.plot([0],[0],[0],'-g',lw=1)
point_me,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="grey", markerfacecolor="grey")
text_me      = ax.text(AU,0,0,'Mercury')
vis_dict['me'] = [line_me,point_me,text_me]
#
# Venus
line_v,     = ax.plot([0],[0],[0],'-g',lw=1)
point_v,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="green", markerfacecolor="green")
text_v      = ax.text(AU,0,0,'Venus')
vis_dict['v'] = [line_v,point_v,text_v]
#
# Earth
line_e,     = ax.plot([0],[0],[0],'-g',lw=1)
point_e,    = ax.plot([AU],[0],[0], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_e      = ax.text(AU,0,0,'Earth')
vis_dict['e'] = [line_e,point_e,text_e]
#
# Mars 
line_m,     = ax.plot([0],[0],[0],'-g',lw=1)
point_m,    = ax.plot([AU],[0],[0], marker="o", markersize=4, markeredgecolor="red", markerfacecolor="red")
text_m      = ax.text(AU,0,0,'Mars')
vis_dict['m'] = [line_m,point_m,text_m]
#
# Jupiter
line_j,     = ax.plot([0],[0],[0],'-g',lw=1)
point_j,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="orange", markerfacecolor="orange")
text_j      = ax.text(AU,0,0,'Jupiter')
vis_dict['j'] = [line_j,point_j,text_j]
#
# Saturn
line_sa,     = ax.plot([0],[0],[0],'-g',lw=1)
point_sa,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="indigo", markerfacecolor="indigo")
text_sa      = ax.text(AU,0,0,'Saturn')
vis_dict['sa'] = [line_sa,point_sa,text_sa]
#
# Uranus
line_u,     = ax.plot([0],[0],[0],'-g',lw=1)
point_u,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="cyan", markerfacecolor="cyan")
text_u      = ax.text(AU,0,0,'Uranus')
vis_dict['u'] = [line_u,point_u,text_u]
#
# Neptune
line_n,     = ax.plot([0],[0],[0],'-g',lw=1)
point_n,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="blue", markerfacecolor="blue")
text_n      = ax.text(AU,0,0,'Neptune')
vis_dict['n'] = [line_n,point_n,text_n]
#
# Pluto
line_p,     = ax.plot([0],[0],[0],'-g',lw=1)
point_p,    = ax.plot([AU],[0],[0], marker="o", markersize=7, markeredgecolor="magenta", markerfacecolor="magenta")
text_p      = ax.text(AU,0,0,'Pluto')
vis_dict['p'] = [line_p,point_p,text_p]
#
# comet
line_c,     = ax.plot([0],[0],[0],'-g',lw=1)
point_c,    = ax.plot([AU],[0],[0], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
text_c      = ax.text(AU,0,0,'comet')
vis_dict['c'] = [line_c,point_c,text_c]



def update(num,data_dict,vis_dict):
    # Sun 
    dataset_s               = data_dict['s']
    line_s,point_s,text_s   = vis_dict['s'][0],vis_dict['s'][1],vis_dict['s'][2]
    line_s.set_data_3d(dataset_s[0][:num],dataset_s[1][:num],dataset_s[2][:num])
    point_s.set_data_3d(dataset_s[0][num],dataset_s[1][num],dataset_s[2][num])
    text_s.set_position((dataset_s[0][num],dataset_s[1][num],dataset_s[2][num]))
    #
    # Mercury 
    dataset_me                 = data_dict['me']
    line_me,point_me,text_me   = vis_dict['me'][0],vis_dict['me'][1],vis_dict['me'][2]
    line_me.set_data_3d(dataset_me[0][:num],dataset_me[1][:num],dataset_me[2][:num])
    point_me.set_data_3d(dataset_me[0][num],dataset_me[1][num],dataset_me[2][num])
    text_me.set_position((dataset_me[0][num],dataset_me[1][num],dataset_me[2][num]))
    #
    # Venus 
    dataset_v               = data_dict['v']
    line_v,point_v,text_v   = vis_dict['v'][0],vis_dict['v'][1],vis_dict['v'][2]
    line_v.set_data_3d(dataset_v[0][:num],dataset_v[1][:num],dataset_v[2][:num])
    point_v.set_data_3d(dataset_v[0][num],dataset_v[1][num],dataset_v[2][num])
    text_v.set_position((dataset_v[0][num],dataset_v[1][num],dataset_v[2][num]))
    #
    # Earth 
    dataset_e               = data_dict['e']
    line_e,point_e,text_e   = vis_dict['e'][0],vis_dict['e'][1],vis_dict['e'][2]
    line_e.set_data_3d(dataset_e[0][:num],dataset_e[1][:num],dataset_e[2][:num])
    point_e.set_data_3d(dataset_e[0][num],dataset_e[1][num],dataset_e[2][num])
    text_e.set_position((dataset_e[0][num],dataset_e[1][num],dataset_e[2][num]))
    #
    # Mars
    dataset_m               = data_dict['m']
    line_m,point_m,text_m   = vis_dict['m'][0],vis_dict['m'][1],vis_dict['m'][2]
    line_m.set_data_3d(dataset_m[0][:num],dataset_m[1][:num],dataset_m[2][:num])
    point_m.set_data_3d(dataset_m[0][num],dataset_m[1][num],dataset_m[2][num])
    text_m.set_position((dataset_m[0][num],dataset_m[1][num],dataset_m[2][num]))
    #
    # Jupiter 
    dataset_j               = data_dict['j']
    line_j,point_j,text_j   = vis_dict['j'][0],vis_dict['j'][1],vis_dict['j'][2]
    line_j.set_data_3d(dataset_j[0][:num],dataset_j[1][:num],dataset_j[2][:num])
    point_j.set_data_3d(dataset_j[0][num],dataset_j[1][num],dataset_j[2][num])
    text_j.set_position((dataset_j[0][num],dataset_j[1][num],dataset_j[2][num]))
    #
    # Saturn
    dataset_sa               = data_dict['sa']
    line_sa,point_sa,text_sa   = vis_dict['sa'][0],vis_dict['sa'][1],vis_dict['sa'][2]
    line_sa.set_data_3d(dataset_sa[0][:num],dataset_sa[1][:num],dataset_sa[2][:num])
    point_sa.set_data_3d(dataset_sa[0][num],dataset_sa[1][num],dataset_sa[2][num])
    text_sa.set_position((dataset_sa[0][num],dataset_sa[1][num],dataset_sa[2][num]))
    #
    # Uranus
    dataset_u               = data_dict['u']
    line_u,point_u,text_u   = vis_dict['u'][0],vis_dict['u'][1],vis_dict['u'][2]
    line_u.set_data_3d(dataset_u[0][:num],dataset_u[1][:num],dataset_u[2][:num])
    point_u.set_data_3d(dataset_u[0][num],dataset_u[1][num],dataset_u[2][num])
    text_u.set_position((dataset_u[0][num],dataset_u[1][num],dataset_u[2][num]))
    #
    # Neptune
    dataset_n               = data_dict['n']
    line_n,point_n,text_n   = vis_dict['n'][0],vis_dict['n'][1],vis_dict['n'][2]
    line_n.set_data_3d(dataset_n[0][:num],dataset_n[1][:num],dataset_n[2][:num])
    point_n.set_data_3d(dataset_n[0][num],dataset_n[1][num],dataset_n[2][num])
    text_n.set_position((dataset_n[0][num],dataset_n[1][num],dataset_n[2][num]))
    #
    # Pluto
    dataset_p               = data_dict['p']
    line_p,point_p,text_p   = vis_dict['p'][0],vis_dict['p'][1],vis_dict['p'][2]
    line_p.set_data_3d(dataset_p[0][:num],dataset_p[1][:num],dataset_p[2][:num])
    point_p.set_data_3d(dataset_p[0][num],dataset_p[1][num],dataset_p[2][num])
    text_p.set_position((dataset_p[0][num],dataset_p[1][num],dataset_p[2][num]))
    #
    #
    #
    # comet
    dataset_c               = data_dict['c']
    line_c,point_c,text_c   = vis_dict['c'][0],vis_dict['c'][1],vis_dict['c'][2]
    line_c.set_data_3d(dataset_c[0][:num],dataset_c[1][:num],dataset_c[2][:num])
    point_c.set_data_3d(dataset_c[0][num],dataset_c[1][num],dataset_c[2][num])
    text_c.set_position((dataset_c[0][num],dataset_c[1][num],dataset_c[2][num]))

ani = animation.FuncAnimation(
    fig
    ,update
    ,len(xelist)
    ,fargs=(datadict, vis_dict)
    ,interval=1
)

plt.show()



