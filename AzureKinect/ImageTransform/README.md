# Azure Kinect Offline Image Transformation
## Need
- Conect Any Azure Kinect to PCs

## Our Folders
- Depth Image : AzureKinectData/<yymmdd>//<subject_id>//<record_sequence>//<2_DepthImage>//<kinect_location>//*.png
- Calibration JSON : AzureKinectData/<yymmdd>//<subject_id>//<record_sequence>//<6_CameraInfo>//*.json

## WorkFlow
1. Get Original Depth Image
2. Get Captured Azure Kinect Camera Calibration JSON
3. Transformation DepthtoColorImage
4. Save Transformed Depth Image
