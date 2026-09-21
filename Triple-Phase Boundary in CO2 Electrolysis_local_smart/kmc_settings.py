model_name = 'Triple-Phase Boundary in CO2 Electrolysis'
simulation_size = 20 #TODO: A. Savara found on 12/04/22 that this is hardcoded in io.py, and it should not be hardcoded. 
buffer_parameter = 1000 #TODO: A. Savara found on 12/04/22 that this block of settings is hardcoded in io.py, and it should not be hardcoded.
threshold_parameter = 0.2
sampling_steps = 20
execution_steps = 200
save_limit = 1000
random_seed = 1 #TODO: A. Savara found on 12/04/22 that this is hardcoded in io.py, and it should not be hardcoded.

def setup_model(model):
    """ Aug 15th 2022: setup_model is legacy code. Please ignore the rest of this comment and this function. 
    Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "A":{"value":"(2.8892*angstrom)**2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "CO2_diffuse":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "CO2_dissolve":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "CO3_diffuse":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "CO_diffuse":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "CO_dissolve":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "Ea_CO2_reduce":{"value":"0.65", "adjustable":True, "min":"-5.0", "max":"5.0","scale":"linear"},
    "Ga_CO2_dissolve":{"value":"0.049", "adjustable":True, "min":"-1.0", "max":"1.0","scale":"linear"},
    "Ga_CO2_undissolve":{"value":"0.047", "adjustable":True, "min":"-1.0", "max":"1.0","scale":"linear"},
    "Ga_CO2_water_adsorb":{"value":"0.094", "adjustable":True, "min":"-1.0", "max":"1.0","scale":"linear"},
    "Ga_CO2_water_desorb":{"value":"0.021", "adjustable":True, "min":"-1.0", "max":"1.0","scale":"linear"},
    "OH_diffuse":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    "T":{"value":"298.15", "adjustable":True, "min":"100.0", "max":"700.0","scale":"linear"},
    "deltaG_CO_dissolve":{"value":"0.1", "adjustable":True, "min":"-1.0", "max":"1.0","scale":"linear"},
    "p_CO":{"value":"0.01", "adjustable":True, "min":"1e-10", "max":"100.0","scale":"linear"},
    "p_CO2":{"value":"1.0", "adjustable":True, "min":"1e-10", "max":"100.0","scale":"linear"},
    "reduce":{"value":"1", "adjustable":True, "min":"1e-10", "max":"10000000000.0","scale":"linear"},
    }

proc_pair_indices = [1, 2, 3, 4, -3, 5, 6, -5, 7, 8, -7, 9, 10, -9, 11, 12, -11, 13, 14, -13, 15, 16, -15, 17, 18, -1, -17, 19, -2, 20, 21, -4, 22, 23, -6, -22, 24, 25, -8, -24, 26, 27, -10, -26, 28, 29, -12, -28, 30, 31, -14, -30, 32, 33, -16, -32, 34, 35, -18, -34, 36, 37, -19, -20, -36, 38, -21, 39, 40, -23, 41, 42, -25, -41, 43, 44, -27, -43, 45, 46, -29, -45, 47, 48, -31, -47, 49, 50, -33, -49, 51, 52, -35, -51, 53, 54, -37, -53, 55, 56, -38, -39, -55, 57, -40, 58, 59, -42, 60, 61, -44, -60, 62, 63, -46, -62, 64, 65, -48, -64, 66, 67, -50, -66, 68, 69, -52, -68, 70, 71, -54, -70, 72, 73, -56, -72, 74, 75, -57, -58, -74, 76, -59, 77, 78, -61, 79, 80, -63, -79, 81, 82, -65, -81, 83, 84, -67, -83, 85, 86, -69, -85, 87, 88, -71, -87, 89, 90, -73, -89, 91, 92, -75, -91, 93, 94, -76, -77, -93, 95, -78, 96, 97, -80, 98, 99, -82, -98, 100, 101, -84, -100, 102, 103, -86, -102, 104, 105, -88, -104, 106, 107, -90, -106, 108, 109, -92, -108, 110, 111, -94, -110, 112, 113, -95, -96, -112, 114, -97, 115, 116, -99, 117, 118, -101, -117, 119, 120, -103, -119, 121, 122, -105, -121, 123, 124, -107, -123, 125, 126, -109, -125, 127, 128, -111, -127, 129, 130, -113, -129, 131, 132, -114, -115, -131, 133, -116, 134, 135, -118, 136, 137, -120, -136, 138, 139, -122, -138, 140, 141, -124, -140, 142, 143, -126, -142, 144, 145, -128, -144, 146, 147, -130, -146, 148, 149, -132, -148, 150, 151, -133, -134, -150, 152, -135, 153, -137, 154, -139, -154, 155, -141, -155, 156, -143, -156, 157, -145, -157, 158, -147, -158, 159, -149, -159, 160, -151, -160, 161, -152, -153, -161, 162, 163, 164, 165, -164, 166, 167, -166, 168, 169, -168, 170, 171, -170, 172, 173, -172, 174, 175, -174, 176, 177, -176, 178, 179, -162, -178, 180, -163, 181, 182, -165, 183, 184, -167, -183, 185, 186, -169, -185, 187, 188, -171, -187, 189, 190, -173, -189, 191, 192, -175, -191, 193, 194, -177, -193, 195, 196, -179, -195, 197, 198, -180, -181, -197, 199, -182, 200, 201, -184, 202, 203, -186, -202, 204, 205, -188, -204, 206, 207, -190, -206, 208, 209, -192, -208, 210, 211, -194, -210, 212, 213, -196, -212, 214, 215, -198, -214, 216, 217, -199, -200, -216, 218, -201, 219, 220, -203, 221, 222, -205, -221, 223, 224, -207, -223, 225, 226, -209, -225, 227, 228, -211, -227, 229, 230, -213, -229, 231, 232, -215, -231, 233, 234, -217, -233, 235, 236, -218, -219, -235, 237, -220, 238, 239, -222, 240, 241, -224, -240, 242, 243, -226, -242, 244, 245, -228, -244, 246, 247, -230, -246, 248, 249, -232, -248, 250, 251, -234, -250, 252, 253, -236, -252, 254, 255, -237, -238, -254, 256, -239, 257, 258, -241, 259, 260, -243, -259, 261, 262, -245, -261, 263, 264, -247, -263, 265, 266, -249, -265, 267, 268, -251, -267, 269, 270, -253, -269, 271, 272, -255, -271, 273, 274, -256, -257, -273, 275, -258, 276, 277, -260, 278, 279, -262, -278, 280, 281, -264, -280, 282, 283, -266, -282, 284, 285, -268, -284, 286, 287, -270, -286, 288, 289, -272, -288, 290, 291, -274, -290, 292, 293, -275, -276, -292, 294, -277, 295, 296, -279, 297, 298, -281, -297, 299, 300, -283, -299, 301, 302, -285, -301, 303, 304, -287, -303, 305, 306, -289, -305, 307, 308, -291, -307, 309, 310, -293, -309, 311, 312, -294, -295, -311, 313, -296, 314, -298, 315, -300, -315, 316, -302, -316, 317, -304, -317, 318, -306, -318, 319, -308, -319, 320, -310, -320, 321, -312, -321, 322, -313, -314, -322, 323, 324, 325, 326, -325, 327, 328, -327, 329, 330, -329, 331, 332, -331, 333, 334, -333, 335, 336, -335, 337, 338, -337, 339, 340, -323, -339, 341, -324, 342, 343, -326, 344, 345, -328, -344, 346, 347, -330, -346, 348, 349, -332, -348, 350, 351, -334, -350, 352, 353, -336, -352, 354, 355, -338, -354, 356, 357, -340, -356, 358, 359, -341, -342, -358, 360, -343, 361, 362, -345, 363, 364, -347, -363, 365, 366, -349, -365, 367, 368, -351, -367, 369, 370, -353, -369, 371, 372, -355, -371, 373, 374, -357, -373, 375, 376, -359, -375, 377, 378, -360, -361, -377, 379, -362, 380, 381, -364, 382, 383, -366, -382, 384, 385, -368, -384, 386, 387, -370, -386, 388, 389, -372, -388, 390, 391, -374, -390, 392, 393, -376, -392, 394, 395, -378, -394, 396, 397, -379, -380, -396, 398, -381, 399, 400, -383, 401, 402, -385, -401, 403, 404, -387, -403, 405, 406, -389, -405, 407, 408, -391, -407, 409, 410, -393, -409, 411, 412, -395, -411, 413, 414, -397, -413, 415, 416, -398, -399, -415, 417, -400, 418, 419, -402, 420, 421, -404, -420, 422, 423, -406, -422, 424, 425, -408, -424, 426, 427, -410, -426, 428, 429, -412, -428, 430, 431, -414, -430, 432, 433, -416, -432, 434, 435, -417, -418, -434, 436, -419, 437, 438, -421, 439, 440, -423, -439, 441, 442, -425, -441, 443, 444, -427, -443, 445, 446, -429, -445, 447, 448, -431, -447, 449, 450, -433, -449, 451, 452, -435, -451, 453, 454, -436, -437, -453, 455, -438, 456, 457, -440, 458, 459, -442, -458, 460, 461, -444, -460, 462, 463, -446, -462, 464, 465, -448, -464, 466, 467, -450, -466, 468, 469, -452, -468, 470, 471, -454, -470, 472, 473, -455, -456, -472, 474, -457, 475, -459, 476, -461, -476, 477, -463, -477, 478, -465, -478, 479, -467, -479, 480, -469, -480, 481, -471, -481, 482, -473, -482, 483, -474, -475, -483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, -484, -485, -486, -487, -488, -489, -490, -491, -492, -493, -494, -495, -496, -497, -498, -499, -500, -501, -502, -503, -504, -505, -506, -507, -508, -509, -510, -511, -512, -513, -514, -515, -516, -517, -518, -519, -520, -521, -522, -523, -524, -525, -526, -527, -528, -529, -530, -531, -532, -533, -534, -535, -536, -537, -538, -539, -540, -541, -542, -543, -544, -545, -546, -547, -548, -549, -550, -551, -552, -553, -554, -555, -556, -557, -558, -559, -560, -561, -562, -563, -564, -565, -566, -567, -568, -569, -570, -571, -572, -573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, -574, -575, -576, -577, -578, -579, -580, -581, -582, -583, -584, -585, -586, -587, -588, -589, -590, -591, -592, -593, -594, -595, -596, -597, -598, -599, -600, -601, -602, -603, -604, -605, -606, -607, -608, -609, -610, -611, -612, -613, -614, -615, -616, -617, -618, -619, -620, -621, -622, -623, -624, -625, -626, -627, -628, -629, -630, -631, -632, -633, -634, -635, -636, -637, -638, -639, -640, -641, -642, -643, -644, -645, -646, -647, -648, -649, -650, -651, -652, -653, -654, -655, -656, -657, -658, -659, -660, -661, -662, -663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, -664, -665, -666, -667, -668, -669, -670, -671, -672, -673, -674, -675, -676, -677, -678, -679, -680, -681, -682, -683, -684, -685, -686, -687, -688, -689, -690, -691, -692, -693, -694, -695, -696, -697, -698, -699, -700, -701, -702, -703, -704, -705, -706, -707, -708, -709, -710, -711, -712, -713, -714, -715, -716, -717, -718, -719, -720, -721, -722, -723, -724, -725, -726, -727, -728, -729, -730, -731, -732, -733, -734, -735, -736, -737, -738, -739, -740, -741, -742, -743, -744, -745, -746, -747, -748, -749, -750, -751, -752, -753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, -764, -765, -766, -767, -768, -769, -770, -771, -772, -754, -755, -756, -757, -758, -759, -760, -761, -762, -763, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, -773, -774, -775, -776, -777, -778, -779, -780, -781, -782]

is_diff_proc = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

rate_constants = {
    "diffuse_CO2_1_10_1_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_10_2_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_1_1_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_1_2_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_2_1_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_2_1_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_2_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_3_1_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_3_1_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_3_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_4_1_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_4_1_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_4_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_5_1_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_5_1_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_5_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_6_1_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_6_1_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_6_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_7_1_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_7_1_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_7_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_8_1_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_8_1_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_8_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_9_1_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_9_1_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_1_9_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_10_1_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_10_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_10_3_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_1_1_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_1_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_1_3_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_2_1_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_2_2_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_2_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_2_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_3_1_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_3_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_3_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_3_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_4_1_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_4_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_4_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_4_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_5_1_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_5_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_5_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_5_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_6_1_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_6_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_6_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_6_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_7_1_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_7_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_7_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_7_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_8_1_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_8_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_8_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_8_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_9_1_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_9_2_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_9_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_2_9_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_10_2_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_10_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_10_4_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_1_2_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_1_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_1_4_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_2_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_2_3_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_2_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_2_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_3_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_3_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_3_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_3_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_4_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_4_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_4_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_4_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_5_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_5_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_5_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_5_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_6_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_6_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_6_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_6_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_7_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_7_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_7_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_7_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_8_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_8_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_8_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_8_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_9_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_9_3_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_9_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_3_9_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_10_3_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_10_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_10_5_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_1_3_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_1_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_1_5_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_2_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_2_4_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_2_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_2_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_3_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_3_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_3_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_3_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_4_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_4_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_4_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_4_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_5_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_5_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_5_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_5_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_6_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_6_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_6_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_6_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_7_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_7_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_7_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_7_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_8_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_8_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_8_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_8_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_9_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_9_4_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_9_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_4_9_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_10_4_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_10_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_10_6_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_1_4_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_1_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_1_6_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_2_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_2_5_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_2_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_2_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_3_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_3_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_3_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_3_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_4_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_4_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_4_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_4_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_5_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_5_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_5_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_5_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_6_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_6_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_6_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_6_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_7_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_7_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_7_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_7_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_8_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_8_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_8_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_8_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_9_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_9_5_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_9_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_5_9_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_10_5_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_10_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_10_7_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_1_5_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_1_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_1_7_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_2_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_2_6_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_2_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_2_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_3_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_3_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_3_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_3_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_4_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_4_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_4_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_4_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_5_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_5_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_5_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_5_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_6_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_6_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_6_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_6_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_7_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_7_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_7_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_7_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_8_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_8_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_8_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_8_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_9_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_9_6_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_9_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_6_9_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_10_6_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_10_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_10_8_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_1_6_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_1_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_1_8_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_2_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_2_7_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_2_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_2_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_3_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_3_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_3_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_3_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_4_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_4_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_4_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_4_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_5_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_5_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_5_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_5_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_6_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_6_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_6_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_6_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_7_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_7_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_7_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_7_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_8_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_8_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_8_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_8_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_9_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_9_7_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_9_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_7_9_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_10_7_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_10_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_10_9_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_1_7_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_1_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_1_9_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_2_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_2_8_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_2_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_2_9_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_3_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_3_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_3_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_3_9_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_4_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_4_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_4_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_4_9_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_5_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_5_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_5_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_5_9_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_6_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_6_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_6_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_6_9_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_7_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_7_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_7_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_7_9_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_8_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_8_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_8_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_8_9_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_9_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_9_8_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_9_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_8_9_9_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_10_8_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_10_9_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_1_8_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_1_9_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_2_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_2_9_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_2_9_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_3_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_3_9_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_3_9_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_4_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_4_9_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_4_9_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_5_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_5_9_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_5_9_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_6_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_6_9_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_6_9_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_7_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_7_9_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_7_9_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_8_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_8_9_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_8_9_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_9_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_9_9_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO2_9_9_9_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_CO3_1_10_1_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_10_2_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_1_1_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_1_2_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_2_1_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_2_1_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_2_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_3_1_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_3_1_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_3_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_4_1_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_4_1_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_4_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_5_1_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_5_1_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_5_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_6_1_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_6_1_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_6_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_7_1_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_7_1_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_7_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_8_1_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_8_1_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_8_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_9_1_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_9_1_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_1_9_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_10_1_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_10_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_10_3_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_1_1_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_1_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_1_3_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_2_1_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_2_2_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_2_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_2_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_3_1_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_3_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_3_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_3_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_4_1_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_4_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_4_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_4_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_5_1_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_5_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_5_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_5_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_6_1_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_6_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_6_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_6_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_7_1_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_7_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_7_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_7_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_8_1_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_8_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_8_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_8_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_9_1_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_9_2_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_9_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_2_9_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_10_2_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_10_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_10_4_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_1_2_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_1_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_1_4_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_2_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_2_3_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_2_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_2_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_3_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_3_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_3_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_3_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_4_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_4_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_4_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_4_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_5_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_5_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_5_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_5_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_6_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_6_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_6_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_6_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_7_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_7_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_7_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_7_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_8_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_8_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_8_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_8_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_9_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_9_3_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_9_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_3_9_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_10_3_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_10_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_10_5_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_1_3_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_1_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_1_5_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_2_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_2_4_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_2_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_2_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_3_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_3_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_3_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_3_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_4_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_4_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_4_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_4_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_5_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_5_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_5_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_5_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_6_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_6_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_6_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_6_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_7_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_7_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_7_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_7_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_8_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_8_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_8_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_8_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_9_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_9_4_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_9_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_4_9_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_10_4_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_10_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_10_6_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_1_4_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_1_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_1_6_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_2_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_2_5_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_2_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_2_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_3_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_3_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_3_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_3_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_4_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_4_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_4_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_4_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_5_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_5_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_5_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_5_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_6_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_6_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_6_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_6_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_7_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_7_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_7_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_7_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_8_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_8_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_8_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_8_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_9_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_9_5_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_9_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_5_9_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_10_5_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_10_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_10_7_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_1_5_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_1_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_1_7_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_2_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_2_6_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_2_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_2_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_3_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_3_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_3_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_3_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_4_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_4_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_4_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_4_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_5_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_5_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_5_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_5_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_6_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_6_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_6_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_6_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_7_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_7_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_7_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_7_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_8_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_8_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_8_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_8_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_9_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_9_6_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_9_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_6_9_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_10_6_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_10_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_10_8_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_1_6_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_1_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_1_8_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_2_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_2_7_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_2_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_2_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_3_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_3_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_3_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_3_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_4_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_4_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_4_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_4_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_5_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_5_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_5_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_5_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_6_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_6_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_6_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_6_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_7_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_7_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_7_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_7_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_8_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_8_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_8_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_8_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_9_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_9_7_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_9_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_7_9_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_10_7_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_10_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_10_9_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_1_7_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_1_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_1_9_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_2_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_2_8_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_2_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_2_9_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_3_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_3_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_3_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_3_9_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_4_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_4_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_4_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_4_9_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_5_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_5_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_5_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_5_9_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_6_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_6_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_6_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_6_9_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_7_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_7_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_7_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_7_9_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_8_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_8_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_8_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_8_9_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_9_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_9_8_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_9_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_8_9_9_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_10_8_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_10_9_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_1_8_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_1_9_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_2_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_2_9_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_2_9_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_3_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_3_9_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_3_9_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_4_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_4_9_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_4_9_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_5_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_5_9_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_5_9_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_6_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_6_9_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_6_9_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_7_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_7_9_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_7_9_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_8_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_8_9_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_8_9_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_9_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_9_9_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_CO3_9_9_9_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_OH_1_10_1_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_10_2_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_1_1_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_1_2_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_2_1_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_2_1_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_2_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_3_1_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_3_1_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_3_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_4_1_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_4_1_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_4_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_5_1_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_5_1_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_5_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_6_1_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_6_1_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_6_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_7_1_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_7_1_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_7_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_8_1_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_8_1_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_8_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_9_1_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_9_1_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_1_9_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_10_1_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_10_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_10_3_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_1_1_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_1_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_1_3_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_2_1_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_2_2_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_2_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_2_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_3_1_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_3_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_3_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_3_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_4_1_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_4_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_4_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_4_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_5_1_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_5_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_5_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_5_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_6_1_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_6_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_6_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_6_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_7_1_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_7_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_7_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_7_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_8_1_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_8_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_8_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_8_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_9_1_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_9_2_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_9_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_2_9_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_10_2_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_10_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_10_4_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_1_2_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_1_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_1_4_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_2_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_2_3_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_2_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_2_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_3_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_3_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_3_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_3_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_4_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_4_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_4_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_4_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_5_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_5_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_5_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_5_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_6_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_6_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_6_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_6_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_7_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_7_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_7_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_7_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_8_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_8_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_8_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_8_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_9_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_9_3_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_9_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_3_9_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_10_3_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_10_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_10_5_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_1_3_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_1_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_1_5_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_2_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_2_4_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_2_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_2_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_3_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_3_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_3_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_3_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_4_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_4_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_4_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_4_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_5_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_5_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_5_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_5_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_6_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_6_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_6_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_6_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_7_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_7_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_7_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_7_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_8_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_8_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_8_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_8_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_9_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_9_4_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_9_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_4_9_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_10_4_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_10_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_10_6_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_1_4_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_1_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_1_6_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_2_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_2_5_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_2_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_2_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_3_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_3_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_3_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_3_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_4_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_4_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_4_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_4_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_5_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_5_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_5_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_5_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_6_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_6_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_6_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_6_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_7_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_7_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_7_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_7_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_8_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_8_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_8_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_8_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_9_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_9_5_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_9_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_5_9_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_10_5_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_10_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_10_7_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_1_5_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_1_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_1_7_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_2_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_2_6_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_2_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_2_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_3_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_3_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_3_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_3_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_4_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_4_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_4_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_4_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_5_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_5_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_5_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_5_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_6_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_6_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_6_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_6_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_7_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_7_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_7_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_7_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_8_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_8_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_8_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_8_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_9_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_9_6_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_9_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_6_9_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_10_6_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_10_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_10_8_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_1_6_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_1_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_1_8_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_2_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_2_7_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_2_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_2_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_3_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_3_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_3_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_3_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_4_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_4_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_4_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_4_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_5_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_5_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_5_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_5_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_6_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_6_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_6_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_6_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_7_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_7_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_7_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_7_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_8_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_8_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_8_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_8_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_9_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_9_7_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_9_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_7_9_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_10_7_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_10_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_10_9_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_1_7_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_1_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_1_9_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_2_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_2_8_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_2_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_2_9_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_3_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_3_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_3_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_3_9_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_4_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_4_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_4_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_4_9_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_5_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_5_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_5_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_5_9_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_6_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_6_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_6_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_6_9_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_7_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_7_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_7_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_7_9_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_8_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_8_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_8_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_8_9_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_9_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_9_8_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_9_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_8_9_9_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_10_8_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_10_9_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_1_8_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_1_9_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_2_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_2_9_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_2_9_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_3_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_3_9_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_3_9_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_4_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_4_9_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_4_9_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_5_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_5_9_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_5_9_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_6_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_6_9_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_6_9_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_7_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_7_9_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_7_9_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_8_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_8_9_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_8_9_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_9_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_9_9_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_OH_9_9_9_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_CO2_from_1_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_1_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_from_9_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_1_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_2_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_3_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_4_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_5_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_6_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_7_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_8_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_1":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_10":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_2":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_3":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_4":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_5":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_6":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_7":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_8":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO2_to_9_9":("1.92e-09/A*CO2_diffuse", True),
    "diffuse_x_CO3_from_1_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_1_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_from_9_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_1_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_2_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_3_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_4_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_5_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_6_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_7_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_8_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_1":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_10":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_2":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_3":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_4":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_5":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_6":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_7":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_8":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_CO3_to_9_9":("9.55e-10/A*CO3_diffuse", True),
    "diffuse_x_OH_from_1_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_1_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_from_9_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_1_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_2_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_3_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_4_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_5_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_6_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_7_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_8_9":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_1":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_10":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_2":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_3":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_4":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_5":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_6":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_7":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_8":("5.3e-09/A*OH_diffuse", True),
    "diffuse_x_OH_to_9_9":("5.3e-09/A*OH_diffuse", True),
    "dissolve_CO2_from_0_1":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_10":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_2":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_3":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_4":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_5":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_6":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_7":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_8":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "dissolve_CO2_from_0_9":("10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)", True),
    "reduction_1":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_2":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_3":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_4":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_5":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_6":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_7":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_8":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_9":("10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce", True),
    "reduction_rev_1":("0.01", True),
    "reduction_rev_2":("0.01", True),
    "reduction_rev_3":("0.01", True),
    "reduction_rev_4":("0.01", True),
    "reduction_rev_5":("0.01", True),
    "reduction_rev_6":("0.01", True),
    "reduction_rev_7":("0.01", True),
    "reduction_rev_8":("0.01", True),
    "reduction_rev_9":("0.01", True),
    "undissolve_CO2_from_0_1":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_10":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_2":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_3":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_4":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_5":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_6":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_7":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_8":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "undissolve_CO2_from_0_9":("10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)", True),
    "water_adsorb_CO2_1":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_10":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_2":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_3":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_4":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_5":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_6":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_7":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_8":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_adsorb_CO2_9":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_1":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_10":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_2":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_3":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_4":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_5":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_6":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_7":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_8":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    "water_desorb_CO2_9":("bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve", True),
    }

site_names = ['tpb_line_0_0_substrate', 'tpb_line_0_1_boundary', 'tpb_line_0_2_boundary', 'tpb_line_0_3_boundary', 'tpb_line_0_4_boundary', 'tpb_line_0_5_boundary', 'tpb_line_0_6_boundary', 'tpb_line_0_7_boundary', 'tpb_line_0_8_boundary', 'tpb_line_0_9_boundary', 'tpb_line_0_10_boundary', 'tpb_line_1_0_substrate', 'tpb_line_1_1_active', 'tpb_line_1_2_bulk', 'tpb_line_1_3_bulk', 'tpb_line_1_4_bulk', 'tpb_line_1_5_bulk', 'tpb_line_1_6_bulk', 'tpb_line_1_7_bulk', 'tpb_line_1_8_bulk', 'tpb_line_1_9_bulk', 'tpb_line_1_10_bulk', 'tpb_line_2_0_substrate', 'tpb_line_2_1_active', 'tpb_line_2_2_bulk', 'tpb_line_2_3_bulk', 'tpb_line_2_4_bulk', 'tpb_line_2_5_bulk', 'tpb_line_2_6_bulk', 'tpb_line_2_7_bulk', 'tpb_line_2_8_bulk', 'tpb_line_2_9_bulk', 'tpb_line_2_10_bulk', 'tpb_line_3_0_substrate', 'tpb_line_3_1_active', 'tpb_line_3_2_bulk', 'tpb_line_3_3_bulk', 'tpb_line_3_4_bulk', 'tpb_line_3_5_bulk', 'tpb_line_3_6_bulk', 'tpb_line_3_7_bulk', 'tpb_line_3_8_bulk', 'tpb_line_3_9_bulk', 'tpb_line_3_10_bulk', 'tpb_line_4_0_substrate', 'tpb_line_4_1_active', 'tpb_line_4_2_bulk', 'tpb_line_4_3_bulk', 'tpb_line_4_4_bulk', 'tpb_line_4_5_bulk', 'tpb_line_4_6_bulk', 'tpb_line_4_7_bulk', 'tpb_line_4_8_bulk', 'tpb_line_4_9_bulk', 'tpb_line_4_10_bulk', 'tpb_line_5_0_substrate', 'tpb_line_5_1_active', 'tpb_line_5_2_bulk', 'tpb_line_5_3_bulk', 'tpb_line_5_4_bulk', 'tpb_line_5_5_bulk', 'tpb_line_5_6_bulk', 'tpb_line_5_7_bulk', 'tpb_line_5_8_bulk', 'tpb_line_5_9_bulk', 'tpb_line_5_10_bulk', 'tpb_line_6_0_substrate', 'tpb_line_6_1_active', 'tpb_line_6_2_bulk', 'tpb_line_6_3_bulk', 'tpb_line_6_4_bulk', 'tpb_line_6_5_bulk', 'tpb_line_6_6_bulk', 'tpb_line_6_7_bulk', 'tpb_line_6_8_bulk', 'tpb_line_6_9_bulk', 'tpb_line_6_10_bulk', 'tpb_line_7_0_substrate', 'tpb_line_7_1_active', 'tpb_line_7_2_bulk', 'tpb_line_7_3_bulk', 'tpb_line_7_4_bulk', 'tpb_line_7_5_bulk', 'tpb_line_7_6_bulk', 'tpb_line_7_7_bulk', 'tpb_line_7_8_bulk', 'tpb_line_7_9_bulk', 'tpb_line_7_10_bulk', 'tpb_line_8_0_substrate', 'tpb_line_8_1_active', 'tpb_line_8_2_bulk', 'tpb_line_8_3_bulk', 'tpb_line_8_4_bulk', 'tpb_line_8_5_bulk', 'tpb_line_8_6_bulk', 'tpb_line_8_7_bulk', 'tpb_line_8_8_bulk', 'tpb_line_8_9_bulk', 'tpb_line_8_10_bulk', 'tpb_line_9_0_substrate', 'tpb_line_9_1_active', 'tpb_line_9_2_bulk', 'tpb_line_9_3_bulk', 'tpb_line_9_4_bulk', 'tpb_line_9_5_bulk', 'tpb_line_9_6_bulk', 'tpb_line_9_7_bulk', 'tpb_line_9_8_bulk', 'tpb_line_9_9_bulk', 'tpb_line_9_10_bulk']
representations = {
    "Ag":"""Atoms('Ag', [[0, 0, 0]])""",
    "CO":"""Atoms('CO', [[0, 0, 0], [0, 0, 1.13]])""",
    "CO2":"""Atoms('OCO', [[-1.163, 0, 0], [0, 0, 0], [1.163, 0, 0]])""",
    "CO3":"""Atoms('COOO',[[0.0, 0.0, 0.0], [0.0, 0.0, 1.28], [1.1085125168440815, 0.0, -0.64], [-1.1085125168440815, 0.0, -0.64]])""",
    "COOH":"""Atoms('COOH',[[0, 0, 0], [-1.0392304845413263, 0, 0.6], [1.1518137870333034, 0, 0.665], [0.9171495483016257, 0, 1.6061868544877167]])""",
    "OH":"""Atoms('OH',[[0.0, 0.0, 0.0], [0.0, 0.0, 0.97]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "Ag":"""""",
    "CO":"""""",
    "CO2":"""""",
    "CO3":"""""",
    "COOH":"""""",
    "OH":"""""",
    "empty":"""""",
    }

tof_count = {
    }

connected_variables={'surroundingSitesDict': {}}
xml = """<?xml version="1.0" ?>
<kmc version="(0, 4)">
    <meta author="Lucas Yuan" email="lucasmyuan@gmail.com" model_name="Triple-Phase Boundary in CO2 Electrolysis" model_dimension="1" debug="0"/>
    <species_list default_species="empty">
        <species name="Ag" representation="Atoms('Ag', [[0, 0, 0]])" color="" tags=""/>
        <species name="CO" representation="Atoms('CO', [[0, 0, 0], [0, 0, 1.13]])" color="" tags=""/>
        <species name="CO2" representation="Atoms('OCO', [[-1.163, 0, 0], [0, 0, 0], [1.163, 0, 0]])" color="" tags=""/>
        <species name="CO3" representation="Atoms('COOO',[[0.0, 0.0, 0.0], [0.0, 0.0, 1.28], [1.1085125168440815, 0.0, -0.64], [-1.1085125168440815, 0.0, -0.64]])" color="" tags=""/>
        <species name="COOH" representation="Atoms('COOH',[[0, 0, 0], [-1.0392304845413263, 0, 0.6], [1.1518137870333034, 0, 0.665], [0.9171495483016257, 0, 1.6061868544877167]])" color="" tags=""/>
        <species name="OH" representation="Atoms('OH',[[0.0, 0.0, 0.0], [0.0, 0.0, 0.97]])" color="" tags=""/>
        <species name="empty" representation="" color="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter name="A" value="(2.8892*angstrom)**2" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="CO2_diffuse" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="CO2_dissolve" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="CO3_diffuse" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="CO_diffuse" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="CO_dissolve" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="Ea_CO2_reduce" value="0.65" adjustable="True" min="-5.0" max="5.0" scale="linear"/>
        <parameter name="Ga_CO2_dissolve" value="0.049" adjustable="True" min="-1.0" max="1.0" scale="linear"/>
        <parameter name="Ga_CO2_undissolve" value="0.047" adjustable="True" min="-1.0" max="1.0" scale="linear"/>
        <parameter name="Ga_CO2_water_adsorb" value="0.094" adjustable="True" min="-1.0" max="1.0" scale="linear"/>
        <parameter name="Ga_CO2_water_desorb" value="0.021" adjustable="True" min="-1.0" max="1.0" scale="linear"/>
        <parameter name="OH_diffuse" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
        <parameter name="T" value="298.15" adjustable="True" min="100.0" max="700.0" scale="linear"/>
        <parameter name="deltaG_CO_dissolve" value="0.1" adjustable="True" min="-1.0" max="1.0" scale="linear"/>
        <parameter name="p_CO" value="0.01" adjustable="True" min="1e-10" max="100.0" scale="linear"/>
        <parameter name="p_CO2" value="1.0" adjustable="True" min="1e-10" max="100.0" scale="linear"/>
        <parameter name="reduce" value="1" adjustable="True" min="1e-10" max="10000000000.0" scale="linear"/>
    </parameter_list>
    <lattice cell_size="2.8892 0.0 0.0 0.0 26.0028 0.0 0.0 0.0 28.892000000000003" default_layer="tpb_line" substrate_layer="tpb_line" representation="">
        <layer name="tpb_line" color="#ffffff">
            <site pos="0.5 0.0 0.0" type="0_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.0 0.09090909090909091" type="0_1_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.18181818181818182" type="0_2_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.2727272727272727" type="0_3_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.36363636363636365" type="0_4_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.45454545454545453" type="0_5_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.5454545454545454" type="0_6_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.6363636363636364" type="0_7_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.7272727272727273" type="0_8_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.8181818181818182" type="0_9_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.0 0.9090909090909091" type="0_10_boundary" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.0" type="1_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.1 0.09090909090909091" type="1_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.18181818181818182" type="1_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.2727272727272727" type="1_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.36363636363636365" type="1_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.45454545454545453" type="1_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.5454545454545454" type="1_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.6363636363636364" type="1_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.7272727272727273" type="1_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.8181818181818182" type="1_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.1 0.9090909090909091" type="1_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.0" type="2_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.2 0.09090909090909091" type="2_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.18181818181818182" type="2_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.2727272727272727" type="2_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.36363636363636365" type="2_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.45454545454545453" type="2_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.5454545454545454" type="2_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.6363636363636364" type="2_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.7272727272727273" type="2_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.8181818181818182" type="2_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.2 0.9090909090909091" type="2_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.0" type="3_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.3 0.09090909090909091" type="3_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.18181818181818182" type="3_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.2727272727272727" type="3_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.36363636363636365" type="3_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.45454545454545453" type="3_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.5454545454545454" type="3_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.6363636363636364" type="3_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.7272727272727273" type="3_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.8181818181818182" type="3_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.3 0.9090909090909091" type="3_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.0" type="4_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.4 0.09090909090909091" type="4_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.18181818181818182" type="4_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.2727272727272727" type="4_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.36363636363636365" type="4_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.45454545454545453" type="4_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.5454545454545454" type="4_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.6363636363636364" type="4_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.7272727272727273" type="4_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.8181818181818182" type="4_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.4 0.9090909090909091" type="4_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.0" type="5_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.5 0.09090909090909091" type="5_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.18181818181818182" type="5_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.2727272727272727" type="5_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.36363636363636365" type="5_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.45454545454545453" type="5_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.5454545454545454" type="5_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.6363636363636364" type="5_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.7272727272727273" type="5_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.8181818181818182" type="5_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.5 0.9090909090909091" type="5_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.0" type="6_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.6 0.09090909090909091" type="6_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.18181818181818182" type="6_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.2727272727272727" type="6_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.36363636363636365" type="6_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.45454545454545453" type="6_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.5454545454545454" type="6_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.6363636363636364" type="6_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.7272727272727273" type="6_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.8181818181818182" type="6_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.6 0.9090909090909091" type="6_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.0" type="7_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.7 0.09090909090909091" type="7_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.18181818181818182" type="7_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.2727272727272727" type="7_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.36363636363636365" type="7_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.45454545454545453" type="7_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.5454545454545454" type="7_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.6363636363636364" type="7_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.7272727272727273" type="7_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.8181818181818182" type="7_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.7 0.9090909090909091" type="7_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.0" type="8_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.8 0.09090909090909091" type="8_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.18181818181818182" type="8_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.2727272727272727" type="8_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.36363636363636365" type="8_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.45454545454545453" type="8_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.5454545454545454" type="8_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.6363636363636364" type="8_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.7272727272727273" type="8_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.8181818181818182" type="8_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.8 0.9090909090909091" type="8_10_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.0" type="9_0_substrate" tags="" default_species="Ag"/>
            <site pos="0.5 0.9 0.09090909090909091" type="9_1_active" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.18181818181818182" type="9_2_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.2727272727272727" type="9_3_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.36363636363636365" type="9_4_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.45454545454545453" type="9_5_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.5454545454545454" type="9_6_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.6363636363636364" type="9_7_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.7272727272727273" type="9_8_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.8181818181818182" type="9_9_bulk" tags="" default_species="empty"/>
            <site pos="0.5 0.9 0.9090909090909091" type="9_10_bulk" tags="" default_species="empty"/>
        </layer>
    </lattice>
    <process_list>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_10_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_10_2_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_1_1_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_1_2_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_2_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_2_1_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_2_2_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_3_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_3_1_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_3_2_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_4_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_4_1_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_4_2_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_5_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_5_1_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_5_2_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_6_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_6_1_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_6_2_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_7_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_7_1_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_7_2_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_8_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_8_1_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_8_2_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_9_1_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_9_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_1_9_2_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_10_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_10_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_10_3_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_1_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_1_2_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_1_3_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_2_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_2_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_2_2_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_2_3_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_3_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_3_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_3_2_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_3_3_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_4_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_4_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_4_2_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_4_3_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_5_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_5_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_5_2_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_5_3_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_6_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_6_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_6_2_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_6_3_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_7_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_7_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_7_2_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_7_3_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_8_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_8_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_8_2_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_8_3_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_9_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_9_2_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_9_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_2_9_3_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_10_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_10_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_10_4_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_1_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_1_3_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_1_4_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_2_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_2_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_2_3_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_2_4_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_3_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_3_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_3_3_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_3_4_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_4_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_4_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_4_3_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_4_4_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_5_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_5_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_5_3_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_5_4_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_6_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_6_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_6_3_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_6_4_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_7_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_7_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_7_3_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_7_4_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_8_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_8_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_8_3_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_8_4_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_9_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_9_3_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_9_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_3_9_4_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_10_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_10_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_10_5_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_1_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_1_4_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_1_5_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_2_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_2_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_2_4_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_2_5_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_3_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_3_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_3_4_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_3_5_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_4_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_4_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_4_4_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_4_5_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_5_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_5_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_5_4_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_5_5_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_6_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_6_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_6_4_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_6_5_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_7_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_7_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_7_4_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_7_5_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_8_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_8_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_8_4_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_8_5_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_9_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_9_4_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_9_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_4_9_5_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_10_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_10_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_10_6_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_1_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_1_5_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_1_6_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_2_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_2_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_2_5_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_2_6_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_3_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_3_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_3_5_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_3_6_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_4_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_4_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_4_5_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_4_6_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_5_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_5_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_5_5_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_5_6_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_6_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_6_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_6_5_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_6_6_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_7_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_7_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_7_5_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_7_6_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_8_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_8_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_8_5_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_8_6_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_9_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_9_5_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_9_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_5_9_6_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_10_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_10_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_10_7_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_1_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_1_6_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_1_7_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_2_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_2_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_2_6_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_2_7_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_3_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_3_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_3_6_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_3_7_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_4_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_4_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_4_6_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_4_7_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_5_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_5_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_5_6_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_5_7_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_6_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_6_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_6_6_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_6_7_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_7_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_7_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_7_6_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_7_7_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_8_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_8_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_8_6_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_8_7_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_9_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_9_6_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_9_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_6_9_7_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_10_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_10_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_10_8_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_1_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_1_7_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_1_8_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_2_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_2_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_2_7_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_2_8_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_3_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_3_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_3_7_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_3_8_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_4_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_4_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_4_7_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_4_8_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_5_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_5_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_5_7_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_5_8_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_6_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_6_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_6_7_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_6_8_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_7_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_7_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_7_7_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_7_8_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_8_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_8_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_8_7_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_8_8_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_9_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_9_7_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_9_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_7_9_8_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_10_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_10_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_10_9_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_1_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_1_8_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_1_9_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_2_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_2_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_2_8_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_2_9_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_3_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_3_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_3_8_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_3_9_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_4_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_4_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_4_8_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_4_9_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_5_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_5_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_5_8_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_5_9_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_6_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_6_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_6_8_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_6_9_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_7_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_7_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_7_8_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_7_9_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_8_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_8_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_8_8_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_8_9_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_9_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_9_8_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_9_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_8_9_9_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_10_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_10_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_1_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_1_9_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_2_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_2_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_2_9_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_3_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_3_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_3_9_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_4_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_4_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_4_9_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_5_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_5_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_5_9_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_6_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_6_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_6_9_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_7_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_7_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_7_9_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_8_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_8_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_8_9_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_9_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_9_9_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_CO2_9_9_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_10_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_10_2_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_1_1_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_1_2_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_2_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_2_1_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_2_2_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_3_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_3_1_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_3_2_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_4_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_4_1_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_4_2_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_5_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_5_1_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_5_2_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_6_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_6_1_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_6_2_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_7_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_7_1_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_7_2_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_8_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_8_1_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_8_2_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_9_1_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_9_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_1_9_2_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_10_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_10_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_10_3_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_1_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_1_2_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_1_3_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_2_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_2_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_2_2_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_2_3_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_3_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_3_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_3_2_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_3_3_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_4_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_4_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_4_2_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_4_3_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_5_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_5_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_5_2_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_5_3_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_6_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_6_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_6_2_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_6_3_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_7_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_7_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_7_2_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_7_3_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_8_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_8_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_8_2_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_8_3_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_9_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_9_2_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_9_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_2_9_3_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_10_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_10_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_10_4_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_1_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_1_3_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_1_4_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_2_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_2_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_2_3_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_2_4_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_3_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_3_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_3_3_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_3_4_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_4_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_4_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_4_3_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_4_4_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_5_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_5_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_5_3_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_5_4_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_6_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_6_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_6_3_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_6_4_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_7_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_7_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_7_3_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_7_4_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_8_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_8_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_8_3_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_8_4_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_9_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_9_3_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_9_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_3_9_4_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_10_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_10_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_10_5_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_1_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_1_4_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_1_5_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_2_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_2_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_2_4_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_2_5_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_3_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_3_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_3_4_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_3_5_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_4_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_4_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_4_4_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_4_5_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_5_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_5_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_5_4_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_5_5_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_6_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_6_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_6_4_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_6_5_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_7_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_7_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_7_4_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_7_5_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_8_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_8_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_8_4_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_8_5_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_9_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_9_4_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_9_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_4_9_5_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_10_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_10_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_10_6_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_1_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_1_5_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_1_6_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_2_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_2_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_2_5_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_2_6_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_3_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_3_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_3_5_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_3_6_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_4_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_4_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_4_5_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_4_6_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_5_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_5_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_5_5_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_5_6_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_6_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_6_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_6_5_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_6_6_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_7_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_7_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_7_5_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_7_6_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_8_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_8_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_8_5_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_8_6_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_9_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_9_5_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_9_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_5_9_6_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_10_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_10_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_10_7_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_1_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_1_6_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_1_7_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_2_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_2_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_2_6_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_2_7_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_3_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_3_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_3_6_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_3_7_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_4_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_4_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_4_6_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_4_7_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_5_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_5_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_5_6_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_5_7_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_6_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_6_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_6_6_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_6_7_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_7_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_7_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_7_6_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_7_7_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_8_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_8_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_8_6_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_8_7_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_9_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_9_6_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_9_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_6_9_7_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_10_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_10_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_10_8_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_1_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_1_7_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_1_8_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_2_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_2_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_2_7_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_2_8_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_3_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_3_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_3_7_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_3_8_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_4_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_4_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_4_7_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_4_8_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_5_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_5_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_5_7_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_5_8_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_6_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_6_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_6_7_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_6_8_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_7_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_7_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_7_7_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_7_8_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_8_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_8_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_8_7_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_8_8_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_9_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_9_7_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_9_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_7_9_8_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_10_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_10_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_10_9_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_1_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_1_8_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_1_9_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_2_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_2_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_2_8_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_2_9_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_3_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_3_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_3_8_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_3_9_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_4_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_4_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_4_8_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_4_9_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_5_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_5_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_5_8_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_5_9_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_6_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_6_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_6_8_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_6_9_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_7_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_7_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_7_8_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_7_9_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_8_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_8_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_8_8_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_8_9_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_9_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_9_8_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_9_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_8_9_9_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_10_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_10_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_1_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_1_9_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_2_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_2_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_2_9_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_3_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_3_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_3_9_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_4_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_4_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_4_9_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_5_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_5_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_5_9_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_6_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_6_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_6_9_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_7_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_7_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_7_9_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_8_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_8_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_8_9_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_9_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_9_9_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_CO3_9_9_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_10_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_10_2_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_1_1_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_1_2_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_2_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_2_1_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_2_2_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_3_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_3_1_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_3_2_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_4_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_4_1_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_4_2_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_5_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_5_1_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_5_2_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_6_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_6_1_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_6_2_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_7_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_7_1_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_7_2_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_8_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_8_1_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_8_2_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_9_1_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_9_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_1_9_2_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_10_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_10_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_10_3_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_1_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_1_2_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_1_3_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_2_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_2_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_2_2_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_2_3_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_3_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_3_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_3_2_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_3_3_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_4_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_4_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_4_2_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_4_3_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_5_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_5_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_5_2_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_5_3_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_6_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_6_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_6_2_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_6_3_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_7_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_7_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_7_2_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_7_3_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_8_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_8_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_8_2_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_8_3_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_9_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_9_2_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_9_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_2_9_3_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_10_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_10_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_10_4_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_1_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_1_3_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_1_4_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_2_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_2_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_2_3_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_2_4_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_3_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_3_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_3_3_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_3_4_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_4_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_4_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_4_3_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_4_4_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_5_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_5_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_5_3_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_5_4_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_6_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_6_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_6_3_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_6_4_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_7_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_7_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_7_3_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_7_4_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_8_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_8_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_8_3_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_8_4_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_9_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_9_3_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_9_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_3_9_4_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_10_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_10_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_10_5_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_1_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_1_4_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_1_5_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_2_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_2_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_2_4_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_2_5_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_3_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_3_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_3_4_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_3_5_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_4_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_4_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_4_4_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_4_5_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_5_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_5_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_5_4_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_5_5_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_6_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_6_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_6_4_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_6_5_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_7_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_7_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_7_4_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_7_5_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_8_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_8_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_8_4_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_8_5_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_9_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_9_4_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_9_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_4_9_5_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_10_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_10_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_10_6_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_1_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_1_5_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_1_6_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_2_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_2_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_2_5_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_2_6_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_3_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_3_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_3_5_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_3_6_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_4_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_4_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_4_5_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_4_6_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_5_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_5_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_5_5_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_5_6_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_6_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_6_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_6_5_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_6_6_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_7_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_7_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_7_5_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_7_6_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_8_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_8_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_8_5_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_8_6_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_9_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_9_5_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_9_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_5_9_6_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_10_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_10_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_10_7_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_1_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_1_6_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_1_7_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_2_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_2_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_2_6_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_2_7_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_3_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_3_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_3_6_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_3_7_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_4_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_4_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_4_6_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_4_7_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_5_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_5_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_5_6_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_5_7_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_6_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_6_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_6_6_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_6_7_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_7_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_7_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_7_6_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_7_7_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_8_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_8_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_8_6_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_8_7_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_9_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_9_6_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_9_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_6_9_7_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_10_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_10_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_10_8_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_1_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_1_7_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_1_8_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_2_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_2_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_2_7_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_2_8_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_3_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_3_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_3_7_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_3_8_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_4_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_4_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_4_7_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_4_8_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_5_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_5_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_5_7_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_5_8_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_6_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_6_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_6_7_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_6_8_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_7_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_7_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_7_7_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_7_8_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_8_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_8_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_8_7_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_8_8_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_9_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_9_7_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_9_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_7_9_8_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_10_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_10_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_10_9_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_1_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_1_8_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_1_9_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_2_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_2_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_2_8_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_2_9_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_3_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_3_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_3_8_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_3_9_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_4_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_4_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_4_8_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_4_9_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_5_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_5_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_5_8_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_5_9_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_6_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_6_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_6_8_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_6_9_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_7_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_7_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_7_8_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_7_9_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_8_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_8_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_8_8_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_8_9_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_9_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_9_8_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_9_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_8_9_9_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_10_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_10_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_1_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_1_9_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_2_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_2_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_2_9_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_3_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_3_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_3_9_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_4_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_4_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_4_9_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_5_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_5_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_5_9_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_6_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_6_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_6_9_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_7_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_7_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_7_9_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_8_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_8_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_8_9_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_9_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_9_9_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_OH_9_9_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_1_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_2_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_3_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_4_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_5_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_6_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_7_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_8_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_from_9_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="1.92e-09/A*CO2_diffuse" name="diffuse_x_CO2_to_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_1_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_2_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_3_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_4_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_5_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_6_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_7_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_8_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_1" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_10" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_2" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_3" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_4" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_5" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_6" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_7" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_8" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_from_9_9" enabled="True">
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="9.55e-10/A*CO3_diffuse" name="diffuse_x_CO3_to_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="CO3" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_1_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_2_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_3_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_4_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_5_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_6_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_7_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_8_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_10" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_from_9_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_1_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_3_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_4_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_5_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_6_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_7_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_8_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_10_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_4_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_5_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_6_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_7_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_8_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="5.3e-09/A*OH_diffuse" name="diffuse_x_OH_to_9_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_9_bulk" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_dissolve*eV*beta)" name="dissolve_CO2_from_0_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ea_CO2_reduce*eV*beta)*reduce" name="reduction_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_1" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_2" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="2_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="2_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_3" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="3_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="3_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_4" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="4_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="4_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_5" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="5_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="5_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_6" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="6_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="6_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_7" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="7_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="7_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_8" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="8_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="8_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="0.01" name="reduction_rev_9" enabled="True">
            <condition species="OH" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <condition species="OH" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="9_1_active" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_2_bulk" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="9_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_1_active" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_10_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_2_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_3_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_4_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_5_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_6_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_7_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_8_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="10000000000000.0*exp(-Ga_CO2_undissolve*eV*beta)" name="undissolve_CO2_from_0_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <condition species="CO2" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="1_9_bulk" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_1" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_10" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_2" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_3" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_4" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_5" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_6" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_7" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_8" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve" name="water_adsorb_CO2_9" enabled="True">
            <condition species="empty" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <action species="CO2" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_1" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_1_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_10" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_10_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_2" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_2_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_3" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_3_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_4" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_4_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_5" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_5_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_6" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_6_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_7" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_7_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_8" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_8_boundary" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve" name="water_desorb_CO2_9" enabled="True">
            <condition species="CO2" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="tpb_line" coord_name="0_9_boundary" coord_offset="0 0 0"/>
        </process>
    </process_list>
    <output_list/>
    <connected_variables connected_variables_string="{'surroundingSitesDict': {}}"/>
</kmc>
"""
if __name__ == "__main__":
    #benchmark if kmc_settings.py is run without additional arguments, else call cli with additional argument provided.
    import sys
    if len(sys.argv) == 1:
        from kmcos import cli
        cli.main("benchmark")
    if len(sys.argv) == 2:
        from kmcos import cli
        cli.main(sys.argv[1])
