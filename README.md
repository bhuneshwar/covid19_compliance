# COVID-19 Compliance
COVID-19 Face Mask and Social Distancing

## Table of Contents

- [Basic Overview](#basic-overview)
  - [Context](#context)
  - [Goal](#goal)
- [Dataset](#dataset)
  - [Initial Intake](#initial-intake)
  - [Cleaning Images](#cleaning-images)
- [Modeling](#modeling)
  - [Transfer Learning](#transfer-learning)
  - [Application](#application)
- [Face Capture and Video Processing](#face-capture-and-video-processing)
  - [Face Capture](#face-capture)
  - [Video Processing](#video-processing)
- [License](#license)

## Basic Overview

### Context

As of March 2020, the world changed when COVID-19 swept across the United States and the rest of the world. Stores were shutdown and interaction between people was halted. As the world begins to reopen, health officials urge people to wear face masks to help prevent the spread of COVID-19.

### Goal

Imagine that you're walking into Costco and you see this sign. There's an employee at the door cheaking for compliance.

<img align="right" src="https://github.com/tylerjwoods/covid19_compliance/blob/master/demo/costco.jpeg">

You walk into the store and only a minute later, you see a customer with their face mask off. There aren't enough employees to make sure every customer is KEEPING their mask on.

The goal of this project is to automatically detect if a person is wearing a face mask in images and videos.


## Dataset

### Initial Intake

### Cleaning Images

## Modeling

### Transfer Learning

### Application

<img align="right" src="https://github.com/tylerjwoods/covid19_compliance/blob/master/predicted_images/first_tyler.jpg">

The model does a good job of identifying wearing a mask. But what about no mask?

<img align="center" src="https://github.com/tylerjwoods/covid19_compliance/blob/master/predicted_images/first_no_mask_tyler.jpg" width="200" height="200" />

Here we see that, again, the model is doing a good job of predicting no mask. So what about if there's an image with both a person wearing a mask and a person not wearing a mask?

<img align="right" src="https://github.com/tylerjwoods/covid19_compliance/blob/master/predicted_images/first_tyler_malia.jpg">

Since the model is binary, i.e., it will predict 'mask' if it finds a mask anywhere in the image, the model found the face mask and predicted face mask. 

The next step would be for detecting faces. The program would be then be broken down into two steps:

1. Find faces in images

2. Predict if that face is wearing a mask

## Face Capture and Video Processing

### Face Capture

### Video Processing

![demo gif](https://github.com/tylerjwoods/covid19_compliance/blob/master/demo/tyler1.gif)