#!/bin/bash

set -e

pushd ../..
workdir=$(pwd)
popd

model_dir=${workdir}/api/v1/model
service_manage_dir=${workdir}/api/v1/service_manage
traffic_manage_dir=${workdir}/api/v1/traffic_manage
fault_tolerance_dir=${workdir}/api/v1/fault_tolerance
config_manage_dir=${workdir}/api/v1/config_manage
security_dir=${workdir}/api/v1/security

rust_root_dir=${workdir}/source/rust/polaris-specification

cp ${model_dir}/*.proto ${rust_root_dir}/proto/
cp ${service_manage_dir}/*.proto ${rust_root_dir}/proto/
cp ${traffic_manage_dir}/*.proto ${rust_root_dir}/proto/
cp ${fault_tolerance_dir}/*.proto ${rust_root_dir}/proto/
cp ${config_manage_dir}/*.proto ${rust_root_dir}/proto/
cp ${security_dir}/*.proto ${rust_root_dir}/proto/

pushd ${rust_root_dir}
cargo build --release
popd
