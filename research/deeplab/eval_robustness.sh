python create_table.py
for i in 500 400 300 200
do
  for j in 0 5 10 15 20 25
  do
    sh ./local_test_eval_only.sh $j $i
  done
done
