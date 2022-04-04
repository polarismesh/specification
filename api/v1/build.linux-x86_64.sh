#!/bin/bash

# 安装protoc和protoc-gen-go插件
#
# 注意：
# grpc包引入github.com/golang/protobuf/proto v1.2.0
# protoc-gen-go插件和引入proto包的版本必须保持一致
#
# github.com/golang/protobuf/
#   protoc-gen-go：在pb.go文件中插入proto.ProtoPackageIsVersionX
#   proto：在lib.go中定义ProtoPackageIsVersionX
#
# ProtoPackageIsVersion并非表示proto2/proto3
# --plugin=protoc-gen-go=${PROTOC}/bin/protoc-gen-go
# --go_out=plugins=grpc:. \

set -x

PROTOC=../protoc/protoc-linux-x86_64

SERVICE_PROTO_PATH=service
TRAFFIC_CONTROL_PROTO_PATH=traffic-control
FAULT_TOLERANCE_PROTO_PATH=fault-tolerance
ACCESS_CONTROL_PROTO_PATH=access-control

PROTO=" \
namespace.proto \
service.proto \
instance.proto \
healthcheck.proto \
router.proto \
loadbalancer.proto \
circuitbreaker.proto \
faultdetector.proto \
limiter.proto \
authentication.proto \
"

# build proto for java

if [ -d "out/java" ];then
	rm -r out/java
fi

mkdir -p out/java

${PROTOC}/bin/protoc \
--java_out=out/java \
--proto_path=${PROTOC}/include \
--proto_path=${SERVICE_PROTO_PATH} \
--proto_path=${TRAFFIC_CONTROL_PROTO_PATH} \
--proto_path=${FAULT_TOLERANCE_PROTO_PATH} \
--proto_path=${ACCESS_CONTROL_PROTO_PATH} \
${PROTO}

# build proto for go

if [ -d "out/go" ];then
	rm -r out/go
fi

mkdir -p out/go

${PROTOC}/bin/protoc \
--plugin=protoc-gen-go=${PROTOC}/bin/protoc-gen-go \
--go_out=out/go \
--proto_path=${PROTOC}/include \
--proto_path=${SERVICE_PROTO_PATH} \
--proto_path=${TRAFFIC_CONTROL_PROTO_PATH} \
--proto_path=${FAULT_TOLERANCE_PROTO_PATH} \
--proto_path=${ACCESS_CONTROL_PROTO_PATH} \
${PROTO}

# build proto for cpp

if [ -d "out/cpp" ];then
	rm -r out/cpp
fi

mkdir -p out/cpp

${PROTOC}/bin/protoc \
--cpp_out=out/cpp \
--proto_path=${PROTOC}/include \
--proto_path=${SERVICE_PROTO_PATH} \
--proto_path=${TRAFFIC_CONTROL_PROTO_PATH} \
--proto_path=${FAULT_TOLERANCE_PROTO_PATH} \
--proto_path=${ACCESS_CONTROL_PROTO_PATH} \
${PROTO}
