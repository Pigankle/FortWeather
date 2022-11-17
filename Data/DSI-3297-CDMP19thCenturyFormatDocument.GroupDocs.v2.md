

**DSI-3297**

**CDMP COOP SUMMARY OF THE DAY FORTS**

**Version 1.1**

**Prepared by**

**Karen Andsager**

**Michael C. Kruk**

**Michael L. Spinar**

**Leslie Stoecker**

**Midwestern Regional Climate Center**

**2204 South Griffith Avenue**

**Champaign, Illinois 61820**

**March 2010**

This document was prepared by the U.S. Department of Commerce, National Oceanic

and Atmospheric Administration, National Environmental Satellite Data and

Information Service, Midwestern Regional Climate Center, Champaign, Illinois, and

the National Climatic Data Center, Asheville, North Carolina.

This document is designed to provide general information on the current, origin,

format, integrity and the availability of this data file.

Errors found in this document should be brought to the attention of the Data Base

Administrator, NCDC. See topic 58 for a summary of this data set.

1





Table of Contents

Page

Number

Topic

INTRODUCTORY TOPICS

\1. Data Set ID................................................4

\2. Data Set Name..............................................4

\3. Data Set Aliases...........................................4

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DESCRIPTION

\4. Access Method and Sort for Archived Data...................4

\5. Access Method and Sort for Supplied Data...................8

\6. Element Names and Definitions.............................10

\7. Start Date................................................17

\8. Stop Date.................................................17

\9. Parameter.................................................17

\10. Discipline................................................17

\11. Coverage..................................................17

\12. Location..................................................18

\13. Keyword...................................................18

\14. Storage Medium............................................18

\15. File Mode.................................................18

\16. How to Acquire the Data...................................18

\17. Historical and Current Data Sources.......................18

\18. Data Derivation, Algorithms...............................19

\19. Data Derivation Algorithms, Responsibility for............19

\20. Project...................................................19

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DATA CENTER

\21. Data Center, Archiving ...................................19

\22. Data Center, Originating .................................19

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PERSONNEL

\23. Archiver..................................................19

\24. Technical Contact.........................................19

\25. Investigator..............................................19

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SENSORS

\26. Sensor Name and Operating Principles......................19

\27. Sensor Siting.............................................20

\28. Sensor Accuracy and Calibration...........................20

\29. Sensor Sampling Characteristics...........................20

\30. Data Capture Method at/near Sensor........................20

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

STATIONS

\31. Station Location Accuracy.................................20

\32. Station Observation Schedule..............................20

\33. Station Data Time Averaging...............................20

\34. Station Groupings, using Spatial Sampling.................20

\35. Network Participation.....................................20

\36. Geographical Criteria for Selecting Stations..............21

\37. Geographical Distribution.................................21

\38. Elevation Distribution....................................21

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DATA QUALITY

\39. Instrument Problems.......................................21

\40. Missing Data Periods......................................21

2





\41. Sampling Biases...........................................21

\42. Error Detection and Correction............................21

\43. Missing Value Estimates...................................22

\44. Quality Control Responsibility............................22

\45. Known Uncorrected Problems................................22

\46. Confidence Factors........................................22

\47. History of Data Usage.....................................22

\48. Quality Statement.........................................22

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DATES

\49. Revision Date.............................................22

\50. Science Review Date.......................................22

\51. Future Review Date........................................23

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

OTHER DATA SETS

\52. Input Sources to this Data Set............................23

\53. Essential Companion Data Sets.............................23

\54. Derived from this Data Set................................23

\55. Larger Collections........................................23

\56. Similar Data Sets.........................................23

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SUMMARIZATION

\57. Reference.................................................23

\58. Summary...................................................23

Glossary.......................................................24

Appendix A. Digitization of Historical Daily Cooperative Network Data

Appendix B. Documentation of Problems with and Changes Made to Keyed Data

3





**1. Data Set ID:**

CDMP-Forts

**2. Data Set Name:**

COOP Summary of the Day – CDMP – 1700s and 1800s Forts and Other Voluntary

Observers

**3. Data Set Aliases:**

Surface Land Daily Cooperative Data

Summary of the Day Data

Co-op Data

Climatological Data

Daily Weather Data

SOD

**4. Access Method and Sort for Archived Data:**

Data are archived in a variable length element file structure. The element

file structure is designed to allow maximum flexibility in requesting data.

Only those elements or groups of elements of particular interest need be

ordered. Archived data are currently sorted by Station-ID (excluding the

Division Number) as the primary key and year, month, and meteorological

element-type as secondary keys.

NCDC maintains an extensive digital collection of historical global, climatic

archives from surface, oceanic, and satellite sources. Like types of

meteorological data are categorized into "Tape Deck (TD) families". For

instance: the TD-5600 series contains upper air data; the 1100 series contains

marine data, the 9700 series contains model analysis data, etc.

In the early 1980's NCDC instituted the 'element file structure' in an effort

to standardize the archival of meteorological data. The 3200 series utilizes

the element file structure to assimilate surface weather information.

The record structure as shared by the TD-32XX records (where "XX" denotes any

one of a particular TD series) may be generalized as two distinct "portions".

These portions are as follows:

The contents of the first portion are essentially 'fixed' as it contains

information used to describe the remainder of the record. By its design, the

second portion allows for a logical maximum of 100 data values; nonetheless,

the actual "maximum" varies with the TD series. For example, in the daily

data series the actual maximum is 62; in the monthly data it is 26; in the

minute data it is 60, etc. In this respect, this portion is termed as

"variable"; consequently, the entire record is also of variable length.

Data may also be received in a fixed length record structure described in

topic 5 "Description: Access Method and Sort for Supplied Data".

Provided within this section are information and examples of how to access the

Variable Length data records, specifically:

a. COBOL Data Description (1 example)

b. FORTRAN Data Descriptions (2 examples)

c. Control Language Notes

d. List of Variables ("Elements")

4





e. Schematic Variable Length Record Format Layout

The following COBOL and FORTRAN statements are to be used as guidelines only.

NCDC recognizes the fact that many different types of equipment are used in

processing these data. It is impossible to cover all the idiosyncrasies of

every system.

**a. COBOL Data Description**

This is a typical ANSI Standard COBOL Variable Length Description.

FD INDATA

LABEL RECORDS ARE STANDARD

RECORDING MODE D

BLOCK CONTAINS 12000 CHARACTERS

DATA RECORD IS DATA-RECORD.

01 DATA-RECORD.

02 RECORD-TYPE

02 STATION-ID

02 ELEMENT-TYPE

02 ELEMENT-UNITS-CODE

02 YEAR

PIC X(3).

PIC X(8).

PIC X(4).

PIC XX.

PIC 9(4).

PIC 99.

02 MONTH

02 FILLER

02 NUMBER-VALUES

02 DAILY-ENTRY

PIC 9(4).

PIC 9(3).

OCCURS 1 TO 100 TIMES DEPENDING ON NUMBER-VALUES.

04 DAY

PIC 99.

04 HOUR

PIC 99.

04 DATA-VALUE

PIC S9(5) SIGN LEADING

SEPARATE.

04 D-VAL REDEFINES DATA-VALUE.

05 SIGN-VAL

05 DATA-IN

PIC X.

PIC X(5).

PIC X.

04 FLAG-1

04 FLAG-2

PIC X.

**b. FORTRAN Data Description**

(1) FORTRAN 77 Example 1

This description is for those systems that can handle variable blocked records

normally.

IMPLICIT INTEGER (A-Z)

OPEN (10,FILE = 'FILENAME',ACCESS = 'SEQUENTIAL', STATUS = 'OLD',

\+

\+

RFORM = 'VB',MRECL = 1230,TYPE = 'ANSI',BLOCK =

\12000)

LAST 2 lines of OPEN statement are SPERRY UNIQUE

C

DEFINE FILE 10 (ANSI, VB, 1230, 12000)

CHARACTER\*3 RECTYP

CHARACTER\*8 STNID

CHARACTER\*4 ELMTYP

CHARACTER\*2 EUNITS

CHARACTER\*1 FLAG1, FLAG2

5





DIMENSION IDAY(100), IHOUR(100), IVALUE(100), FLAG1(100),

FLAG2(100)

\+

10 READ (10,20,END=999,ERR=10) RECTYP, STNID, ELMTYP, EUNITS,

IYEAR,

\+

\+

IMON, IFIL, NUMVAL, (IDAY(J), IHOUR(J), IVALUE(J),

FLAG1(J), FLAG2(J), J=1, NUMVAL)

20 FORMAT (A3, A8, A4, A2, I4, I2, I4, I3, 100(2I2, I6, 2A1))

(2) FORTRAN 77 Example 2

This description is for those systems that can't handle variable blocked

records normally.

PROGRAM TAPEREAD

IMPLICIT INTEGER (A-Z)

.....

OPEN(1,FILE=TAPE:',ACCESS='SEQUENTIAL',FORM=FORMATTED',

\+ STATUS='OLD',READONLY)

CHARACTER BUFFER\*12000

! YOUR MACHINE MUST SUPPORT

! CHARACTER VARIABLES THIS LARGE

CHARACTER\*3 RECTYP

CHARACTER\*8 STNID

CHARACTER\*4 ELMTYP

CHARACTER\*2 EUNITS

CHARACTER\*1 FLAG1, FLAG2

DIMENSION IDAY(100), IHOUR(100), IVALUE(100), FLAG1(100)

FLAG2(100)

.....

\+

NBYTES=0

NBEG=1

READ(1,101,END=99)BUFFER

NBEG=NBEG+NBYTES

5

!READ IN PHYSICAL RECORD (BLOCK)

10

READ(BUFFER(NBEG:NBEG+3,102)NBYTES !READ THE CONTROL WORD

IF( NBYTES.EQ.0 )GO TO 5

READ(BUFFER(NBEG+4:NBEG+NBYTES-1),103) RECTYP, STNID, ELMTYP,

\+ EUNITS, 1YEAR, IMON, IFIL, NUMVAL, (DAY(J), IHOUR(J),

\+ IVALUE(J), FLAG1(J), FLAG2(J), J=1, NUMVAL)

.....

.....

GO TO 10

99

CONTINUE

.....

.....

STOP 'FINISHED'

101

102

103

FORMAT(A)

FORMAT(I4)

FORMAT (A3, A8, A4, A2, I4, I2, I4, I3, 100(212, 16, 2A1))

END

**c. Control Language Notes**

(1) IBM JCL Notes

For ASCII Variable specify:

LRECL = 1234

RECFM = DB

6





OPTCODE = Q

For EBCDIC Variable specify:

LRECL = 1234

RECFM = VB

(2) VAX DCL Notes

$ MOUNT/FOREIGN/BLOCKSIZE=12000 MT: tapename TAPE:

**d. List of Variables**

ELEMENT

001 RECORD TYPE (= DLY)

002 STATION ID

003 METEOROLOGICAL ELEMENT TYPE

004 MET. ELEMENT MEASUREMENT UNITS CODE

005 YEAR

WIDTH

POSITION

3

8

4

2

4

001-003 **--**

004-011 **|**

012-015 **|**

016-017 -- ID

018-021 **|**

PORTION

006 MONTH

007 AMOUNT OF TIME BETWEEN MEASUREMENTS

008 FILLER (= 99)

009 NUMBER OF DATA PORTIONS THAT FOLLOW

010 DAY OF MONTH

011 HOUR OF OBSERVATION

012 SIGN OF METEOROLOGICAL ELEMENT VALUE

VALUE OF METEOROLOGICAL ELEMENT

PORTION

2

2

4

3

2

2

1

5

022-023 **|**

024-025 **|**

026-027 **|**

028-030 **--**

031-032 **--**

033-034 **|**

035

036-040 **|**

**--** DATA

QUALITY CONTROL FLAG 1

QUALITY CONTROL FLAG 2

1

1

041

042

**|**

**--**

DATA GROUPS IN THE SAME FORM AS ELEMENT 12

PORTION

POSITIONS 31-42 REPEATED AS MANY

PORTION

TIMES AS NEEDED TO CONTAIN ONE MONTH

PORTION

043-054 DATA

055-066 DATA

067-078 DATA

12

12

OF RECORDS.

.....

12

.....

1219-1230 DATA

608

PORTION

**e. Format (Variable Length Record Layout)**

\1. The first eight elements (positions 001-030) constitute the ID PORTION

of the record and describe the characteristics of the entire record. The next

six elements, the DATA PORTION of the record contains information about each

meteorological element value reported. This portion is repeated for as many

values as occur in the monthly record.

\2. Each logical record is of variable length with a maximum of 1230

characters. Each logical record contains a station's data for a specific

meteorological element over a one-month interval. The form of a record is:

ID PORTION (30 Characters) Fixed length

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**\*** REC **|** STATION **|** ELEM **|**

**|**

**|**

**|**

**|**

**|** NUM >

**\*** TYP **|** ID **|** TYPE **|** UNT **|** YEAR **|** MO **| DUR |** FILL **|** VAL >

**\*\*\*\*\*\*|\*\*\*\*\*\*\*\*\*\*|\*\*\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*\*|\*\*\*\*\*\***

7





**\*** XXX **|** XXXXXXXX **|** XXXX **|** XX **|** XXXX **|** XX **|** XX **|** XX **|** XXX **>**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS 001

002

003 004

005 006 007

008 009

DATA PORTION (12 Characters, repeated "NUM-VAL" times--up to 100)

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**<** DY **|** HR **|** MET. ELEM **|** FL **|** FL **|** DY **|** HR **|** MET. ELEM **|** FL **|** FL **>**

**<**

**<**

**<**

**<**

**|**

**|**

**|**

**|**

**|**

**|** 1 **|** 2 **|**

**|**

**|**

**|**

**|**

**|**

**|** 1 **|** 2 **>**

**|\*\*\*\*\*\*\*\*\*\*\*\*|**

**|** DATA **|**

**|** S **|** VALUE **|**

**|**

**|**

**|**

**|**

**|**

**|**

**|\*\*\*\*\*\*\*\*\*\*\*\*|**

**|** DATA **|**

**|** S **|** VALUE**|**

**|**

**|**

**|**

**>**

**>**

**>**

**|**

**|**

**<\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*\*| \*\*\*\*\*|\*\*\*\*|\*\*\* >**

**<** XX **|** XX **|** X **|** XXXXX **|** X **|** X **|** XX **|** XX**|** X **|** XXXXX**|** X **|** X **>**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS 010 011 012 013

014 015 016 017 018

019 020 021

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**<** DY **|** HR **|** MET. ELEM **|** FL **|** FL **\***

**<**

**<**

**<**

**<**

**|**

**|**

**|**

**|**

**|**

**|** 1 **|** 2 **\***

**|\*\*\*\*\*\*\*\*\*\*\*|**

**| |** DATA **|**

**|** S **|** VALUE **|**

**|**

**|**

**|**

**\***

**\***

**\***

**<\*\*\*\*|\*\*\*\*|\*\*\*|\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*\***

**<** XX **|** XX **|** X **|** XXXXX **|** X **|** X **\***

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS 604 605 606 607

608 609

\3. The Number of Data Portions (position 009) for the logical record of

type "DLY" ranges from 1 to 62.

**5. Access Method and Sort for Supplied Data:**

In addition to a variable length record structure, users may also receive data

in a fixed length record structure as described below. However, the user must

specify whether to extract either the original or edited data values. Supplied

data are in the same sort as archived data (see topic 4 "Description: Access

Method and Sort for Archived Data").

Provided within this section are information and examples of how to access the

fixed length data records, specifically:

a. COBOL Data Description

b. FORTRAN Data Description

c. List of Variables ("Elements")

d. Schematic Fixed Length Record Format Layout

**a. COBOL Data Description**

This is a typical ANSI Standard COBOL Fixed Record Length Description

8





FD INDATA

LABEL RECORDS ARE STANDARD (FOR STD LABEL TAPES)

RECORDING MODE F

BLOCK CONTAINS 15 RECORDS

DATA IS DATA-RECORD

01 DATA RECORD

02 RECORD-TYPE

02 STATION-ID

02 ELEMENT-TYPE

02 ELEMENT-UNITS

02 YEAR

02 MONTH

02 FILLER

02 NUMBER-VALUES

02 DAILY-ENTRY

OCCURS 31 TIMES.

04 DAY

PIC X(3).

PIC X(8).

PIC X(4).

PIC XX.

PIC 9(4).

PIC 99.

PIC 9(4).

PIC 9(3).

PIC 99.

PIC 99.

04 HOUR

04 DATA-VALUE

04 D-VAL REDEFINES DATA-VALUE.

05 SIGN-VAL

05 DATA-IN

04 FLAG-1

PIC S9(5) SIGN LEADING SEPARATE.

PIC X.

PIC X(5).

PIC X.

04 FLAG-2

**b. FORTRAN Data Description**

FORTRAN 77 Example

PIC X.

DEFINE FILE 10 (ANSI, FB, 402, 6030)

CHARACTER\*3 RECTYP

CHARACTER\*8 STNID

CHARACTER\*4 ELMTYP

CHARACTER\*2 EUNITS

CHARACTER\*1 FLAGI, FLAG2

DIMENSION IDAY(31), IHOUR(31),

\+ IVALUE(31), FLAG1(31), FLAG2(31)

10 READ (10,20,END=999,ERR=10)RECTYP, STNID, ELMTYP, EUNITS, IYEAR,

\+

\+

IMON, IFIL, NUMVAL, (IDAY(J), IHOUR(J), IVALUE(J),

FLAG1(J), FLAG2(J), J=1, 31)

20 FORMAT (A3, A8, A4, A2, I4,I2, I4, 13, 31(212, I6, 2A1))

**c. List of Variables**

ELEMENT

001 RECORD TYPE (= DLY)

002 STATION ID

003 METEOROLOGICAL ELEMENT TYPE

004 MET. ELEMENT MEASUREMENT UNITS CODE

005 YEAR

006 MONTH

007 AMOUNT OF TIME BETWEEN MEASUREMENTS

008 FILLER (= 99)

WIDTH POSITION

3

8

4

2

4

2

2

2

001-003**--**

004-011 **|**

012-015 **|**

016-017 **|--**ID

018-021 **|** PORTION

O22-023 **|**

024-025 **|**

026-027 **|**

028-030**--**

009 NO. OF DATA PORTIONS THAT FOLLOW (= 031) 3

010 DAY OF MONTH

2

031-032**--**

9





011 HOUR OF OBSERVATION

2

1

5

1

1

033-034 **|** DATA

012 SIGN OF METEOROLOGICAL ELEMENT VALUE

VALUE OF METEOROLOGICAL ELEMENT

QUALITY CONTROL FLAG 1

035

**|--**PORTION

036-040 **|**

041

042

**|**

QUALITY CONTROL FLAG 2

**--**

DATA GROUPS IN THE SAME FORM AS ELEMENT 12

043-054 DATA PORTION

055-066 DATA PORTION

.....

POSITIONS 31-42 ARE REPEATED

31 TIMES.

12

.....

12

194

391-402 DATA PORTION

**d. Format (Fixed Length Record Layout)**

\1. The first eight elements (positions 001-030) constitute the ID PORTION

of the record and describe the characteristics of the entire record. The next

six elements, the DATA PORTION of the record, contain information about each

meteorological element value, reported. This portion is repeated 31 times.

\2. Each logical record is fixed with 402 characters. Each logical record

contains a station's data for a specific meteorological element over a one

month interval. The form of a record is:

ID PORTION (30 characters) Fixed Length

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**\*** REC **|** STATION **|** ELEM **|**

**|**

**|**

**|**

**|**

**|** NUM >

**\*** TYP **|** ID **|** TYPE **|** UNT **|** YEAR **|** MO **| DUR |** FILL **|** VAL >

**\*\*\*\*\*\*|\*\*\*\*\*\*\*\*\*\*|\*\*\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*\*|\*\*\*\*\*\***

**\*** XXX **|** XXXXXXXX **|** XXXX **|** XX **|** XXXX **|** XX **|** XX **|** XX **|** XXX **>**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS 001

002

003 004

005 006 007

008 009

DATA PORTION (12 Characters, repeated 31 Times)

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**<** DY **|** HR **|** MET. ELEM **|** FL **|** FL **|** DY **|** HR **|** MET. ELEM **>**

**<**

**<**

**<**

**|**

**|**

**|**

**|\*\*\*\*\*\*\*\*\*\*\*|**

**| |** DATA **|**

**|** S **|** VALUE **|**

**|**

**|**

**|**

**|**

**|**

**|**

**|**

**|**

**|**

**|\*\*\*\*\*\*\*\*\*\* >**

**| |** DATA >

**|** S **|** VALUE >

**< \*\*\*|\*\*\*\*|\*\*\*\*\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*\*|\*\*\*|\*\*\*\*\*\* >**

**<** XX **|** XX **|** X ***|*** XXXXX **|** X **|** X **|** XX **|** XX | X | XXXXX **>**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS

010 011 012 013

014 015 016 017 018 019

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**<** DY **|** HR **|** MET. ELEM **|** FL **|** FL **\***

<

**<**

**<**

**|**

**|**

**|**

**|\*\*\*\*\*\*\*\*\*\*\*|** 1 **|** 2 **\***

**| |** DATA **|**

**|** S **|** VALUE **|**

**|**

**|**

**\***

**\***

**< \*\*\*|\*\*\*\*|\*\*\*|\*\*\*\*\*\*\*|\*\*\*\*|\*\*\*\*\***

**<** XX **|** XX **|** X **|** XXXXX | X **|** X **\***

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

ELEMENTS

190 191 192 193

194 195

**6. Element Names and Definitions**:

10





RECORD TYPE

The type of data stored in this record. (Value is "DLY"). Each record

contains one month of daily values.

STATION-ID

This 8-character alphanumeric station identifier is assigned by the National

Climatic Data Center. The first two digits refer to a state code (value range

is 01-91; reference Table "A"). The next four digits refer to the Cooperative

Network Index number (value range is 0001-9999). The last two digits are the

Cooperative Network Division Number (value range is 01-10; 99 = Missing

Division Number; reference Table "B").

METEOROLOGICAL ELEMENT-TYPE

The type of meteorological elements stored in this record. Range of values is

listed below.

BARP

Barometric pressure, unadjusted instrument reading. Unit

Measurement, Thousandths of Inches of Mercury.

BPTI

Barometric pressure, instrument reading adjusted for temperature and

instrument correction. Unit Measurement, Thousandths of Inches of

Mercury.

BPSL

Barometric pressure, instrument reading adjusted for temperature and

instrument correction and reduced to sea level. Unit Measurement,

Thousandths of Inches of Mercury.

CLSK

Clearness of sky, on a scale of 0-10, with clear sky being 10, and

cloudy being 0.

CLDL, CLDU

Cloud direction of motion. CLDL for lower clouds; CLDU for upper

clouds. Unit Measurement, Whole Degrees.

CLTL, CLTU

Cloud type (reference Table "C"). CLTL for lower clouds; CLTU for

upper clouds.

CLVL, CLVU

Cloud velocity – speed component. CLVL for lower clouds; CLVU for

upper clouds. Unit Measurement, Whole Miles per Hour.

DPTP

Dew point temperature. Unit Measurement, Hundredths of Degrees

Fahrenheit.

DPTD

11





Dew point temperature depression. Unit Measurement, Hundredths of

Degrees Fahrenheit.

DYSW

Daily occurrence of weather, including all different types of weather

occurring that day (reference Table "D").

MNTP

Mean daily temperature, for 24-hour period ending at observation

time. Generally, this mean is calculated from the average of the

maximum and minimum daily temperatures, when available. See Section

33 – Station Data Time Averaging. Unit Measurement, Hundredths of

Degrees Fahrenheit.

MNTO

Mean daily temperature, for 24-hour period ending at observation

time. Generally, this mean is calculated from the average of three

point measurements of the temperature observed over the course of the

24-hour period. See Section 33 – Station Data Time Averaging. Unit

Measurement, Hundredths of Degrees Fahrenheit.

PTYP

Precipitation type (reference Table "E").

PRCP

Daily precipitation. Trace is less than 0.005 inch. Unit

Measurement, Hundredths of Inches.

RGHT

River gauge height, or height of other body of water. Point

measurement at time of observation. Unit Measurement, Tenths of

Feet.

RGHC

Daily change in river gauge height, or height of other body of water.

Change ending at time of observation. Unit Measurement, Tenths of

Feet.

RHUM

Relative Humidity. Point measurement at the time of observation.

Unit Measurement, Whole Percent.

SKYL, SKYU

Daily cloudiness. SKYL for measurement of lower clouds; SKYU for

measurement of upper clouds. Clear is zero coverage of the sky by

clouds; “10” is completely cloudy. Unit Measurement, Scale of 0-10.

This element was sometimes recorded on a scale of 0-4; when this is

occurred is not indicated in the daily data at this time.

12





SMEL

Water equivalent of melted snowfall. Trace is less than 0.05 inch.

Unit Measurement, Hundredths of Inches.

SNOW

Daily snowfall. Sleet and hail may or may not be included in the

snowfall measurement, depending on the general and specific observer

practices of the time. Trace is less than 0.05 inch. Unit

Measurement, Hundredths of Inches.

SNWD

Snow depth at observation time. Snow depth is depth of snow on the

ground at time of observation. Trace is depth less than 0.5 inch.

Unit Measurement, Tenths of Inches.

STWX

State of the weather at time of observation (reference Table "D").

TAHR

Temperature measurement. Point measurement at time of observation.

Unit Measurement, Hundredths of Degrees Fahrenheit.

TBAR

Temperature measurement using thermometer attached to barometer.

Used to adjust barometer reading for temperature. Unit Measurement,

Hundredths of Degrees Fahrenheit.

TMAX

Daily maximum temperature. Maximum temperature reading for 24 hours

ending at time of observation. Unit Measurement, Hundredths of

Degrees Fahrenheit.

TMIN

Daily minimum temperature. Minimum temperature reading for 24 hours

ending at time of observation. Unit Measurement, Hundredths of

Degrees Fahrenheit.

TMPD

Dry bulb temperature. Point measurement at time of observation.

Unit Measurement, Hundredths of Degrees Fahrenheit.

TMDW

Wet bulb temperature. Point measurement at time of observation.

Unit Measurement, Hundreths of Degrees Fahrenheit.

13





TPBG, TPEN

Time of beginning and ending of precipitation. TPBG and TPEN for

time of beginning and ending for 24-hour observation of precipitation

events (one time of beginning and ending within each 24-hour period).

Unit Measurement, Hour and Minutes, AM/PM indicator (reference Table

"F").

TRNG

Daily temperature range. Maximum temperature minus minimum

temperature. Unit Measurement, Whole Degrees Fahrenheit.

TWAR

Surface air temperature observed at location of water temperature

observation. Unit Measurement, Hundredths of Degrees Fahrenheit.

TWBT

Bottom water temperature. Unit Measurement, Hundredths of Degrees

Fahrenheit.

TWDP

Depth of water for TWBT – bottom water temperature observation. Unit

Measurement, Tenths of Feet.

TWSR

Surface water temperature. Unit Measurement, Hundredths of Degrees

Fahrenheit.

WD16

Prevailing wind direction. Unit Measurement, 8-Point or 16-Point

Compass Directions, Expressed as Whole Degrees (Calm is “0”, North is

“360”, Changing or Variable is “991”).

WDDM

Maximum wind direction. Unit Measurement, 8-Point or 16-Point

Compass Directions, Expressed as Whole Degrees (Calm is “0”, North is

“360”, Changing or Variable is “991”).

WDFC

Prevailing wind force. Unit Measurement, Scale of 0-10 or Scale of

0-12; which scale was used is not indicated in the daily data at this

time.

WDMV

Total wind movement. Unit Measurement, Whole Miles.

WDVL

14





Prevailing wind velocity, speed component. Unit Measurement, Whole

Miles.

WDVM

Maximum wind velocity, speed component. Unit Measurement, Miles per

Hour.

METEOROLOGICAL ELEMENT MEASUREMENT UNITS CODE

The units and decimal position (precision) of the data value for this record

(reference Table "G").

YEAR

This is the year of the record. Range of values is 1800-current year

processed.

MONTH

This is the month of the record. Range of values is 01-12 LST.

DURATION

This is the number of hours over which the observation was collected. Range

of values is 00-24, and 99 for missing. A duration of 00 indicates a point

measurement in time, while 24 indicates a true daily observation.

FILLER

Filler value is 99.

NUMBER OF DATA PORTIONS THAT FOLLOW

This notes the actual number of values reported. Range of values is 01-62.

NOTE: A record may contain fewer or more data values than you might expect.

A monthly record of daily values may contain as few as one data value or as

many as 62 data values.

A maximum of two DATA PORTIONS are used for each day of the month so as to

allow one original meteorological data value and one edited data value. The

only exception at this time, is that the "days with weather" element-types

(DYSW) of original data values can be reported in multiple logical records

(e.g. only one original DYSW Data Portion for each day is given within a

single DLY logical record). When more than two types of weather on any given

day, a new DLY logical record for the same month will exists until DYSW is

exhausted. At most, 62 data values may be contained in any given logical

record (e.g., 30 + (62 x 12) = 774 characters). Thus, while a maximum of

1,230 characters has been assigned, no more than 774 characters will be used

for the daily data record types.

If a particular data value was not taken or is unavailable, there is no entry

for it. (For meteorological elements observed once a day, if all the daily

observations of a given month are received and pass QC checks, there will be

one DATA PORTION for each day. If every value were to fail the QC, there may

be two DATA PORTIONS for every day of that month. When two DATA PORTIONS for

15





a daily record are encountered (with the exception of DYSW), the original data

values are flagged and the second DATA PORTION is the best possible

replacement. (See code definitions for the Flag 2 element).

DAY OF MONTH

Contains the day of the month on which the data element was observed. Range

of values is 01-33. Day 32 is the monthly sum; Day 33 is the monthly average.

HOUR OF OBSERVATION

Contains the hour of the daily observation. Hour is reported using the 24-

hour clock 00-23 LST. Other codes for non-specific hours are listed in the

table below.

Sunrise

Sunset

Morning

Afternoon

Evening, night

Missing hour

Midnight

Noon

91

92

93

94

95

99

0

12

SIGN OF METEOROLOGICAL VALUE

The algebraic sign of the meteorological data value is given as either a blank

or a minus sign (-). Blank indicates a positive value and a minus sign

represents a negative value (see topic 45 "Data Quality: Known Uncorrected

Problems").

VALUE OF METEOROLOGICAL ELEMENT

The actual data value is given as a five-digit integer, except for cloud type,

precipitation type, precipitation time of beginning and ending, and days with

weather/state of the weather. (Tables “C” through “F”).

For fixed length records only when a data value is missing, the sign of the

data value is set to "-", the data value is set to "99999", flag position 1 is

set to "M" and flag position 2 is blank.

When no daily precipitation reading was taken but the amount from that day (if

any) is included in a subsequent value, the data value of precipitation is set

equal to "99999" and flagged with an "S" in flag position 1. In turn, the

successive accumulated amount will be flagged with an "A" in flag position 1.

FLAG1

The Data Measurement FLAG (reference Table "H").

FLAG2

The Data Quality FLAG (reference Table "I").

16





17





**TABLES**

**TABLE “A”**

**State-Code Table**

01 Alabama

28 New Jersey

29 New Mexico

30 New York

31 North Carolina

32 North Dakota

33 Ohio

02 Arizona

03 Arkansas

04 California

05 Colorado

06 Connecticut

07 Delaware

08 Florida

09 Georgia

10 Idaho

11 Illinois

12 Indiana

13 Iowa

14 Kansas

15 Kentucky

16 Louisiana

17 Maine

34 Oklahoma

35 Oregon

36 Pennsylvania

37 Rhode Island

38 South Carolina

39 South Dakota

40 Tennessee

41 Texas

42 Utah

43 Vermont

44 Virginia

18 Maryland

19 Massachusetts

20 Michigan

21 Minnesota

22 Mississippi

23 Missouri

24 Montana

25 Nebraska

26 Nevada

27 New Hampshire

45 Washington

46 West Virginia

47 Wisconsin

48 Wyoming

49 Not Used

50 Alaska

51 Hawaii

66 Puerto Rico

67 Virgin Islands

91 Pacific Islands

**TABLE "B"**

**Cooperative Network Division Table**

NOTE: The division number for a station may change over time.

HAWAII (STATE 51)\*

ISLAND NAME

DIVISION

Kauai

Oahu

01

02

03

04

05

06

Molokai

Lanai

Maui

Hawaii

\*NOTE: Hawaii (State 51) division numbers were changed during the initial

conversion of this file. Divisions within islands no longer exist. Division

numbers now represent each island.

18





PACIFIC ISLANDS (STATE 91)

Division

02 -

East of 180th Meridian - Phoenix Islands, Line Islands, and

American Samoa

03 -

04 -

Western Pacific Islands, North of 12N

Caroline and Marshall Islands

**TABLE "C"**

**CLTL, CLTU – Cloud Type Table**

C

K

Cirrus

Cumulus

Stratus

Cirro-cumulus

Cirro-stratus

Cumulo-stratus

Cumulo-nimbus

Nimbus

ST

CC

CS

KS

KN

N

NS

3

Nimbo-stratus

clouds

1

clear

HZ

F

haze

fog

HF

SM

SD

high fog

smoky

scudd

These two-character CLTL/CLTU cloud type codes are stored into the rightmost

two characters of the data value portion of the meteorological element.

Within the two characters used, the weather codes are entered left justified

and zero filled. Thus, if cloud type is reported, the data values would

appear as 000XX, where XX is the appropriate cloud type code. Cloud types may

include codes for Daily Occurrence of Weather (Table D), or Precipitation Type

(Table E).

**TABLE "D"**

**DYSW/STWX - Daily Occurrence of Weather/State of the Weather Table**

1

2

3

Clear

Partly cloudy

Cloudy

Rain

Clearing, variable

Threatening

Showers/sprinkles

4

5

Snow

6

7

Smoke/haze

Fog

8

9

Drizzle (mist)

Sleet

Misty clouds

10

Glaze

19





11

12

13

14

15

16

17

18

19

20

21

99

Thunder

Hail

Dust storm

Blowing snow

High wind

Tornado

Fair

Squalls

Frost

Mixed rain and snow

Dew

Illegible

Hoar Frost

These two-character DYSW/STWX element-type codes are stored into the rightmost

four characters of the data value portion of the meteorological element.

Within the four characters used, the weather codes are entered left justified

and zero filled. Thus, if one type of weather occurs during a day, the data

values would appear as OXXOO, where XX is the appropriate weather code. If

two types of weather occur, the data value will contain OXXYY, where XX is

value 1 and YY is value 2. If more than two types of weather occur on the

same day, they will be stored into additional "DLY" records of the element-

type code "DYSW" as needed. For STWX, only one element-type code is allowed

for each observation time over the course of the day. The codes for cloud

type (TABLE “C”) may also appear in the DYSW/STWX data, if recorded as such by

the observer. Each element-type code is reported only once for a given day,

even if, for example, there were more than one case of thunder reported for

the day.

**TABLE "E"**

**PTYP – Precipitation Type Table**

R

T

Rain

thunderstorm

S

D

E

G

H

I

Snow

drizzle/mist

Sleet

Glaze

Hail

Ice

M

W

F

mixed - rain and snow

squalls/showers/sprinkles

Fog

X

Z

Dew

Frost

These one-character PTYP element-type codes are stored into the rightmost

character of the data value portion of the meteorological element. Thus, if

precipitation occurs during a day, and the precipitation type is available,

the data value would appear as 0000X, where X is the appropriate precipitation

type code. Only one code is recorded for each day for PTYP.

**TABLE "F"**

20





**TPBG, TPEN - Time Table**

Sunrise

Sunset

Morning

Afternoon, evening

Missing hour

Midnight

1300A

1400P

\_\_\_\_A

\_\_\_\_P

1200A

1200P

Noon

DN - during night - means after midnight

Continuing or unknown

\_\_\_\_A

\_\_\_\_\_D

Times are given in hours and minutes using a 12-hour clock and an AM/PM

indicator. For TPBG/TPEN, if the observer wrote more than one time of

beginning/ending into the slot for the day, the keyer digitized the first

beginning time, and the last ending time, for each day.

**TABLE "G"**

**Units of Measurement Table**

Range of values where b = Blank:

HF

bI

TI

HI

IT

MH

bM

NA

DG

TN

WN

PC

TP

TG

HG

Hundredths of degrees Fahrenheit

Inches

Tenths of an inch

Hundredths of inches

Thousandths of inches of mercury

Miles per hour

Whole miles (right justified)

No units applicable (nondimensional)

whole degrees

Scale of 0 to 10

Scale of 0 to 12

Whole percent

Tenths of a percent

Tenths of feet

Hundredths of feet

**TABLE "H"**

**Data Measurement Flag 1**

A - Accumulated amount since last measurement.

M - For fixed length records only.

Flag1 is "M" if the data value is missing. In this case, the sign of the

meteorological value is assigned "-" and the value of the meteorological

element is assigned "99999".

S - Included in a subsequent value. (data value = "00000" OR "99999").

T - Trace (data value = 00000 for a trace).

Blank -

Flag not needed.

Flag 1 values of "S" and "A" usually occur in pairs (ie. a daily value will

have Flag 1 assigned as "S" and the next daily value will have Flag 1 assigned

as "A"). For some daily values these flags do not occur in pairs.

21





**TABLE "I"**

**Data Quality Flag 2**

2 - Invalid data element (subsequent value replaces original value).

3 - Invalid data element (no replacement value follows).

4 - Validity unknown (not checked).

T - Failed internal consistency check

**7. Start Date:**

Data prior to 1896 comprise the bulk of the data set with most of the earliest

records dating back to 1820.

**8. Stop Date:**

For the bulk of the data, the stop date is 1892 or 1896, but some data stop

after 1900.

**9. Parameter**:

Atmospheric Dynamics>Atmospheric Temperature>Daily Maximum Temperature

Atmospheric Dynamics>Atmospheric Temperature>Daily Minimum Temperature

Atmospheric Dynamics>Atmospheric Temperature>Daily Average Temperature

Atmospheric Dynamics>Atmospheric Temperature>Daily Temperature Range

Atmospheric Dynamics>Atmospheric Temperature>Observation Time Temperature

Atmospheric Dynamics>Precipitation>Daily Precipitation

Atmospheric Dynamics>Precipitation>Daily Snowfall

Atmospheric Dynamics>Precipitation>Daily Snow Depth

Atmospheric Dynamics>Wind>Wind Movement

Atmospheric Dynamics>Wind>Daily Prevailing Wind Direction

Atmospheric Dynamics>Cloud>Daily Cloud Amount

**10. Discipline:**

Earth Science>Atmospheric>Meteorology/Climatology

Daily Precipitation, Daily Snowfall, Daily Snow Depth, Daily Maximum

Temperature, Daily Minimum Temperature, Observation Time Temperature, Wind

Movement, Weather

Earth Science>Land>Hydrology

Evaporation, Daily Snowfall, Daily Snow Depth, Daily Precipitation

Earth Science>Land>Agriculture

Daily Precipitation, Evaporation

**11. Coverage:**

Southernmost Latitude

Northernmost Latitude

Westernmost Longitude

Easternmost Longitude

22N

65N

178W

68W

**12. Location**:

Areal Coverage

North America>Continental USA

**13. Keywords:**

22





Temperature

Maximum Temperature (24 HR)

Minimum Temperature (24 HR)

Mean Temperature (24 HR)

Temperature at Observation Time

Precipitation

Snow

Snow on Ground

Evaporation

Sky Condition

Weather

Drizzle

Ice Pellets

Glaze

Thunder

Hail

Dust

Sand Storm

Blowing Snow

Winds

Tornado

Rain

Smoke

Fog

TD-3206

3206

**14. Storage Medium**:

HDSS

**15. File Mode:**

ASCII

**16. How to Order Data**:

These data are available for purchase from the National Climatic Data Center,

Climate Services Branch, Federal Building, 151 Patton Avenue, Room 120,

Asheville, NC., 28801-5001, phone number (828)-271-4800, e-mail

ncdc.orders@noaa.gov

**17. Historical and Current Data Sources**:

Cooperative Observations

Principal Climatological Stations

Summary of the Day Observations

Punched Card Deck 345

Punched Card Deck 486

State Universities

Evaporation Observations

Digital Files

Daily Observations (manuscripts and publications)

Tape Deck 9639

Tape Deck 9727

Historical Files

MAPSO Diskettes

23





**18. Algorithms**:

No information available at this time.

**19. Responsibility for Algorithms**:

No information available at this time.

**20. Project**:

National Weather Service (NWS) Cooperative Program

**21. Archiving Data Center:**

National Climatic Data Center,

NOAA/NESDIS/NCDC

151 Patton Avenue

Asheville, NC 28801-5001

Phone (828) 271-4800

**22. Originating Data Center**:

National Climatic Data Center

NOAA/NESDIS/NCDC

151 Patton Avenue

Asheville, NC 28801-5001

Phone (828) 271-4800

**23. Technical Contact**:

National Climatic Data Center

NOAA/NESDIS/NCDC

151 Patton Avenue

Asheville, NC 28801-5001

Phone (828) 271-4800

**25. Sensor Name and Operating Principles:**

No information available at this time.

**26. Sensor Siting**:

No information available at this time.

**27. Sensor Accuracy and Calibration**:

No information available at this time.

**28. Sensor Sampling Characteristics**:

No information available at this time.

**29. Data Capture Method:**

No information available at this time.

**30. Station Location Accuracy:**

24





Station History Locations are digitized as recorded on the original forms. In

most cases, the latitude and longitude were recorded to the nearest minute; in

some cases, to the nearest second. The accuracy of the instrumentation and

process of measuring the locations is unknown.

**31. Station Observation Schedule:**

Since the observations preserved in this digital data set are from the

beginnings of instrumented weather observations and observing networks, the

station observation schedule is non-standard, especially for the records for

the early 1800’s. Observations in this data set include daily observations

recorded in either the morning, evening, or at midnight, as well as

observations at one or more points in time throughout the day.

**32. Station Data Time Averaging:**

The daily mean temperatures keyed for this data set are those as recorded on

the original forms by the observers. In general, when daily maximum and

minimum temperatures were available, the daily mean was calculated by the

observer or other editor as the simple average of the two. When three point

measurements of the temperature (TAHR) were recorded over the course of the

24-hour period, the mean was generally calculated in one of two ways. One was

to take the simple average of the three measurements; the other, to add in the

evening temperature twice and divide by four. Which calculation method was

used by the observer or other editor to calculate the daily mean is generally

not available. Some information may be available in the accompanying

metadata.

**33. Spatial Sampling Using Station Grouping**:

Not Applicable.

**34. Network Participation**:

This data set is comprised of stations from the 1800’s from a variety of

networks, as well as private journals and other documents. The networks

include military and civil; some observers were paid, while others were

volunteers. The funding and responsibility for maintenance of the instruments

varied by network.

**35. Geographic Criteria for Selecting Stations:**

Not Applicable.

**36. Geographical Distribution:**

The distribution of stations varies over time and space as a result of the

expansion of observers across the country and the evolution of observer

networks. There are approximately 5,000 stations, as defined by location

name, in the entire historical archive for the 1800’s. A subset of these were

selected for digitization based on length and continuity of record, location,

and other factors.

**37. Elevation Distribution**:

Elevations for fixed surface locations for the data set are mostly below 1,000

meters above sea level.

25





**38. Instrument Problems**:

No information available at this time.

**39. Missing Data Periods:**

No information available at this time.

**40. Sampling Biases:**

No information available at this time.

**41. Error Detection and Correction:**

The historical data were keyed from microfilm copies of original observation

forms. A quality control process developed specifically for this data set

performs internal consistency, climatological limit, and serial checks on both

daily values and monthly values derived from the daily values. This process

includes manual verification of flagged data. In general, quality control

flags are not included in the digitized data set. The general purpose of the

quality control process is to assure that the digitized data accurately

reflect the observations as recorded on the form. In some cases, the

assignment of element code to the data is adjusted to match the data rather

than the column headings on the forms. For more information about the quality

control process, please refer to Appendix A, “Digitization of Historical Daily

Data from the 1800’s”. The user should investigate the accuracy and

homogeneity of the data for each specific application.

**42. Missing Value Estimates:**

No information available at this time.

**43. Quality Control Responsibility:**

Responsibility for data quality rested with the individual observer, as well

as the historical network managers.

**44. Known Uncorrected Problems**:

For some stations for some time periods, the date of the maximum temperature

may be wrong by one day. The problem arises because the observer or network

manager may have recorded the maximum temperature on a calendar date rather

than on the date of the end of the 24-hour observation. This problem

sometimes causes the maximum temperature for a day to be less than the minimum

temperature. For more information about uncorrected problems, please refer to

Appendix A.

**45. Confidence Factors:**

Because the data were keyed from microfilm, because the operational

observation and quality assurance procedures changed markedly over the

historical period of the data set, and because no quality assurance of the

data was performed for this project other than those noted in Appendix A, the

user should be wary of all the data in this data set.

**46. History of Data Usage:**

26





This digital data set is new and does not yet have a history of use.

**47. Quality Statement:**

The historical nature of the data set, as well as limited resources (monetary

and personnel) for applying quality control and assurance, contribute toward

less than optimum conditions in ensuring the integrity of the data.

**48. Revision Date**:

None.

**49. Science Review Date:**

None.

**50. Future Review Date:**

Not applicable at this time.

**51. Source Data Sets**:

This data set is currently compiled from microfilm copies of manuscript forms

from the National Archives.

**52. Essential Companion Data Sets**:

TD-3200.

**53. Derived Data Sets:**

None.

**54. Larger Collections:**

No information available at this time.

**55. Similar Data Sets:**

DS-3200 Coop Summary of the Day

DS-3210 Summary of Day-First Order

DS-3220 Coop Summary of Month

DS-3240 Hourly Precipitation

DS-3260 15-Minute Precipitation

DS-3280 US Global Surface Airways Hourly Observations

**56. References:**

See Appendix A.

**57. Summary:**

This data set is a compilation of digitized daily observations for the 1800’s.

The period of record and number of stations varies among the states. The

records generally date back to the late 1820’s. These data have been

subjected to internal consistency checks, compared against climatological

limits, and checked serially.

27





28





**Glossary**

**Access Method for Archived Data -- How a digital data set can be accessed in**

**its archived condition.**

**Access Method for Supplied Data** -- How the user can access data in its most

commonly supplied form.

**Archiver** -- The one person or institution responsible for archival and

maintenance of the data, and how to contact.

**Archiving Data Center** -- Name, organizational acronym and address of

institution that archive and distribute the data.

**Confidence Factors** -- The expected numerical accuracy of the data.

**Cost of Acquiring Data** -- Describes how to find the approximate costs that are

associated with obtaining the data set, or quotes the cost.

**Coverage** -- The smallest latitude-longitude "box" on the earth's surface that

all data measurements occurred within.

**Data Capture Method at Sensor** -- The method used to collect data initially at

the sensor. Aspects that should be mentioned here include such concepts as

manual, automatic, forms, charts, telemetered, etc.

**Data Derivation Algorithm**s -- The methods, if any, used to calculate values in

the data set.

**Data Derivation Algorithms, Responsibility for** -- A list of programs or

agencies that provide data derivation algorithms or which carry out the data

derivations using the algorithms.

**Data Set Aliases** -- Other names associated with the data set, now or in the

past.

**Data Set ID** -- A unique code number or acronym identifying the data set.

Normally, it is the code number used by the data center as the data set is

archived.

**Data Set Name** -- A descriptive name for the data set that provides a Thumbnail

description.

**Derived Data Sets** -- Other data sets that are partly or entirely derived of

this data set.

**Discipline** -- A collection of standard phrases that name the scientific

disciplines, or fields, in which the data are normally used. Most of each

phrase comes from the "Directory Interchange Format Manual".

**Elements** -- The basic units of data that need to be described. Often,

elements are simply data variables such as station id, precipitation or ocean

depth. However, when FORTRAN, C, etc. issued to access a digital data set,

elements are the same as the "fields" used in the access software, such as in

a FORTRAN "READ" format. (This definition simplifies the preparation and

maintenance of the documentation.

29





**Element Names and Definitions** -- The names and brief definitions of the basic

units of data that need to be described.

**Elevation Distribution** -- Variation of the elevations of the fixed observing

locations.

**Error Detection and Correction** -- Any procedures used now or in the past to

identify, and avoid or correct, data errors.

**Essential Companion Data Sets** -- Other data sets, if any, that must be

obtained in order to use this data set.

**File Mode** -- The mode, or code standard, of a digital file in which a digital

data set is stored. Commonly seen modes include ASCII, EBCDIC, Fielddata

(unisys only), and binary.

**Future Review Data** -- The date, if any, recommended by the archiver for the

next science review.

**Geographic Criteria for Selecting Stations** -- Fixed surface locations may be

selected with a specific type of geographic environment in mind. Geographic

selection criteria describes this.

**Geographic Distribution** -- The spatial sampling, i.e. the number and closeness

of fixed observing locations within a geographical area.

**History of Data Usage** -- The extent to which this data set, or parts of it,

has been used by researchers, and how they rated its quality.

**Instrument Problems** -- Difficulties that occur as a natural result of sensor

operation.

**Investigator** -- Data set experts other than the archiver or technical contact,

who can provide information that they cannot.

**Keyword** -- Words or short phrases that suggest the data set, or suggest

aspects of it. Actual variable names should not be used as keywords.

**Known Uncorrected Problems** -- Known data difficulties, if any, for which no

corrections have been made.

**Larger Collections** -- Supersets of data sets, if any, that include this data

set.

**Location** -- A collection of standard phrases that name the major geographic

area(s), and the atmospheric layer(s), that the data refer to. Most of each

phrase comes from the "Directory Interchange Format Manual".

**Missing Data Periods** -- Times when major parts of the data are missing.

**Missing Value Estimates** -- Procedures used to produce estimated values for

missing data.

**Network Participation** -- Describes the named collections of fixed surface

locations, if any, whose data contribute to this data set.

**Originating Data Center** -- Name, organizational acronym, and address of the

30





data center(s) that generated the data documentation.

**Parameter** -- A collection of standard phrases that briefly name and describe

the measured parameters of the data set. Most of each phrase comes from the

"Directory Interchange Format Manual".

**Project** -- Specific campaign or effort, if any, with which the data set is

associated.

**Quality Control Responsibility** -- Agencies or programs, if any, that provide

major quality control processing.

**Quality Statement** -- A brief generalization of how good the data are. Includes

a "quality value" number.

Reference -- Any important bibliographic reference pertaining to the data set

or any part of it.

**Revision Date** -- The date that this documentation is created, or the date of

its latest revision.

**Sampling Biases** -- Data biases caused by inadequacies in spatial or temporal

sampling.

**Science Review Date** -- The date, if any, of the latest review of this

documentation for accuracy of technical content.

**Sensor Accuracy and Calibration** -- The precision to which the measured

variables are known. It refers both to the accuracy of the sensor and to the

significant digits in the data values captured by the sensor.

**Sensor Name and Operating Principles** -- The sensors used to obtain the data in

the data set.

**Sensor Sampling Characteristics** -- Spatial averaging, temporal accumulation,

and sampling frequency that occur at the sensor.

**Sensor Siting** -- The local environment into which sensors are placed.

**Source Data Sets** -- Other data sets, if any, used to assemble this data set.

**Similar Data Sets** -- Other data sets, if any, used to assemble this data set.

**Sources** -- Origins of the data set.

**Spatial Sampling Using Station Groupings** -- How data from specific locations

are collected, aggregated, or arranged to represent a geographical area.

**Start Date** -- The date of an earliest appearance.

**Station** -- A fixed surface location that reports data.

**Station Data Time Averaging** -- Aggregation or averaging of data over time to

obtain values representative of a time period.

**Station Location Accuracy** -- How accurately the positions of the fixed surface

location are known.

31





**Station Observation Schedule** -- When fixed surface locations make data

measurements.

**Stop Date** -- The date of latest appearance.

**Storage Medium** -- The quantities, capacities, and types of media on which the

data are now stored.

**Summary** -- A concise abstract that is used to capture a few of the most

important facts about the data set, all of which should have appeared in more

detail under individual topic discussions.

**Technical Contact** -- The person who can be contacted to obtain and provide

information about the data.

32





**Appendix A**

**Quality Control of Daily Data from the 1800’s**

The quality control tests developed for this data set are listed in the

following table. The quality control tests are applied in order, with the

outliers from each test verified before continuing to the next test. The

outliers generated by each test are appended to the outlier file for each

station. The verification process produces two files, one listing the

verification with explanation for each outlier, the other listing necessary

corrections to be applied to the data. After the outliers for one test are

verified, the corrections are all applied in order to the data for the

station, and then the next test is run.

33





**Quality Control**

**Sub-Flag**

**Type**

**Name**

**Flag Type**

**Description**

This test checks for elements on an image with the

same month/year/hour/duration. Outlier are

produced for the second occurrence of the same

month/year/hour/duration with a 30 in the hour

postions so no data is overwritten. This test

produces outliers that must be manually checked.

Duplication Test

01

00

01

This test is applied during translation of the data

from SourceCorp format to TD-3200 format. This

test flags individual daily values, with cutoffs set to

the extreme range of each element type. This test

produces outliers that must be manually checked

Gross Errors Check

01

This test is applied after each run time the

corrections is applied. It pulls the duration of each

element from the metadata and inserts it into the

TD-3200 format data in columns 24 & 25. No

corrections are added to the Corrections file for

this test

Apply Durations

01

01

01

02

03

04

This test compres the date for each image in the

3200 output file, with the dates keyed for that

image in the metadata. The entire month is

flagged during this test. This test produces

outliers that must be manually checked.

Date Check

This test compares the station number as entered

in the metadata through the PICS tool, with the

station number keyed by the daily data keyers.

This is an automatic test which produces only

corrections which are applied by the test.

Station Number Check

This test compares the monthly mean

temperatures entered in the 3200 output file with

that in the metadata. If MNTP is keyed when

MNTO is asked for, the data is switched to MNTO.

Corrections are automatically created and applied

by the test

Monthly Mean Check

01

05

34





If dry-bulb temperature for a day is less than or

equal to 32(F) and the wet-bulb temperature is

greater than the dry-bulb, a correction is added to

the file flagging the wet-bulb temperature as an

observer error.

Wet Bulb Check

01

06

The tests verifies that the number of digits in the

monthly total wind movement as keyed is

consistent with the sum of the daily data values. If

any inconsistency exists, the program will write a

correction to the Corrections file.

Wind Movement

Check

01

01

07

09

This test converts any 3200-format SKYC

elements to SKYL. Corrections are automatically

added to the Corrections file

Sky Cover Check

This test checks the 3200-format precipitation data

to see if any values can be automatically

corrected. One is to correct daily sums from

hourly observations if they work with the monthly

sums. Another is to correct the monthly mean if

the daily sum and the keyed sum are equal.

Precipitation Check

01

10

This test checks that all elements for an image in

the metadata matches all the elements for an

image in the 3200-format data. There are 3

subcategories of outliers

Metadata Test

\*\*

\*\*

This subcategory always has a +3200 in the

outlier. It indicates that an element is in the 3200-

format but not in the metadata

02

01

This subcategory always has a -3200 in the

outlier. It indicates that an element is in the

metadata but was not keyed in the 3200-format

data.

02

02

02

03

This subcategory offers a suggestion about what

is possibly wrong between the metadata and the

keyed 3200 data

This test checks the keyed monthly values against

the calculated monthly values from the daily data.

This is only done for TMAX, TMIN, TAHR, PRCP

and SNOW

Monthly Means

05

\*\*

35





When a monthly mean (day 33) is keyed for a

temperature element, this mean is compared to

the mean calculated for all of the daily values. If

the difference between the two is greater than

5(F), the day 33 value is flagged

05

01

When a monthly sum (day 32) is keyed for a snow

element, this sum is compared to the sum

calculated for all of the daily values. If the two are

not equal the day 32 value is flagged.

05

05

06

02

05

\*\*

When the monthly sum (day 32) for PRCP is

missing or not equal to the sum of the daily values,

the day 32 value is flagged.

This test checks for internal consistency of the

monthly means and totals from the daily values for

all element types within each station. This test

flags the day 33 means.

Monthly Temperature

Consistency

06

06

06

01

02

03

monthly mean max < monthly mean min

monthly mean max < mean of all at-hour

temperatures

monthly mean min > mean of all at-hour

temperatures

11AM-4PM temperatures < sunrise-1AM-10AM

tempreatures (afternoon < morning temperatures)

06

06

04

05

11AM-4PM tempreatures < 5PM-sunset-midnight

temperatures (afternoon < evening temperatures)

06

06

06

07

mean dry-bulb < mean wet-bulb (for each hour)

at-hour temperature < wet-bulb temperature (for

each hour)

06

06

08

09

dry-bulb < dewpoint (for each hour)

at-hour < dewpoint (for each hour)

lowest at-hour minimum temperature > mean

temperature > highest at-hour max temperature

06

10

mean monthly max temperature > mean monthly

min temperature + 60(F)

06

06

11

12

mean average temperature range > 50(F)

mean average temperature range does not equal

(mean max - mean min) +/- 1(F)

06

13

36





all at-hour pressure-attached temperatures <

morning temperatures (or minimum temperature,

whichever lower)

06

07

14

\*\*

This test checks for internal consistency of the

monthly means and totals from the daily values for

all element types within each station. This test

flags the day 32 sums.

Monthly Precipitation

Tests

snowfall > 0 and the lowest monthly minimum

temperature is > 39

07

07

07

01

02

03

snowfall > 0 and there was no precipitation during

the month

snowfall > 1 inch and was also greater than 50

times the precipitation amount

snowfall was zero and precipitation > 0.05 and the

highest monthly max temperature was < 30

07

04

snowfall > 1 inch and snowdepth was zero and the

highest monthly max temperature was > 30

07

07

05

06

snow depth > 0 and the lowest monthly minimum

temperature was > 39

If there was precipitation data on all days in the

month, and only one day is missing (I.e. n-1 days),

who summed together total zero. That is, the

number of days with precip, including traces, is

greather than or equal to n-1.

07

07

The number of days with precipitation is less than

the number of days with snowfall, and no snow

depth.

07

08

Precipitation amount is the highest monthly total in

the record.

07

07

07

07

07

07

07

07

71

72

73

74

75

81

82

83

Precipitation amount is the second highest

monthly total in the record.

Precipitation amount is the third highest monthly

total in the record.

Precipitation amount is the fourth highest monthly

total in the record.

Precipitation amount is the fifth highest monthly

total in the record.

Snowfall amount is the highest monthly total in the

record.

Snowfall amount is the second highest monthly

total in the record.

Snowfall is the third highest monthly total in the

record.

37





Snowfall is the fourth highest monthly total in the

record.

07

07

07

07

07

07

07

84

85

91

92

93

94

95

Snowfall is the fifth highest monthly total in the

record.

Snowdepth is the highest monthly snowdepth in

the record.

Snowdepth is the second highest monthly total in

the record.

Snowdepth is the third highest monthly total in the

record.

Snowdepth is the fourth highest monthly total in

the record.

Snowdepth is the fifth highest monthly total in the

record.

This checks for extremes and internal consistency

of the daily values within each station. The

extreme limits are set on a daily basis using the

climatology of the station within the CDMP Forts

data set. This test flags individual daily values.

Daily Extremes and

Climatological

Consistency

08

08

\*\*

Extremes test of maximum and minimum

temperature

01

08

08

02

03

Max/min inconsistency checks

Flatliner check for TMAX and TMIN

08

04

Excessive diurnal range for TMAX and TMIN.

08

08

08

08

51

52

06

07

Spike Check

Spike Check

Step Check

Extreme test of precipitation

Precipitation cloud test: If a station reports

precipitation, there must be at least one

observation on that day of some sort of cloud

cover.

08

08

08

09

TMAX must be greater than or equal to largest at

hour temperature (or drybulb), and TMIN must be

less than or equal to lowest at hour temperaure (or

drybulb).

This test checks for consistency of the daily values

that can be calculated from other keyed daily

values within each station. This test flags

individual daily values.

Daily Calculated

Consistency

09

09

\*\*

Daily mean temperature consistency with at-

hour/max-min temperatures check. Includes a

check that doubles the 9pm temperature as

another method for determining the daily mean.

01

38





Daily range in temperature with at-hour/max-min

temperatures check

09

09

02

03

Daily consistency of dew point/dew point

depression/relative humidity with exposed/dry

bulb/wet bulb temperatures

Daily total preciptation/snowfall measurements

(24-hr duration) with partial-day duration (not 24-

hrs) precipitation/snowfall consistency check

09

09

04

05

Daily mean wind direction, velocity, force,

movement, max direction, and max velocity with

at-hour/duration observations consistency check

Daily mean clearness and cloud amount with at-

hour clearness and cloud amount consistency

check

09

09

06

07

River gauge height and gauge height change

consistency check

39





**Appendix B**

**Documentation of Problems with and Changes Made to Keyed Data**

The quality control suite finds many issues within the data. Most are able to

be corrected; some are not. An overwhelming number of errors are due to

unclearly scanned images of the original forms, smeared or illegible script,

or messy and faded forms. The following sections document the recurring

problems that have been found and how they are being fixed.

**Non-Standard Units**

While specific units are used to record meteorological conditions today, the

observers of the 1800s recorded data in several different units. The table

below lists the ones found to date.

Element

Non-Standard Unit

Degrees Celsius

0-4, 0-1, 0-12

Cubic Centimeters

0-1

Conversion

Converted to Degrees Fahrenheit

Converted to 0-10

Temperature

Sky Cover

Precipitation

Relative

Converted to Inches

Converted to 0-100

Humidity

Barometric

Centimeters of Mercury

Millimeters of Mercury

Many different scales

Converted to Inches of Mercury

Pressure

Wind Force

These cannot be fixed because

most observers did not note

what scale they were using.

These are marked with a flag 2

in the data

**Keying Error**

These occur through simple human error. It could be typing in the incorrect

value to confusing columns on the form. Some of the more common are listed

below:

\1. Keying the TMAX column as TMIN and TMIN column as TMAX.

\2. Keying one element as another element.

\3. Keying one hour as another hour.

\4. Keying the date of the form.

\5. Shifting the day of the data up or down to the incorrect day

**Observer Error**

This category occurs when what is on the form matches what is in the digitized

daily data, but there is something obviously wrong with the data because

meteorological it makes no sense. Some of the common types of these are

listed below:

\1. Observers recorded TMAX values less than/TMIN values greater than at-hour

temperatures

\2. Adding and division errors when calculating sums and means of the daily

values.

\3. Including snowfall amounts in precipitation totals.

40





\4. Recording wet-bulb temperatures higher than dry-bulb temperatures

41


