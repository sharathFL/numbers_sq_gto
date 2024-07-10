# Use an official GPU-enabled TensorFlow image
# FROM tensorflow/tensorflow:2.13.0-gpu
FROM tensorflow/tensorflow:latest-gpu
# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
RUN apt-get update && apt-get install -y git
COPY requirements.txt /app
# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt
ARG USERNAME=dvc
ARG USER_UID=1000
ARG USER_GID=$USER_UID
#adding for joystick support without sudo
#https://www.reddit.com/r/linuxquestions/comments/bh4ex1/is_adding_a_user_to_input_group_secure/
#https://stackoverflow.com/questions/29357095/linux-how-to-get-group-id-from-group-name-and-vice-versa


# ARG INPUT_GID=107          

# in this build with osrf/ros:iron-desktop-full there is no "input" group but instead there is an "rdma" group
# which seems to be its equivalent(?..no source) 
RUN groupadd --gid $USER_GID $USERNAME \
    # && groupadd --gid $INPUT_GID input \
    # && groupadd --gid $INPUT_GID dialout \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
    # && usermod -a -G dialout  $USERNAME \
    # && usermod -a -G rdma  $USERNAME     
# Expose 10050
EXPOSE 10050
USER $USERNAME


# Run the Python script
CMD ["bash"]


# # Use the official Python base image
# FROM python:3.9

# # Set the working directory inside the container
# WORKDIR /app


# COPY requirements.txt /app
# # Install required libraries
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the Python script into the container
# COPY src /app/

# COPY ../params.yaml /app/

# # Run the Python script
# CMD ["bash"]
# #CMD ["python", "convert_to_xarray.py"]
