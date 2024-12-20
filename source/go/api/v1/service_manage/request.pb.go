// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.33.0
// 	protoc        v5.27.3
// source: request.proto

package service_manage

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type DiscoverRequest_DiscoverRequestType int32

const (
	DiscoverRequest_UNKNOWN         DiscoverRequest_DiscoverRequestType = 0
	DiscoverRequest_INSTANCE        DiscoverRequest_DiscoverRequestType = 1
	DiscoverRequest_CLUSTER         DiscoverRequest_DiscoverRequestType = 2
	DiscoverRequest_ROUTING         DiscoverRequest_DiscoverRequestType = 3
	DiscoverRequest_RATE_LIMIT      DiscoverRequest_DiscoverRequestType = 4
	DiscoverRequest_CIRCUIT_BREAKER DiscoverRequest_DiscoverRequestType = 5
	DiscoverRequest_SERVICES        DiscoverRequest_DiscoverRequestType = 6
	DiscoverRequest_NAMESPACES      DiscoverRequest_DiscoverRequestType = 12
	DiscoverRequest_FAULT_DETECTOR  DiscoverRequest_DiscoverRequestType = 13
	DiscoverRequest_LANE            DiscoverRequest_DiscoverRequestType = 100
	// 自定义路由规则
	DiscoverRequest_CUSTOM_ROUTE_RULE DiscoverRequest_DiscoverRequestType = 101
	// 就近路由规则
	DiscoverRequest_NEARBY_ROUTE_RULE DiscoverRequest_DiscoverRequestType = 102
	// 无损上下线规则
	DiscoverRequest_LOSSLESS DiscoverRequest_DiscoverRequestType = 103
	// 服务黑白名单规则
	DiscoverRequest_BLOCK_ALLOW_RULE DiscoverRequest_DiscoverRequestType = 104
)

// Enum value maps for DiscoverRequest_DiscoverRequestType.
var (
	DiscoverRequest_DiscoverRequestType_name = map[int32]string{
		0:   "UNKNOWN",
		1:   "INSTANCE",
		2:   "CLUSTER",
		3:   "ROUTING",
		4:   "RATE_LIMIT",
		5:   "CIRCUIT_BREAKER",
		6:   "SERVICES",
		12:  "NAMESPACES",
		13:  "FAULT_DETECTOR",
		100: "LANE",
		101: "CUSTOM_ROUTE_RULE",
		102: "NEARBY_ROUTE_RULE",
		103: "LOSSLESS",
		104: "BLOCK_ALLOW_RULE",
	}
	DiscoverRequest_DiscoverRequestType_value = map[string]int32{
		"UNKNOWN":           0,
		"INSTANCE":          1,
		"CLUSTER":           2,
		"ROUTING":           3,
		"RATE_LIMIT":        4,
		"CIRCUIT_BREAKER":   5,
		"SERVICES":          6,
		"NAMESPACES":        12,
		"FAULT_DETECTOR":    13,
		"LANE":              100,
		"CUSTOM_ROUTE_RULE": 101,
		"NEARBY_ROUTE_RULE": 102,
		"LOSSLESS":          103,
		"BLOCK_ALLOW_RULE":  104,
	}
)

func (x DiscoverRequest_DiscoverRequestType) Enum() *DiscoverRequest_DiscoverRequestType {
	p := new(DiscoverRequest_DiscoverRequestType)
	*p = x
	return p
}

func (x DiscoverRequest_DiscoverRequestType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (DiscoverRequest_DiscoverRequestType) Descriptor() protoreflect.EnumDescriptor {
	return file_request_proto_enumTypes[0].Descriptor()
}

func (DiscoverRequest_DiscoverRequestType) Type() protoreflect.EnumType {
	return &file_request_proto_enumTypes[0]
}

func (x DiscoverRequest_DiscoverRequestType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use DiscoverRequest_DiscoverRequestType.Descriptor instead.
func (DiscoverRequest_DiscoverRequestType) EnumDescriptor() ([]byte, []int) {
	return file_request_proto_rawDescGZIP(), []int{1, 0}
}

type DiscoverFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	OnlyHealthyInstance bool `protobuf:"varint,1,opt,name=OnlyHealthyInstance,proto3" json:"OnlyHealthyInstance,omitempty"`
}

func (x *DiscoverFilter) Reset() {
	*x = DiscoverFilter{}
	if protoimpl.UnsafeEnabled {
		mi := &file_request_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DiscoverFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DiscoverFilter) ProtoMessage() {}

func (x *DiscoverFilter) ProtoReflect() protoreflect.Message {
	mi := &file_request_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DiscoverFilter.ProtoReflect.Descriptor instead.
func (*DiscoverFilter) Descriptor() ([]byte, []int) {
	return file_request_proto_rawDescGZIP(), []int{0}
}

func (x *DiscoverFilter) GetOnlyHealthyInstance() bool {
	if x != nil {
		return x.OnlyHealthyInstance
	}
	return false
}

type DiscoverRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type    DiscoverRequest_DiscoverRequestType `protobuf:"varint,1,opt,name=type,proto3,enum=v1.DiscoverRequest_DiscoverRequestType" json:"type,omitempty"`
	Service *Service                            `protobuf:"bytes,2,opt,name=service,proto3" json:"service,omitempty"`
	Filter  *DiscoverFilter                     `protobuf:"bytes,30,opt,name=Filter,proto3" json:"Filter,omitempty"`
}

func (x *DiscoverRequest) Reset() {
	*x = DiscoverRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_request_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DiscoverRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DiscoverRequest) ProtoMessage() {}

func (x *DiscoverRequest) ProtoReflect() protoreflect.Message {
	mi := &file_request_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DiscoverRequest.ProtoReflect.Descriptor instead.
func (*DiscoverRequest) Descriptor() ([]byte, []int) {
	return file_request_proto_rawDescGZIP(), []int{1}
}

func (x *DiscoverRequest) GetType() DiscoverRequest_DiscoverRequestType {
	if x != nil {
		return x.Type
	}
	return DiscoverRequest_UNKNOWN
}

func (x *DiscoverRequest) GetService() *Service {
	if x != nil {
		return x.Service
	}
	return nil
}

func (x *DiscoverRequest) GetFilter() *DiscoverFilter {
	if x != nil {
		return x.Filter
	}
	return nil
}

var File_request_proto protoreflect.FileDescriptor

var file_request_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x02, 0x76, 0x31, 0x1a, 0x0d, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x22, 0x42, 0x0a, 0x0e, 0x44, 0x69, 0x73, 0x63, 0x6f, 0x76, 0x65, 0x72, 0x46, 0x69,
	0x6c, 0x74, 0x65, 0x72, 0x12, 0x30, 0x0a, 0x13, 0x4f, 0x6e, 0x6c, 0x79, 0x48, 0x65, 0x61, 0x6c,
	0x74, 0x68, 0x79, 0x49, 0x6e, 0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x08, 0x52, 0x13, 0x4f, 0x6e, 0x6c, 0x79, 0x48, 0x65, 0x61, 0x6c, 0x74, 0x68, 0x79, 0x49, 0x6e,
	0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x22, 0xb3, 0x03, 0x0a, 0x0f, 0x44, 0x69, 0x73, 0x63, 0x6f,
	0x76, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x3b, 0x0a, 0x04, 0x74, 0x79,
	0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x27, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x69,
	0x73, 0x63, 0x6f, 0x76, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x2e, 0x44, 0x69,
	0x73, 0x63, 0x6f, 0x76, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x54, 0x79, 0x70,
	0x65, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x25, 0x0a, 0x07, 0x73, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0b, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65,
	0x72, 0x76, 0x69, 0x63, 0x65, 0x52, 0x07, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x2a,
	0x0a, 0x06, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x18, 0x1e, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12,
	0x2e, 0x76, 0x31, 0x2e, 0x44, 0x69, 0x73, 0x63, 0x6f, 0x76, 0x65, 0x72, 0x46, 0x69, 0x6c, 0x74,
	0x65, 0x72, 0x52, 0x06, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x22, 0x89, 0x02, 0x0a, 0x13, 0x44,
	0x69, 0x73, 0x63, 0x6f, 0x76, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x54, 0x79,
	0x70, 0x65, 0x12, 0x0b, 0x0a, 0x07, 0x55, 0x4e, 0x4b, 0x4e, 0x4f, 0x57, 0x4e, 0x10, 0x00, 0x12,
	0x0c, 0x0a, 0x08, 0x49, 0x4e, 0x53, 0x54, 0x41, 0x4e, 0x43, 0x45, 0x10, 0x01, 0x12, 0x0b, 0x0a,
	0x07, 0x43, 0x4c, 0x55, 0x53, 0x54, 0x45, 0x52, 0x10, 0x02, 0x12, 0x0b, 0x0a, 0x07, 0x52, 0x4f,
	0x55, 0x54, 0x49, 0x4e, 0x47, 0x10, 0x03, 0x12, 0x0e, 0x0a, 0x0a, 0x52, 0x41, 0x54, 0x45, 0x5f,
	0x4c, 0x49, 0x4d, 0x49, 0x54, 0x10, 0x04, 0x12, 0x13, 0x0a, 0x0f, 0x43, 0x49, 0x52, 0x43, 0x55,
	0x49, 0x54, 0x5f, 0x42, 0x52, 0x45, 0x41, 0x4b, 0x45, 0x52, 0x10, 0x05, 0x12, 0x0c, 0x0a, 0x08,
	0x53, 0x45, 0x52, 0x56, 0x49, 0x43, 0x45, 0x53, 0x10, 0x06, 0x12, 0x0e, 0x0a, 0x0a, 0x4e, 0x41,
	0x4d, 0x45, 0x53, 0x50, 0x41, 0x43, 0x45, 0x53, 0x10, 0x0c, 0x12, 0x12, 0x0a, 0x0e, 0x46, 0x41,
	0x55, 0x4c, 0x54, 0x5f, 0x44, 0x45, 0x54, 0x45, 0x43, 0x54, 0x4f, 0x52, 0x10, 0x0d, 0x12, 0x08,
	0x0a, 0x04, 0x4c, 0x41, 0x4e, 0x45, 0x10, 0x64, 0x12, 0x15, 0x0a, 0x11, 0x43, 0x55, 0x53, 0x54,
	0x4f, 0x4d, 0x5f, 0x52, 0x4f, 0x55, 0x54, 0x45, 0x5f, 0x52, 0x55, 0x4c, 0x45, 0x10, 0x65, 0x12,
	0x15, 0x0a, 0x11, 0x4e, 0x45, 0x41, 0x52, 0x42, 0x59, 0x5f, 0x52, 0x4f, 0x55, 0x54, 0x45, 0x5f,
	0x52, 0x55, 0x4c, 0x45, 0x10, 0x66, 0x12, 0x0c, 0x0a, 0x08, 0x4c, 0x4f, 0x53, 0x53, 0x4c, 0x45,
	0x53, 0x53, 0x10, 0x67, 0x12, 0x14, 0x0a, 0x10, 0x42, 0x4c, 0x4f, 0x43, 0x4b, 0x5f, 0x41, 0x4c,
	0x4c, 0x4f, 0x57, 0x5f, 0x52, 0x55, 0x4c, 0x45, 0x10, 0x68, 0x22, 0x04, 0x08, 0x07, 0x10, 0x0b,
	0x22, 0x04, 0x08, 0x0e, 0x10, 0x63, 0x4a, 0x04, 0x08, 0x03, 0x10, 0x05, 0x42, 0x8d, 0x01, 0x0a,
	0x37, 0x63, 0x6f, 0x6d, 0x2e, 0x74, 0x65, 0x6e, 0x63, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x6f, 0x6c,
	0x61, 0x72, 0x69, 0x73, 0x2e, 0x73, 0x70, 0x65, 0x63, 0x69, 0x66, 0x69, 0x63, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x2e, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x42, 0x0c, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x5a, 0x44, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x70, 0x6f, 0x6c, 0x61, 0x72, 0x69, 0x73, 0x6d, 0x65, 0x73, 0x68, 0x2f, 0x73,
	0x70, 0x65, 0x63, 0x69, 0x66, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2f, 0x73, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x73, 0x65,
	0x72, 0x76, 0x69, 0x63, 0x65, 0x5f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_request_proto_rawDescOnce sync.Once
	file_request_proto_rawDescData = file_request_proto_rawDesc
)

func file_request_proto_rawDescGZIP() []byte {
	file_request_proto_rawDescOnce.Do(func() {
		file_request_proto_rawDescData = protoimpl.X.CompressGZIP(file_request_proto_rawDescData)
	})
	return file_request_proto_rawDescData
}

var file_request_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_request_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_request_proto_goTypes = []interface{}{
	(DiscoverRequest_DiscoverRequestType)(0), // 0: v1.DiscoverRequest.DiscoverRequestType
	(*DiscoverFilter)(nil),                   // 1: v1.DiscoverFilter
	(*DiscoverRequest)(nil),                  // 2: v1.DiscoverRequest
	(*Service)(nil),                          // 3: v1.Service
}
var file_request_proto_depIdxs = []int32{
	0, // 0: v1.DiscoverRequest.type:type_name -> v1.DiscoverRequest.DiscoverRequestType
	3, // 1: v1.DiscoverRequest.service:type_name -> v1.Service
	1, // 2: v1.DiscoverRequest.Filter:type_name -> v1.DiscoverFilter
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_request_proto_init() }
func file_request_proto_init() {
	if File_request_proto != nil {
		return
	}
	file_service_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_request_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DiscoverFilter); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_request_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DiscoverRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_request_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_request_proto_goTypes,
		DependencyIndexes: file_request_proto_depIdxs,
		EnumInfos:         file_request_proto_enumTypes,
		MessageInfos:      file_request_proto_msgTypes,
	}.Build()
	File_request_proto = out.File
	file_request_proto_rawDesc = nil
	file_request_proto_goTypes = nil
	file_request_proto_depIdxs = nil
}
