/// 限流请求
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitRequest {
    /// 命令字
    #[prost(enumeration = "RateLimitCmd", tag = "1")]
    pub cmd: i32,
    /// 初始化请求
    #[prost(message, optional, tag = "2")]
    pub rate_limit_init_request: ::core::option::Option<RateLimitInitRequest>,
    /// 上报请求
    #[prost(message, optional, tag = "3")]
    pub rate_limit_report_request: ::core::option::Option<RateLimitReportRequest>,
    /// 批量初始化请求
    #[prost(message, optional, tag = "4")]
    pub rate_limit_batch_init_request: ::core::option::Option<RateLimitBatchInitRequest>,
}
/// 限流应答
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitResponse {
    /// 命令字
    #[prost(enumeration = "RateLimitCmd", tag = "1")]
    pub cmd: i32,
    /// 初始化应答
    #[prost(message, optional, tag = "2")]
    pub rate_limit_init_response: ::core::option::Option<RateLimitInitResponse>,
    /// 上报应答
    #[prost(message, optional, tag = "3")]
    pub rate_limit_report_response: ::core::option::Option<RateLimitReportResponse>,
    /// 批量初始化应答
    #[prost(message, optional, tag = "4")]
    pub rate_limit_batch_init_response: ::core::option::Option<
        RateLimitBatchInitResponse,
    >,
}
/// 初始化请求
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitInitRequest {
    /// 限流目标对象数据
    #[prost(message, optional, tag = "1")]
    pub target: ::core::option::Option<LimitTarget>,
    /// 客户端唯一标识
    #[prost(string, tag = "2")]
    pub client_id: ::prost::alloc::string::String,
    /// 限流规则信息
    #[prost(message, repeated, tag = "3")]
    pub totals: ::prost::alloc::vec::Vec<QuotaTotal>,
    /// 客户端可指定滑窗数，不指定用默认值
    #[prost(uint32, tag = "4")]
    pub slide_count: u32,
    /// 限流模式
    #[prost(enumeration = "Mode", tag = "5")]
    pub mode: i32,
}
/// 初始化应答
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitInitResponse {
    /// 应答错误码
    #[prost(uint32, tag = "1")]
    pub code: u32,
    /// 限流目标对象，回传给客户端
    #[prost(message, optional, tag = "2")]
    pub target: ::core::option::Option<LimitTarget>,
    /// 客户端的标识，与clientId对应，一个server全局唯一，上报时候带入
    #[prost(uint32, tag = "3")]
    pub client_key: u32,
    /// 计数器的标识
    #[prost(message, repeated, tag = "5")]
    pub counters: ::prost::alloc::vec::Vec<QuotaCounter>,
    /// 实际滑窗个数
    #[prost(uint32, tag = "6")]
    pub slide_count: u32,
    /// 限流server绝对时间，单位ms
    #[prost(int64, tag = "7")]
    pub timestamp: i64,
}
/// 批量初始化请求
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitBatchInitRequest {
    /// 每条规则汇总成一个Init请求
    #[prost(message, repeated, tag = "1")]
    pub request: ::prost::alloc::vec::Vec<RateLimitInitRequest>,
    /// 客户端唯一标识
    #[prost(string, tag = "2")]
    pub client_id: ::prost::alloc::string::String,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct LabeledQuotaCounter {
    /// 自定义标签
    #[prost(string, tag = "1")]
    pub labels: ::prost::alloc::string::String,
    /// 计数器的标识
    #[prost(message, repeated, tag = "2")]
    pub counters: ::prost::alloc::vec::Vec<QuotaCounter>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BatchInitResult {
    /// 应答错误码
    #[prost(uint32, tag = "1")]
    pub code: u32,
    /// 限流目标对象，回传给客户端，labels为规则
    #[prost(message, optional, tag = "2")]
    pub target: ::core::option::Option<LimitTarget>,
    /// 计数器的标识
    #[prost(message, repeated, tag = "3")]
    pub counters: ::prost::alloc::vec::Vec<LabeledQuotaCounter>,
    /// 实际滑窗个数
    #[prost(uint32, tag = "4")]
    pub slide_count: u32,
}
/// 批量初始化应答
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitBatchInitResponse {
    /// 应答错误码
    #[prost(uint32, tag = "1")]
    pub code: u32,
    /// 客户端的标识，与clientId对应，一个server全局唯一，上报时候带入
    #[prost(uint32, tag = "2")]
    pub client_key: u32,
    /// 限流server绝对时间，单位ms
    #[prost(int64, tag = "3")]
    pub timestamp: i64,
    /// 批量初始化结果
    #[prost(message, repeated, tag = "4")]
    pub result: ::prost::alloc::vec::Vec<BatchInitResult>,
}
/// 限流上报请求
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitReportRequest {
    /// 客户端标识
    #[prost(uint32, tag = "1")]
    pub client_key: u32,
    /// 已使用的配额数
    #[prost(message, repeated, tag = "2")]
    pub quota_uses: ::prost::alloc::vec::Vec<QuotaSum>,
    /// 配额发生的时间，单位ms
    #[prost(int64, tag = "3")]
    pub timestamp: i64,
}
/// 限流上报应答
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitReportResponse {
    #[prost(uint32, tag = "1")]
    pub code: u32,
    /// 剩余配额数
    #[prost(message, repeated, tag = "2")]
    pub quota_lefts: ::prost::alloc::vec::Vec<QuotaLeft>,
    /// 限流server绝对时间，单位ms
    #[prost(int64, tag = "3")]
    pub timestamp: i64,
}
/// 限流目标，针对哪部分数据进行限流
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct LimitTarget {
    /// 命名空间
    #[prost(string, tag = "1")]
    pub namespace: ::prost::alloc::string::String,
    /// 服务名
    #[prost(string, tag = "2")]
    pub service: ::prost::alloc::string::String,
    /// 自定义标签
    #[prost(string, tag = "3")]
    pub labels: ::prost::alloc::string::String,
    /// 批量自定义标签
    #[prost(string, repeated, tag = "4")]
    pub labels_list: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
/// 阈值配置的值
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QuotaTotal {
    /// 阈值模式
    #[prost(enumeration = "QuotaMode", tag = "1")]
    pub mode: i32,
    /// 单位秒
    #[prost(uint32, tag = "2")]
    pub duration: u32,
    /// 限流阈值
    #[prost(uint32, tag = "3")]
    pub max_amount: u32,
}
/// 限流计数器
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QuotaCounter {
    /// 单位秒
    #[prost(uint32, tag = "1")]
    pub duration: u32,
    /// bucket的标识，上报时候带入
    #[prost(uint32, tag = "2")]
    pub counter_key: u32,
    /// 剩余配额数，应答返回，允许为负数
    #[prost(int64, tag = "3")]
    pub left: i64,
    /// 实际限流模式
    #[prost(enumeration = "Mode", tag = "4")]
    pub mode: i32,
    /// 接入的客户端数量
    #[prost(uint32, tag = "5")]
    pub client_count: u32,
}
/// 客户端阈值使用统计
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QuotaSum {
    /// 计数器的标识，一个server全局唯一，上报时候带入
    #[prost(uint32, tag = "1")]
    pub counter_key: u32,
    /// 已使用的配额数，上报时候带入
    #[prost(uint32, tag = "2")]
    pub used: u32,
    /// 被限流数，上报时候带入
    #[prost(uint32, tag = "3")]
    pub limited: u32,
}
/// 客户端阈值使用统计，由服务端返回
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QuotaLeft {
    /// 计数器的标识，一个server全局唯一，上报时候带入
    #[prost(uint32, tag = "1")]
    pub counter_key: u32,
    /// 剩余配额数，应答返回，允许为负数
    #[prost(int64, tag = "2")]
    pub left: i64,
    /// 当前限流模式
    #[prost(enumeration = "Mode", tag = "3")]
    pub mode: i32,
    /// 接入的客户端数量
    #[prost(uint32, tag = "4")]
    pub client_count: u32,
}
/// 时间点对齐的请求
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct TimeAdjustRequest {}
/// 时间点对齐的应答
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct TimeAdjustResponse {
    /// 服务器时间点，毫秒
    #[prost(int64, tag = "1")]
    pub server_timestamp: i64,
}
/// 命令字
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum RateLimitCmd {
    Init = 0,
    Acquire = 1,
    BatchInit = 2,
    BatchAcquire = 3,
}
impl RateLimitCmd {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            RateLimitCmd::Init => "INIT",
            RateLimitCmd::Acquire => "ACQUIRE",
            RateLimitCmd::BatchInit => "BATCH_INIT",
            RateLimitCmd::BatchAcquire => "BATCH_ACQUIRE",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "INIT" => Some(Self::Init),
            "ACQUIRE" => Some(Self::Acquire),
            "BATCH_INIT" => Some(Self::BatchInit),
            "BATCH_ACQUIRE" => Some(Self::BatchAcquire),
            _ => None,
        }
    }
}
/// 限频模式
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum Mode {
    /// 自适应模式，根据历史流量自动调整
    Adaptive = 0,
    /// 批量抢占模式，客户端进行拉取，Server返回全量剩余配额
    BatchOccupy = 1,
    /// 批量分摊模式，客户端进行拉取，Server按比例进行分摊
    BatchShare = 2,
}
impl Mode {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            Mode::Adaptive => "ADAPTIVE",
            Mode::BatchOccupy => "BATCH_OCCUPY",
            Mode::BatchShare => "BATCH_SHARE",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "ADAPTIVE" => Some(Self::Adaptive),
            "BATCH_OCCUPY" => Some(Self::BatchOccupy),
            "BATCH_SHARE" => Some(Self::BatchShare),
            _ => None,
        }
    }
}
/// 阈值模式
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum QuotaMode {
    /// 整体阈值
    Whole = 0,
    /// 单机均分阈值
    Divide = 1,
}
impl QuotaMode {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            QuotaMode::Whole => "WHOLE",
            QuotaMode::Divide => "DIVIDE",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "WHOLE" => Some(Self::Whole),
            "DIVIDE" => Some(Self::Divide),
            _ => None,
        }
    }
}
