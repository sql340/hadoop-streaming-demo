hadoop jar /opt/meituan/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapreduce.job.queuename=root.hadoop-mining.ad-online \
 -input shangqilong/data/kv.txt \
 -output shangqilong/data/output \
 -file "./mapper.py" \
 -file "./reducer.py" \
 -mapper "python mapper.py" \
 -reducer "python reducer.py" 
