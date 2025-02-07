!------------------------------------------------------------------------------
! Input file for mc_single_arm 					11/15/2024
! NPS version - using pre-generated events
!------------------------------------------------------------------------------
        1       Spectrometer (1=HMS, 2=SHMS, 3=..)
     2200.0	Spectrometer momentum (in MeV/c)
     26.273	Spectrometer angle (in degrees)
    #  0.0        Horiz beam spot size in cm (Full width of +/- 3 sigma)
    #  0.0        Vert  beam spot size in cm (Full width of +/- 3 sigma)
     10.0	Thickness of target (Full width, cm)
    #  0.0        Raster full-width x (cm)
    #  0.0        Raster full-width y (cm)
     890.5	one radiation length of target material (in cm)
    #  0.0        Beam x offset (cm)  +x = beam left
    #  0.0	Beam y offset (cm)  +y = up
    #  0.0        Target z offset (cm)+z = downstream (0.25)
     0.0        Spectrometer x offset (cm) +x = down
     0.0        Spectrometer y offset (cm)
     0.0        Spectrometer z offset (cm)
     1.1        Spectrometer xp offset (mr)
     0.0        Spectrometer yp offset (mr)
     0		particle identification :e=0, p=1, d=2, pi=3, ka=4
     1		flag for multiple scattering
     1		flag for wire chamber smearing
     1	        flag for storing all events (including failed events with stop_id > 0)