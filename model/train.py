import os
import sys
from jetson.inference import detectNet
from jetson.utils import cudaDeviceSynchronize

# Set up dataset paths
train_images = "dataset/training/images"
val_images = "dataset/val/images"
labels_file = "dataset/training/labels.txt"

# Output model directory
output_dir = "model"

# Number of training epochs
num_epochs = 50

# Batch size
batch_size = 4

# Load DetectNet with transfer learning
net = detectNet(
    argv=[
        '--model=',
        f'--labels={labels_file}',
        '--input-blob=input_0',
        '--output-cvg=scores',
        '--output-bbox=boxes',
        f'--data={train_images}',
        f'--val={val_images}',
        f'--batch-size={batch_size}',
        f'--epochs={num_epochs}',
        f'--output-dir={output_dir}',
        '--arch=resnet18',
        '--resume',  # Resume training if interrupted
        '--log-interval=10',
        '--save-interval=5'
    ]
)

# Start training
net.Train()

# Optional: Sync CUDA (clean exit)
cudaDeviceSynchronize()
