FROM byangintel/ubuntu_openvino
MAINTAINER yong.hu@intel.com
WORKDIR /opt/openvino

RUN apt-get update && apt-get install -y python-flask udev usb-modeswitch usbutils

COPY ubuntu_openvino_face_detect/face_detect /opt/face_detect 
RUN cd /opt/face_detect/ \
	&& mkdir build \
	&& cd build \
	&& source /opt/intel/computer_vision_sdk/bin/setupvars.sh \
	&& cmake -DCMAKE_BUILD_TYPE=Release ../ \
	&& make -j$(nproc)

ENTRYPOINT ["/usr/local/bin/tini", "-g", "/opt/face_detect/face_detect.sh", "--"]
