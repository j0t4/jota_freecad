import WebGui
from StartPage import StartPage
WebGui.openBrowserHTML(StartPage.handle(),'file://' + App.getResourceDir() + 'Mod/Start/StartPage/','Start page')
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
from FreeCAD import Vector
from pyooml import *
a1 = -60
a2 = 70
L1 = 40
L2 = 40
v1 = Vector(L1, 0, 0)
v2 = Vector(L2, 0, 0)
f0 = frame()
f1 = frame()
f2 = frame()
sv1 = svector(v1).color("yellow")
sv2 = svector(v2).color("yellow")
import HMatrix
Ma = HMatrix.Roty(a1)
Mb = HMatrix.Translation(v1)
Mc = HMatrix.Roty(a2)
Md = HMatrix.Translation(v2)
sv1.T = Ma
f1.T = Ma * Mb
sv2.T = Ma * Mb * Mc
f2.T = Ma * Mb * Mc * Md
vr = f2.T.multiply(Vector(0,0,0))
svr = svector(vr).color("orange")
l1 = link(l = L1, D = 10, w = 5).ice(80)
l2 = link(l = L2, D = 10, w = 3).ice(80)
l2.T = Ma * Mb * Mc
l1.T = Ma
base = sphere(r = 14, angle1 = 0).translate(0, 0, -6).ice(80)
