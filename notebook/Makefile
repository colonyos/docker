BUILD_IMAGE ?= colonyos/notebook
PUSH_IMAGE ?= colonyos/notebook:v1.0.12

build:
	docker build -t $(BUILD_IMAGE) . --no-cache
	#docker build -t $(BUILD_IMAGE) . 
push:
	docker tag $(BUILD_IMAGE) $(PUSH_IMAGE) 
	docker push $(PUSH_IMAGE)
run:
	docker tag $(BUILD_IMAGE) $(PUSH_IMAGE) 
	# podman run --rm --device nvidia.com/gpu=all -v $(pwd):/root --gpus all -p 18888:8888 colonyos/notebook
	docker run -v $(HOME):/root/home --gpus all -it -p 18888:8888 $(PUSH_IMAGE)

shell:
	docker tag $(BUILD_IMAGE) $(PUSH_IMAGE) 
	docker run -v $(HOME):/root/home --gpus all -it -p 18888:8888 $(PUSH_IMAGE) fish
