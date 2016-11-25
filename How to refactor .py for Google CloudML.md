#Refactoring your python to run on Google CloudML

## 1) SAVE INPUT AND OUTPUT FILES TO GOOGLE STORAGE
Save all the files in google storage by running    

`gsutil cp /your_input_files $INPUT_PATH/`    
`gsutil cp /your_output_files $OUTPUT_PATH/`    

where $INPUT_PATH and $OUTPUT_PATH are already defined it as...    
```
JOB_NAME="your_job"
PROJECT_ID=`gcloud config list project --format "value(core.project)"`
BUCKET_NAME=gs://your_bucketname
TRAIN_PATH=${BUCKET_NAME}/${JOB_NAME}
INPUT_PATH=${BUCKET_NAME}/input
OUTPUT_PATH=${BUCKET_NAME}/output
```

## 2) CHANGE PATH TO INPUT/OUTPUT FILES
#### Path to input file
`${INPUT_PATH}/your_input_file`

#### Path to output file
`${OUTPUT_PATH}/your_output_file`

##### Examples
```
input_file = 'gs://your_bucketname/input/your_input_file.txt'
output_file = 'gs://your_bucketname/output/your_output_file.txt'
log_file = 'gs://your_bucketname/log/your_log_file.txt'
your_pickle_file = 'gs://your_bucketname/input/your_pickle_params.pkl'
```

## 3) IMPORT MODULE
Include the following line in your code:  
`from tensorflow.python.lib.io import file_io`



## 4) READING FILE
##### Example 1
`open('input/your_pickle_params.pkl')`   
Change it to  
`file_io.read_file_to_string('gs://seqgan-cloudml/input/you_pickle_params.pkl')`

##### Example 2
`cPickle.load(open('/your_pickle_file'))`  
Change it to:   
`cPickle.loads(file_io.read_file_to_string('/your_pickle_file'))`



## 5) WRITING FILE
##### Example 1
`open('/your_output_file', mode="w")`   
Change it to:   
`file_io.FileIO('/your_output_file', mode="w")`

##### Example 2
```
with open('/your_output_file', 'w') as fout:
        for poem in generated_samples:
            buffer = ' '.join([str(x) for x in poem]) + '\n'
            fout.write(buffer)
```
Change it to:   
```
with file_io.FileIO(output_file, mode='w') as fout:
        for poem in generated_samples:
            buffer = ' '.join([str(x) for x in poem]) + '\n'
            fout.write(buffer)
```
        

## note..   
* `python -m module`  <-- Just because -m option runs on local machine didn't mean that it was able to run on cloud.


 * For more info refer to tensorflow file_io.py: [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/lib/io/file_io.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/lib/io/file_io.py) 

 * Also, check this stackoverflow: [http://stackoverflow.com/questions/40396552/google-storage-gs-wrapper-file-input-out-for-cloud-ml](http://stackoverflow.com/questions/40396552/google-storage-gs-wrapper-file-input-out-for-cloud-ml). 


 * Change `tf.initialize_all_variables()` to `tf.global_variables_initializer()`. The `initialize_all_variables` (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
