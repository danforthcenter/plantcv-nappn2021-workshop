#!/usr/bin/env python
import os
import argparse
import matplotlib
import numpy as np
from plantcv import plantcv as pcv
import argparse


def options():
    """Parse command-line options

    The options function was converted from the class options in Jupyter.
    Rather than hardcoding the inputs, input arguments with the same
    variable names are used to retrieve inputs from the commandline.

    """
    parser = argparse.ArgumentParser(description="PlantCV multi-plant workflow")
    parser.add_argument("--image", help="Input image", required=True)
    parser.add_argument("--result", help="Results file", required=True)
    parser.add_argument("--outdir", help="Output directory", required=True)
    parser.add_argument("--writeimg", help="Save output images", action="store_true")
    parser.add_argument("--debug", help="Set debug mode", default=None)
    args = parser.parse_args()
    return args


def main():
    """Main workflow"""
    # Parse command-line arguments
    args = options()
    pcv.params.debug_outdir = args.outdir
    pcv.params.debug = args.debug

    # Read input image
    img, path, filename = pcv.readimage(filename=args.image)

    # Rotate input image 1 degree
    rot_img = pcv.rotate(img=img, rotation_deg=1, crop=True)

    #### Create a mask and begin to clean it ####
    # Change color space for plant extraction
    a = pcv.rgb2gray_lab(rgb_img=rot_img, channel="a")

    # Threshold
    a_thresh = pcv.threshold.binary(gray_img=a, threshold=120, max_value=255, object_type='dark')

    # Remove small objects
    a_fill_image = pcv.fill(bin_img=a_thresh, size=50)

    # Dilate the white regions
    a_dilated = pcv.dilate(gray_img=a_fill_image, ksize=2, i=1)

    # Convert white areas into connected component contours (polygons)
    obj, obj_hierarchy = pcv.find_objects(img=rot_img, mask=a_dilated)

    # Create a grid of ROIs
    pcv.params.line_thickness = 10
    rois1, roi_hierarchy1 = pcv.roi.multi(img=rot_img, coord=(1260, 155), radius=150,
                                          spacing=(500, 415), nrows=6, ncols=4)

    # Create a plant ID list
    plant_id = range(0,len(rois1))

    # Copy the input image to plot on it
    img_copy = np.copy(rot_img)
    # Disable debug mode for the for loop
    pcv.params.debug = None
    # Loop over the ROIs
    for i in range(0, len(rois1)):
        # Retrieve the ith ROI
        roi = rois1[i]
        # Retrieve the ith ROI structure
        hierarchy = roi_hierarchy1[i]
        # Retrieve the ith plant ID
        id_label = plant_id[i]
        # Find objects. Filter the connected components by the ith ROI
        filtered_contours, filtered_hierarchy, filtered_mask, filtered_area = pcv.roi_objects(
            img=rot_img, roi_type="partial", roi_contour=roi, roi_hierarchy=hierarchy, object_contour=obj,
            obj_hierarchy=obj_hierarchy)

        # Skip empty pots
        if filtered_area > 0:
            # Combine objects together in each plant
            plant_contour, plant_mask = pcv.object_composition(img=rot_img, contours=filtered_contours, hierarchy=filtered_hierarchy)

            # Analyze the shape of each plant
            img_copy = pcv.analyze_object(img=img_copy, obj=plant_contour, mask=plant_mask, label=id_label)

    if args.writeimg:
        # Save the output image
        pcv.print_image(img_copy, os.path.join(args.outdir, filename + "_shapes.jpg"))

    # Save the results
    pcv.print_results(filename=args.result)


if __name__ == "__main__":
    main()
