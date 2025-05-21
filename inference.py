from ultralytics import YOLO
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import torch
import cv2

labels = ['Mask', 'can', 'cellphone', 'electronics', 'gbottle', 'glove', 'metal', 'misc', 'net', 'pbag', 'pbottle',
          'plastic', 'rod', 'sunglasses', 'tire']

garbage = []
def detect(image):
    model = YOLO(r"yolov8m.pt")  # Using a pre-trained model
    results = model(image) 
    class_list = []

    for result in results:
        boxes = result.boxes
        class_list = boxes.cls.tolist()

    int_list = [int(num) for num in class_list]

    # Handle indices that are out of range for labels
    class_names = [labels[i] if i < len(labels) else 'Unknown' for i in int_list]

    garbage.extend(class_names)
    res_plotted = results[0].plot()
    return res_plotted, class_names
