from cleanfid import fid

fdir1 = './images/truth'
fdir2 = './images/new'

# import os
# import shutil

# # Define source and destination directories
# source_dir = '/home/fcao017/GeoDiff/experiments/NASA_16_10/results_logs/doc/images'
# destination_dir = '/home/fcao017/clean-fid/images'

# # Create the destination directory if it doesn't exist
# if not os.path.exists(destination_dir):
#     os.makedirs(destination_dir)

# # Iterate through the files in the source directory
# for filename in os.listdir(source_dir):
#     # Check if the file matches the specified patterns
#     if filename.startswith('groudtruth_') and filename.endswith('.png') or \
#        filename.startswith('samples_') and filename.endswith('.png'):
#         # Construct full file paths
#         src_file = os.path.join(source_dir, filename)
#         dest_file = os.path.join(destination_dir, filename)
#         # Copy the file to the destination directory
#         shutil.copy(src_file, dest_file)
#         print(f"Copied {filename} to {destination_dir}")

score = fid.compute_fid(fdir1, fdir2)
print(score)