

exp='exp1'
OBSTYPE='rw'
VarName='radial_velocity'
taskdir=./
filename="ufo_${OBSTYPE}_2020101300_0000.nc4"
python plt_ufo_omb.py $taskdir/$filename $OBSTYPE $VarName $exp
