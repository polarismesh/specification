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

proto_files_model="model.proto namespace.proto code.proto"
proto_files_service_manage="client.proto service.proto request.proto response.proto grpcapi.proto configrelease.proto"
proto_files_traffic_manage="routing.proto ratelimit.proto"
proto_files_fault_tolerance="circuitbreaker.proto fault_detector.proto"
proto_files_config_manage="config_file.proto config_file_response.proto grpc_config_api.proto"
proto_files_security="auth.proto"

protoc_dir="protoc"
protoc_include="${workdir}/source/protoc/protoc-linux-x86_64/include"

python_root_dir=${workdir}/source/python
python_source_dir=${python_root_dir}/polarismesh_specification/api/v1

function detection_protoc() {
  protoc_dir=${workdir}/source/protoc/protoc-${CURRENT_OS}-${CURRENT_ARCH}
  protoc_dirs="protoc ${protoc_dir} /opt/homebrew/bin/protoc /usr/local/bin/protoc /usr/bin/protoc"
  for dir in ${protoc_dirs}; do
    if [ -x "${dir}" ]; then
      protoc_dir=${dir}
      break
    fi
  done
}

function check_dir_and_make() {
  if [ ! -d "$1" ]; then
    mkdir -p "$1"
  fi
}

function add_python_init() {
  dir=$1
  # shellcheck disable=SC2124
  files=${@:2}
  if [ -f "${dir}/__init__.py" ]; then
    rm "${dir}/__init__.py"
  fi
  # pyi
  if [ -f "${dir}/__init__.pyi" ]; then
    rm "${dir}/__init__.pyi"
  fi

  for file in ${files}; do
    # add import
    echo "from .${file%.*}_pb2 import *" >>"${dir}/__init__.py"
    echo "from .${file%.*}_pb2 import *" >>"${dir}/__init__.pyi"
  done
}

function gen_protoc_by_dir() {
  proto_dir=$1
  out_dir=$2
  include_path=$3
  # shellcheck disable=SC2124
  files=${@:4}
  check_dir_and_make "${out_dir}"
  pushd "${proto_dir}"

  proto_paths=()
  if [ "${include_path}" != "" ]; then
    for path in ${include_path//,/ }; do
      proto_paths+=("--proto_path=${workdir}/api/v1/${path}")
    done
  fi

  # shellcheck disable=SC2068
  # shellcheck disable=SC2215
  "${protoc_dir}" --proto_path=. ${files[@]} \
    --proto_path=${protoc_include} \
    --python_out=${out_dir} \
    --pyi_out=${out_dir} \
    "${proto_paths[@]}"

  add_python_init "${out_dir}" "${files}"

  popd
  echo "gen python source code in ${out_dir} done"
  echo
}

function check_and_fix_imports() {
  output_dir=$1

  function get_import_path() {
    name=$1
    # find $name_pb2.py in output_dirs
    for dir in ${output_dirs}; do
      if [ -f "${dir}/${name}.py" ]; then
        echo "${dir#${output_dir}/}"
        return
      fi
    done
  }

  echo "check and fix imports"
  echo "===================="
  echo "output_dir: ${output_dir}"

  output_dirs=$(find "${output_dir}" -type d)
  for dir in ${output_dirs}; do
    # find all *.py and *.pyi
    py_files=$(find "${dir}" -type f -name "*.py" -o -name "*.pyi")
    for file in ${py_files}; do
      cat "${file}" | while read -r line; do
        if [[ "${line}" =~ ^import.*_pb2.*$ ]]; then
          # import aaa as bbb

          # get aaa
          import_name=$(echo "${line}" | awk '{print $2}' | awk -F '.' '{print $1}')
          # get bbb
          as_name=$(echo "${line}" | awk '{print $4}')
          echo "import_name: ${import_name} as_name: ${as_name}"
          # find aaa in output_dirs, set to xxx
          import_path=$(get_import_path "${import_name}")
          # if find, replace line
          if [ "${import_path}" != "" ]; then
            # modify import to from ..xxx import aaa as bbb
            new_line="from ..${import_path} import ${import_name} as ${as_name}"
            sed -e "s#${line}#${new_line}#" -i "" "${file}"
          fi
        fi
      done
    done
  done

}

detection_protoc

gen_protoc_by_dir ${model_dir} ${python_source_dir}/model "" ${proto_files_model}
gen_protoc_by_dir ${service_manage_dir} ${python_source_dir}/service_manage "model,traffic_manage,fault_tolerance,config_manage,security" ${proto_files_service_manage}
gen_protoc_by_dir ${traffic_manage_dir} ${python_source_dir}/traffic_manage "model" ${proto_files_traffic_manage}
gen_protoc_by_dir ${fault_tolerance_dir} ${python_source_dir}/fault_tolerance "model" ${proto_files_fault_tolerance}
gen_protoc_by_dir ${config_manage_dir} ${python_source_dir}/config_manage "model" ${proto_files_config_manage}
gen_protoc_by_dir ${security_dir} ${python_source_dir}/security "" ${proto_files_security}

# 这个步骤可以手动进行修改
check_and_fix_imports "${python_source_dir}"
