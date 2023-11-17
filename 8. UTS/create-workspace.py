import os

custom_model_name = 'horbra' # Custom model name
pretrained_model = 'ssd_mobilenet_v2_320x320_coco17_tpu-8' # Pre-trained model 
tf_record_script = 'generate_tfrecord.py'
label_map = 'label_map.pbtxt'

# Setting up Folder Structure 
paths = {
    'tensorflow_path': os.path.join('Tensorflow'),    
    'workspace_path': os.path.join('Tensorflow', 'workspace'),
    'scripts_path': os.path.join('Tensorflow','scripts'),
    'api_path': os.path.join('Tensorflow','models'),
    'annotation_path': os.path.join('Tensorflow', 'workspace','annotations'),
    'image_path': os.path.join('Tensorflow', 'workspace','images'),
    'train_image_path': os.path.join('Tensorflow', 'workspace','images','train'),
    'test_image_path': os.path.join('Tensorflow', 'workspace','images','test'),
    'model_path': os.path.join('Tensorflow', 'workspace','models'),
    'pretrained_model_path': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'checkpoint_path': os.path.join('Tensorflow', 'workspace','models', custom_model_name), 
    'output_path': os.path.join('Tensorflow', 'workspace','models', custom_model_name, 'export'), 
    'protoc_path':os.path.join('Tensorflow','protoc')
 }
 
files = {
    'pipeline_config':os.path.join('Tensorflow', 'workspace','models', custom_model_name, 'pipeline.config'),
    'tf_record_script': os.path.join(paths['scripts_path'], tf_record_script), 
    'labelmap': os.path.join(paths['annotation_path'], label_map)
}

# Create Folder Structure
for path in paths.values():
    if not os.path.exists(path):
        os.mkdir(path)