#!/bin/bash
# Tencent is pleased to support the open source community by making Polaris available.
#
# Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
#
# Licensed under the BSD 3-Clause License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

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
java_root_dir=${workdir}/source/java/polaris-specification
java_test_root_dir=${workdir}/source/java/polaris-specification-test
java_source_dir=${java_root_dir}/src/main

if [ ! -d "${java_source_dir}/proto" ]; then
  mkdir -p ${java_source_dir}/proto
fi
cp ${model_dir}/*.proto ${java_source_dir}/proto/
cp ${service_manage_dir}/*.proto ${java_source_dir}/proto/
cp ${traffic_manage_dir}/*.proto ${java_source_dir}/proto/
cp ${fault_tolerance_dir}/*.proto ${java_source_dir}/proto/
cp ${config_manage_dir}/*.proto ${java_source_dir}/proto/
cp ${security_dir}/*.proto ${java_source_dir}/proto/
cp ${traffic_manage_dir}/ratelimiter/*.proto ${java_source_dir}/proto/

version=`cat ${workdir}/VERSION`
echo $version
pushd ${java_root_dir}
cp pom.xml pom.xml.bak
sed -i "" "s/##VERSION##/${version}/g" pom.xml
mvn clean install
mv pom.xml.bak pom.xml
popd
pushd ${java_test_root_dir}
cp pom.xml pom.xml.bak
sed -i "" "s/##VERSION##/${version}/g" pom.xml
mvn clean install
mv pom.xml.bak pom.xml
popd

rm -rf ${java_source_dir}/proto

