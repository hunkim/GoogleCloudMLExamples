# Google Cloud ML Examples

## Simple multiplication (train.1-multiply)

### Run locally:
```bash
python -m train.1-multiply
```

### Run in ClouldML
Set variables

```bash
JOB_NAME=<your job name>
  
JOB_NAME="task8"

PROJECT_ID=`gcloud config list project --format "value(core.project)"`
STAGING_BUCKET=gs://${PROJECT_ID}-ml
```
  
Submit a job

```bash
gcloud beta ml jobs submit training ${JOB_NAME} \
--package-path=train \
--staging-bucket="${STAGING_BUCKET}" \
--module-name=train.1-multiply
```

## Read input.csv from Google Storage (train.2-input)

### Run locally:
```bash
python -m train.2-input
```

### Run in ClouldML
Set variables

```bash
JOB_NAME="task8"

PROJECT_ID=`gcloud config list project --format "value(core.project)"`
STAGING_BUCKET=gs://${PROJECT_ID}-ml
INPUT_PATH=${STAGING_BUCKET}/input
```

Copy input.csv to Google Storage
```bash
gsutil cp input/input.csv $INPUT_PATH/input.csv
```
 
Submit a job

```bash
gcloud beta ml jobs submit training ${JOB_NAME} \
--package-path=train \
--staging-bucket="${STAGING_BUCKET}" \
--module-name=train.2-input \
-- \  # starting arguments for train.2-input
--input_dir="${INPUT_PATH}"
```


## Write checkpoint files to Google Storage (train.3-output)

### Run locally:
```bash
python -m train.3-output
```

### Run in CloudML
Set variables
```bash
JOB_NAME="task20"
PROJECT_ID=`gcloud config list project --format "value(core.project)"`
STAGING_BUCKET=gs://${PROJECT_ID}-ml
OUTPUT_PATH=${STAGING_BUCKET}/output/
```
 
Crete the output folder 
(Copy an empty file to the GS path with a trailing `/`)
```bash
gsutil cp /dev/null $OUTPUT_PATH
```

Submit a job

```bash
gcloud beta ml jobs submit training ${JOB_NAME} \
--package-path=train \
--staging-bucket="${STAGING_BUCKET}" \
--module-name=train.3-output \
-- \
--output_dir="${OUTPUT_PATH}"
```