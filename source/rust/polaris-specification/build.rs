extern crate prost_build;

use std::io::Result;

fn main() -> Result<()> {
    let mut config = prost_build::Config::new();
    config.protoc_arg("--experimental_allow_proto3_optional");
    config.default_package_filename("specification");
    config
        .out_dir("src")
        .compile_protos(
            &[
                "proto/config_file.proto",
                "proto/config_file_response.proto",
                "proto/grpc_config_api.proto",
                "proto/auth.proto",
                "proto/model.proto",
                "proto/namespace.proto",
                "proto/code.proto",
                "proto/client.proto",
                "proto/service.proto",
                "proto/request.proto",
                "proto/response.proto",
                "proto/grpcapi.proto",
                "proto/configrelease.proto",
                "proto/routing.proto",
                "proto/ratelimit.proto",
                "proto/circuitbreaker.proto",
                "proto/fault_detector.proto",
            ],
            &["proto/"],
        )
        .unwrap();
    Ok(())
}
