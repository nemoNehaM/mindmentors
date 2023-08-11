# mindmentors
The following file was created as part of ONE API Hackathon 2023-Christ Deemed To Be University

# Enhancing Classroom Dynamics with Facial Emotion Recognition

# Team Members
Abith K Sunil - 22122002  
Divya Mary Biji - 22122020  
Prakruthi R Rai - 22122035  
Neha Elizabeth Mathew - 22122133  
Surya Prakash V - 22122156

# Team Name
MindMentors

# Problem Statement

The lack of real-time recognition and response to students' emotional states in classrooms often hinders personalized learning, engagement, and well-being. Therefore, we need an empathetic, privacy-respecting solution that can analyze students' emotional cues for a more supportive learning environment. This study focuses on bridging the gap between educators' understanding of their learners and their social well-being in the classroom environment.

# Emotions:
Angry 😠  
Disgust 😧  
Fear 😨  
Happy 😃  
Sad 😞  
Surprise 😮  
Neutral 😐  

Dataset link - https://www.kaggle.com/datasets/aadityasinghal/facial-expression-dataset

# What We Offer

Real-time detection and interpretation of students' facial expressions.  
Valuable insights into emotional engagement, comprehension levels, and overall well-being.  
Enabled and tailored teaching strategies fostering an empathetic and inclusive learning environment.  
Comprehensive understanding of classroom dynamics and educational insights.  
Continuous updates and timely feedback to learners.

# A Fresh Approach

Instead of solely focusing on recognizing facial emotions, we take facial emotion recognition to the next level by creating an interactive emotion-based learning environment. Our goal is to build a system that can detect students' emotions and dynamically adapt classroom dynamics to create a more engaging and supportive learning experience, thereby transforming the landscape of educational platforms.

# Features

Emotion Detection  
Emotion Identification  
Personalization - Student-Teacher Approach  
Engagement Tracking  
Mental Health Monitoring and Inclusivity  
Real-time Feedback  
Data-Driven Insights  
Collaborative Learning  
Room for Action Research

# List of API Toolkits/Libraries

oneDNN  
oneMKL  
oneDAL  
OpenVINO
# Technologies Used
Pandas  
Numpy  
Tensorflow  
OpenCV  
Keras  
TensorFlow Hub
# Architecture Diagram
<img width="650" alt="Screenshot 2023-08-11 103415" src="https://github.com/nemoNehaM/mindmentors/assets/118044299/804bb340-c834-48a8-bebc-4169329d9435">

# Model Creation  
### 1) Using Transfer Learning(ResNet50)  
Transfer learning (TL) is a research problem in machine learning (ML) that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem. For example, knowledge gained while learning to recognize cars could apply when trying to recognize trucks. Reusing or transferring information from previously learned tasks to learning of new tasks has the potential to significantly improve the sample efficiency of a Data Scientist.  
<img width="635" alt="Screenshot 2023-08-11 131002" src="https://github.com/nemoNehaM/mindmentors/assets/118044299/04d9b03f-19ed-4a2e-8c8d-963031ed84f6">  
We have trained the model with ResNet50 and got the training accuracy of 43% and validation accuracy of 41% which is not acceptable because model is underfitted.This error is may be because the model was trained on rgb images and the data set contains grascale images.  
### 2) Using Convolutional Neural Network  
A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics. The architecture of a ConvNet is analogous to that of the connectivity pattern of Neurons in the Human Brain and was inspired by the organization of the Visual Cortex. Individual neurons respond to stimuli only in a restricted region of the visual field known as the Receptive Field. A collection of such fields overlap to cover the entire visual area.  
<img width="630" alt="Screenshot 2023-08-11 131031" src="https://github.com/nemoNehaM/mindmentors/assets/118044299/adf7a8cb-95e0-49cc-9db0-3030c261cd3a">  
• The training gave the accuracy of 74% and test accuracy of 64%. It seems excellent. So, I save the model and the detection i got from live video was excellent.

• One drawback of the system is the some Disgust faces are showing Neutral .Because less no. of disgust faces are given to train .This may be the reason.

• I thought it was a good score should improve the score.

• Thus I decided that I will deploy the model.  
# Estimated Cost

The primary expense for implementing the proposed solution will be the AI cameras to be installed in the classrooms. The cost of basic AI-enabled cameras in India typically ranges from 10,000 to 30,000 INR per camera. However, for a more extensive setup with advanced features and higher capabilities, the cost per camera can be in the range of 50,000 to 1,00,000 INR or more.


