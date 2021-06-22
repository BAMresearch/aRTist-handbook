BAM CT File Format
==================

Header Size and Data Offset
---------------------------

A BAM CT file starts with a 512 bytes long header. This header may be followed by zero-padding until the actual data block. The beginning of the **image data block** is located at a multiple of the size of a pixel row (in bytes). If a pixel row needs at least 512 bytes, the data offset can be calculated by

	data offset = (number of columns) × (bytes per pixel).

If this data offset is smaller than the significant header size of 512 bytes, the data offset will instead be the smallest multiple of the above-shown row length in bytes:

	data offset = N × (number of columns) × (bytes per pixel)

with the smallest N that leads to a data offset ≥ 512.

For example, if you have X-ray projections with 1000 pixel columns and 16 bit grey values (i.e. 2 bytes per pixel), the data offset will be at
	
	data offset = 1000 px × 2 bytes/px = 2000 bytes.


Byte Order
----------

Any header or image data unit that is stored in more than 1 byte can be either written in *big-endian byte order* or in *little-endian byte order*. Since today's CPUs usually operate in little-endian mode, this is the byte order that BAM CT files generated with *aRT*\ ist use.


File Name
---------

The BAM CT header starts with 12 bytes that contain a "file name" (a string of twelve 1-byte characters, not null-terminated). It follows a structure that reveals additional information:

* character 0 to 6: arbitrary name
* character 7: must be a dot :code:`.`
* character 8: content type

	- :code:`d` for projection data
	- :code:`b` for tomograms ("Bild")

* character 9: CT device code (a BAM internal ID)
* character 10: image data type:

	- :code:`c`: 8 bit unsigned int
	- :code:`s`: 16 bit unsigned int
	- :code:`i`: 32 bit unsigned int
	- :code:`r`: 32 bit float (real)

* character 11: byte order:

	- :code:`s`: little endian
	- :code:`x`: big endian


Header Data
-----------

The following table lists the elements of a BAM CT header.

.. note:: The element at **offset 12 (0xC)** represents one of the following:

	* **tomograms:** the number of rows in an image
	* **projections:** (number of rows) × (number of angular steps)

====  =====  =====  ============  =====================================================
Byte  (hex)  Count  Data Type     Description
====  =====  =====  ============  =====================================================
0     0x00   12     8 bit char    File name, see above
12    0x0C   1      32 bit uint   Number of rows (X) or rows × angular steps, see above
16    0x10   1      32 bit uint   Number of columns (Y)
20    0x14   1      32 bit uint   Number of angular steps
24    0x18   1      32 bit int    Number of angular steps up to 180°
28    0x1C   1      32 bit uint   Number of slices (Z)
32    0x20   1      32 bit uint   Number of translations
36    0x24   1      32 bit uint   Number of intermediate angles
40    0x28   1      32 bit uint   Number of margin points
44    0x2C   1      32 bit uint   Number of detectors
48    0x30   1      32 bit uint   Bytes per pixel
52    0x34   1      32 bit uint   Number of diodes per detector
56    0x38   6      32 bit uint   *Reserved*
80    0x50   1      32 bit float  Minimum attenuation coefficient [1/cm]
84    0x54   1      32 bit float  Maximum attenuation coefficient [1/cm]
88    0x58   1      32 bit float  Total number of photons
92    0x5C   1      32 bit float  Measurement time per point [s]
96    0x60   1      32 bit float  Velocity number
100   0x64   1      32 bit float  Start angle
104   0x68   1      32 bit float  Scan centre point [mm] (horizontal position)
108   0x6C   1      32 bit float  Scan length without ramp [mm]
112   0x70   1      32 bit float  Sampling step size [mm] (horizontal)
116   0x74   1      32 bit float  Stage elevation [mm] (vertical position)
120   0x78   1      32 bit float  Elevation increment [mm]
124   0x7C   1      32 bit float  Source-object distance SOD [mm]
128   0x80   1      32 bit float  Source-detector distance SDD [mm]
132   0x84   1      32 bit float  Source elevation [mm] (vertical position)
136   0x88   1      32 bit float  Source centre [mm] (horizontal position)
140   0x8C   1      32 bit float  Source distance [mm] (magnificational position)
144   0x90   1      32 bit float  Detector elevation [mm] (vertical position)
148   0x94   1      32 bit float  Detector centre [mm] (horizontal position)
152   0x98   1      32 bit float  Detector distance [mm] (magnificational position)
156   0x9C   1      32 bit float  Spacer elevation [mm] (thickness)
160   0xA0   1      32 bit float  Object weight [kg]
164   0xA4   1      32 bit float  Beam elevation [mm]
168   0xA8   1      32 bit float  Collimator width [mm]
172   0xAC   1      32 bit float  Collimator height [mm]
176   0xB0   1      32 bit float  Angular separation of detectors [deg]
180   0xB4   1      32 bit float  PCD clear time per point [s]
184   0xB8   1      32 bit float  Density correction factor [g/cm]
188   0xBC   1      32 bit float  ROI centre [mm]
192   0xC0   1      32 bit float  ROI distance [mm]
196   0xC4   1      32 bit float  *Reserved*
200   0xC8   8      8 bit char    Source type
208   0xD0   8      8 bit char    Source energy
216   0xD8   8      8 bit char    Source intensity
224   0xE0   8      8 bit char    Detector type
232   0xE8   80     8 bit char    Sample name
312   0x138  4      8 bit char    Program ID
316   0x13C  16     8 bit char    Measurement start time (TT.MM.JJJJ/hh:mm)
332   0x14C  16     8 bit char    Measurement stop time (TT.MM.JJJJ/hh:mm)
348   0x15C  16     8 bit char    Time and date of last edit (TT.MM.JJJJ/hh:mm)
364   0x16C  12     8 bit char    Look Up Table File 1
376   0x178  12     8 bit char    Look Up Table File 2
388   0x184  12     8 bit char    Look Up Table File 3
400   0x190  12     8 bit char    Tube filter
412   0x19C  96     8 bit char    Processing steps
508   0x1FC  4      8 bit char    Reserved
512   0x200                       Data or zero-padding until data offset, see above
====  =====  =====  ============  =====================================================
