#!/bin/bash

set -e

CURRENT_OS=$(uname -s | tr 'A-Z' 'a-z')
CURRENT_ARCH=$(uname -m | tr 'A-Z' 'a-z')

pushd ../..
workdir=$(pwd)
popd
model_dir=${workdir}/api/v1/model
service_manage_dir=${workdir}/api/v1/service_manage
traffic_manage_dir=${workdir}/api/v1/traffic_manage
fault_tolerance_dir=${workdir}/api/v1/fault_tolerance
config_manage_dir=${workdir}/api/v1/config_manage
security_dir=${workdir}/api/v1/security
ratelimiter_dir=${workdir}/api/v1/traffic_manage/ratelimiter
out_dir=${workdir}/source/go

# Function to scan .proto files in a directory
scan_proto_files() {
    local dir=$1
    local files=""
    for file in "$dir"/*.proto; do
        if [[ -f "$file" ]]; then
            files+=" $(basename "$file")"
        fi
    done
    echo "$files" | sed 's/^ //'
}

# Dynamically scan .proto files
proto_files_model=$(scan_proto_files "$model_dir")
proto_files_service_manage=$(scan_proto_files "$service_manage_dir")
proto_files_traffic_manage=$(scan_proto_files "$traffic_manage_dir")
proto_files_fault_tolerance=$(scan_proto_files "$fault_tolerance_dir")
proto_files_config_manage=$(scan_proto_files "$config_manage_dir")
proto_files_security=$(scan_proto_files "$security_dir")
proto_files_ratelimiter=$(scan_proto_files "$ratelimiter_dir")

if [[ "$CURRENT_OS" == "linux" || "$CURRENT_OS" == "darwin" ]]; then
    protoc_dir=${workdir}/source/protoc/protoc-${CURRENT_OS}-${CURRENT_ARCH}
    pushd "${protoc_dir}"/bin
    chmod +x *
    popd
    rm -rf "${out_dir}/api/v1"
    mkdir -p "${out_dir}/api/v1"
    # generate model
    pushd "${model_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path=. ${proto_files_model}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/model" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/model"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${fault_tolerance_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path="${model_dir}" \
        --proto_path=. ${proto_files_fault_tolerance}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/fault_tolerance" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/fault_tolerance"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${traffic_manage_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path="${model_dir}" \
        --proto_path=. ${proto_files_traffic_manage}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/traffic_manage" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/traffic_manage"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${config_manage_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path="${model_dir}" \
        --proto_path=. ${proto_files_config_manage}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/config_manage" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/config_manage"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${security_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path="${model_dir}" \
        --proto_path=. ${proto_files_security}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/security" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/security"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${service_manage_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path=. \
        --proto_path="${model_dir}" \
        --proto_path="${traffic_manage_dir}" \
        --proto_path="${fault_tolerance_dir}" \
        --proto_path="${security_dir}" \
        --proto_path=. ${proto_files_service_manage}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/service_manage" "${out_dir}/api/v1"
    pushd "${out_dir}/api/v1/service_manage"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    pushd "${ratelimiter_dir}"
    "${protoc_dir}"/bin/protoc \
        --plugin=protoc-gen-go="${protoc_dir}"/bin/protoc-gen-go \
        --go_out=plugins=grpc:"${out_dir}" \
        --proto_path="${protoc_dir}"/include \
        --proto_path=. ${proto_files_ratelimiter}
    mv "${out_dir}/github.com/polarismesh/specification/source/go/api/v1/traffic_manage/ratelimiter" "${out_dir}/api/v1/traffic_manage"
    pushd "${out_dir}/api/v1/traffic_manage/ratelimiter"
    "${protoc_dir}"/bin/protoc-go-inject-tag -input="*.pb.go"
    popd
    popd

    rm -rf "${out_dir}/github.com"
else
    docker run --rm -it -v "$(dirname $(pwd))":/app --workdir /app/source/go debian:buster bash build.sh
fi
