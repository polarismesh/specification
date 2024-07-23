use std::io::Result;
use std::path::PathBuf;

fn main() -> Result<()> {
    let proto_dir: PathBuf = "proto".into(); // rust proto file dir
    let mut proto_list = Vec::new(); // proto file list
    let lists = proto_dir.read_dir().expect("read proto dir failed");
    for entry_path in lists {
        if entry_path.as_ref().unwrap().path().is_file() {
            proto_list.push(entry_path.unwrap().path())
        }
    }

    let mut config = prost_build::Config::new();
    config.protoc_arg("--experimental_allow_proto3_optional");
    config.default_package_filename("specification");
    config
        .out_dir("src")
        .compile_protos(&proto_list, &["proto/"])
        .unwrap();

    tonic_build::configure()
        .build_server(true)
        .out_dir("src")
        .compile(&proto_list, &["proto/"])
        .unwrap();
    Ok(())
}
