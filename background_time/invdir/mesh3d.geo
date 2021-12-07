//3D half space problem mesh for ResIPy - no topography
Mesh.Binary = 0;//specify we want ASCII format
cl=6.03;//define characteristic length for fine mesh region
//Fine mesh region.
Point (1) = {672232.51,5127453.29,0.00, cl*1.2};
Point (2) = {672232.51,5127415.37,0.00, cl*1.2};
Point (3) = {672194.91,5127415.37,0.00, cl*1.2};
Point (4) = {672194.91,5127453.29,0.00, cl*1.2};
Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,1};
cl2=cl*2.00;//define characteristic length for base of fine mesh region
Point (5) = {672232.51,5127453.29,-29.12, cl2};
Point (6) = {672232.51,5127415.37,-29.12, cl2};
Point (7) = {672194.91,5127415.37,-29.12, cl2};
Point (8) = {672194.91,5127453.29,-29.12, cl2};
Line(5) = {5,6};
Line(6) = {6,7};
Line(7) = {7,8};
Line(8) = {8,5};
Line(9) = {1,5};
Line(10) = {2,6};
Line(11) = {3,7};
Line(12) = {4,8};
//End fine mesh region points
//Neumannn boundary points
cln = 602.51;//characteristic length for background region
Point (9) = {672416.00,5127636.79,0.00, cln};
Point (10) = {672416.00,5127231.88,0.00, cln};
Point (11) = {672011.42,5127231.88,0.00, cln};
Point (12) = {672011.42,5127636.79,0.00, cln};
Line(13) = {9,10};
Line(14) = {10,11};
Line(15) = {11,12};
Line(16) = {12,9};
Point (13) = {672416.00,5127636.79,-116.47, cln};
Point (14) = {672416.00,5127231.88,-116.47, cln};
Point (15) = {672011.42,5127231.88,-116.47, cln};
Point (16) = {672011.42,5127636.79,-116.47, cln};
Line(17) = {13,14};
Line(18) = {14,15};
Line(19) = {15,16};
Line(20) = {16,13};
Line(21) = {9,13};
Line(22) = {10,14};
Line(23) = {11,15};
Line(24) = {12,16};
//End of nuemmon boundary points
Line Loop(1) = {1,2,3,4};
Line Loop(2) = {13,14,15,16};
Plane Surface(1) = {1};
Plane Surface(2) = {2,1};
//Below ground fine mesh surfaces
Line Loop(3) = {5,6,7,8};
Line Loop(4) = {5,-10,-1,9};
Line Loop(5) = {11,-6,-10,2};
Line Loop(6) = {11,7,-12,-3};
Line Loop(7) = {8,-9,-4,12};
Plane Surface(3) = {3};
Plane Surface(4) = {4};
Plane Surface(5) = {5};
Plane Surface(6) = {6};
Plane Surface(7) = {7};
Surface Loop (1) = {1,3,4,5,6,7};
Volume(1) = {1};//End Fine mesh region surfaces.
//Below ground background surfaces
Line Loop(8) = {20, 17, 18, 19};
Line Loop(9) = {24, -19, -23, 15};
Line Loop(10) = {16, 21, -20, -24};
Line Loop(11) = {17, -22, -13, 21};
Line Loop(12) = {18, -23, -14, 22};
Plane Surface(8) = {8};
Plane Surface(9) = {9};
Plane Surface(10) = {10};
Plane Surface(11) = {11};
Plane Surface(12) = {12};
Surface Loop (2) = {2,3,4,5,6,7,8,9,10,11,12};
Volume(2) = {2};//End background mesh surfaces
//Electrode positions.
Point (17) = {672200.29,5127430.68,-23.00, cl};
Point{17} In Volume{1};//buried electrode
Point (18) = {672200.29,5127430.68,-22.00, cl};
Point{18} In Volume{1};//buried electrode
Point (19) = {672200.29,5127430.68,-21.00, cl};
Point{19} In Volume{1};//buried electrode
Point (20) = {672200.29,5127430.68,-20.00, cl};
Point{20} In Volume{1};//buried electrode
Point (21) = {672200.29,5127430.68,-19.00, cl};
Point{21} In Volume{1};//buried electrode
Point (22) = {672200.29,5127430.68,-18.00, cl};
Point{22} In Volume{1};//buried electrode
Point (23) = {672200.29,5127430.68,-17.00, cl};
Point{23} In Volume{1};//buried electrode
Point (24) = {672200.29,5127430.68,-16.00, cl};
Point{24} In Volume{1};//buried electrode
Point (25) = {672200.29,5127430.68,-15.00, cl};
Point{25} In Volume{1};//buried electrode
Point (26) = {672200.29,5127430.68,-14.00, cl};
Point{26} In Volume{1};//buried electrode
Point (27) = {672200.29,5127430.68,-13.00, cl};
Point{27} In Volume{1};//buried electrode
Point (28) = {672200.29,5127430.68,-12.00, cl};
Point{28} In Volume{1};//buried electrode
Point (29) = {672200.29,5127430.68,-11.00, cl};
Point{29} In Volume{1};//buried electrode
Point (30) = {672200.29,5127430.68,-10.00, cl};
Point{30} In Volume{1};//buried electrode
Point (31) = {672200.29,5127430.68,-9.00, cl};
Point{31} In Volume{1};//buried electrode
Point (32) = {672200.29,5127430.68,-8.00, cl};
Point{32} In Volume{1};//buried electrode
Point (33) = {672200.29,5127430.68,-7.00, cl};
Point{33} In Volume{1};//buried electrode
Point (34) = {672200.29,5127430.68,-6.00, cl};
Point{34} In Volume{1};//buried electrode
Point (35) = {672200.29,5127430.68,-5.00, cl};
Point{35} In Volume{1};//buried electrode
Point (36) = {672200.29,5127430.68,-4.00, cl};
Point{36} In Volume{1};//buried electrode
Point (37) = {672200.29,5127430.68,-3.00, cl};
Point{37} In Volume{1};//buried electrode
Point (38) = {672200.29,5127430.68,-2.00, cl};
Point{38} In Volume{1};//buried electrode
Point (39) = {672200.29,5127430.68,-1.00, cl};
Point{39} In Volume{1};//buried electrode
Point (40) = {672200.29,5127430.68,0.00, cl};
Point{40} In Surface{1};//surface electrode
Point (41) = {672209.76,5127447.88,0.00, cl};
Point{41} In Surface{1};//surface electrode
Point (42) = {672209.76,5127447.88,-1.00, cl};
Point{42} In Volume{1};//buried electrode
Point (43) = {672209.76,5127447.88,-2.00, cl};
Point{43} In Volume{1};//buried electrode
Point (44) = {672209.76,5127447.88,-3.00, cl};
Point{44} In Volume{1};//buried electrode
Point (45) = {672209.76,5127447.88,-4.00, cl};
Point{45} In Volume{1};//buried electrode
Point (46) = {672209.76,5127447.88,-5.00, cl};
Point{46} In Volume{1};//buried electrode
Point (47) = {672209.76,5127447.88,-6.00, cl};
Point{47} In Volume{1};//buried electrode
Point (48) = {672209.76,5127447.88,-7.00, cl};
Point{48} In Volume{1};//buried electrode
Point (49) = {672209.76,5127447.88,-8.00, cl};
Point{49} In Volume{1};//buried electrode
Point (50) = {672209.76,5127447.88,-9.00, cl};
Point{50} In Volume{1};//buried electrode
Point (51) = {672209.76,5127447.88,-10.00, cl};
Point{51} In Volume{1};//buried electrode
Point (52) = {672209.76,5127447.88,-11.00, cl};
Point{52} In Volume{1};//buried electrode
Point (53) = {672209.76,5127447.88,-12.00, cl};
Point{53} In Volume{1};//buried electrode
Point (54) = {672209.76,5127447.88,-13.00, cl};
Point{54} In Volume{1};//buried electrode
Point (55) = {672209.76,5127447.88,-14.00, cl};
Point{55} In Volume{1};//buried electrode
Point (56) = {672209.76,5127447.88,-15.00, cl};
Point{56} In Volume{1};//buried electrode
Point (57) = {672209.76,5127447.88,-16.00, cl};
Point{57} In Volume{1};//buried electrode
Point (58) = {672209.76,5127447.88,-17.00, cl};
Point{58} In Volume{1};//buried electrode
Point (59) = {672209.76,5127447.88,-18.00, cl};
Point{59} In Volume{1};//buried electrode
Point (60) = {672209.76,5127447.88,-19.00, cl};
Point{60} In Volume{1};//buried electrode
Point (61) = {672209.76,5127447.88,-20.00, cl};
Point{61} In Volume{1};//buried electrode
Point (62) = {672209.76,5127447.88,-21.00, cl};
Point{62} In Volume{1};//buried electrode
Point (63) = {672209.76,5127447.88,-22.00, cl};
Point{63} In Volume{1};//buried electrode
Point (64) = {672209.76,5127447.88,-23.00, cl};
Point{64} In Volume{1};//buried electrode
Point (65) = {672211.27,5127435.64,0.00, cl};
Point{65} In Surface{1};//surface electrode
Point (66) = {672211.27,5127435.64,-1.00, cl};
Point{66} In Volume{1};//buried electrode
Point (67) = {672211.27,5127435.64,-2.00, cl};
Point{67} In Volume{1};//buried electrode
Point (68) = {672211.27,5127435.64,-3.00, cl};
Point{68} In Volume{1};//buried electrode
Point (69) = {672211.27,5127435.64,-4.00, cl};
Point{69} In Volume{1};//buried electrode
Point (70) = {672211.27,5127435.64,-5.00, cl};
Point{70} In Volume{1};//buried electrode
Point (71) = {672211.27,5127435.64,-6.00, cl};
Point{71} In Volume{1};//buried electrode
Point (72) = {672211.27,5127435.64,-7.00, cl};
Point{72} In Volume{1};//buried electrode
Point (73) = {672211.27,5127435.64,-8.00, cl};
Point{73} In Volume{1};//buried electrode
Point (74) = {672211.27,5127435.64,-9.00, cl};
Point{74} In Volume{1};//buried electrode
Point (75) = {672211.27,5127435.64,-10.00, cl};
Point{75} In Volume{1};//buried electrode
Point (76) = {672211.27,5127435.64,-11.00, cl};
Point{76} In Volume{1};//buried electrode
Point (77) = {672211.27,5127435.64,-12.00, cl};
Point{77} In Volume{1};//buried electrode
Point (78) = {672211.27,5127435.64,-13.00, cl};
Point{78} In Volume{1};//buried electrode
Point (79) = {672211.27,5127435.64,-14.00, cl};
Point{79} In Volume{1};//buried electrode
Point (80) = {672211.27,5127435.64,-15.00, cl};
Point{80} In Volume{1};//buried electrode
Point (81) = {672211.27,5127435.64,-16.00, cl};
Point{81} In Volume{1};//buried electrode
Point (82) = {672211.27,5127435.64,-17.00, cl};
Point{82} In Volume{1};//buried electrode
Point (83) = {672211.27,5127435.64,-18.00, cl};
Point{83} In Volume{1};//buried electrode
Point (84) = {672211.27,5127435.64,-19.00, cl};
Point{84} In Volume{1};//buried electrode
Point (85) = {672211.27,5127435.64,-20.00, cl};
Point{85} In Volume{1};//buried electrode
Point (86) = {672211.27,5127435.64,-21.00, cl};
Point{86} In Volume{1};//buried electrode
Point (87) = {672211.27,5127435.64,-22.00, cl};
Point{87} In Volume{1};//buried electrode
Point (88) = {672211.27,5127435.64,-23.00, cl};
Point{88} In Volume{1};//buried electrode
Point (89) = {672227.14,5127438.64,0.00, cl};
Point{89} In Surface{1};//surface electrode
Point (90) = {672227.14,5127438.64,-1.00, cl};
Point{90} In Volume{1};//buried electrode
Point (91) = {672227.14,5127438.64,-2.00, cl};
Point{91} In Volume{1};//buried electrode
Point (92) = {672227.14,5127438.64,-3.00, cl};
Point{92} In Volume{1};//buried electrode
Point (93) = {672227.14,5127438.64,-4.00, cl};
Point{93} In Volume{1};//buried electrode
Point (94) = {672227.14,5127438.64,-5.00, cl};
Point{94} In Volume{1};//buried electrode
Point (95) = {672227.14,5127438.64,-6.00, cl};
Point{95} In Volume{1};//buried electrode
Point (96) = {672227.14,5127438.64,-7.00, cl};
Point{96} In Volume{1};//buried electrode
Point (97) = {672227.14,5127438.64,-8.00, cl};
Point{97} In Volume{1};//buried electrode
Point (98) = {672227.14,5127438.64,-9.00, cl};
Point{98} In Volume{1};//buried electrode
Point (99) = {672227.14,5127438.64,-10.00, cl};
Point{99} In Volume{1};//buried electrode
Point (100) = {672227.14,5127438.64,-11.00, cl};
Point{100} In Volume{1};//buried electrode
Point (101) = {672227.14,5127438.64,-12.00, cl};
Point{101} In Volume{1};//buried electrode
Point (102) = {672227.14,5127438.64,-13.00, cl};
Point{102} In Volume{1};//buried electrode
Point (103) = {672227.14,5127438.64,-14.00, cl};
Point{103} In Volume{1};//buried electrode
Point (104) = {672227.14,5127438.64,-15.00, cl};
Point{104} In Volume{1};//buried electrode
Point (105) = {672227.14,5127438.64,-16.00, cl};
Point{105} In Volume{1};//buried electrode
Point (106) = {672227.14,5127438.64,-17.00, cl};
Point{106} In Volume{1};//buried electrode
Point (107) = {672227.14,5127438.64,-18.00, cl};
Point{107} In Volume{1};//buried electrode
Point (108) = {672227.14,5127438.64,-19.00, cl};
Point{108} In Volume{1};//buried electrode
Point (109) = {672227.14,5127438.64,-20.00, cl};
Point{109} In Volume{1};//buried electrode
Point (110) = {672227.14,5127438.64,-21.00, cl};
Point{110} In Volume{1};//buried electrode
Point (111) = {672227.14,5127438.64,-22.00, cl};
Point{111} In Volume{1};//buried electrode
Point (112) = {672227.14,5127438.64,-23.00, cl};
Point{112} In Volume{1};//buried electrode
Point (113) = {672218.92,5127420.79,0.00, cl};
Point{113} In Surface{1};//surface electrode
Point (114) = {672218.92,5127420.79,-1.00, cl};
Point{114} In Volume{1};//buried electrode
Point (115) = {672218.92,5127420.79,-2.00, cl};
Point{115} In Volume{1};//buried electrode
Point (116) = {672218.92,5127420.79,-3.00, cl};
Point{116} In Volume{1};//buried electrode
Point (117) = {672218.92,5127420.79,-4.00, cl};
Point{117} In Volume{1};//buried electrode
Point (118) = {672218.92,5127420.79,-5.00, cl};
Point{118} In Volume{1};//buried electrode
Point (119) = {672218.92,5127420.79,-6.00, cl};
Point{119} In Volume{1};//buried electrode
Point (120) = {672218.92,5127420.79,-7.00, cl};
Point{120} In Volume{1};//buried electrode
Point (121) = {672218.92,5127420.79,-8.00, cl};
Point{121} In Volume{1};//buried electrode
Point (122) = {672218.92,5127420.79,-9.00, cl};
Point{122} In Volume{1};//buried electrode
Point (123) = {672218.92,5127420.79,-10.00, cl};
Point{123} In Volume{1};//buried electrode
Point (124) = {672218.92,5127420.79,-11.00, cl};
Point{124} In Volume{1};//buried electrode
Point (125) = {672218.92,5127420.79,-12.00, cl};
Point{125} In Volume{1};//buried electrode
Point (126) = {672218.92,5127420.79,-13.00, cl};
Point{126} In Volume{1};//buried electrode
Point (127) = {672218.92,5127420.79,-14.00, cl};
Point{127} In Volume{1};//buried electrode
Point (128) = {672218.92,5127420.79,-15.00, cl};
Point{128} In Volume{1};//buried electrode
Point (129) = {672218.92,5127420.79,-16.00, cl};
Point{129} In Volume{1};//buried electrode
Point (130) = {672218.92,5127420.79,-17.00, cl};
Point{130} In Volume{1};//buried electrode
Point (131) = {672218.92,5127420.79,-18.00, cl};
Point{131} In Volume{1};//buried electrode
Point (132) = {672218.92,5127420.79,-19.00, cl};
Point{132} In Volume{1};//buried electrode
Point (133) = {672218.92,5127420.79,-20.00, cl};
Point{133} In Volume{1};//buried electrode
Point (134) = {672218.92,5127420.79,-21.00, cl};
Point{134} In Volume{1};//buried electrode
Point (135) = {672218.92,5127420.79,-22.00, cl};
Point{135} In Volume{1};//buried electrode
Point (136) = {672218.92,5127420.79,-23.00, cl};
Point{136} In Volume{1};//buried electrode
//End electrodes
