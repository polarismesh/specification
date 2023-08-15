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

$ErrorActionPreference = "Stop"

Push-Location ../..
$workdir = Get-Location | Foreach-Object { $_.Path }
Pop-Location

$model_dir = "${workdir}/api/v1/model"
$service_manage_dir = "${workdir}/api/v1/service_manage"
$traffic_manage_dir = "${workdir}/api/v1/traffic_manage"
$fault_tolerance_dir = "${workdir}/api/v1/fault_tolerance"
$config_manage_dir = "${workdir}/api/v1/config_manage"
$security_dir = "${workdir}/api/v1/security"

$java_root_dir = "${workdir}/source/java/polaris-specification"
$java_source_dir = "${java_root_dir}/src/main"

Copy-Item "${model_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${service_manage_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${traffic_manage_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${fault_tolerance_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${config_manage_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${security_dir}/*.proto" -Destination "${java_source_dir}/proto/"
Copy-Item "${traffic_manage_dir}/ratelimiter/*.proto" -Destination "${java_source_dir}/proto/"

Push-Location ${java_root_dir}
mvn clean install
Pop-Location

#Remove-Item "${java_source_dir}/proto/*.proto"