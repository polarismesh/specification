#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Namespace {
    #[prost(message, optional, tag = "1")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub owners: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub total_service_count: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "8")]
    pub total_health_instance_count: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "9")]
    pub total_instance_count: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "10")]
    pub user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "11")]
    pub group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "13")]
    pub remove_user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "14")]
    pub remove_group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "15")]
    pub editable: ::core::option::Option<bool>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Location {
    #[prost(message, optional, tag = "1")]
    pub region: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub zone: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub campus: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MatchString {
    #[prost(enumeration = "match_string::MatchStringType", tag = "1")]
    pub r#type: i32,
    #[prost(message, optional, tag = "2")]
    pub value: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(enumeration = "match_string::ValueType", tag = "3")]
    pub value_type: i32,
}
/// Nested message and enum types in `MatchString`.
pub mod match_string {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum MatchStringType {
        /// Equivalent match
        Exact = 0,
        /// Regular match
        Regex = 1,
        /// Not equals match
        NotEquals = 2,
        /// Include match
        In = 3,
        /// Not include match
        NotIn = 4,
        /// Range match
        Range = 5,
    }
    impl MatchStringType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                MatchStringType::Exact => "EXACT",
                MatchStringType::Regex => "REGEX",
                MatchStringType::NotEquals => "NOT_EQUALS",
                MatchStringType::In => "IN",
                MatchStringType::NotIn => "NOT_IN",
                MatchStringType::Range => "RANGE",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "EXACT" => Some(Self::Exact),
                "REGEX" => Some(Self::Regex),
                "NOT_EQUALS" => Some(Self::NotEquals),
                "IN" => Some(Self::In),
                "NOT_IN" => Some(Self::NotIn),
                "RANGE" => Some(Self::Range),
                _ => None,
            }
        }
    }
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum ValueType {
        Text = 0,
        Parameter = 1,
        Variable = 2,
    }
    impl ValueType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                ValueType::Text => "TEXT",
                ValueType::Parameter => "PARAMETER",
                ValueType::Variable => "VARIABLE",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "TEXT" => Some(Self::Text),
                "PARAMETER" => Some(Self::Parameter),
                "VARIABLE" => Some(Self::Variable),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct StringList {
    #[prost(string, repeated, tag = "1")]
    pub values: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
/// 汇总查询数据
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Summary {
    /// 服务总数
    #[prost(uint32, tag = "1")]
    pub total_service_count: u32,
    /// 健康实例总数
    #[prost(uint32, tag = "2")]
    pub total_health_instance_count: u32,
    /// 实例总数
    #[prost(uint32, tag = "3")]
    pub total_instance_count: u32,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Service {
    #[prost(message, optional, tag = "1")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(map = "string, string", tag = "3")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
    #[prost(message, optional, tag = "4")]
    pub ports: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub business: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub department: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub cmdb_mod1: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub cmdb_mod2: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub cmdb_mod3: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "10")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub owners: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "13")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "14")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "15")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "16")]
    pub platform_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "17")]
    pub total_instance_count: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "18")]
    pub healthy_instance_count: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "19")]
    pub user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "20")]
    pub group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "22")]
    pub remove_user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "23")]
    pub remove_group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "21")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "24")]
    pub editable: ::core::option::Option<bool>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ServiceAlias {
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub alias: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub alias_namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(enumeration = "AliasType", tag = "5")]
    pub r#type: i32,
    #[prost(message, optional, tag = "6")]
    pub owners: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub service_token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "10")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub editable: ::core::option::Option<bool>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Instance {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "21")]
    pub vpc_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub host: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub port: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "6")]
    pub protocol: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub version: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub priority: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "9")]
    pub weight: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "20")]
    pub enable_health_check: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "10")]
    pub health_check: ::core::option::Option<HealthCheck>,
    #[prost(message, optional, tag = "11")]
    pub healthy: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "12")]
    pub isolate: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "13")]
    pub location: ::core::option::Option<Location>,
    #[prost(map = "string, string", tag = "14")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
    #[prost(message, optional, tag = "15")]
    pub logic_set: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "16")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "17")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "18")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "19")]
    pub service_token: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HealthCheck {
    #[prost(enumeration = "health_check::HealthCheckType", tag = "1")]
    pub r#type: i32,
    #[prost(message, optional, tag = "2")]
    pub heartbeat: ::core::option::Option<HeartbeatHealthCheck>,
}
/// Nested message and enum types in `HealthCheck`.
pub mod health_check {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum HealthCheckType {
        Unknown = 0,
        Heartbeat = 1,
    }
    impl HealthCheckType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                HealthCheckType::Unknown => "UNKNOWN",
                HealthCheckType::Heartbeat => "HEARTBEAT",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "HEARTBEAT" => Some(Self::Heartbeat),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HeartbeatHealthCheck {
    #[prost(message, optional, tag = "1")]
    pub ttl: ::core::option::Option<u32>,
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum AliasType {
    Default = 0,
    Cl5sid = 1,
}
impl AliasType {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            AliasType::Default => "DEFAULT",
            AliasType::Cl5sid => "CL5SID",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "DEFAULT" => Some(Self::Default),
            "CL5SID" => Some(Self::Cl5sid),
            _ => None,
        }
    }
}
/// 规则所属服务以及命名空间
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Routing {
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 每个服务可以配置多条入站或者出站规则
    /// 对于每个请求，从上到下依次匹配，若命中则终止
    #[prost(message, repeated, tag = "3")]
    pub inbounds: ::prost::alloc::vec::Vec<Route>,
    #[prost(message, repeated, tag = "4")]
    pub outbounds: ::prost::alloc::vec::Vec<Route>,
    #[prost(message, optional, tag = "5")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub service_token: ::core::option::Option<::prost::alloc::string::String>,
    /// route rules for current service
    #[prost(message, repeated, tag = "21")]
    pub rules: ::prost::alloc::vec::Vec<RouteRule>,
}
/// deprecated: only for compatible to the old version server
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Route {
    /// 如果匹配Source规则，按照Destination路由
    /// 多个Source之间的关系为或
    #[prost(message, repeated, tag = "1")]
    pub sources: ::prost::alloc::vec::Vec<Source>,
    #[prost(message, repeated, tag = "2")]
    pub destinations: ::prost::alloc::vec::Vec<Destination>,
    /// extendInfo 用于承载一些额外信息
    /// case 1: 升级到 v2 版本时，记录对应到 v2 版本的 id 信息
    #[prost(map = "string, string", tag = "3")]
    pub extend_info: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
}
/// deprecated: only for compatible to the old version server
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Source {
    /// 主调方服务以及命名空间
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 主调方服务实例标签或者请求标签
    /// value支持正则匹配
    #[prost(map = "string, message", tag = "3")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        MatchString,
    >,
}
/// deprecated: only for compatible to the old version server
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Destination {
    /// 被调方服务以及命名空间
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 被调方服务实例标签
    /// value支持正则匹配
    #[prost(map = "string, message", tag = "3")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        MatchString,
    >,
    /// 根据服务名和服务实例metadata筛选符合条件的服务实例子集
    /// 服务实例子集可以设置优先级和权重
    /// 优先级：整型，范围[0, 9]，最高优先级为0
    /// 权重：整型
    /// 先按优先级路由，如果存在高优先级，不会使用低优先级
    /// 如果存在优先级相同的子集，再按权重分配
    /// 优先级和权重可以都不设置/设置一个/设置两个
    /// 如果部分设置优先级，部分没有设置，认为没有设置的优先级最低
    /// 如果部分设置权重，部分没有设置，认为没有设置的权重为0
    /// 如果全部没有设置权重，认为权重相同
    #[prost(message, optional, tag = "4")]
    pub priority: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "5")]
    pub weight: ::core::option::Option<u32>,
    /// 将请求转发到代理服务
    #[prost(message, optional, tag = "6")]
    pub transfer: ::core::option::Option<::prost::alloc::string::String>,
    /// 是否对该set执行隔离，隔离后，不会再分配流量
    #[prost(message, optional, tag = "7")]
    pub isolate: ::core::option::Option<bool>,
    /// 实例分组名
    #[prost(message, optional, tag = "8")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
}
/// configuration root for route
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RouteRule {
    #[prost(string, tag = "1")]
    pub id: ::prost::alloc::string::String,
    /// route rule name
    #[prost(string, tag = "2")]
    pub name: ::prost::alloc::string::String,
    /// namespace namingspace of routing rules
    #[prost(string, tag = "3")]
    pub namespace: ::prost::alloc::string::String,
    /// Enable this router
    #[prost(bool, tag = "4")]
    pub enable: bool,
    /// Router type
    #[prost(enumeration = "RoutingPolicy", tag = "5")]
    pub routing_policy: i32,
    /// Routing configuration for router
    #[prost(message, optional, tag = "6")]
    pub routing_config: ::core::option::Option<::prost_types::Any>,
    /// revision routing version
    #[prost(string, tag = "7")]
    pub revision: ::prost::alloc::string::String,
    /// ctime create time of the rules
    #[prost(string, tag = "8")]
    pub ctime: ::prost::alloc::string::String,
    /// mtime modify time of the rules
    #[prost(string, tag = "9")]
    pub mtime: ::prost::alloc::string::String,
    /// etime enable time of the rules
    #[prost(string, tag = "10")]
    pub etime: ::prost::alloc::string::String,
    /// priority rules priority
    #[prost(uint32, tag = "11")]
    pub priority: u32,
    /// description simple description rules
    #[prost(string, tag = "12")]
    pub description: ::prost::alloc::string::String,
    /// extendInfo 用于承载一些额外信息
    /// case 1: 升级到 v2 版本时，记录对应到 v1 版本的 id 信息
    #[prost(map = "string, string", tag = "20")]
    pub extend_info: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MetadataFailover {
    /// failover_range metadata route bottom type
    #[prost(enumeration = "metadata_failover::FailoverRange", tag = "1")]
    pub failover_range: i32,
    /// only use to failover_range == OTHER_KEYS
    #[prost(map = "string, string", tag = "2")]
    pub labels: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
}
/// Nested message and enum types in `MetadataFailover`.
pub mod metadata_failover {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum FailoverRange {
        /// ALL return all instances
        All = 0,
        /// OTHERS retuen without thie labels instances
        Others = 1,
        /// OTHER_KEYS return other instances which match keys
        OtherKeys = 2,
    }
    impl FailoverRange {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                FailoverRange::All => "ALL",
                FailoverRange::Others => "OTHERS",
                FailoverRange::OtherKeys => "OTHER_KEYS",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "ALL" => Some(Self::All),
                "OTHERS" => Some(Self::Others),
                "OTHER_KEYS" => Some(Self::OtherKeys),
                _ => None,
            }
        }
    }
}
/// MetadataRoutingConfig metadata routing configuration
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MetadataRoutingConfig {
    /// service
    #[prost(string, tag = "1")]
    pub service: ::prost::alloc::string::String,
    /// namespace
    #[prost(string, tag = "2")]
    pub namespace: ::prost::alloc::string::String,
    #[prost(map = "string, string", tag = "3")]
    pub labels: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
    /// When metadata not found, it will fall back to the
    #[prost(message, optional, tag = "4")]
    pub failover: ::core::option::Option<MetadataFailover>,
}
/// RuleRoutingConfig routing configuration
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RuleRoutingConfig {
    /// source source info
    /// deprecated: only for compatible to the old version server
    #[prost(message, repeated, tag = "1")]
    pub sources: ::prost::alloc::vec::Vec<SourceService>,
    /// destination destinations info
    /// deprecated: only for compatible to the old version server
    #[prost(message, repeated, tag = "2")]
    pub destinations: ::prost::alloc::vec::Vec<DestinationGroup>,
    /// rule route chain
    #[prost(message, repeated, tag = "3")]
    pub rules: ::prost::alloc::vec::Vec<SubRuleRouting>,
}
/// SubRuleRouting sub routing configuration
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SubRuleRouting {
    /// sub routing rule name
    #[prost(string, tag = "1")]
    pub name: ::prost::alloc::string::String,
    /// source source info
    #[prost(message, repeated, tag = "2")]
    pub sources: ::prost::alloc::vec::Vec<SourceService>,
    /// destination destinations info
    #[prost(message, repeated, tag = "3")]
    pub destinations: ::prost::alloc::vec::Vec<DestinationGroup>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SourceService {
    /// Main tuning service and namespace
    #[prost(string, tag = "1")]
    pub service: ::prost::alloc::string::String,
    #[prost(string, tag = "2")]
    pub namespace: ::prost::alloc::string::String,
    /// Master Control Service Example Tag or Request Label
    /// Value supports regular matching
    #[prost(message, repeated, tag = "3")]
    pub arguments: ::prost::alloc::vec::Vec<SourceMatch>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DestinationGroup {
    /// Templated service and namespace
    #[prost(string, tag = "1")]
    pub service: ::prost::alloc::string::String,
    #[prost(string, tag = "2")]
    pub namespace: ::prost::alloc::string::String,
    /// Templated service example label
    /// Value supports regular matching
    #[prost(map = "string, message", tag = "3")]
    pub labels: ::std::collections::HashMap<::prost::alloc::string::String, MatchString>,
    /// According to the service name and service instance Metadata Filter the
    /// qualified service instance subset Service instance subset can set priority
    /// and weight Priority: integer, range [0, 9], the highest priority is 0
    /// Weight: Integer
    /// Press priority routing, if there is high priority, low priority will not
    /// use If there is a subset of the same priority, then assign by weight
    /// Priority and weight can be not set / set up one / set two
    /// If the section is set priority, some are not set, it is considered that the
    /// priority is not set. If the part is set, some is not set, it is considered
    /// that the weight is not set to 0 If you have no weight, you think the weight
    /// is the same
    #[prost(uint32, tag = "4")]
    pub priority: u32,
    #[prost(uint32, tag = "5")]
    pub weight: u32,
    /// Forward requests to proxy service
    #[prost(string, tag = "6")]
    pub transfer: ::prost::alloc::string::String,
    /// Whether to isolate the SET, after isolation, no traffic will be allocated
    #[prost(bool, tag = "7")]
    pub isolate: bool,
    /// name desition name
    #[prost(string, tag = "8")]
    pub name: ::prost::alloc::string::String,
}
/// SourceMatch
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SourceMatch {
    #[prost(enumeration = "source_match::Type", tag = "1")]
    pub r#type: i32,
    /// header key or query key
    #[prost(string, tag = "2")]
    pub key: ::prost::alloc::string::String,
    /// header value or query value
    #[prost(message, optional, tag = "3")]
    pub value: ::core::option::Option<MatchString>,
}
/// Nested message and enum types in `SourceMatch`.
pub mod source_match {
    /// label type for gateway request
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Type {
        /// custom arguments
        Custom = 0,
        /// method, match the http post/get/put/delete or grpc method
        Method = 1,
        /// header, match the http header, dubbo attachment, grpc header
        Header = 2,
        /// query, match the http query, dubbo argument
        Query = 3,
        /// caller host ip
        CallerIp = 4,
        /// path, math the http url
        Path = 5,
        /// cookie match http cookie
        Cookie = 6,
    }
    impl Type {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Type::Custom => "CUSTOM",
                Type::Method => "METHOD",
                Type::Header => "HEADER",
                Type::Query => "QUERY",
                Type::CallerIp => "CALLER_IP",
                Type::Path => "PATH",
                Type::Cookie => "COOKIE",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "CUSTOM" => Some(Self::Custom),
                "METHOD" => Some(Self::Method),
                "HEADER" => Some(Self::Header),
                "QUERY" => Some(Self::Query),
                "CALLER_IP" => Some(Self::CallerIp),
                "PATH" => Some(Self::Path),
                "COOKIE" => Some(Self::Cookie),
                _ => None,
            }
        }
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum RoutingPolicy {
    /// Route by rule rule => RuleRoutingConfig
    RulePolicy = 0,
    /// Route by destination metadata ==> MetadataRoutingConfig
    MetadataPolicy = 1,
}
impl RoutingPolicy {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            RoutingPolicy::RulePolicy => "RulePolicy",
            RoutingPolicy::MetadataPolicy => "MetadataPolicy",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "RulePolicy" => Some(Self::RulePolicy),
            "MetadataPolicy" => Some(Self::MetadataPolicy),
            _ => None,
        }
    }
}
/// 同一服务下限流规则集合
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimit {
    /// 限流规则集合
    #[prost(message, repeated, tag = "1")]
    pub rules: ::prost::alloc::vec::Vec<Rule>,
    /// 限流规则汇总的revision信息
    #[prost(message, optional, tag = "2")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
}
/// 单个限流规则信息
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Rule {
    /// 限流规则唯一标识
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则所属服务名
    #[prost(message, optional, tag = "2")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则所属命名空间
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 可选，SUBSET标识
    #[prost(map = "string, message", tag = "4")]
    pub subset: ::std::collections::HashMap<::prost::alloc::string::String, MatchString>,
    /// 限流规则优先级，0值最高
    #[prost(message, optional, tag = "5")]
    pub priority: ::core::option::Option<u32>,
    #[prost(enumeration = "rule::Resource", tag = "6")]
    pub resource: i32,
    #[prost(enumeration = "rule::Type", tag = "7")]
    pub r#type: i32,
    /// 业务标签集合，通过KV进行匹配，全部匹配才使用该规则
    #[prost(map = "string, message", tag = "8")]
    pub labels: ::std::collections::HashMap<::prost::alloc::string::String, MatchString>,
    /// 限流阈值
    /// 可以有多个粒度的配置（比如同时针对秒级，分钟级，天级），匹配一个则进行限流
    /// 全局限流模式下，该值为服务配额总量；单机限流模式下，该值为单个节点能处理的配额量
    #[prost(message, repeated, tag = "9")]
    pub amounts: ::prost::alloc::vec::Vec<Amount>,
    /// 限流动作，对应着客户端的插件名字
    #[prost(message, optional, tag = "10")]
    pub action: ::core::option::Option<::prost::alloc::string::String>,
    /// 是否停用该限流规则，默认启用
    #[prost(message, optional, tag = "11")]
    pub disable: ::core::option::Option<bool>,
    /// 限流上报方式，同时支持按固定周期上报，以及达到配额百分比后上报
    #[prost(message, optional, tag = "12")]
    pub report: ::core::option::Option<Report>,
    /// 限流规则创建时间
    #[prost(message, optional, tag = "13")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则修改时间
    #[prost(message, optional, tag = "14")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则revision信息
    #[prost(message, optional, tag = "15")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
    /// 服务的TOKEN信息，仅用于控制台，discover接口不下发
    #[prost(message, optional, tag = "16")]
    pub service_token: ::core::option::Option<::prost::alloc::string::String>,
    /// 配额调整算法
    #[prost(message, optional, tag = "17")]
    pub adjuster: ::core::option::Option<AmountAdjuster>,
    /// 通配符是否合并计算，默认分开计数
    #[prost(message, optional, tag = "18")]
    pub regex_combine: ::core::option::Option<bool>,
    #[prost(enumeration = "rule::AmountMode", tag = "19")]
    pub amount_mode: i32,
    #[prost(enumeration = "rule::FailoverType", tag = "20")]
    pub failover: i32,
    /// 分布式限流服务集群
    #[prost(message, optional, tag = "21")]
    pub cluster: ::core::option::Option<RateLimitCluster>,
    /// 被调接口名
    #[prost(message, optional, tag = "22")]
    pub method: ::core::option::Option<MatchString>,
    /// 被调的参数过滤条件，满足过滤条件才进入限流规则
    #[prost(message, repeated, tag = "23")]
    pub arguments: ::prost::alloc::vec::Vec<MatchArgument>,
    /// 限流规则名
    #[prost(message, optional, tag = "24")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则启用时间
    #[prost(message, optional, tag = "25")]
    pub etime: ::core::option::Option<::prost::alloc::string::String>,
    /// 最大排队时长，单位秒
    #[prost(message, optional, tag = "26")]
    pub max_queue_delay: ::core::option::Option<u32>,
}
/// Nested message and enum types in `Rule`.
pub mod rule {
    /// 限流资源
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Resource {
        /// 针对QPS进行限流
        Qps = 0,
        /// 针对并发数进行限流
        Concurrency = 1,
    }
    impl Resource {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Resource::Qps => "QPS",
                Resource::Concurrency => "CONCURRENCY",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "QPS" => Some(Self::Qps),
                "CONCURRENCY" => Some(Self::Concurrency),
                _ => None,
            }
        }
    }
    /// 限流类型
    /// global全局限流(默认)或者local单机限流
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Type {
        Global = 0,
        Local = 1,
    }
    impl Type {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Type::Global => "GLOBAL",
                Type::Local => "LOCAL",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "GLOBAL" => Some(Self::Global),
                "LOCAL" => Some(Self::Local),
                _ => None,
            }
        }
    }
    /// 限流阈值模
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum AmountMode {
        /// 总体阈值
        GlobalTotal = 0,
        /// 单机均摊阈值
        ShareEqually = 1,
    }
    impl AmountMode {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                AmountMode::GlobalTotal => "GLOBAL_TOTAL",
                AmountMode::ShareEqually => "SHARE_EQUALLY",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "GLOBAL_TOTAL" => Some(Self::GlobalTotal),
                "SHARE_EQUALLY" => Some(Self::ShareEqually),
                _ => None,
            }
        }
    }
    /// 与限流集群连接失败时降级模式
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum FailoverType {
        /// 降级成本地阈值
        FailoverLocal = 0,
        /// 降级成直接通过
        FailoverPass = 1,
    }
    impl FailoverType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                FailoverType::FailoverLocal => "FAILOVER_LOCAL",
                FailoverType::FailoverPass => "FAILOVER_PASS",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "FAILOVER_LOCAL" => Some(Self::FailoverLocal),
                "FAILOVER_PASS" => Some(Self::FailoverPass),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MatchArgument {
    #[prost(enumeration = "match_argument::Type", tag = "1")]
    pub r#type: i32,
    /// header key or query key
    #[prost(string, tag = "2")]
    pub key: ::prost::alloc::string::String,
    /// header value or query value
    #[prost(message, optional, tag = "3")]
    pub value: ::core::option::Option<MatchString>,
}
/// Nested message and enum types in `MatchArgument`.
pub mod match_argument {
    /// label type for gateway request
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Type {
        /// custom arguments
        Custom = 0,
        /// method, match the http post/get/put/delete or grpc method
        Method = 1,
        /// header, match the http header, dubbo attachment, grpc header
        Header = 2,
        /// query, match the http query, dubbo argument
        Query = 3,
        /// caller service
        CallerService = 4,
        /// caller host ip
        CallerIp = 5,
    }
    impl Type {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Type::Custom => "CUSTOM",
                Type::Method => "METHOD",
                Type::Header => "HEADER",
                Type::Query => "QUERY",
                Type::CallerService => "CALLER_SERVICE",
                Type::CallerIp => "CALLER_IP",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "CUSTOM" => Some(Self::Custom),
                "METHOD" => Some(Self::Method),
                "HEADER" => Some(Self::Header),
                "QUERY" => Some(Self::Query),
                "CALLER_SERVICE" => Some(Self::CallerService),
                "CALLER_IP" => Some(Self::CallerIp),
                _ => None,
            }
        }
    }
}
/// 分布式限流服务集群
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RateLimitCluster {
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    /// 限流规则所属命名空间
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
}
/// 限流配额
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Amount {
    /// 时间周期内的最大配额数
    #[prost(message, optional, tag = "1")]
    pub max_amount: ::core::option::Option<u32>,
    /// 配额生效的时间周期，必须大于等于1s
    #[prost(message, optional, tag = "2")]
    pub valid_duration: ::core::option::Option<::prost_types::Duration>,
    /// 请求统计精度
    #[prost(message, optional, tag = "3")]
    pub precision: ::core::option::Option<u32>,
    /// 可选，起始限流阈值，爬坡起始值
    #[prost(message, optional, tag = "4")]
    pub start_amount: ::core::option::Option<u32>,
    /// 可选，最小限流阈值，降低时最小值
    #[prost(message, optional, tag = "5")]
    pub min_amount: ::core::option::Option<u32>,
}
/// 限流上报方式
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Report {
    /// 配额固定上报周期，单位毫秒
    #[prost(message, optional, tag = "1")]
    pub interval: ::core::option::Option<::prost_types::Duration>,
    /// 使用了百分之多少配额后启动一次实时上报，值范围(0,100]
    #[prost(message, optional, tag = "2")]
    pub amount_percent: ::core::option::Option<u32>,
}
/// 配额调整算法
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct AmountAdjuster {
    #[prost(message, optional, tag = "1")]
    pub climb: ::core::option::Option<ClimbConfig>,
}
/// 限流调整算法Climb相关配置
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ClimbConfig {
    /// 是否开启
    #[prost(message, optional, tag = "1")]
    pub enable: ::core::option::Option<bool>,
    /// 限流数据统计配置
    #[prost(message, optional, tag = "2")]
    pub metric: ::core::option::Option<climb_config::MetricConfig>,
    /// 触发调整策略
    #[prost(message, optional, tag = "3")]
    pub policy: ::core::option::Option<climb_config::TriggerPolicy>,
    /// 限流调整相关参数
    #[prost(message, optional, tag = "4")]
    pub throttling: ::core::option::Option<climb_config::ClimbThrottling>,
}
/// Nested message and enum types in `ClimbConfig`.
pub mod climb_config {
    /// 限流数据统计配置
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct MetricConfig {
        /// 限流数据度量周期，默认60s
        #[prost(message, optional, tag = "1")]
        pub window: ::core::option::Option<::prost_types::Duration>,
        /// 数据统计精度，决定数据度量的最小周期，度量滑窗的步长=window/precision
        #[prost(message, optional, tag = "2")]
        pub precision: ::core::option::Option<u32>,
        /// 上报周期，默认20s
        #[prost(message, optional, tag = "3")]
        pub report_interval: ::core::option::Option<::prost_types::Duration>,
    }
    /// 触发调整的策略
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct TriggerPolicy {
        /// 按错误率阈值调整
        #[prost(message, optional, tag = "1")]
        pub error_rate: ::core::option::Option<trigger_policy::ErrorRate>,
        /// 慢调用进行触发调整
        #[prost(message, optional, tag = "2")]
        pub slow_rate: ::core::option::Option<trigger_policy::SlowRate>,
    }
    /// Nested message and enum types in `TriggerPolicy`.
    pub mod trigger_policy {
        /// 错误率触发调整配置
        #[allow(clippy::derive_partial_eq_without_eq)]
        #[derive(Clone, PartialEq, ::prost::Message)]
        pub struct ErrorRate {
            /// 是否开启
            #[prost(message, optional, tag = "1")]
            pub enable: ::core::option::Option<bool>,
            /// 触发限流调整的最小的请求数
            #[prost(message, optional, tag = "2")]
            pub request_volume_threshold: ::core::option::Option<u32>,
            /// 触发限流的错误率配置
            #[prost(message, optional, tag = "3")]
            pub error_rate: ::core::option::Option<i32>,
            /// 针对部分错误码，使用额外的错误率统计，可设置多组特殊规则
            #[prost(message, repeated, tag = "4")]
            pub specials: ::prost::alloc::vec::Vec<error_rate::SpecialConfig>,
        }
        /// Nested message and enum types in `ErrorRate`.
        pub mod error_rate {
            /// 特殊错误码触发调整配置
            #[allow(clippy::derive_partial_eq_without_eq)]
            #[derive(Clone, PartialEq, ::prost::Message)]
            pub struct SpecialConfig {
                /// 自定义错误类型
                #[prost(message, optional, tag = "1")]
                pub r#type: ::core::option::Option<::prost::alloc::string::String>,
                /// 特定规则针对的错误码
                #[prost(message, repeated, tag = "2")]
                pub error_codes: ::prost::alloc::vec::Vec<i64>,
                /// 特定规则错误率
                #[prost(message, optional, tag = "3")]
                pub error_rate: ::core::option::Option<i32>,
            }
        }
        /// 慢调用触发调整配置
        #[allow(clippy::derive_partial_eq_without_eq)]
        #[derive(Clone, PartialEq, ::prost::Message)]
        pub struct SlowRate {
            /// 是否开启
            #[prost(message, optional, tag = "1")]
            pub enable: ::core::option::Option<bool>,
            /// 最大响应时间，超过该响应时间属于慢调用
            #[prost(message, optional, tag = "2")]
            pub max_rt: ::core::option::Option<::prost_types::Duration>,
            /// 慢请求率阈值，达到该阈值进行限流
            #[prost(message, optional, tag = "3")]
            pub slow_rate: ::core::option::Option<i32>,
        }
    }
    /// 爬坡调整相关参数
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct ClimbThrottling {
        /// 冷水位以下区间的下调百分比
        #[prost(message, optional, tag = "1")]
        pub cold_below_tune_down_rate: ::core::option::Option<i32>,
        /// 冷水位以下区间的上调百分比
        #[prost(message, optional, tag = "2")]
        pub cold_below_tune_up_rate: ::core::option::Option<i32>,
        /// 冷水位以上区间的下调百分比
        #[prost(message, optional, tag = "3")]
        pub cold_above_tune_down_rate: ::core::option::Option<i32>,
        /// 冷水位以上区间的上调百分比
        #[prost(message, optional, tag = "4")]
        pub cold_above_tune_up_rate: ::core::option::Option<i32>,
        /// 冷水位以上，超过该百分的请求被限流后进行阈值上调
        #[prost(message, optional, tag = "5")]
        pub limit_threshold_to_tune_up: ::core::option::Option<i32>,
        /// 阈值调整规则的决策间隔
        #[prost(message, optional, tag = "6")]
        pub judge_duration: ::core::option::Option<::prost_types::Duration>,
        /// 阈值上调周期数，连续N个决策间隔都为上调，才执行上调
        #[prost(message, optional, tag = "7")]
        pub tune_up_period: ::core::option::Option<i32>,
        /// 阈值下调周期数，连续N个决策间隔都为下调，才执行下调
        #[prost(message, optional, tag = "8")]
        pub tune_down_period: ::core::option::Option<i32>,
    }
}
/// 单个熔断规则定义
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CircuitBreaker {
    /// deprecated
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    /// 规则版本
    /// deprecated
    #[prost(message, optional, tag = "2")]
    pub version: ::core::option::Option<::prost::alloc::string::String>,
    /// 规则名
    /// deprecated
    #[prost(message, optional, tag = "3")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    /// 规则命名空间
    /// deprecated
    #[prost(message, optional, tag = "4")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 规则所属服务
    #[prost(message, optional, tag = "5")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub service_namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 熔断规则可以分为被调规则和主调规则
    /// 被调规则针对所有的指定主调生效，假如不指定则对所有的主调生效
    /// 主调规则为当前主调方的规则，假如不指定则针对所有被调生效
    /// deprecated
    #[prost(message, repeated, tag = "7")]
    pub inbounds: ::prost::alloc::vec::Vec<CbRule>,
    /// deprecated
    #[prost(message, repeated, tag = "8")]
    pub outbounds: ::prost::alloc::vec::Vec<CbRule>,
    /// deprecated
    #[prost(message, optional, tag = "9")]
    pub token: ::core::option::Option<::prost::alloc::string::String>,
    /// deprecated
    #[prost(message, optional, tag = "10")]
    pub owners: ::core::option::Option<::prost::alloc::string::String>,
    /// 业务
    /// deprecated
    #[prost(message, optional, tag = "11")]
    pub business: ::core::option::Option<::prost::alloc::string::String>,
    /// 部门
    /// deprecated
    #[prost(message, optional, tag = "12")]
    pub department: ::core::option::Option<::prost::alloc::string::String>,
    /// 规则描述
    /// deprecated
    #[prost(message, optional, tag = "13")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    /// deprecated
    #[prost(message, optional, tag = "14")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    /// deprecated
    #[prost(message, optional, tag = "15")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "16")]
    pub revision: ::core::option::Option<::prost::alloc::string::String>,
    /// circuitbreaker rules for current service
    #[prost(message, repeated, tag = "21")]
    pub rules: ::prost::alloc::vec::Vec<CircuitBreakerRule>,
}
/// 主调匹配规则
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SourceMatcher {
    /// 主调命名空间以及服务名，可以为*，代表全匹配
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 可选，主调业务标签，用于匹配是否使用该熔断规则，可放置用户的接口信息等
    #[prost(map = "string, message", tag = "3")]
    pub labels: ::std::collections::HashMap<::prost::alloc::string::String, MatchString>,
}
/// 熔断恢复配置
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RecoverConfig {
    /// 触发熔断后到半开状态之间的等待间隔
    #[prost(message, optional, tag = "1")]
    pub sleep_window: ::core::option::Option<::prost_types::Duration>,
    /// 半开后，最多重试多少次恢复
    #[prost(message, optional, tag = "2")]
    pub max_retry_after_half_open: ::core::option::Option<u32>,
    /// 半开后放量的最大百分比
    #[prost(message, repeated, tag = "3")]
    pub request_rate_after_half_open: ::prost::alloc::vec::Vec<u32>,
    /// 熔断器半开到关闭所必须的最少成功率，默认100%
    #[prost(message, optional, tag = "4")]
    pub success_rate_to_close: ::core::option::Option<u32>,
    /// 半开后最大放量数（用户不配置最大百分比时默认使用该配置）
    #[prost(message, optional, tag = "5")]
    pub request_count_after_half_open: ::core::option::Option<u32>,
    #[prost(enumeration = "recover_config::OutlierDetectWhen", tag = "6")]
    pub outlier_detect_when: i32,
}
/// Nested message and enum types in `RecoverConfig`.
pub mod recover_config {
    /// 主动探测配置
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum OutlierDetectWhen {
        /// 不开启监控探测
        Never = 0,
        /// 只有在熔断恢复时才开启健康探测
        OnRecover = 1,
        /// 一直开启健康探测
        Always = 2,
    }
    impl OutlierDetectWhen {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                OutlierDetectWhen::Never => "NEVER",
                OutlierDetectWhen::OnRecover => "ON_RECOVER",
                OutlierDetectWhen::Always => "ALWAYS",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "NEVER" => Some(Self::Never),
                "ON_RECOVER" => Some(Self::OnRecover),
                "ALWAYS" => Some(Self::Always),
                _ => None,
            }
        }
    }
}
/// 熔断策略
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CbPolicy {
    #[prost(message, optional, tag = "1")]
    pub error_rate: ::core::option::Option<cb_policy::ErrRateConfig>,
    #[prost(message, optional, tag = "2")]
    pub slow_rate: ::core::option::Option<cb_policy::SlowRateConfig>,
    /// 熔断的决策周期，多久触发一次熔断决策
    #[prost(message, optional, tag = "3")]
    pub judge_duration: ::core::option::Option<::prost_types::Duration>,
    /// 最大熔断比例，超过多少比例后不会继续熔断
    #[prost(message, optional, tag = "4")]
    pub max_ejection_percent: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "5")]
    pub consecutive: ::core::option::Option<cb_policy::ConsecutiveErrConfig>,
}
/// Nested message and enum types in `CbPolicy`.
pub mod cb_policy {
    /// 错误率熔断配置
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct ErrRateConfig {
        /// 是否启用错误率配置
        #[prost(message, optional, tag = "1")]
        pub enable: ::core::option::Option<bool>,
        /// 触发错误率熔断的最低请求阈值
        #[prost(message, optional, tag = "2")]
        pub request_volume_threshold: ::core::option::Option<u32>,
        /// 可选。触发保持状态的错误率阈值，假如不配置，则默认不会进入Preserved状态
        #[prost(message, optional, tag = "3")]
        pub error_rate_to_preserved: ::core::option::Option<u32>,
        /// 触发熔断的错误率阈值
        #[prost(message, optional, tag = "4")]
        pub error_rate_to_open: ::core::option::Option<u32>,
        #[prost(message, repeated, tag = "5")]
        pub specials: ::prost::alloc::vec::Vec<err_rate_config::SpecialConfig>,
    }
    /// Nested message and enum types in `ErrRateConfig`.
    pub mod err_rate_config {
        /// 错误码相关特定配置
        #[allow(clippy::derive_partial_eq_without_eq)]
        #[derive(Clone, PartialEq, ::prost::Message)]
        pub struct SpecialConfig {
            /// 熔断关心的错误类型，用户可以自己定义
            #[prost(message, optional, tag = "1")]
            pub r#type: ::core::option::Option<::prost::alloc::string::String>,
            #[prost(message, repeated, tag = "2")]
            pub error_codes: ::prost::alloc::vec::Vec<i64>,
            #[prost(message, optional, tag = "3")]
            pub error_rate_to_preserved: ::core::option::Option<u32>,
            #[prost(message, optional, tag = "4")]
            pub error_rate_to_open: ::core::option::Option<u32>,
        }
    }
    /// 慢调用率熔断策略配置
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct SlowRateConfig {
        /// 是否启用慢调用率配置
        #[prost(message, optional, tag = "1")]
        pub enable: ::core::option::Option<bool>,
        /// 最大响应时间，超过该时间属于慢调用请求
        #[prost(message, optional, tag = "2")]
        pub max_rt: ::core::option::Option<::prost_types::Duration>,
        /// 可选。触发保持状态的超时率阈值，假如不配置，则默认不会进入Preserved状态
        #[prost(message, optional, tag = "3")]
        pub slow_rate_to_preserved: ::core::option::Option<u32>,
        /// 触发熔断的超时率阈值
        #[prost(message, optional, tag = "4")]
        pub slow_rate_to_open: ::core::option::Option<u32>,
    }
    /// 连续错误数熔断配置
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct ConsecutiveErrConfig {
        /// 是否启用连续错误数配置
        #[prost(message, optional, tag = "1")]
        pub enable: ::core::option::Option<bool>,
        /// 连续错误数阈值，进入Preserved状态
        #[prost(message, optional, tag = "2")]
        pub consecutive_error_to_preserved: ::core::option::Option<u32>,
        /// 连续错误数阈值，进入Open状态
        #[prost(message, optional, tag = "3")]
        pub consecutive_error_to_open: ::core::option::Option<u32>,
    }
}
/// 目标set的规则
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DestinationSet {
    /// 被调命名空间以及服务名，可以为*，代表全匹配
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    /// 可选，SUBSET标识
    #[prost(map = "string, message", tag = "3")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        MatchString,
    >,
    #[prost(enumeration = "destination_set::Resource", tag = "4")]
    pub resource: i32,
    #[prost(enumeration = "destination_set::Type", tag = "5")]
    pub r#type: i32,
    #[prost(enumeration = "destination_set::Scope", tag = "6")]
    pub scope: i32,
    /// 熔断数据度量周期
    /// 所有的阈值指标按此周期进行统计
    #[prost(message, optional, tag = "7")]
    pub metric_window: ::core::option::Option<::prost_types::Duration>,
    /// 熔断数据统计精度，决定数据度量的最小周期
    /// 度量滑窗的步长=window/precision
    #[prost(message, optional, tag = "8")]
    pub metric_precision: ::core::option::Option<u32>,
    /// 熔断数据上报周期，对分布式熔断有效
    #[prost(message, optional, tag = "9")]
    pub update_interval: ::core::option::Option<::prost_types::Duration>,
    /// 触发熔断后恢复配置
    #[prost(message, optional, tag = "10")]
    pub recover: ::core::option::Option<RecoverConfig>,
    /// 熔断策略
    #[prost(message, optional, tag = "11")]
    pub policy: ::core::option::Option<CbPolicy>,
    /// 被调的接口信息，指定哪些接口会使用该规则
    #[prost(message, optional, tag = "12")]
    pub method: ::core::option::Option<MatchString>,
    /// 返回码，指定哪些返回码会使用该规则
    #[prost(message, repeated, tag = "13")]
    pub error_codes: ::prost::alloc::vec::Vec<i64>,
}
/// Nested message and enum types in `DestinationSet`.
pub mod destination_set {
    /// 需要进行熔断的资源
    /// 支持SUBSET（子集群），以及INSTANCE（单个实例），默认为SUBSET
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Resource {
        /// 针对实例分组进行熔断
        Subset = 0,
        /// 针对实例进行熔断
        Instance = 1,
    }
    impl Resource {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Resource::Subset => "SUBSET",
                Resource::Instance => "INSTANCE",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "SUBSET" => Some(Self::Subset),
                "INSTANCE" => Some(Self::Instance),
                _ => None,
            }
        }
    }
    /// 熔断决策类型，支持GLOBAL（分布式决策）以及LOCAL(本地决策），默认GLOBAL
    /// 当指定为GLOBAL时，则会定期上报统计数据并根据汇总数据进行熔断决策
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Type {
        Global = 0,
        Local = 1,
    }
    impl Type {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Type::Global => "GLOBAL",
                Type::Local => "LOCAL",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "GLOBAL" => Some(Self::Global),
                "LOCAL" => Some(Self::Local),
                _ => None,
            }
        }
    }
    /// 熔断范围，是否扩散针对相同服务下所有接口进行熔断
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Scope {
        /// 触发熔断条件，扩散熔断所有接口
        All = 0,
        /// 触发熔断条件，只熔断当前接口
        Current = 1,
    }
    impl Scope {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Scope::All => "ALL",
                Scope::Current => "CURRENT",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "ALL" => Some(Self::All),
                "CURRENT" => Some(Self::Current),
                _ => None,
            }
        }
    }
}
/// 具体熔断规则
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CbRule {
    /// 如果匹配Source规则，按照Destination进行熔断
    /// 多个Source之间的关系为或
    #[prost(message, repeated, tag = "1")]
    pub sources: ::prost::alloc::vec::Vec<SourceMatcher>,
    #[prost(message, repeated, tag = "2")]
    pub destinations: ::prost::alloc::vec::Vec<DestinationSet>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RuleMatcher {
    #[prost(message, optional, tag = "1")]
    pub source: ::core::option::Option<rule_matcher::SourceService>,
    #[prost(message, optional, tag = "2")]
    pub destination: ::core::option::Option<rule_matcher::DestinationService>,
}
/// Nested message and enum types in `RuleMatcher`.
pub mod rule_matcher {
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct SourceService {
        #[prost(string, tag = "1")]
        pub service: ::prost::alloc::string::String,
        #[prost(string, tag = "2")]
        pub namespace: ::prost::alloc::string::String,
    }
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct DestinationService {
        #[prost(string, tag = "1")]
        pub service: ::prost::alloc::string::String,
        #[prost(string, tag = "2")]
        pub namespace: ::prost::alloc::string::String,
        #[prost(message, optional, tag = "3")]
        pub method: ::core::option::Option<super::MatchString>,
    }
}
/// new specific rule for circuitbreaker config
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CircuitBreakerRule {
    #[prost(string, tag = "1")]
    pub id: ::prost::alloc::string::String,
    /// rule name
    #[prost(string, tag = "2")]
    pub name: ::prost::alloc::string::String,
    /// namespace of rule
    #[prost(string, tag = "3")]
    pub namespace: ::prost::alloc::string::String,
    /// enable this router
    #[prost(bool, tag = "4")]
    pub enable: bool,
    /// revision routing version
    #[prost(string, tag = "5")]
    pub revision: ::prost::alloc::string::String,
    /// ctime create time of the rules
    #[prost(string, tag = "6")]
    pub ctime: ::prost::alloc::string::String,
    /// mtime modify time of the rules
    #[prost(string, tag = "7")]
    pub mtime: ::prost::alloc::string::String,
    /// etime enable time of the rules
    #[prost(string, tag = "8")]
    pub etime: ::prost::alloc::string::String,
    /// description simple description rules
    #[prost(string, tag = "9")]
    pub description: ::prost::alloc::string::String,
    /// the circuitbreaking level
    #[prost(enumeration = "Level", tag = "21")]
    pub level: i32,
    /// match condition for this rule
    #[prost(message, optional, tag = "22")]
    pub rule_matcher: ::core::option::Option<RuleMatcher>,
    /// error conditions to judge an invocation as an error
    #[prost(message, repeated, tag = "23")]
    pub error_conditions: ::prost::alloc::vec::Vec<ErrorCondition>,
    /// trigger condition to trigger circuitbreaking
    #[prost(message, repeated, tag = "24")]
    pub trigger_condition: ::prost::alloc::vec::Vec<TriggerCondition>,
    /// the maximum % of an upstream cluster that can be ejected
    #[prost(uint32, tag = "25")]
    pub max_ejection_percent: u32,
    /// recover condition to make resource open to close
    #[prost(message, optional, tag = "26")]
    pub recover_condition: ::core::option::Option<RecoverCondition>,
    /// fault detection enable config
    #[prost(message, optional, tag = "27")]
    pub fault_detect_config: ::core::option::Option<FaultDetectConfig>,
    /// fall back configuration
    #[prost(message, optional, tag = "28")]
    pub fallback_config: ::core::option::Option<FallbackConfig>,
}
/// the condition to judge an input invocation as an error
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ErrorCondition {
    #[prost(enumeration = "error_condition::InputType", tag = "1")]
    pub input_type: i32,
    #[prost(message, optional, tag = "2")]
    pub condition: ::core::option::Option<MatchString>,
}
/// Nested message and enum types in `ErrorCondition`.
pub mod error_condition {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum InputType {
        Unknown = 0,
        RetCode = 1,
        Delay = 2,
    }
    impl InputType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                InputType::Unknown => "UNKNOWN",
                InputType::RetCode => "RET_CODE",
                InputType::Delay => "DELAY",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "RET_CODE" => Some(Self::RetCode),
                "DELAY" => Some(Self::Delay),
                _ => None,
            }
        }
    }
}
/// the error condition to trigger circuitbreaking
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct TriggerCondition {
    #[prost(enumeration = "trigger_condition::TriggerType", tag = "1")]
    pub trigger_type: i32,
    #[prost(uint32, tag = "2")]
    pub error_count: u32,
    #[prost(uint32, tag = "3")]
    pub error_percent: u32,
    #[prost(uint32, tag = "4")]
    pub interval: u32,
    #[prost(uint32, tag = "5")]
    pub minimum_request: u32,
}
/// Nested message and enum types in `TriggerCondition`.
pub mod trigger_condition {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum TriggerType {
        Unknown = 0,
        ErrorRate = 1,
        ConsecutiveError = 2,
    }
    impl TriggerType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                TriggerType::Unknown => "UNKNOWN",
                TriggerType::ErrorRate => "ERROR_RATE",
                TriggerType::ConsecutiveError => "CONSECUTIVE_ERROR",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "ERROR_RATE" => Some(Self::ErrorRate),
                "CONSECUTIVE_ERROR" => Some(Self::ConsecutiveError),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RecoverCondition {
    /// seconds from open to half-open
    #[prost(uint32, tag = "1")]
    pub sleep_window: u32,
    /// consecutive success request to recover
    #[prost(uint32, tag = "2")]
    pub consecutive_success: u32,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct FaultDetectConfig {
    #[prost(bool, tag = "1")]
    pub enable: bool,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct FallbackConfig {
    #[prost(bool, tag = "1")]
    pub enable: bool,
    #[prost(message, optional, tag = "2")]
    pub response: ::core::option::Option<FallbackResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct FallbackResponse {
    #[prost(int32, tag = "1")]
    pub code: i32,
    #[prost(message, repeated, tag = "2")]
    pub headers: ::prost::alloc::vec::Vec<fallback_response::MessageHeader>,
    #[prost(string, tag = "3")]
    pub body: ::prost::alloc::string::String,
}
/// Nested message and enum types in `FallbackResponse`.
pub mod fallback_response {
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct MessageHeader {
        #[prost(string, tag = "1")]
        pub key: ::prost::alloc::string::String,
        #[prost(string, tag = "2")]
        pub value: ::prost::alloc::string::String,
    }
}
/// circuitbreaking level
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum Level {
    Unknown = 0,
    /// service level circuitbreaking
    Service = 1,
    /// method level circuitbreaking
    Method = 2,
    /// group level circuitbreaking
    Group = 3,
    /// instance level circuitbreaking
    Instance = 4,
}
impl Level {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            Level::Unknown => "UNKNOWN",
            Level::Service => "SERVICE",
            Level::Method => "METHOD",
            Level::Group => "GROUP",
            Level::Instance => "INSTANCE",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "UNKNOWN" => Some(Self::Unknown),
            "SERVICE" => Some(Self::Service),
            "METHOD" => Some(Self::Method),
            "GROUP" => Some(Self::Group),
            "INSTANCE" => Some(Self::Instance),
            _ => None,
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Client {
    #[prost(message, optional, tag = "1")]
    pub host: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(enumeration = "client::ClientType", tag = "2")]
    pub r#type: i32,
    #[prost(message, optional, tag = "3")]
    pub version: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub location: ::core::option::Option<Location>,
    #[prost(message, optional, tag = "5")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "6")]
    pub stat: ::prost::alloc::vec::Vec<StatInfo>,
    #[prost(message, optional, tag = "7")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
}
/// Nested message and enum types in `Client`.
pub mod client {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum ClientType {
        Unknown = 0,
        Sdk = 1,
        Agent = 2,
    }
    impl ClientType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                ClientType::Unknown => "UNKNOWN",
                ClientType::Sdk => "SDK",
                ClientType::Agent => "AGENT",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "SDK" => Some(Self::Sdk),
                "AGENT" => Some(Self::Agent),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct StatInfo {
    #[prost(message, optional, tag = "1")]
    pub target: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub port: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "3")]
    pub path: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub protocol: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigRelease {
    #[prost(message, optional, tag = "1")]
    pub service: ::core::option::Option<Service>,
    #[prost(message, optional, tag = "2")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub circuit_breaker: ::core::option::Option<CircuitBreaker>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigWithService {
    #[prost(message, repeated, tag = "1")]
    pub services: ::prost::alloc::vec::Vec<Service>,
    #[prost(message, optional, tag = "2")]
    pub circuit_breaker: ::core::option::Option<CircuitBreaker>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct FaultDetector {
    /// fault detect rules for current service
    #[prost(message, repeated, tag = "1")]
    pub rules: ::prost::alloc::vec::Vec<FaultDetectRule>,
    /// total revision for the fault detect rules
    #[prost(string, tag = "2")]
    pub revision: ::prost::alloc::string::String,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct FaultDetectRule {
    #[prost(string, tag = "1")]
    pub id: ::prost::alloc::string::String,
    /// rule name
    #[prost(string, tag = "2")]
    pub name: ::prost::alloc::string::String,
    /// namespace of rule
    #[prost(string, tag = "3")]
    pub namespace: ::prost::alloc::string::String,
    /// revision routing version
    #[prost(string, tag = "4")]
    pub revision: ::prost::alloc::string::String,
    /// ctime create time of the rules
    #[prost(string, tag = "5")]
    pub ctime: ::prost::alloc::string::String,
    /// mtime modify time of the rules
    #[prost(string, tag = "6")]
    pub mtime: ::prost::alloc::string::String,
    /// description simple description rules
    #[prost(string, tag = "7")]
    pub description: ::prost::alloc::string::String,
    /// detect target
    #[prost(message, optional, tag = "21")]
    pub target_service: ::core::option::Option<fault_detect_rule::DestinationService>,
    /// detect interval
    #[prost(uint32, tag = "22")]
    pub interval: u32,
    /// detect timeout
    #[prost(uint32, tag = "23")]
    pub timeout: u32,
    /// detect port
    #[prost(uint32, tag = "24")]
    pub port: u32,
    #[prost(enumeration = "fault_detect_rule::Protocol", tag = "25")]
    pub protocol: i32,
    /// http detect config
    #[prost(message, optional, tag = "26")]
    pub http_config: ::core::option::Option<HttpProtocolConfig>,
    /// tcp detect config
    #[prost(message, optional, tag = "27")]
    pub tcp_config: ::core::option::Option<TcpProtocolConfig>,
    /// udp detect config
    #[prost(message, optional, tag = "28")]
    pub udp_config: ::core::option::Option<UdpProtocolConfig>,
}
/// Nested message and enum types in `FaultDetectRule`.
pub mod fault_detect_rule {
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct DestinationService {
        #[prost(string, tag = "1")]
        pub service: ::prost::alloc::string::String,
        #[prost(string, tag = "2")]
        pub namespace: ::prost::alloc::string::String,
        #[prost(message, optional, tag = "3")]
        pub method: ::core::option::Option<super::MatchString>,
    }
    /// detect protocol
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum Protocol {
        Unknown = 0,
        Http = 1,
        Tcp = 2,
        Udp = 3,
    }
    impl Protocol {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Protocol::Unknown => "UNKNOWN",
                Protocol::Http => "HTTP",
                Protocol::Tcp => "TCP",
                Protocol::Udp => "UDP",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "HTTP" => Some(Self::Http),
                "TCP" => Some(Self::Tcp),
                "UDP" => Some(Self::Udp),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HttpProtocolConfig {
    #[prost(string, tag = "1")]
    pub method: ::prost::alloc::string::String,
    #[prost(string, tag = "2")]
    pub url: ::prost::alloc::string::String,
    #[prost(message, repeated, tag = "3")]
    pub headers: ::prost::alloc::vec::Vec<http_protocol_config::MessageHeader>,
    #[prost(string, tag = "4")]
    pub body: ::prost::alloc::string::String,
}
/// Nested message and enum types in `HttpProtocolConfig`.
pub mod http_protocol_config {
    #[allow(clippy::derive_partial_eq_without_eq)]
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct MessageHeader {
        #[prost(string, tag = "1")]
        pub key: ::prost::alloc::string::String,
        #[prost(string, tag = "2")]
        pub value: ::prost::alloc::string::String,
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct TcpProtocolConfig {
    #[prost(string, tag = "1")]
    pub send: ::prost::alloc::string::String,
    #[prost(string, repeated, tag = "2")]
    pub receive: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UdpProtocolConfig {
    #[prost(string, tag = "1")]
    pub send: ::prost::alloc::string::String,
    #[prost(string, repeated, tag = "2")]
    pub receive: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct LoginRequest {
    #[prost(message, optional, tag = "1")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub password: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct LoginResponse {
    #[prost(message, optional, tag = "1")]
    pub user_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub role: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub owner_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub token: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct User {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub password: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub source: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub auth_token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub token_enable: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "8")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "10")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub user_type: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub mobile: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "13")]
    pub email: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ModifyUserPassword {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub old_password: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub new_password: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UserGroupRelation {
    #[prost(message, optional, tag = "1")]
    pub group_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "2")]
    pub users: ::prost::alloc::vec::Vec<User>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UserGroup {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub auth_token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub token_enable: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "6")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub relation: ::core::option::Option<UserGroupRelation>,
    #[prost(message, optional, tag = "10")]
    pub user_count: ::core::option::Option<u32>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ModifyUserGroup {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub auth_token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub token_enable: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "6")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub add_relations: ::core::option::Option<UserGroupRelation>,
    #[prost(message, optional, tag = "8")]
    pub remove_relations: ::core::option::Option<UserGroupRelation>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Principal {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Principals {
    #[prost(message, repeated, tag = "1")]
    pub users: ::prost::alloc::vec::Vec<Principal>,
    #[prost(message, repeated, tag = "2")]
    pub groups: ::prost::alloc::vec::Vec<Principal>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct StrategyResourceEntry {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct StrategyResources {
    #[prost(message, optional, tag = "1")]
    pub strategy_id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "2")]
    pub namespaces: ::prost::alloc::vec::Vec<StrategyResourceEntry>,
    #[prost(message, repeated, tag = "3")]
    pub services: ::prost::alloc::vec::Vec<StrategyResourceEntry>,
    #[prost(message, repeated, tag = "4")]
    pub config_groups: ::prost::alloc::vec::Vec<StrategyResourceEntry>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct AuthStrategy {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub principals: ::core::option::Option<Principals>,
    #[prost(message, optional, tag = "4")]
    pub resources: ::core::option::Option<StrategyResources>,
    #[prost(enumeration = "AuthAction", tag = "5")]
    pub action: i32,
    #[prost(message, optional, tag = "6")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub ctime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub mtime: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "10")]
    pub auth_token: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub default_strategy: ::core::option::Option<bool>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ModifyAuthStrategy {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub add_principals: ::core::option::Option<Principals>,
    #[prost(message, optional, tag = "4")]
    pub remove_principals: ::core::option::Option<Principals>,
    #[prost(message, optional, tag = "5")]
    pub add_resources: ::core::option::Option<StrategyResources>,
    #[prost(message, optional, tag = "6")]
    pub remove_resources: ::core::option::Option<StrategyResources>,
    #[prost(enumeration = "AuthAction", tag = "7")]
    pub action: i32,
    #[prost(message, optional, tag = "8")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum AuthAction {
    OnlyRead = 0,
    ReadWrite = 1,
}
impl AuthAction {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            AuthAction::OnlyRead => "ONLY_READ",
            AuthAction::ReadWrite => "READ_WRITE",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "ONLY_READ" => Some(Self::OnlyRead),
            "READ_WRITE" => Some(Self::ReadWrite),
            _ => None,
        }
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum ResourceType {
    Namespaces = 0,
    Services = 1,
    ConfigGroups = 2,
}
impl ResourceType {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            ResourceType::Namespaces => "Namespaces",
            ResourceType::Services => "Services",
            ResourceType::ConfigGroups => "ConfigGroups",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "Namespaces" => Some(Self::Namespaces),
            "Services" => Some(Self::Services),
            "ConfigGroups" => Some(Self::ConfigGroups),
            _ => None,
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Response {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub client: ::core::option::Option<Client>,
    #[prost(message, optional, tag = "4")]
    pub namespace: ::core::option::Option<Namespace>,
    #[prost(message, optional, tag = "5")]
    pub service: ::core::option::Option<Service>,
    #[prost(message, optional, tag = "6")]
    pub instance: ::core::option::Option<Instance>,
    #[prost(message, optional, tag = "7")]
    pub routing: ::core::option::Option<Routing>,
    #[prost(message, optional, tag = "8")]
    pub alias: ::core::option::Option<ServiceAlias>,
    #[prost(message, optional, tag = "9")]
    pub rate_limit: ::core::option::Option<Rule>,
    #[prost(message, optional, tag = "10")]
    pub circuit_breaker: ::core::option::Option<CircuitBreaker>,
    #[prost(message, optional, tag = "11")]
    pub config_release: ::core::option::Option<ConfigRelease>,
    #[prost(message, optional, tag = "19")]
    pub user: ::core::option::Option<User>,
    #[prost(message, optional, tag = "20")]
    pub user_group: ::core::option::Option<UserGroup>,
    #[prost(message, optional, tag = "21")]
    pub auth_strategy: ::core::option::Option<AuthStrategy>,
    #[prost(message, optional, tag = "22")]
    pub relation: ::core::option::Option<UserGroupRelation>,
    #[prost(message, optional, tag = "23")]
    pub login_response: ::core::option::Option<LoginResponse>,
    #[prost(message, optional, tag = "24")]
    pub modify_auth_strategy: ::core::option::Option<ModifyAuthStrategy>,
    #[prost(message, optional, tag = "25")]
    pub modify_user_group: ::core::option::Option<ModifyUserGroup>,
    #[prost(message, optional, tag = "26")]
    pub resources: ::core::option::Option<StrategyResources>,
    #[prost(message, optional, tag = "27")]
    pub option_switch: ::core::option::Option<OptionSwitch>,
    #[prost(message, optional, tag = "28")]
    pub instance_labels: ::core::option::Option<InstanceLabels>,
    #[prost(message, optional, tag = "29")]
    pub data: ::core::option::Option<::prost_types::Any>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BatchWriteResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub size: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "4")]
    pub responses: ::prost::alloc::vec::Vec<Response>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BatchQueryResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub amount: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "4")]
    pub size: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "5")]
    pub namespaces: ::prost::alloc::vec::Vec<Namespace>,
    #[prost(message, repeated, tag = "6")]
    pub services: ::prost::alloc::vec::Vec<Service>,
    #[prost(message, repeated, tag = "7")]
    pub instances: ::prost::alloc::vec::Vec<Instance>,
    #[prost(message, repeated, tag = "8")]
    pub routings: ::prost::alloc::vec::Vec<Routing>,
    #[prost(message, repeated, tag = "9")]
    pub aliases: ::prost::alloc::vec::Vec<ServiceAlias>,
    #[prost(message, repeated, tag = "10")]
    pub rate_limits: ::prost::alloc::vec::Vec<Rule>,
    #[prost(message, repeated, tag = "11")]
    pub config_with_services: ::prost::alloc::vec::Vec<ConfigWithService>,
    #[prost(message, repeated, tag = "18")]
    pub users: ::prost::alloc::vec::Vec<User>,
    #[prost(message, repeated, tag = "19")]
    pub user_groups: ::prost::alloc::vec::Vec<UserGroup>,
    #[prost(message, repeated, tag = "20")]
    pub auth_strategies: ::prost::alloc::vec::Vec<AuthStrategy>,
    #[prost(message, repeated, tag = "21")]
    pub clients: ::prost::alloc::vec::Vec<Client>,
    #[prost(message, repeated, tag = "22")]
    pub data: ::prost::alloc::vec::Vec<::prost_types::Any>,
    #[prost(message, optional, tag = "23")]
    pub summary: ::core::option::Option<Summary>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DiscoverResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(enumeration = "discover_response::DiscoverResponseType", tag = "3")]
    pub r#type: i32,
    #[prost(message, optional, tag = "4")]
    pub service: ::core::option::Option<Service>,
    #[prost(message, repeated, tag = "5")]
    pub instances: ::prost::alloc::vec::Vec<Instance>,
    #[prost(message, optional, tag = "6")]
    pub routing: ::core::option::Option<Routing>,
    #[prost(message, optional, tag = "7")]
    pub rate_limit: ::core::option::Option<RateLimit>,
    #[prost(message, optional, tag = "8")]
    pub circuit_breaker: ::core::option::Option<CircuitBreaker>,
    #[prost(message, repeated, tag = "9")]
    pub services: ::prost::alloc::vec::Vec<Service>,
    #[prost(message, repeated, tag = "10")]
    pub namespaces: ::prost::alloc::vec::Vec<Namespace>,
    #[prost(message, optional, tag = "11")]
    pub fault_detector: ::core::option::Option<FaultDetector>,
    #[prost(message, optional, tag = "21")]
    pub alias_for: ::core::option::Option<Service>,
}
/// Nested message and enum types in `DiscoverResponse`.
pub mod discover_response {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum DiscoverResponseType {
        Unknown = 0,
        Instance = 1,
        Cluster = 2,
        Routing = 3,
        RateLimit = 4,
        CircuitBreaker = 5,
        Services = 6,
        Namespaces = 12,
        FaultDetector = 13,
    }
    impl DiscoverResponseType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                DiscoverResponseType::Unknown => "UNKNOWN",
                DiscoverResponseType::Instance => "INSTANCE",
                DiscoverResponseType::Cluster => "CLUSTER",
                DiscoverResponseType::Routing => "ROUTING",
                DiscoverResponseType::RateLimit => "RATE_LIMIT",
                DiscoverResponseType::CircuitBreaker => "CIRCUIT_BREAKER",
                DiscoverResponseType::Services => "SERVICES",
                DiscoverResponseType::Namespaces => "NAMESPACES",
                DiscoverResponseType::FaultDetector => "FAULT_DETECTOR",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "INSTANCE" => Some(Self::Instance),
                "CLUSTER" => Some(Self::Cluster),
                "ROUTING" => Some(Self::Routing),
                "RATE_LIMIT" => Some(Self::RateLimit),
                "CIRCUIT_BREAKER" => Some(Self::CircuitBreaker),
                "SERVICES" => Some(Self::Services),
                "NAMESPACES" => Some(Self::Namespaces),
                "FAULT_DETECTOR" => Some(Self::FaultDetector),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct OptionSwitch {
    #[prost(map = "string, string", tag = "1")]
    pub options: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct InstanceLabels {
    #[prost(map = "string, message", tag = "1")]
    pub labels: ::std::collections::HashMap<::prost::alloc::string::String, StringList>,
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum Code {
    /// base module status codes
    Unknown = 0,
    ExecuteSuccess = 200000,
    DataNoChange = 200001,
    NoNeedUpdate = 200002,
    BadRequest = 400000,
    ParseException = 400001,
    EmptyRequest = 400002,
    BatchSizeOverLimit = 400003,
    InvalidDiscoverResource = 400004,
    InvalidRequestId = 400100,
    InvalidUserName = 400101,
    InvalidUserToken = 400102,
    InvalidParameter = 400103,
    EmptyQueryParameter = 400104,
    InvalidQueryInsParameter = 400105,
    InvalidNamespaceName = 400110,
    InvalidNamespaceOwners = 400111,
    InvalidNamespaceToken = 400112,
    InvalidServiceName = 400120,
    InvalidServiceOwners = 400121,
    InvalidServiceToken = 400122,
    InvalidServiceMetadata = 400123,
    InvalidServicePorts = 400124,
    InvalidServiceBusiness = 400125,
    InvalidServiceDepartment = 400126,
    InvalidServiceCmdb = 400127,
    InvalidServiceComment = 400128,
    InvalidServiceAliasComment = 400129,
    InvalidInstanceId = 400130,
    InvalidInstanceHost = 400131,
    InvalidInstancePort = 400132,
    InvalidServiceAlias = 400133,
    InvalidNamespaceWithAlias = 400134,
    InvalidServiceAliasOwners = 400135,
    InvalidInstanceProtocol = 400136,
    InvalidInstanceVersion = 400137,
    InvalidInstanceLogicSet = 400138,
    InvalidInstanceIsolate = 400139,
    HealthCheckNotOpen = 400140,
    HeartbeatOnDisabledIns = 400141,
    HeartbeatExceedLimit = 400142,
    HeartbeatTypeNotFound = 400143,
    InvalidMetadata = 400150,
    InvalidRateLimitId = 400151,
    InvalidRateLimitLabels = 400152,
    InvalidRateLimitAmounts = 400153,
    InvalidRateLimitName = 400154,
    InvalidCircuitBreakerId = 400160,
    InvalidCircuitBreakerVersion = 400161,
    InvalidCircuitBreakerName = 400162,
    InvalidCircuitBreakerNamespace = 400163,
    InvalidCircuitBreakerOwners = 400164,
    InvalidCircuitBreakerToken = 400165,
    InvalidCircuitBreakerBusiness = 400166,
    InvalidCircuitBreakerDepartment = 400167,
    InvalidCircuitBreakerComment = 400168,
    CircuitBreakerRuleExisted = 400169,
    InvalidRoutingId = 400700,
    InvalidRoutingPolicy = 400701,
    InvalidRoutingName = 400702,
    InvalidRoutingPriority = 400703,
    InvalidFaultDetectId = 400900,
    InvalidFaultDetectName = 400901,
    InvalidFaultDetectNamespace = 400902,
    FaultDetectRuleExisted = 400903,
    /// network relative codes
    ServicesExistedMesh = 400170,
    ResourcesExistedMesh = 400171,
    InvalidMeshParameter = 400172,
    /// platform relative codes
    InvalidPlatformId = 400180,
    InvalidPlatformName = 400181,
    InvalidPlatformDomain = 400182,
    InvalidPlatformQps = 400183,
    InvalidPlatformToken = 400184,
    InvalidPlatformOwner = 400185,
    InvalidPlatformDepartment = 400186,
    InvalidPlatformComment = 400187,
    NotFoundPlatform = 400188,
    /// flux relative codes
    InvalidFluxRateLimitId = 400190,
    InvalidFluxRateLimitQps = 400191,
    InvalidFluxRateLimitSetKey = 400192,
    ExistedResource = 400201,
    NotFoundResource = 400202,
    NamespaceExistedServices = 400203,
    ServiceExistedInstances = 400204,
    ServiceExistedRoutings = 400205,
    ServiceExistedRateLimits = 400206,
    ExistReleasedConfig = 400207,
    SameInstanceRequest = 400208,
    ServiceExistedCircuitBreakers = 400209,
    ServiceExistedAlias = 400210,
    NamespaceExistedMeshResources = 400211,
    NamespaceExistedCircuitBreakers = 400212,
    ServiceSubscribedByMeshes = 400213,
    ServiceExistedFluxRateLimits = 400214,
    NamespaceExistedConfigGroups = 400219,
    NotFoundService = 400301,
    NotFoundRouting = 400302,
    NotFoundInstance = 400303,
    NotFoundServiceAlias = 400304,
    NotFoundNamespace = 400305,
    NotFoundSourceService = 400306,
    NotFoundRateLimit = 400307,
    NotFoundCircuitBreaker = 400308,
    NotFoundMasterConfig = 400309,
    NotFoundTagConfig = 400310,
    NotFoundTagConfigOrService = 400311,
    ClientApiNotOpen = 400401,
    NotAllowBusinessService = 400402,
    NotAllowAliasUpdate = 400501,
    NotAllowAliasCreateInstance = 400502,
    NotAllowAliasCreateRouting = 400503,
    NotAllowCreateAliasForAlias = 400504,
    NotAllowAliasCreateRateLimit = 400505,
    NotAllowAliasBindRule = 400506,
    NotAllowDifferentNamespaceBindRule = 400507,
    Unauthorized = 401000,
    NotAllowedAccess = 401001,
    CmdbNotFindHost = 404001,
    DataConflict = 409000,
    InstanceTooManyRequests = 429001,
    IpRateLimit = 429002,
    ApiRateLimit = 403003,
    ExecuteException = 500000,
    StoreLayerException = 500001,
    CmdbPluginException = 500002,
    ParseRoutingException = 500004,
    ParseRateLimitException = 500005,
    ParseCircuitBreakerException = 500006,
    HeartbeatException = 500007,
    InstanceRegisTimeout = 500008,
    /// config center status codes
    InvalidConfigFileGroupName = 400801,
    InvalidConfigFileName = 400802,
    InvalidConfigFileContentLength = 400803,
    InvalidConfigFileFormat = 400804,
    InvalidConfigFileTags = 400805,
    InvalidWatchConfigFileFormat = 400806,
    NotFoundResourceConfigFile = 400807,
    InvalidConfigFileTemplateName = 400808,
    EncryptConfigFileException = 400809,
    DecryptConfigFileException = 400810,
    /// auth codes
    InvalidUserOwners = 400410,
    InvalidUserId = 400411,
    InvalidUserPassword = 400412,
    InvalidUserMobile = 400413,
    InvalidUserEmail = 400414,
    InvalidUserGroupOwners = 400420,
    InvalidUserGroupId = 400421,
    InvalidAuthStrategyOwners = 400430,
    InvalidAuthStrategyName = 400431,
    InvalidAuthStrategyId = 400432,
    InvalidPrincipalType = 400440,
    UserExisted = 400215,
    UserGroupExisted = 400216,
    AuthStrategyRuleExisted = 400217,
    SubAccountExisted = 400218,
    NotFoundUser = 400312,
    NotFoundOwnerUser = 400313,
    NotFoundUserGroup = 400314,
    NotFoundAuthStrategyRule = 400315,
    NotAllowModifyDefaultStrategyPrincipal = 400508,
    NotAllowModifyOwnerDefaultStrategy = 400509,
    EmptyAutToken = 401002,
    TokenDisabled = 401003,
    TokenNotExisted = 401004,
    AuthTokenForbidden = 403001,
    OperationRoleForbidden = 403002,
}
impl Code {
    /// String value of the enum field names used in the ProtoBuf definition.
    ///
    /// The values are not transformed in any way and thus are considered stable
    /// (if the ProtoBuf definition does not change) and safe for programmatic use.
    pub fn as_str_name(&self) -> &'static str {
        match self {
            Code::Unknown => "Unknown",
            Code::ExecuteSuccess => "ExecuteSuccess",
            Code::DataNoChange => "DataNoChange",
            Code::NoNeedUpdate => "NoNeedUpdate",
            Code::BadRequest => "BadRequest",
            Code::ParseException => "ParseException",
            Code::EmptyRequest => "EmptyRequest",
            Code::BatchSizeOverLimit => "BatchSizeOverLimit",
            Code::InvalidDiscoverResource => "InvalidDiscoverResource",
            Code::InvalidRequestId => "InvalidRequestID",
            Code::InvalidUserName => "InvalidUserName",
            Code::InvalidUserToken => "InvalidUserToken",
            Code::InvalidParameter => "InvalidParameter",
            Code::EmptyQueryParameter => "EmptyQueryParameter",
            Code::InvalidQueryInsParameter => "InvalidQueryInsParameter",
            Code::InvalidNamespaceName => "InvalidNamespaceName",
            Code::InvalidNamespaceOwners => "InvalidNamespaceOwners",
            Code::InvalidNamespaceToken => "InvalidNamespaceToken",
            Code::InvalidServiceName => "InvalidServiceName",
            Code::InvalidServiceOwners => "InvalidServiceOwners",
            Code::InvalidServiceToken => "InvalidServiceToken",
            Code::InvalidServiceMetadata => "InvalidServiceMetadata",
            Code::InvalidServicePorts => "InvalidServicePorts",
            Code::InvalidServiceBusiness => "InvalidServiceBusiness",
            Code::InvalidServiceDepartment => "InvalidServiceDepartment",
            Code::InvalidServiceCmdb => "InvalidServiceCMDB",
            Code::InvalidServiceComment => "InvalidServiceComment",
            Code::InvalidServiceAliasComment => "InvalidServiceAliasComment",
            Code::InvalidInstanceId => "InvalidInstanceID",
            Code::InvalidInstanceHost => "InvalidInstanceHost",
            Code::InvalidInstancePort => "InvalidInstancePort",
            Code::InvalidServiceAlias => "InvalidServiceAlias",
            Code::InvalidNamespaceWithAlias => "InvalidNamespaceWithAlias",
            Code::InvalidServiceAliasOwners => "InvalidServiceAliasOwners",
            Code::InvalidInstanceProtocol => "InvalidInstanceProtocol",
            Code::InvalidInstanceVersion => "InvalidInstanceVersion",
            Code::InvalidInstanceLogicSet => "InvalidInstanceLogicSet",
            Code::InvalidInstanceIsolate => "InvalidInstanceIsolate",
            Code::HealthCheckNotOpen => "HealthCheckNotOpen",
            Code::HeartbeatOnDisabledIns => "HeartbeatOnDisabledIns",
            Code::HeartbeatExceedLimit => "HeartbeatExceedLimit",
            Code::HeartbeatTypeNotFound => "HeartbeatTypeNotFound",
            Code::InvalidMetadata => "InvalidMetadata",
            Code::InvalidRateLimitId => "InvalidRateLimitID",
            Code::InvalidRateLimitLabels => "InvalidRateLimitLabels",
            Code::InvalidRateLimitAmounts => "InvalidRateLimitAmounts",
            Code::InvalidRateLimitName => "InvalidRateLimitName",
            Code::InvalidCircuitBreakerId => "InvalidCircuitBreakerID",
            Code::InvalidCircuitBreakerVersion => "InvalidCircuitBreakerVersion",
            Code::InvalidCircuitBreakerName => "InvalidCircuitBreakerName",
            Code::InvalidCircuitBreakerNamespace => "InvalidCircuitBreakerNamespace",
            Code::InvalidCircuitBreakerOwners => "InvalidCircuitBreakerOwners",
            Code::InvalidCircuitBreakerToken => "InvalidCircuitBreakerToken",
            Code::InvalidCircuitBreakerBusiness => "InvalidCircuitBreakerBusiness",
            Code::InvalidCircuitBreakerDepartment => "InvalidCircuitBreakerDepartment",
            Code::InvalidCircuitBreakerComment => "InvalidCircuitBreakerComment",
            Code::CircuitBreakerRuleExisted => "CircuitBreakerRuleExisted",
            Code::InvalidRoutingId => "InvalidRoutingID",
            Code::InvalidRoutingPolicy => "InvalidRoutingPolicy",
            Code::InvalidRoutingName => "InvalidRoutingName",
            Code::InvalidRoutingPriority => "InvalidRoutingPriority",
            Code::InvalidFaultDetectId => "InvalidFaultDetectID",
            Code::InvalidFaultDetectName => "InvalidFaultDetectName",
            Code::InvalidFaultDetectNamespace => "InvalidFaultDetectNamespace",
            Code::FaultDetectRuleExisted => "FaultDetectRuleExisted",
            Code::ServicesExistedMesh => "ServicesExistedMesh",
            Code::ResourcesExistedMesh => "ResourcesExistedMesh",
            Code::InvalidMeshParameter => "InvalidMeshParameter",
            Code::InvalidPlatformId => "InvalidPlatformID",
            Code::InvalidPlatformName => "InvalidPlatformName",
            Code::InvalidPlatformDomain => "InvalidPlatformDomain",
            Code::InvalidPlatformQps => "InvalidPlatformQPS",
            Code::InvalidPlatformToken => "InvalidPlatformToken",
            Code::InvalidPlatformOwner => "InvalidPlatformOwner",
            Code::InvalidPlatformDepartment => "InvalidPlatformDepartment",
            Code::InvalidPlatformComment => "InvalidPlatformComment",
            Code::NotFoundPlatform => "NotFoundPlatform",
            Code::InvalidFluxRateLimitId => "InvalidFluxRateLimitId",
            Code::InvalidFluxRateLimitQps => "InvalidFluxRateLimitQps",
            Code::InvalidFluxRateLimitSetKey => "InvalidFluxRateLimitSetKey",
            Code::ExistedResource => "ExistedResource",
            Code::NotFoundResource => "NotFoundResource",
            Code::NamespaceExistedServices => "NamespaceExistedServices",
            Code::ServiceExistedInstances => "ServiceExistedInstances",
            Code::ServiceExistedRoutings => "ServiceExistedRoutings",
            Code::ServiceExistedRateLimits => "ServiceExistedRateLimits",
            Code::ExistReleasedConfig => "ExistReleasedConfig",
            Code::SameInstanceRequest => "SameInstanceRequest",
            Code::ServiceExistedCircuitBreakers => "ServiceExistedCircuitBreakers",
            Code::ServiceExistedAlias => "ServiceExistedAlias",
            Code::NamespaceExistedMeshResources => "NamespaceExistedMeshResources",
            Code::NamespaceExistedCircuitBreakers => "NamespaceExistedCircuitBreakers",
            Code::ServiceSubscribedByMeshes => "ServiceSubscribedByMeshes",
            Code::ServiceExistedFluxRateLimits => "ServiceExistedFluxRateLimits",
            Code::NamespaceExistedConfigGroups => "NamespaceExistedConfigGroups",
            Code::NotFoundService => "NotFoundService",
            Code::NotFoundRouting => "NotFoundRouting",
            Code::NotFoundInstance => "NotFoundInstance",
            Code::NotFoundServiceAlias => "NotFoundServiceAlias",
            Code::NotFoundNamespace => "NotFoundNamespace",
            Code::NotFoundSourceService => "NotFoundSourceService",
            Code::NotFoundRateLimit => "NotFoundRateLimit",
            Code::NotFoundCircuitBreaker => "NotFoundCircuitBreaker",
            Code::NotFoundMasterConfig => "NotFoundMasterConfig",
            Code::NotFoundTagConfig => "NotFoundTagConfig",
            Code::NotFoundTagConfigOrService => "NotFoundTagConfigOrService",
            Code::ClientApiNotOpen => "ClientAPINotOpen",
            Code::NotAllowBusinessService => "NotAllowBusinessService",
            Code::NotAllowAliasUpdate => "NotAllowAliasUpdate",
            Code::NotAllowAliasCreateInstance => "NotAllowAliasCreateInstance",
            Code::NotAllowAliasCreateRouting => "NotAllowAliasCreateRouting",
            Code::NotAllowCreateAliasForAlias => "NotAllowCreateAliasForAlias",
            Code::NotAllowAliasCreateRateLimit => "NotAllowAliasCreateRateLimit",
            Code::NotAllowAliasBindRule => "NotAllowAliasBindRule",
            Code::NotAllowDifferentNamespaceBindRule => {
                "NotAllowDifferentNamespaceBindRule"
            }
            Code::Unauthorized => "Unauthorized",
            Code::NotAllowedAccess => "NotAllowedAccess",
            Code::CmdbNotFindHost => "CMDBNotFindHost",
            Code::DataConflict => "DataConflict",
            Code::InstanceTooManyRequests => "InstanceTooManyRequests",
            Code::IpRateLimit => "IPRateLimit",
            Code::ApiRateLimit => "APIRateLimit",
            Code::ExecuteException => "ExecuteException",
            Code::StoreLayerException => "StoreLayerException",
            Code::CmdbPluginException => "CMDBPluginException",
            Code::ParseRoutingException => "ParseRoutingException",
            Code::ParseRateLimitException => "ParseRateLimitException",
            Code::ParseCircuitBreakerException => "ParseCircuitBreakerException",
            Code::HeartbeatException => "HeartbeatException",
            Code::InstanceRegisTimeout => "InstanceRegisTimeout",
            Code::InvalidConfigFileGroupName => "InvalidConfigFileGroupName",
            Code::InvalidConfigFileName => "InvalidConfigFileName",
            Code::InvalidConfigFileContentLength => "InvalidConfigFileContentLength",
            Code::InvalidConfigFileFormat => "InvalidConfigFileFormat",
            Code::InvalidConfigFileTags => "InvalidConfigFileTags",
            Code::InvalidWatchConfigFileFormat => "InvalidWatchConfigFileFormat",
            Code::NotFoundResourceConfigFile => "NotFoundResourceConfigFile",
            Code::InvalidConfigFileTemplateName => "InvalidConfigFileTemplateName",
            Code::EncryptConfigFileException => "EncryptConfigFileException",
            Code::DecryptConfigFileException => "DecryptConfigFileException",
            Code::InvalidUserOwners => "InvalidUserOwners",
            Code::InvalidUserId => "InvalidUserID",
            Code::InvalidUserPassword => "InvalidUserPassword",
            Code::InvalidUserMobile => "InvalidUserMobile",
            Code::InvalidUserEmail => "InvalidUserEmail",
            Code::InvalidUserGroupOwners => "InvalidUserGroupOwners",
            Code::InvalidUserGroupId => "InvalidUserGroupID",
            Code::InvalidAuthStrategyOwners => "InvalidAuthStrategyOwners",
            Code::InvalidAuthStrategyName => "InvalidAuthStrategyName",
            Code::InvalidAuthStrategyId => "InvalidAuthStrategyID",
            Code::InvalidPrincipalType => "InvalidPrincipalType",
            Code::UserExisted => "UserExisted",
            Code::UserGroupExisted => "UserGroupExisted",
            Code::AuthStrategyRuleExisted => "AuthStrategyRuleExisted",
            Code::SubAccountExisted => "SubAccountExisted",
            Code::NotFoundUser => "NotFoundUser",
            Code::NotFoundOwnerUser => "NotFoundOwnerUser",
            Code::NotFoundUserGroup => "NotFoundUserGroup",
            Code::NotFoundAuthStrategyRule => "NotFoundAuthStrategyRule",
            Code::NotAllowModifyDefaultStrategyPrincipal => {
                "NotAllowModifyDefaultStrategyPrincipal"
            }
            Code::NotAllowModifyOwnerDefaultStrategy => {
                "NotAllowModifyOwnerDefaultStrategy"
            }
            Code::EmptyAutToken => "EmptyAutToken",
            Code::TokenDisabled => "TokenDisabled",
            Code::TokenNotExisted => "TokenNotExisted",
            Code::AuthTokenForbidden => "AuthTokenForbidden",
            Code::OperationRoleForbidden => "OperationRoleForbidden",
        }
    }
    /// Creates an enum from field names used in the ProtoBuf definition.
    pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
        match value {
            "Unknown" => Some(Self::Unknown),
            "ExecuteSuccess" => Some(Self::ExecuteSuccess),
            "DataNoChange" => Some(Self::DataNoChange),
            "NoNeedUpdate" => Some(Self::NoNeedUpdate),
            "BadRequest" => Some(Self::BadRequest),
            "ParseException" => Some(Self::ParseException),
            "EmptyRequest" => Some(Self::EmptyRequest),
            "BatchSizeOverLimit" => Some(Self::BatchSizeOverLimit),
            "InvalidDiscoverResource" => Some(Self::InvalidDiscoverResource),
            "InvalidRequestID" => Some(Self::InvalidRequestId),
            "InvalidUserName" => Some(Self::InvalidUserName),
            "InvalidUserToken" => Some(Self::InvalidUserToken),
            "InvalidParameter" => Some(Self::InvalidParameter),
            "EmptyQueryParameter" => Some(Self::EmptyQueryParameter),
            "InvalidQueryInsParameter" => Some(Self::InvalidQueryInsParameter),
            "InvalidNamespaceName" => Some(Self::InvalidNamespaceName),
            "InvalidNamespaceOwners" => Some(Self::InvalidNamespaceOwners),
            "InvalidNamespaceToken" => Some(Self::InvalidNamespaceToken),
            "InvalidServiceName" => Some(Self::InvalidServiceName),
            "InvalidServiceOwners" => Some(Self::InvalidServiceOwners),
            "InvalidServiceToken" => Some(Self::InvalidServiceToken),
            "InvalidServiceMetadata" => Some(Self::InvalidServiceMetadata),
            "InvalidServicePorts" => Some(Self::InvalidServicePorts),
            "InvalidServiceBusiness" => Some(Self::InvalidServiceBusiness),
            "InvalidServiceDepartment" => Some(Self::InvalidServiceDepartment),
            "InvalidServiceCMDB" => Some(Self::InvalidServiceCmdb),
            "InvalidServiceComment" => Some(Self::InvalidServiceComment),
            "InvalidServiceAliasComment" => Some(Self::InvalidServiceAliasComment),
            "InvalidInstanceID" => Some(Self::InvalidInstanceId),
            "InvalidInstanceHost" => Some(Self::InvalidInstanceHost),
            "InvalidInstancePort" => Some(Self::InvalidInstancePort),
            "InvalidServiceAlias" => Some(Self::InvalidServiceAlias),
            "InvalidNamespaceWithAlias" => Some(Self::InvalidNamespaceWithAlias),
            "InvalidServiceAliasOwners" => Some(Self::InvalidServiceAliasOwners),
            "InvalidInstanceProtocol" => Some(Self::InvalidInstanceProtocol),
            "InvalidInstanceVersion" => Some(Self::InvalidInstanceVersion),
            "InvalidInstanceLogicSet" => Some(Self::InvalidInstanceLogicSet),
            "InvalidInstanceIsolate" => Some(Self::InvalidInstanceIsolate),
            "HealthCheckNotOpen" => Some(Self::HealthCheckNotOpen),
            "HeartbeatOnDisabledIns" => Some(Self::HeartbeatOnDisabledIns),
            "HeartbeatExceedLimit" => Some(Self::HeartbeatExceedLimit),
            "HeartbeatTypeNotFound" => Some(Self::HeartbeatTypeNotFound),
            "InvalidMetadata" => Some(Self::InvalidMetadata),
            "InvalidRateLimitID" => Some(Self::InvalidRateLimitId),
            "InvalidRateLimitLabels" => Some(Self::InvalidRateLimitLabels),
            "InvalidRateLimitAmounts" => Some(Self::InvalidRateLimitAmounts),
            "InvalidRateLimitName" => Some(Self::InvalidRateLimitName),
            "InvalidCircuitBreakerID" => Some(Self::InvalidCircuitBreakerId),
            "InvalidCircuitBreakerVersion" => Some(Self::InvalidCircuitBreakerVersion),
            "InvalidCircuitBreakerName" => Some(Self::InvalidCircuitBreakerName),
            "InvalidCircuitBreakerNamespace" => {
                Some(Self::InvalidCircuitBreakerNamespace)
            }
            "InvalidCircuitBreakerOwners" => Some(Self::InvalidCircuitBreakerOwners),
            "InvalidCircuitBreakerToken" => Some(Self::InvalidCircuitBreakerToken),
            "InvalidCircuitBreakerBusiness" => Some(Self::InvalidCircuitBreakerBusiness),
            "InvalidCircuitBreakerDepartment" => {
                Some(Self::InvalidCircuitBreakerDepartment)
            }
            "InvalidCircuitBreakerComment" => Some(Self::InvalidCircuitBreakerComment),
            "CircuitBreakerRuleExisted" => Some(Self::CircuitBreakerRuleExisted),
            "InvalidRoutingID" => Some(Self::InvalidRoutingId),
            "InvalidRoutingPolicy" => Some(Self::InvalidRoutingPolicy),
            "InvalidRoutingName" => Some(Self::InvalidRoutingName),
            "InvalidRoutingPriority" => Some(Self::InvalidRoutingPriority),
            "InvalidFaultDetectID" => Some(Self::InvalidFaultDetectId),
            "InvalidFaultDetectName" => Some(Self::InvalidFaultDetectName),
            "InvalidFaultDetectNamespace" => Some(Self::InvalidFaultDetectNamespace),
            "FaultDetectRuleExisted" => Some(Self::FaultDetectRuleExisted),
            "ServicesExistedMesh" => Some(Self::ServicesExistedMesh),
            "ResourcesExistedMesh" => Some(Self::ResourcesExistedMesh),
            "InvalidMeshParameter" => Some(Self::InvalidMeshParameter),
            "InvalidPlatformID" => Some(Self::InvalidPlatformId),
            "InvalidPlatformName" => Some(Self::InvalidPlatformName),
            "InvalidPlatformDomain" => Some(Self::InvalidPlatformDomain),
            "InvalidPlatformQPS" => Some(Self::InvalidPlatformQps),
            "InvalidPlatformToken" => Some(Self::InvalidPlatformToken),
            "InvalidPlatformOwner" => Some(Self::InvalidPlatformOwner),
            "InvalidPlatformDepartment" => Some(Self::InvalidPlatformDepartment),
            "InvalidPlatformComment" => Some(Self::InvalidPlatformComment),
            "NotFoundPlatform" => Some(Self::NotFoundPlatform),
            "InvalidFluxRateLimitId" => Some(Self::InvalidFluxRateLimitId),
            "InvalidFluxRateLimitQps" => Some(Self::InvalidFluxRateLimitQps),
            "InvalidFluxRateLimitSetKey" => Some(Self::InvalidFluxRateLimitSetKey),
            "ExistedResource" => Some(Self::ExistedResource),
            "NotFoundResource" => Some(Self::NotFoundResource),
            "NamespaceExistedServices" => Some(Self::NamespaceExistedServices),
            "ServiceExistedInstances" => Some(Self::ServiceExistedInstances),
            "ServiceExistedRoutings" => Some(Self::ServiceExistedRoutings),
            "ServiceExistedRateLimits" => Some(Self::ServiceExistedRateLimits),
            "ExistReleasedConfig" => Some(Self::ExistReleasedConfig),
            "SameInstanceRequest" => Some(Self::SameInstanceRequest),
            "ServiceExistedCircuitBreakers" => Some(Self::ServiceExistedCircuitBreakers),
            "ServiceExistedAlias" => Some(Self::ServiceExistedAlias),
            "NamespaceExistedMeshResources" => Some(Self::NamespaceExistedMeshResources),
            "NamespaceExistedCircuitBreakers" => {
                Some(Self::NamespaceExistedCircuitBreakers)
            }
            "ServiceSubscribedByMeshes" => Some(Self::ServiceSubscribedByMeshes),
            "ServiceExistedFluxRateLimits" => Some(Self::ServiceExistedFluxRateLimits),
            "NamespaceExistedConfigGroups" => Some(Self::NamespaceExistedConfigGroups),
            "NotFoundService" => Some(Self::NotFoundService),
            "NotFoundRouting" => Some(Self::NotFoundRouting),
            "NotFoundInstance" => Some(Self::NotFoundInstance),
            "NotFoundServiceAlias" => Some(Self::NotFoundServiceAlias),
            "NotFoundNamespace" => Some(Self::NotFoundNamespace),
            "NotFoundSourceService" => Some(Self::NotFoundSourceService),
            "NotFoundRateLimit" => Some(Self::NotFoundRateLimit),
            "NotFoundCircuitBreaker" => Some(Self::NotFoundCircuitBreaker),
            "NotFoundMasterConfig" => Some(Self::NotFoundMasterConfig),
            "NotFoundTagConfig" => Some(Self::NotFoundTagConfig),
            "NotFoundTagConfigOrService" => Some(Self::NotFoundTagConfigOrService),
            "ClientAPINotOpen" => Some(Self::ClientApiNotOpen),
            "NotAllowBusinessService" => Some(Self::NotAllowBusinessService),
            "NotAllowAliasUpdate" => Some(Self::NotAllowAliasUpdate),
            "NotAllowAliasCreateInstance" => Some(Self::NotAllowAliasCreateInstance),
            "NotAllowAliasCreateRouting" => Some(Self::NotAllowAliasCreateRouting),
            "NotAllowCreateAliasForAlias" => Some(Self::NotAllowCreateAliasForAlias),
            "NotAllowAliasCreateRateLimit" => Some(Self::NotAllowAliasCreateRateLimit),
            "NotAllowAliasBindRule" => Some(Self::NotAllowAliasBindRule),
            "NotAllowDifferentNamespaceBindRule" => {
                Some(Self::NotAllowDifferentNamespaceBindRule)
            }
            "Unauthorized" => Some(Self::Unauthorized),
            "NotAllowedAccess" => Some(Self::NotAllowedAccess),
            "CMDBNotFindHost" => Some(Self::CmdbNotFindHost),
            "DataConflict" => Some(Self::DataConflict),
            "InstanceTooManyRequests" => Some(Self::InstanceTooManyRequests),
            "IPRateLimit" => Some(Self::IpRateLimit),
            "APIRateLimit" => Some(Self::ApiRateLimit),
            "ExecuteException" => Some(Self::ExecuteException),
            "StoreLayerException" => Some(Self::StoreLayerException),
            "CMDBPluginException" => Some(Self::CmdbPluginException),
            "ParseRoutingException" => Some(Self::ParseRoutingException),
            "ParseRateLimitException" => Some(Self::ParseRateLimitException),
            "ParseCircuitBreakerException" => Some(Self::ParseCircuitBreakerException),
            "HeartbeatException" => Some(Self::HeartbeatException),
            "InstanceRegisTimeout" => Some(Self::InstanceRegisTimeout),
            "InvalidConfigFileGroupName" => Some(Self::InvalidConfigFileGroupName),
            "InvalidConfigFileName" => Some(Self::InvalidConfigFileName),
            "InvalidConfigFileContentLength" => {
                Some(Self::InvalidConfigFileContentLength)
            }
            "InvalidConfigFileFormat" => Some(Self::InvalidConfigFileFormat),
            "InvalidConfigFileTags" => Some(Self::InvalidConfigFileTags),
            "InvalidWatchConfigFileFormat" => Some(Self::InvalidWatchConfigFileFormat),
            "NotFoundResourceConfigFile" => Some(Self::NotFoundResourceConfigFile),
            "InvalidConfigFileTemplateName" => Some(Self::InvalidConfigFileTemplateName),
            "EncryptConfigFileException" => Some(Self::EncryptConfigFileException),
            "DecryptConfigFileException" => Some(Self::DecryptConfigFileException),
            "InvalidUserOwners" => Some(Self::InvalidUserOwners),
            "InvalidUserID" => Some(Self::InvalidUserId),
            "InvalidUserPassword" => Some(Self::InvalidUserPassword),
            "InvalidUserMobile" => Some(Self::InvalidUserMobile),
            "InvalidUserEmail" => Some(Self::InvalidUserEmail),
            "InvalidUserGroupOwners" => Some(Self::InvalidUserGroupOwners),
            "InvalidUserGroupID" => Some(Self::InvalidUserGroupId),
            "InvalidAuthStrategyOwners" => Some(Self::InvalidAuthStrategyOwners),
            "InvalidAuthStrategyName" => Some(Self::InvalidAuthStrategyName),
            "InvalidAuthStrategyID" => Some(Self::InvalidAuthStrategyId),
            "InvalidPrincipalType" => Some(Self::InvalidPrincipalType),
            "UserExisted" => Some(Self::UserExisted),
            "UserGroupExisted" => Some(Self::UserGroupExisted),
            "AuthStrategyRuleExisted" => Some(Self::AuthStrategyRuleExisted),
            "SubAccountExisted" => Some(Self::SubAccountExisted),
            "NotFoundUser" => Some(Self::NotFoundUser),
            "NotFoundOwnerUser" => Some(Self::NotFoundOwnerUser),
            "NotFoundUserGroup" => Some(Self::NotFoundUserGroup),
            "NotFoundAuthStrategyRule" => Some(Self::NotFoundAuthStrategyRule),
            "NotAllowModifyDefaultStrategyPrincipal" => {
                Some(Self::NotAllowModifyDefaultStrategyPrincipal)
            }
            "NotAllowModifyOwnerDefaultStrategy" => {
                Some(Self::NotAllowModifyOwnerDefaultStrategy)
            }
            "EmptyAutToken" => Some(Self::EmptyAutToken),
            "TokenDisabled" => Some(Self::TokenDisabled),
            "TokenNotExisted" => Some(Self::TokenNotExisted),
            "AuthTokenForbidden" => Some(Self::AuthTokenForbidden),
            "OperationRoleForbidden" => Some(Self::OperationRoleForbidden),
            _ => None,
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileGroup {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub create_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub create_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub modify_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub modify_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub file_count: ::core::option::Option<u64>,
    #[prost(message, repeated, tag = "10")]
    pub user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "11")]
    pub group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "13")]
    pub remove_user_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "14")]
    pub remove_group_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "15")]
    pub editable: ::core::option::Option<bool>,
    #[prost(message, optional, tag = "16")]
    pub owner: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "17")]
    pub business: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "18")]
    pub department: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(map = "string, string", tag = "19")]
    pub metadata: ::std::collections::HashMap<
        ::prost::alloc::string::String,
        ::prost::alloc::string::String,
    >,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFile {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub group: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub content: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub format: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub status: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "9")]
    pub tags: ::prost::alloc::vec::Vec<ConfigFileTag>,
    #[prost(message, optional, tag = "10")]
    pub create_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub create_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub modify_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "13")]
    pub modify_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "14")]
    pub release_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "15")]
    pub release_by: ::core::option::Option<::prost::alloc::string::String>,
    /// 是否为加密配置文件
    #[prost(message, optional, tag = "16")]
    pub encrypted: ::core::option::Option<bool>,
    /// 加密算法
    #[prost(message, optional, tag = "17")]
    pub encrypt_algo: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileTag {
    #[prost(message, optional, tag = "1")]
    pub key: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub value: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileRelease {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub group: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub file_name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub content: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub md5: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub version: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "10")]
    pub create_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub create_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "12")]
    pub modify_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "13")]
    pub modify_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "14")]
    pub tags: ::prost::alloc::vec::Vec<ConfigFileTag>,
    /// 当前生效配置
    #[prost(message, optional, tag = "15")]
    pub active: ::core::option::Option<bool>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileReleaseHistory {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub group: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub file_name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub content: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub format: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub md5: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "10")]
    pub r#type: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "11")]
    pub status: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "12")]
    pub tags: ::prost::alloc::vec::Vec<ConfigFileTag>,
    #[prost(message, optional, tag = "13")]
    pub create_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "14")]
    pub create_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "15")]
    pub modify_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "16")]
    pub modify_by: ::core::option::Option<::prost::alloc::string::String>,
    /// 配置发布失败的原因
    #[prost(message, optional, tag = "17")]
    pub reason: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileTemplate {
    #[prost(message, optional, tag = "1")]
    pub id: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "2")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub content: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub format: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub comment: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "6")]
    pub create_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "7")]
    pub create_by: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "8")]
    pub modify_time: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "9")]
    pub modify_by: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ClientConfigFileInfo {
    #[prost(message, optional, tag = "1")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub group: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub file_name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "4")]
    pub content: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "5")]
    pub version: ::core::option::Option<u64>,
    #[prost(message, optional, tag = "6")]
    pub md5: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "7")]
    pub tags: ::prost::alloc::vec::Vec<ConfigFileTag>,
    /// 是否为加密配置文件
    #[prost(message, optional, tag = "8")]
    pub encrypted: ::core::option::Option<bool>,
    /// 公钥，用于加密数据密钥
    #[prost(message, optional, tag = "9")]
    pub public_key: ::core::option::Option<::prost::alloc::string::String>,
    /// 配置文件版本名称
    #[prost(message, optional, tag = "10")]
    pub name: ::core::option::Option<::prost::alloc::string::String>,
    /// 配置文件的发布时间
    #[prost(message, optional, tag = "11")]
    pub release_time: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ClientWatchConfigFileRequest {
    #[prost(message, optional, tag = "1")]
    pub client_ip: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "2")]
    pub service_name: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "3")]
    pub watch_files: ::prost::alloc::vec::Vec<ClientConfigFileInfo>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigFileExportRequest {
    #[prost(message, optional, tag = "1")]
    pub namespace: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "2")]
    pub groups: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "3")]
    pub names: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigSimpleResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub config_file_group: ::core::option::Option<ConfigFileGroup>,
    #[prost(message, optional, tag = "4")]
    pub config_file: ::core::option::Option<ConfigFile>,
    #[prost(message, optional, tag = "5")]
    pub config_file_release: ::core::option::Option<ConfigFileRelease>,
    #[prost(message, optional, tag = "6")]
    pub config_file_release_history: ::core::option::Option<ConfigFileReleaseHistory>,
    #[prost(message, optional, tag = "7")]
    pub config_file_template: ::core::option::Option<ConfigFileTemplate>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigBatchWriteResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub total: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "4")]
    pub responses: ::prost::alloc::vec::Vec<ConfigResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigBatchQueryResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub total: ::core::option::Option<u32>,
    #[prost(message, repeated, tag = "4")]
    pub config_file_groups: ::prost::alloc::vec::Vec<ConfigFileGroup>,
    #[prost(message, repeated, tag = "5")]
    pub config_files: ::prost::alloc::vec::Vec<ConfigFile>,
    #[prost(message, repeated, tag = "6")]
    pub config_file_releases: ::prost::alloc::vec::Vec<ConfigFileRelease>,
    #[prost(message, repeated, tag = "7")]
    pub config_file_release_histories: ::prost::alloc::vec::Vec<
        ConfigFileReleaseHistory,
    >,
    #[prost(message, repeated, tag = "8")]
    pub config_file_templates: ::prost::alloc::vec::Vec<ConfigFileTemplate>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigClientResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub config_file: ::core::option::Option<ClientConfigFileInfo>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigImportResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "3")]
    pub create_config_files: ::prost::alloc::vec::Vec<ConfigFile>,
    #[prost(message, repeated, tag = "4")]
    pub skip_config_files: ::prost::alloc::vec::Vec<ConfigFile>,
    #[prost(message, repeated, tag = "5")]
    pub overwrite_config_files: ::prost::alloc::vec::Vec<ConfigFile>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigExportResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, optional, tag = "3")]
    pub data: ::core::option::Option<::prost::alloc::vec::Vec<u8>>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigEncryptAlgorithmResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(message, repeated, tag = "3")]
    pub algorithms: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ConfigClientListResponse {
    #[prost(message, optional, tag = "1")]
    pub code: ::core::option::Option<u32>,
    #[prost(message, optional, tag = "2")]
    pub info: ::core::option::Option<::prost::alloc::string::String>,
    #[prost(string, tag = "3")]
    pub namespace: ::prost::alloc::string::String,
    #[prost(string, tag = "4")]
    pub group: ::prost::alloc::string::String,
    #[prost(message, repeated, tag = "5")]
    pub config_file_names: ::prost::alloc::vec::Vec<ClientConfigFileInfo>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DiscoverRequest {
    #[prost(enumeration = "discover_request::DiscoverRequestType", tag = "1")]
    pub r#type: i32,
    #[prost(message, optional, tag = "2")]
    pub service: ::core::option::Option<Service>,
}
/// Nested message and enum types in `DiscoverRequest`.
pub mod discover_request {
    #[derive(
        Clone,
        Copy,
        Debug,
        PartialEq,
        Eq,
        Hash,
        PartialOrd,
        Ord,
        ::prost::Enumeration
    )]
    #[repr(i32)]
    pub enum DiscoverRequestType {
        Unknown = 0,
        Instance = 1,
        Cluster = 2,
        Routing = 3,
        RateLimit = 4,
        CircuitBreaker = 5,
        Services = 6,
        Namespaces = 12,
        FaultDetector = 13,
    }
    impl DiscoverRequestType {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                DiscoverRequestType::Unknown => "UNKNOWN",
                DiscoverRequestType::Instance => "INSTANCE",
                DiscoverRequestType::Cluster => "CLUSTER",
                DiscoverRequestType::Routing => "ROUTING",
                DiscoverRequestType::RateLimit => "RATE_LIMIT",
                DiscoverRequestType::CircuitBreaker => "CIRCUIT_BREAKER",
                DiscoverRequestType::Services => "SERVICES",
                DiscoverRequestType::Namespaces => "NAMESPACES",
                DiscoverRequestType::FaultDetector => "FAULT_DETECTOR",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "UNKNOWN" => Some(Self::Unknown),
                "INSTANCE" => Some(Self::Instance),
                "CLUSTER" => Some(Self::Cluster),
                "ROUTING" => Some(Self::Routing),
                "RATE_LIMIT" => Some(Self::RateLimit),
                "CIRCUIT_BREAKER" => Some(Self::CircuitBreaker),
                "SERVICES" => Some(Self::Services),
                "NAMESPACES" => Some(Self::Namespaces),
                "FAULT_DETECTOR" => Some(Self::FaultDetector),
                _ => None,
            }
        }
    }
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HeartbeatRecord {
    #[prost(string, tag = "1")]
    pub instance_id: ::prost::alloc::string::String,
    #[prost(int64, tag = "6")]
    pub last_heartbeat_sec: i64,
    #[prost(bool, tag = "7")]
    pub exist: bool,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct InstanceHeartbeat {
    #[prost(string, tag = "1")]
    pub instance_id: ::prost::alloc::string::String,
    #[prost(string, tag = "2")]
    pub service: ::prost::alloc::string::String,
    #[prost(string, tag = "3")]
    pub namespace: ::prost::alloc::string::String,
    #[prost(string, tag = "4")]
    pub host: ::prost::alloc::string::String,
    #[prost(uint32, tag = "5")]
    pub port: u32,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HeartbeatsRequest {
    #[prost(message, repeated, tag = "1")]
    pub heartbeats: ::prost::alloc::vec::Vec<InstanceHeartbeat>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct HeartbeatsResponse {}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GetHeartbeatsRequest {
    #[prost(string, repeated, tag = "1")]
    pub instance_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GetHeartbeatsResponse {
    #[prost(message, repeated, tag = "1")]
    pub records: ::prost::alloc::vec::Vec<HeartbeatRecord>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DelHeartbeatsRequest {
    #[prost(string, repeated, tag = "1")]
    pub instance_ids: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DelHeartbeatsResponse {
    #[prost(uint32, tag = "1")]
    pub code: u32,
    #[prost(string, tag = "2")]
    pub info: ::prost::alloc::string::String,
}
