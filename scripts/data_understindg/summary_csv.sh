# @Author: juan
# @Date:   2018-08-18 17:25:28
# @Last Modified by:   juan
# @Last Modified time: 2018-08-18 18:24:34

# arguments
FINPUT=$1
FOUTPUT=$2

# validate arguments
if [ "$FINPUT" == "" ]
then
  echo "[error] you have to introduce an input path."
  exit 1
fi
if [ "$FOUTPUT" == "" ]
then
  echo "[error] you have to introduce an output path."
  exit 1
fi

# header
echo > $FOUTPUT
echo "###" >> $FOUTPUT
echo "date:" $(date +"%Y-%m-%d") >> $FOUTPUT
echo "input:" $FINPUT >> $FOUTPUT
echo "output:" $FOUTPUT >> $FOUTPUT
echo "###" >> $FOUTPUT

# number of rows
echo >> $FOUTPUT
echo "--> Number of rows (included header):" >> $FOUTPUT
wc -l $FINPUT >> $FOUTPUT

# list of columns
echo >> $FOUTPUT
echo "--> Columns:" >> $FOUTPUT
csvcut -n $FINPUT >> $FOUTPUT

# summary statistics
echo >> $FOUTPUT
echo "--> Summary:" >> $FOUTPUT
csvstat $FINPUT >> $FOUTPUT

# head
echo >> $FOUTPUT
echo "--> Head:" >> $FOUTPUT
csvlook $FINPUT | head -10 >> $FOUTPUT

# tail
echo >> $FOUTPUT
echo "--> Tail:" >> $FOUTPUT
csvlook $FINPUT | tail -10 >> $FOUTPUT


# exit
echo "[success] it was created '$FOUTPUT'."
exit 0
