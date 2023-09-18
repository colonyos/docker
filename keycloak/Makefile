BUILD_IMAGE ?= colonyos/keycloak
PUSH_IMAGE ?= colonyos/keycloak

build:
	docker build -t $(BUILD_IMAGE) . --no-cache
push:
	docker tag $(BUILD_IMAGE) $(PUSH_IMAGE) 
	docker push $(PUSH_IMAGE)
