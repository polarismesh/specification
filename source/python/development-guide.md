# polarismesh-specification Python 包

这个目录是协议桩包 `polarismesh-specification`。protobuf 与 gRPC 代码由 `build.py` 从仓库的 `api/v1` 生成，提交进 `src/`。版本号写在 `src/polarismesh_specification/__about__.py`，由 Hatchling 从这里读取。当前仓库中的版本是 `1.9.0.dev0`。

根目录的 `VERSION` 只给 Java 使用。Python 发版不读它。`1.9.0-SNAPSHOT` 不是合法的 Python 版本。

包要求 Python 3.10+，并依赖 `grpcio>=1.84.0` 和 `protobuf>=7.35.1,<8`。

## 版本号命名

写进 `__about__.py` 和上传到 PyPI 的版本必须符合 [PEP 440](https://peps.python.org/pep-0440/)。Hatchling 构建时会校验，PyPI 上传时也会校验。git tag 的写法不受这个限制；受限的是包里实际的版本字符串。

| 用途 | 写法 | 说明 |
| --- | --- | --- |
| 正式版 | `1.9.0` | 对应 tag `v1.9.0` |
| 预发布 | `1.9.0a1`、`1.9.0b1`、`1.9.0rc1` | `1.9.0-alpha.1` 合法，规范化后是 `1.9.0a1`。tag `v1.9.0-alpha.1` 对应 `1.9.0a1` |
| 开发版 | `1.9.0.dev0`、`1.9.0.dev1` | 仓库开发和 Snapshot 发布使用。低于同号的预发布版和正式版 |
| 补丁重发 | `1.9.0.post1` | 同一个正式版需要再发一次时使用 |
| 本地版本 | `1.9.0+git.5698b30` | 可以本地构建，PyPI 拒收 |

`#VERSION#`、`1.9.0-SNAPSHOT`、`latest` 都不能构建。

版本从低到高：

```text
1.9.0.dev1 < 1.9.0a1 < 1.9.0b1 < 1.9.0rc1 < 1.9.0 < 1.9.0.post1
```

因此 `main` 上保持 `1.9.0.dev0`。Snapshot 把它发布成 `1.9.0.devN` 后，仍然低于 `1.9.0a1`。依赖方使用 `polarismesh-specification>=1.9.0a1,<2` 时不会选中这些开发版。

上界 `<2` 需要保留。PyPI 上已有不含当前桩的 `2.0.0.0a0` 和 `2.0.0.0a1`。约束允许预发布却没有上界时，解析器会选中它们。`<2` 不包含 2 的预发布版本。

`main` 上不要写成即将发布或已经发布的正式版、预发布版，例如 `1.9.0` 或 `1.9.0a1`。也不要写成 `1.9.0a2.dev0` 这类更高的开发版：它高于 `1.9.0a1`，公开安装时会压过已经发布的预发布版。

PyPI 上同一个版本号只能上传一次，不能像 Maven SNAPSHOT 那样覆盖。发错后只能 yank，再使用新的版本号。

## 两种发布版本从哪来

发布时只改 CI 工作区里的 `__about__.py`，不提交回仓库，也不改已有 tag。仓库里可以一直保持 `1.9.0.dev0`，方便 git 和本地路径安装。打进 PyPI 的版本由对应工作流决定。

打包必须在仓库根目录执行 `python -m build source/python`。在 `source/python` 里执行时，这里的 `build.py` 会挡住 PyPA 的 `build` 模块。工作流打包的是仓库里已经提交的桩，不会重新运行 `build.py`。proto 有变化时，先在本地用 `grpcio-tools>=1.84.0` 运行 `python source/python/build.py`，再提交生成结果。

### Release-Python

工作流是 `.github/workflows/python-release.yaml`。发布 GitHub Release 时运行，也可以手动指定一个已有 tag。

它用 `packaging` 把 tag 转成 PEP 440 版本后写入包：

| tag | PyPI 版本 |
| --- | --- |
| `v1.9.0-alpha.1` | `1.9.0a1` |
| `v1.9.0` | `1.9.0` |

正式版 tag 用 `v1.9.0`。预发布 tag 用 `v1.9.0-alpha.N`，并在 GitHub Release 上勾选 pre-release。上传使用仓库 secret `PYPI_API_TOKEN`。

手动补发某个 tag 时，工作流 checkout 的是该 tag。tag 上没有的元数据或桩代码不会进入这次包。

### Snapshot-Python

工作流是 `.github/workflows/python-snapshot.yaml`。代码推送到 `main` 或 `release/*`，且本次变更包含 `source/python` 下的非 Markdown 文件，或包含这个工作流文件时运行。只改 proto 或其他语言不会发布 Python 开发版，因为这里打包的是已经提交的桩。

`__about__.py` 是开发版时才发布。正式版和预发布版会跳过。发布版本保留开发版点号前的基线，并把开发序号换成这次工作流的 run number。当前仓库版本会变成：

```text
1.9.0.dev0 -> 1.9.0.dev42
```

同一次 workflow 重跑时 run number 不变。上传步骤设置了 `skip-existing`，版本已经存在时不再失败。

## 依赖方怎么选版本

对外安装和 SDK 发版使用 PyPI 约束：

```toml
dependencies = [
    "polarismesh-specification>=1.9.0a1,<2",
]
```

下界要写出预发布号。只写 `>=1.9.0` 时，解析器不会选中 `1.9.0a1`。

本机或团队联调还没发布的协议时，用本地路径或 git `rev` 指向一次 `__about__.py` 已是合法版本的提交。git 源放在 `[tool.uv.sources]`，`dependencies` 里仍保留上面的普通约束。不要把 `git+https://...` 直接写进 `dependencies`，这种写法会进入 wheel 元数据，PyPI 拒收。

用 `rev` 锁定提交或 tag，不用 `branch = "main"`。`[tool.uv.sources]` 只影响 uv；pip 仍按 PyPI 约束安装。uv 也不会检查 source 的实际版本是否满足约束，约束需要和协议版本保持一致。
