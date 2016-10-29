Run locally:
  python -m train.1-multiply
Run in ClouldML
  JOB_NAME=<your job name>
  
  JOB_NAME="task8"

  PROJECT_ID=`gcloud config list project --format "value(core.project)"`
  STAGING_BUCKET=gs://${PROJECT_ID}-ml
  INPUT_PATH=${STAGING_BUCKET}/input
  
 
  gcloud beta ml jobs submit training ${JOB_NAME} --package-path=train \
          --staging-bucket="${STAGING_BUCKET}" \
          --module-name=train.1-multiply


  JOB_NAME="task8"

  PROJECT_ID=`gcloud config list project --format "value(core.project)"`
  STAGING_BUCKET=gs://${PROJECT_ID}-ml
  INPUT_PATH=${STAGING_BUCKET}/input
  gsutil cp input/input.csv $INPUT_PATH
  
  gcloud beta ml jobs submit training ${JOB_NAME} --package-path=train \
  --staging-bucket="${STAGING_BUCKET}" \
  --module-name=train.2-input \
  -- --input_dir="${INPUT_PATH}"


 JOB_NAME="task20"
 PROJECT_ID=`gcloud config list project --format "value(core.project)"`
 STAGING_BUCKET=gs://${PROJECT_ID}-ml
 OUTPUT_PATH=${STAGING_BUCKET}/output
 
 gcloud beta ml jobs submit training ${JOB_NAME} \
 --package-path=train \
 --staging-bucket="${STAGING_BUCKET}" \
 --module-name=train.3-output \
 -- --output_dir="${OUTPUT_PATH}"
