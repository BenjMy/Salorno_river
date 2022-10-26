//3D half space problem mesh for ResIPy - no topography
Mesh.Binary = 0;//specify we want ASCII format
cl=1.00;//define characteristic length for fine mesh region
//Fine mesh region.
Point (1) = {32.22,32.51,0.00, cl*1.2};
Point (2) = {32.22,-5.42,0.00, cl*1.2};
Point (3) = {-5.37,-5.42,0.00, cl*1.2};
Point (4) = {-5.37,32.51,0.00, cl*1.2};
Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,1};
cl2=cl*5.00;//define characteristic length for base of fine mesh region
Point (5) = {32.22,32.51,-29.12, cl2};
Point (6) = {32.22,-5.42,-29.12, cl2};
Point (7) = {-5.37,-5.42,-29.12, cl2};
Point (8) = {-5.37,32.51,-29.12, cl2};
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
cln = 100.00;//characteristic length for background region
Point (9) = {215.71,216.00,0.00, cln};
Point (10) = {215.71,-188.91,0.00, cln};
Point (11) = {-188.86,-188.91,0.00, cln};
Point (12) = {-188.86,216.00,0.00, cln};
Line(13) = {9,10};
Line(14) = {10,11};
Line(15) = {11,12};
Line(16) = {12,9};
Point (13) = {215.71,216.00,-212.61, cln};
Point (14) = {215.71,-188.91,-212.61, cln};
Point (15) = {-188.86,-188.91,-212.61, cln};
Point (16) = {-188.86,216.00,-212.61, cln};
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
Point (17) = {0.00,9.89,-23.00, cl};
Point{17} In Volume{1};//buried electrode
Point (18) = {0.00,9.89,-22.00, cl};
Point{18} In Volume{1};//buried electrode
Point (19) = {0.00,9.89,-21.00, cl};
Point{19} In Volume{1};//buried electrode
Point (20) = {0.00,9.89,-20.00, cl};
Point{20} In Volume{1};//buried electrode
Point (21) = {0.00,9.89,-19.00, cl};
Point{21} In Volume{1};//buried electrode
Point (22) = {0.00,9.89,-18.00, cl};
Point{22} In Volume{1};//buried electrode
Point (23) = {0.00,9.89,-17.00, cl};
Point{23} In Volume{1};//buried electrode
Point (24) = {0.00,9.89,-16.00, cl};
Point{24} In Volume{1};//buried electrode
Point (25) = {0.00,9.89,-15.00, cl};
Point{25} In Volume{1};//buried electrode
Point (26) = {0.00,9.89,-14.00, cl};
Point{26} In Volume{1};//buried electrode
Point (27) = {0.00,9.89,-13.00, cl};
Point{27} In Volume{1};//buried electrode
Point (28) = {0.00,9.89,-12.00, cl};
Point{28} In Volume{1};//buried electrode
Point (29) = {0.00,9.89,-11.00, cl};
Point{29} In Volume{1};//buried electrode
Point (30) = {0.00,9.89,-10.00, cl};
Point{30} In Volume{1};//buried electrode
Point (31) = {0.00,9.89,-9.00, cl};
Point{31} In Volume{1};//buried electrode
Point (32) = {0.00,9.89,-8.00, cl};
Point{32} In Volume{1};//buried electrode
Point (33) = {0.00,9.89,-7.00, cl};
Point{33} In Volume{1};//buried electrode
Point (34) = {0.00,9.89,-6.00, cl};
Point{34} In Volume{1};//buried electrode
Point (35) = {0.00,9.89,-5.00, cl};
Point{35} In Volume{1};//buried electrode
Point (36) = {0.00,9.89,-4.00, cl};
Point{36} In Volume{1};//buried electrode
Point (37) = {0.00,9.89,-3.00, cl};
Point{37} In Volume{1};//buried electrode
Point (38) = {0.00,9.89,-2.00, cl};
Point{38} In Volume{1};//buried electrode
Point (39) = {0.00,9.89,-1.00, cl};
Point{39} In Volume{1};//buried electrode
Point (40) = {0.00,9.89,0.00, cl};
Point{40} In Surface{1};//surface electrode
Point (41) = {9.47,27.09,0.00, cl};
Point{41} In Surface{1};//surface electrode
Point (42) = {9.47,27.09,-1.00, cl};
Point{42} In Volume{1};//buried electrode
Point (43) = {9.47,27.09,-2.00, cl};
Point{43} In Volume{1};//buried electrode
Point (44) = {9.47,27.09,-3.00, cl};
Point{44} In Volume{1};//buried electrode
Point (45) = {9.47,27.09,-4.00, cl};
Point{45} In Volume{1};//buried electrode
Point (46) = {9.47,27.09,-5.00, cl};
Point{46} In Volume{1};//buried electrode
Point (47) = {9.47,27.09,-6.00, cl};
Point{47} In Volume{1};//buried electrode
Point (48) = {9.47,27.09,-7.00, cl};
Point{48} In Volume{1};//buried electrode
Point (49) = {9.47,27.09,-8.00, cl};
Point{49} In Volume{1};//buried electrode
Point (50) = {9.47,27.09,-9.00, cl};
Point{50} In Volume{1};//buried electrode
Point (51) = {9.47,27.09,-10.00, cl};
Point{51} In Volume{1};//buried electrode
Point (52) = {9.47,27.09,-11.00, cl};
Point{52} In Volume{1};//buried electrode
Point (53) = {9.47,27.09,-12.00, cl};
Point{53} In Volume{1};//buried electrode
Point (54) = {9.47,27.09,-13.00, cl};
Point{54} In Volume{1};//buried electrode
Point (55) = {9.47,27.09,-14.00, cl};
Point{55} In Volume{1};//buried electrode
Point (56) = {9.47,27.09,-15.00, cl};
Point{56} In Volume{1};//buried electrode
Point (57) = {9.47,27.09,-16.00, cl};
Point{57} In Volume{1};//buried electrode
Point (58) = {9.47,27.09,-17.00, cl};
Point{58} In Volume{1};//buried electrode
Point (59) = {9.47,27.09,-18.00, cl};
Point{59} In Volume{1};//buried electrode
Point (60) = {9.47,27.09,-19.00, cl};
Point{60} In Volume{1};//buried electrode
Point (61) = {9.47,27.09,-20.00, cl};
Point{61} In Volume{1};//buried electrode
Point (62) = {9.47,27.09,-21.00, cl};
Point{62} In Volume{1};//buried electrode
Point (63) = {9.47,27.09,-22.00, cl};
Point{63} In Volume{1};//buried electrode
Point (64) = {9.47,27.09,-23.00, cl};
Point{64} In Volume{1};//buried electrode
Point (65) = {10.98,14.86,0.00, cl};
Point{65} In Surface{1};//surface electrode
Point (66) = {10.98,14.86,-1.00, cl};
Point{66} In Volume{1};//buried electrode
Point (67) = {10.98,14.86,-2.00, cl};
Point{67} In Volume{1};//buried electrode
Point (68) = {10.98,14.86,-3.00, cl};
Point{68} In Volume{1};//buried electrode
Point (69) = {10.98,14.86,-4.00, cl};
Point{69} In Volume{1};//buried electrode
Point (70) = {10.98,14.86,-5.00, cl};
Point{70} In Volume{1};//buried electrode
Point (71) = {10.98,14.86,-6.00, cl};
Point{71} In Volume{1};//buried electrode
Point (72) = {10.98,14.86,-7.00, cl};
Point{72} In Volume{1};//buried electrode
Point (73) = {10.98,14.86,-8.00, cl};
Point{73} In Volume{1};//buried electrode
Point (74) = {10.98,14.86,-9.00, cl};
Point{74} In Volume{1};//buried electrode
Point (75) = {10.98,14.86,-10.00, cl};
Point{75} In Volume{1};//buried electrode
Point (76) = {10.98,14.86,-11.00, cl};
Point{76} In Volume{1};//buried electrode
Point (77) = {10.98,14.86,-12.00, cl};
Point{77} In Volume{1};//buried electrode
Point (78) = {10.98,14.86,-13.00, cl};
Point{78} In Volume{1};//buried electrode
Point (79) = {10.98,14.86,-14.00, cl};
Point{79} In Volume{1};//buried electrode
Point (80) = {10.98,14.86,-15.00, cl};
Point{80} In Volume{1};//buried electrode
Point (81) = {10.98,14.86,-16.00, cl};
Point{81} In Volume{1};//buried electrode
Point (82) = {10.98,14.86,-17.00, cl};
Point{82} In Volume{1};//buried electrode
Point (83) = {10.98,14.86,-18.00, cl};
Point{83} In Volume{1};//buried electrode
Point (84) = {10.98,14.86,-19.00, cl};
Point{84} In Volume{1};//buried electrode
Point (85) = {10.98,14.86,-20.00, cl};
Point{85} In Volume{1};//buried electrode
Point (86) = {10.98,14.86,-21.00, cl};
Point{86} In Volume{1};//buried electrode
Point (87) = {10.98,14.86,-22.00, cl};
Point{87} In Volume{1};//buried electrode
Point (88) = {10.98,14.86,-23.00, cl};
Point{88} In Volume{1};//buried electrode
Point (89) = {26.85,17.85,0.00, cl};
Point{89} In Surface{1};//surface electrode
Point (90) = {26.85,17.85,-1.00, cl};
Point{90} In Volume{1};//buried electrode
Point (91) = {26.85,17.85,-2.00, cl};
Point{91} In Volume{1};//buried electrode
Point (92) = {26.85,17.85,-3.00, cl};
Point{92} In Volume{1};//buried electrode
Point (93) = {26.85,17.85,-4.00, cl};
Point{93} In Volume{1};//buried electrode
Point (94) = {26.85,17.85,-5.00, cl};
Point{94} In Volume{1};//buried electrode
Point (95) = {26.85,17.85,-6.00, cl};
Point{95} In Volume{1};//buried electrode
Point (96) = {26.85,17.85,-7.00, cl};
Point{96} In Volume{1};//buried electrode
Point (97) = {26.85,17.85,-8.00, cl};
Point{97} In Volume{1};//buried electrode
Point (98) = {26.85,17.85,-9.00, cl};
Point{98} In Volume{1};//buried electrode
Point (99) = {26.85,17.85,-10.00, cl};
Point{99} In Volume{1};//buried electrode
Point (100) = {26.85,17.85,-11.00, cl};
Point{100} In Volume{1};//buried electrode
Point (101) = {26.85,17.85,-12.00, cl};
Point{101} In Volume{1};//buried electrode
Point (102) = {26.85,17.85,-13.00, cl};
Point{102} In Volume{1};//buried electrode
Point (103) = {26.85,17.85,-14.00, cl};
Point{103} In Volume{1};//buried electrode
Point (104) = {26.85,17.85,-15.00, cl};
Point{104} In Volume{1};//buried electrode
Point (105) = {26.85,17.85,-16.00, cl};
Point{105} In Volume{1};//buried electrode
Point (106) = {26.85,17.85,-17.00, cl};
Point{106} In Volume{1};//buried electrode
Point (107) = {26.85,17.85,-18.00, cl};
Point{107} In Volume{1};//buried electrode
Point (108) = {26.85,17.85,-19.00, cl};
Point{108} In Volume{1};//buried electrode
Point (109) = {26.85,17.85,-20.00, cl};
Point{109} In Volume{1};//buried electrode
Point (110) = {26.85,17.85,-21.00, cl};
Point{110} In Volume{1};//buried electrode
Point (111) = {26.85,17.85,-22.00, cl};
Point{111} In Volume{1};//buried electrode
Point (112) = {26.85,17.85,-23.00, cl};
Point{112} In Volume{1};//buried electrode
Point (113) = {18.64,0.00,0.00, cl};
Point{113} In Surface{1};//surface electrode
Point (114) = {18.64,0.00,-1.00, cl};
Point{114} In Volume{1};//buried electrode
Point (115) = {18.64,0.00,-2.00, cl};
Point{115} In Volume{1};//buried electrode
Point (116) = {18.64,0.00,-3.00, cl};
Point{116} In Volume{1};//buried electrode
Point (117) = {18.64,0.00,-4.00, cl};
Point{117} In Volume{1};//buried electrode
Point (118) = {18.64,0.00,-5.00, cl};
Point{118} In Volume{1};//buried electrode
Point (119) = {18.64,0.00,-6.00, cl};
Point{119} In Volume{1};//buried electrode
Point (120) = {18.64,0.00,-7.00, cl};
Point{120} In Volume{1};//buried electrode
Point (121) = {18.64,0.00,-8.00, cl};
Point{121} In Volume{1};//buried electrode
Point (122) = {18.64,0.00,-9.00, cl};
Point{122} In Volume{1};//buried electrode
Point (123) = {18.64,0.00,-10.00, cl};
Point{123} In Volume{1};//buried electrode
Point (124) = {18.64,0.00,-11.00, cl};
Point{124} In Volume{1};//buried electrode
Point (125) = {18.64,0.00,-12.00, cl};
Point{125} In Volume{1};//buried electrode
Point (126) = {18.64,0.00,-13.00, cl};
Point{126} In Volume{1};//buried electrode
Point (127) = {18.64,0.00,-14.00, cl};
Point{127} In Volume{1};//buried electrode
Point (128) = {18.64,0.00,-15.00, cl};
Point{128} In Volume{1};//buried electrode
Point (129) = {18.64,0.00,-16.00, cl};
Point{129} In Volume{1};//buried electrode
Point (130) = {18.64,0.00,-17.00, cl};
Point{130} In Volume{1};//buried electrode
Point (131) = {18.64,0.00,-18.00, cl};
Point{131} In Volume{1};//buried electrode
Point (132) = {18.64,0.00,-19.00, cl};
Point{132} In Volume{1};//buried electrode
Point (133) = {18.64,0.00,-20.00, cl};
Point{133} In Volume{1};//buried electrode
Point (134) = {18.64,0.00,-21.00, cl};
Point{134} In Volume{1};//buried electrode
Point (135) = {18.64,0.00,-22.00, cl};
Point{135} In Volume{1};//buried electrode
Point (136) = {18.64,0.00,-23.00, cl};
Point{136} In Volume{1};//buried electrode
//End electrodes
