// Code generated by protoc-gen-go. DO NOT EDIT.
// source: fault_detector.proto

package fault_tolerance // import "github.com/polarismesh/specification/source/go/api/v1/fault_tolerance"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import model "github.com/polarismesh/specification/source/go/api/v1/model"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// detect protocol
type FaultDetectRule_Protocol int32

const (
	FaultDetectRule_UNKNOWN FaultDetectRule_Protocol = 0
	FaultDetectRule_HTTP    FaultDetectRule_Protocol = 1
	FaultDetectRule_TCP     FaultDetectRule_Protocol = 2
	FaultDetectRule_UDP     FaultDetectRule_Protocol = 3
)

var FaultDetectRule_Protocol_name = map[int32]string{
	0: "UNKNOWN",
	1: "HTTP",
	2: "TCP",
	3: "UDP",
}
var FaultDetectRule_Protocol_value = map[string]int32{
	"UNKNOWN": 0,
	"HTTP":    1,
	"TCP":     2,
	"UDP":     3,
}

func (x FaultDetectRule_Protocol) String() string {
	return proto.EnumName(FaultDetectRule_Protocol_name, int32(x))
}
func (FaultDetectRule_Protocol) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{1, 0}
}

type FaultDetector struct {
	// fault detect rules for current service
	Rules []*FaultDetectRule `protobuf:"bytes,1,rep,name=rules,proto3" json:"rules,omitempty"`
	// total revision for the fault detect rules
	Revision             string   `protobuf:"bytes,2,opt,name=revision,proto3" json:"revision,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *FaultDetector) Reset()         { *m = FaultDetector{} }
func (m *FaultDetector) String() string { return proto.CompactTextString(m) }
func (*FaultDetector) ProtoMessage()    {}
func (*FaultDetector) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{0}
}
func (m *FaultDetector) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FaultDetector.Unmarshal(m, b)
}
func (m *FaultDetector) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FaultDetector.Marshal(b, m, deterministic)
}
func (dst *FaultDetector) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FaultDetector.Merge(dst, src)
}
func (m *FaultDetector) XXX_Size() int {
	return xxx_messageInfo_FaultDetector.Size(m)
}
func (m *FaultDetector) XXX_DiscardUnknown() {
	xxx_messageInfo_FaultDetector.DiscardUnknown(m)
}

var xxx_messageInfo_FaultDetector proto.InternalMessageInfo

func (m *FaultDetector) GetRules() []*FaultDetectRule {
	if m != nil {
		return m.Rules
	}
	return nil
}

func (m *FaultDetector) GetRevision() string {
	if m != nil {
		return m.Revision
	}
	return ""
}

type FaultDetectRule struct {
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// rule name
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// namespace of rule
	Namespace string `protobuf:"bytes,3,opt,name=namespace,proto3" json:"namespace,omitempty"`
	// revision routing version
	Revision string `protobuf:"bytes,4,opt,name=revision,proto3" json:"revision,omitempty"`
	// ctime create time of the rules
	Ctime string `protobuf:"bytes,5,opt,name=ctime,proto3" json:"ctime,omitempty"`
	// mtime modify time of the rules
	Mtime string `protobuf:"bytes,6,opt,name=mtime,proto3" json:"mtime,omitempty"`
	// description simple description rules
	Description string `protobuf:"bytes,7,opt,name=description,proto3" json:"description,omitempty"`
	// detect target
	TargetService *FaultDetectRule_DestinationService `protobuf:"bytes,21,opt,name=target_service,json=targetService,proto3" json:"target_service,omitempty"`
	// detect interval
	Interval uint32 `protobuf:"varint,22,opt,name=interval,proto3" json:"interval,omitempty"`
	// detect timeout
	Timeout uint32 `protobuf:"varint,23,opt,name=timeout,proto3" json:"timeout,omitempty"`
	// detect port
	Port     uint32                   `protobuf:"varint,24,opt,name=port,proto3" json:"port,omitempty"`
	Protocol FaultDetectRule_Protocol `protobuf:"varint,25,opt,name=protocol,proto3,enum=v1.FaultDetectRule_Protocol" json:"protocol,omitempty"`
	// http detect config
	HttpConfig *HttpProtocolConfig `protobuf:"bytes,26,opt,name=http_config,json=httpConfig,proto3" json:"http_config,omitempty"`
	// tcp detect config
	TcpConfig *TcpProtocolConfig `protobuf:"bytes,27,opt,name=tcp_config,json=tcpConfig,proto3" json:"tcp_config,omitempty"`
	// udp detect config
	UdpConfig            *UdpProtocolConfig `protobuf:"bytes,28,opt,name=udp_config,json=udpConfig,proto3" json:"udp_config,omitempty"`
	XXX_NoUnkeyedLiteral struct{}           `json:"-"`
	XXX_unrecognized     []byte             `json:"-"`
	XXX_sizecache        int32              `json:"-"`
}

func (m *FaultDetectRule) Reset()         { *m = FaultDetectRule{} }
func (m *FaultDetectRule) String() string { return proto.CompactTextString(m) }
func (*FaultDetectRule) ProtoMessage()    {}
func (*FaultDetectRule) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{1}
}
func (m *FaultDetectRule) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FaultDetectRule.Unmarshal(m, b)
}
func (m *FaultDetectRule) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FaultDetectRule.Marshal(b, m, deterministic)
}
func (dst *FaultDetectRule) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FaultDetectRule.Merge(dst, src)
}
func (m *FaultDetectRule) XXX_Size() int {
	return xxx_messageInfo_FaultDetectRule.Size(m)
}
func (m *FaultDetectRule) XXX_DiscardUnknown() {
	xxx_messageInfo_FaultDetectRule.DiscardUnknown(m)
}

var xxx_messageInfo_FaultDetectRule proto.InternalMessageInfo

func (m *FaultDetectRule) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *FaultDetectRule) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *FaultDetectRule) GetNamespace() string {
	if m != nil {
		return m.Namespace
	}
	return ""
}

func (m *FaultDetectRule) GetRevision() string {
	if m != nil {
		return m.Revision
	}
	return ""
}

func (m *FaultDetectRule) GetCtime() string {
	if m != nil {
		return m.Ctime
	}
	return ""
}

func (m *FaultDetectRule) GetMtime() string {
	if m != nil {
		return m.Mtime
	}
	return ""
}

func (m *FaultDetectRule) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func (m *FaultDetectRule) GetTargetService() *FaultDetectRule_DestinationService {
	if m != nil {
		return m.TargetService
	}
	return nil
}

func (m *FaultDetectRule) GetInterval() uint32 {
	if m != nil {
		return m.Interval
	}
	return 0
}

func (m *FaultDetectRule) GetTimeout() uint32 {
	if m != nil {
		return m.Timeout
	}
	return 0
}

func (m *FaultDetectRule) GetPort() uint32 {
	if m != nil {
		return m.Port
	}
	return 0
}

func (m *FaultDetectRule) GetProtocol() FaultDetectRule_Protocol {
	if m != nil {
		return m.Protocol
	}
	return FaultDetectRule_UNKNOWN
}

func (m *FaultDetectRule) GetHttpConfig() *HttpProtocolConfig {
	if m != nil {
		return m.HttpConfig
	}
	return nil
}

func (m *FaultDetectRule) GetTcpConfig() *TcpProtocolConfig {
	if m != nil {
		return m.TcpConfig
	}
	return nil
}

func (m *FaultDetectRule) GetUdpConfig() *UdpProtocolConfig {
	if m != nil {
		return m.UdpConfig
	}
	return nil
}

type FaultDetectRule_DestinationService struct {
	Service              string             `protobuf:"bytes,1,opt,name=service,proto3" json:"service,omitempty"`
	Namespace            string             `protobuf:"bytes,2,opt,name=namespace,proto3" json:"namespace,omitempty"`
	Method               *model.MatchString `protobuf:"bytes,3,opt,name=method,proto3" json:"method,omitempty"`
	XXX_NoUnkeyedLiteral struct{}           `json:"-"`
	XXX_unrecognized     []byte             `json:"-"`
	XXX_sizecache        int32              `json:"-"`
}

func (m *FaultDetectRule_DestinationService) Reset()         { *m = FaultDetectRule_DestinationService{} }
func (m *FaultDetectRule_DestinationService) String() string { return proto.CompactTextString(m) }
func (*FaultDetectRule_DestinationService) ProtoMessage()    {}
func (*FaultDetectRule_DestinationService) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{1, 0}
}
func (m *FaultDetectRule_DestinationService) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FaultDetectRule_DestinationService.Unmarshal(m, b)
}
func (m *FaultDetectRule_DestinationService) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FaultDetectRule_DestinationService.Marshal(b, m, deterministic)
}
func (dst *FaultDetectRule_DestinationService) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FaultDetectRule_DestinationService.Merge(dst, src)
}
func (m *FaultDetectRule_DestinationService) XXX_Size() int {
	return xxx_messageInfo_FaultDetectRule_DestinationService.Size(m)
}
func (m *FaultDetectRule_DestinationService) XXX_DiscardUnknown() {
	xxx_messageInfo_FaultDetectRule_DestinationService.DiscardUnknown(m)
}

var xxx_messageInfo_FaultDetectRule_DestinationService proto.InternalMessageInfo

func (m *FaultDetectRule_DestinationService) GetService() string {
	if m != nil {
		return m.Service
	}
	return ""
}

func (m *FaultDetectRule_DestinationService) GetNamespace() string {
	if m != nil {
		return m.Namespace
	}
	return ""
}

func (m *FaultDetectRule_DestinationService) GetMethod() *model.MatchString {
	if m != nil {
		return m.Method
	}
	return nil
}

type HttpProtocolConfig struct {
	Method               string                              `protobuf:"bytes,1,opt,name=method,proto3" json:"method,omitempty"`
	Url                  string                              `protobuf:"bytes,2,opt,name=url,proto3" json:"url,omitempty"`
	Headers              []*HttpProtocolConfig_MessageHeader `protobuf:"bytes,3,rep,name=headers,proto3" json:"headers,omitempty"`
	Body                 string                              `protobuf:"bytes,4,opt,name=body,proto3" json:"body,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                            `json:"-"`
	XXX_unrecognized     []byte                              `json:"-"`
	XXX_sizecache        int32                               `json:"-"`
}

func (m *HttpProtocolConfig) Reset()         { *m = HttpProtocolConfig{} }
func (m *HttpProtocolConfig) String() string { return proto.CompactTextString(m) }
func (*HttpProtocolConfig) ProtoMessage()    {}
func (*HttpProtocolConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{2}
}
func (m *HttpProtocolConfig) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_HttpProtocolConfig.Unmarshal(m, b)
}
func (m *HttpProtocolConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_HttpProtocolConfig.Marshal(b, m, deterministic)
}
func (dst *HttpProtocolConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_HttpProtocolConfig.Merge(dst, src)
}
func (m *HttpProtocolConfig) XXX_Size() int {
	return xxx_messageInfo_HttpProtocolConfig.Size(m)
}
func (m *HttpProtocolConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_HttpProtocolConfig.DiscardUnknown(m)
}

var xxx_messageInfo_HttpProtocolConfig proto.InternalMessageInfo

func (m *HttpProtocolConfig) GetMethod() string {
	if m != nil {
		return m.Method
	}
	return ""
}

func (m *HttpProtocolConfig) GetUrl() string {
	if m != nil {
		return m.Url
	}
	return ""
}

func (m *HttpProtocolConfig) GetHeaders() []*HttpProtocolConfig_MessageHeader {
	if m != nil {
		return m.Headers
	}
	return nil
}

func (m *HttpProtocolConfig) GetBody() string {
	if m != nil {
		return m.Body
	}
	return ""
}

type HttpProtocolConfig_MessageHeader struct {
	Key                  string   `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	Value                string   `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *HttpProtocolConfig_MessageHeader) Reset()         { *m = HttpProtocolConfig_MessageHeader{} }
func (m *HttpProtocolConfig_MessageHeader) String() string { return proto.CompactTextString(m) }
func (*HttpProtocolConfig_MessageHeader) ProtoMessage()    {}
func (*HttpProtocolConfig_MessageHeader) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{2, 0}
}
func (m *HttpProtocolConfig_MessageHeader) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_HttpProtocolConfig_MessageHeader.Unmarshal(m, b)
}
func (m *HttpProtocolConfig_MessageHeader) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_HttpProtocolConfig_MessageHeader.Marshal(b, m, deterministic)
}
func (dst *HttpProtocolConfig_MessageHeader) XXX_Merge(src proto.Message) {
	xxx_messageInfo_HttpProtocolConfig_MessageHeader.Merge(dst, src)
}
func (m *HttpProtocolConfig_MessageHeader) XXX_Size() int {
	return xxx_messageInfo_HttpProtocolConfig_MessageHeader.Size(m)
}
func (m *HttpProtocolConfig_MessageHeader) XXX_DiscardUnknown() {
	xxx_messageInfo_HttpProtocolConfig_MessageHeader.DiscardUnknown(m)
}

var xxx_messageInfo_HttpProtocolConfig_MessageHeader proto.InternalMessageInfo

func (m *HttpProtocolConfig_MessageHeader) GetKey() string {
	if m != nil {
		return m.Key
	}
	return ""
}

func (m *HttpProtocolConfig_MessageHeader) GetValue() string {
	if m != nil {
		return m.Value
	}
	return ""
}

type TcpProtocolConfig struct {
	Send                 string   `protobuf:"bytes,1,opt,name=send,proto3" json:"send,omitempty"`
	Receive              []string `protobuf:"bytes,2,rep,name=receive,proto3" json:"receive,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *TcpProtocolConfig) Reset()         { *m = TcpProtocolConfig{} }
func (m *TcpProtocolConfig) String() string { return proto.CompactTextString(m) }
func (*TcpProtocolConfig) ProtoMessage()    {}
func (*TcpProtocolConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{3}
}
func (m *TcpProtocolConfig) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TcpProtocolConfig.Unmarshal(m, b)
}
func (m *TcpProtocolConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TcpProtocolConfig.Marshal(b, m, deterministic)
}
func (dst *TcpProtocolConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TcpProtocolConfig.Merge(dst, src)
}
func (m *TcpProtocolConfig) XXX_Size() int {
	return xxx_messageInfo_TcpProtocolConfig.Size(m)
}
func (m *TcpProtocolConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_TcpProtocolConfig.DiscardUnknown(m)
}

var xxx_messageInfo_TcpProtocolConfig proto.InternalMessageInfo

func (m *TcpProtocolConfig) GetSend() string {
	if m != nil {
		return m.Send
	}
	return ""
}

func (m *TcpProtocolConfig) GetReceive() []string {
	if m != nil {
		return m.Receive
	}
	return nil
}

type UdpProtocolConfig struct {
	Send                 string   `protobuf:"bytes,1,opt,name=send,proto3" json:"send,omitempty"`
	Receive              []string `protobuf:"bytes,2,rep,name=receive,proto3" json:"receive,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UdpProtocolConfig) Reset()         { *m = UdpProtocolConfig{} }
func (m *UdpProtocolConfig) String() string { return proto.CompactTextString(m) }
func (*UdpProtocolConfig) ProtoMessage()    {}
func (*UdpProtocolConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_fault_detector_4af7b01d1c238a61, []int{4}
}
func (m *UdpProtocolConfig) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UdpProtocolConfig.Unmarshal(m, b)
}
func (m *UdpProtocolConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UdpProtocolConfig.Marshal(b, m, deterministic)
}
func (dst *UdpProtocolConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UdpProtocolConfig.Merge(dst, src)
}
func (m *UdpProtocolConfig) XXX_Size() int {
	return xxx_messageInfo_UdpProtocolConfig.Size(m)
}
func (m *UdpProtocolConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_UdpProtocolConfig.DiscardUnknown(m)
}

var xxx_messageInfo_UdpProtocolConfig proto.InternalMessageInfo

func (m *UdpProtocolConfig) GetSend() string {
	if m != nil {
		return m.Send
	}
	return ""
}

func (m *UdpProtocolConfig) GetReceive() []string {
	if m != nil {
		return m.Receive
	}
	return nil
}

func init() {
	proto.RegisterType((*FaultDetector)(nil), "v1.FaultDetector")
	proto.RegisterType((*FaultDetectRule)(nil), "v1.FaultDetectRule")
	proto.RegisterType((*FaultDetectRule_DestinationService)(nil), "v1.FaultDetectRule.DestinationService")
	proto.RegisterType((*HttpProtocolConfig)(nil), "v1.HttpProtocolConfig")
	proto.RegisterType((*HttpProtocolConfig_MessageHeader)(nil), "v1.HttpProtocolConfig.MessageHeader")
	proto.RegisterType((*TcpProtocolConfig)(nil), "v1.TcpProtocolConfig")
	proto.RegisterType((*UdpProtocolConfig)(nil), "v1.UdpProtocolConfig")
	proto.RegisterEnum("v1.FaultDetectRule_Protocol", FaultDetectRule_Protocol_name, FaultDetectRule_Protocol_value)
}

func init() {
	proto.RegisterFile("fault_detector.proto", fileDescriptor_fault_detector_4af7b01d1c238a61)
}

var fileDescriptor_fault_detector_4af7b01d1c238a61 = []byte{
	// 682 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x54, 0xdd, 0x4e, 0xdb, 0x4a,
	0x10, 0x3e, 0xce, 0x0f, 0x09, 0x13, 0x05, 0x72, 0xf6, 0x00, 0x67, 0x4f, 0x0e, 0x17, 0x51, 0x54,
	0xb5, 0xe9, 0x8d, 0x23, 0x42, 0x25, 0xb8, 0xaa, 0x54, 0xa0, 0x15, 0x6a, 0x05, 0x8d, 0x4c, 0x68,
	0xa5, 0xde, 0xa0, 0x65, 0x3d, 0x24, 0xab, 0xda, 0x5e, 0x6b, 0x77, 0x6d, 0x89, 0x07, 0xe9, 0x53,
	0xf5, 0x41, 0xfa, 0x1a, 0xd5, 0xae, 0xed, 0x40, 0x08, 0x37, 0xbd, 0xca, 0x7c, 0x33, 0xdf, 0x37,
	0x33, 0x99, 0x99, 0x35, 0xec, 0xdc, 0xb1, 0x2c, 0x32, 0x37, 0x21, 0x1a, 0xe4, 0x46, 0x2a, 0x3f,
	0x55, 0xd2, 0x48, 0x52, 0xcb, 0x0f, 0xfa, 0x9d, 0x58, 0x86, 0x18, 0x15, 0x8e, 0xe1, 0x17, 0xe8,
	0x7e, 0xb0, 0xc4, 0xb3, 0x92, 0x47, 0x5e, 0x43, 0x53, 0x65, 0x11, 0x6a, 0xea, 0x0d, 0xea, 0xa3,
	0xce, 0xe4, 0x1f, 0x3f, 0x3f, 0xf0, 0x1f, 0x31, 0x82, 0x2c, 0xc2, 0xa0, 0x60, 0x90, 0x3e, 0xb4,
	0x15, 0xe6, 0x42, 0x0b, 0x99, 0xd0, 0xda, 0xc0, 0x1b, 0x6d, 0x06, 0x4b, 0x3c, 0xfc, 0xd5, 0x84,
	0xed, 0x27, 0x32, 0xb2, 0x05, 0x35, 0x11, 0x52, 0xcf, 0x31, 0x6b, 0x22, 0x24, 0x04, 0x1a, 0x09,
	0x8b, 0xb1, 0xd4, 0x3a, 0x9b, 0xec, 0xc3, 0xa6, 0xfd, 0xd5, 0x29, 0xe3, 0x48, 0xeb, 0x2e, 0xf0,
	0xe0, 0x58, 0xa9, 0xd8, 0x58, 0xad, 0x48, 0x76, 0xa0, 0xc9, 0x8d, 0x88, 0x91, 0x36, 0x5d, 0xa0,
	0x00, 0xd6, 0x1b, 0x3b, 0xef, 0x46, 0xe1, 0x75, 0x80, 0x0c, 0xa0, 0x13, 0xa2, 0xe6, 0x4a, 0xa4,
	0xc6, 0xa6, 0x6a, 0xb9, 0xd8, 0x63, 0x17, 0xb9, 0x80, 0x2d, 0xc3, 0xd4, 0x1c, 0xcd, 0x8d, 0x46,
	0x95, 0x0b, 0x8e, 0x74, 0x77, 0xe0, 0x8d, 0x3a, 0x93, 0x97, 0xcf, 0xcc, 0xc3, 0x3f, 0x43, 0x6d,
	0x44, 0xc2, 0xac, 0xf0, 0xaa, 0x60, 0x07, 0xdd, 0x42, 0x5d, 0x42, 0xdb, 0xb8, 0x48, 0x0c, 0xaa,
	0x9c, 0x45, 0x74, 0x6f, 0xe0, 0x8d, 0xba, 0xc1, 0x12, 0x13, 0x0a, 0x2d, 0xdb, 0x94, 0xcc, 0x0c,
	0xfd, 0xd7, 0x85, 0x2a, 0x68, 0x07, 0x94, 0x4a, 0x65, 0x28, 0x75, 0x6e, 0x67, 0x93, 0x63, 0x68,
	0xbb, 0xcd, 0x71, 0x19, 0xd1, 0xff, 0x06, 0xde, 0x68, 0x6b, 0xb2, 0xff, 0x5c, 0x4b, 0xd3, 0x92,
	0x13, 0x2c, 0xd9, 0xe4, 0x08, 0x3a, 0x0b, 0x63, 0xd2, 0x1b, 0x2e, 0x93, 0x3b, 0x31, 0xa7, 0x7d,
	0xf7, 0x7f, 0xf6, 0xac, 0xf8, 0xdc, 0x98, 0xb4, 0x12, 0x9c, 0xba, 0x68, 0x00, 0x96, 0x5a, 0xd8,
	0xe4, 0x0d, 0x80, 0xe1, 0x4b, 0xdd, 0xff, 0x4e, 0xb7, 0x6b, 0x75, 0x33, 0xfe, 0x54, 0xb6, 0x69,
	0xf8, 0x23, 0x55, 0x16, 0x2e, 0x55, 0xfb, 0x0f, 0xaa, 0xeb, 0x70, 0x4d, 0x95, 0x85, 0xa5, 0xaa,
	0x9f, 0x01, 0x59, 0x9f, 0xa6, 0x1d, 0x51, 0xb5, 0x86, 0xe2, 0x7c, 0x2a, 0xb8, 0x7a, 0x2f, 0xb5,
	0xa7, 0xf7, 0xf2, 0x0a, 0x36, 0x62, 0x34, 0x0b, 0x19, 0xba, 0x53, 0xea, 0x4c, 0xb6, 0x6d, 0xfd,
	0x0b, 0x66, 0xf8, 0xe2, 0xca, 0x28, 0x91, 0xcc, 0x83, 0x32, 0x3c, 0x3c, 0x84, 0x76, 0xd5, 0x13,
	0xe9, 0x40, 0xeb, 0xfa, 0xf2, 0xd3, 0xe5, 0xe7, 0xaf, 0x97, 0xbd, 0xbf, 0x48, 0x1b, 0x1a, 0xe7,
	0xb3, 0xd9, 0xb4, 0xe7, 0x91, 0x16, 0xd4, 0x67, 0xa7, 0xd3, 0x5e, 0xcd, 0x1a, 0xd7, 0x67, 0xd3,
	0x5e, 0xfd, 0x63, 0xa3, 0xdd, 0xee, 0xed, 0x0e, 0x7f, 0x7a, 0x40, 0xd6, 0x07, 0x48, 0xf6, 0x96,
	0xa5, 0x8b, 0x8e, 0x4b, 0x44, 0x7a, 0x50, 0xcf, 0x54, 0x54, 0xb6, 0x6a, 0x4d, 0xf2, 0x16, 0x5a,
	0x0b, 0x64, 0x21, 0x2a, 0x4d, 0xeb, 0xee, 0xcd, 0xbd, 0x78, 0x7e, 0x27, 0xfe, 0x05, 0x6a, 0xcd,
	0xe6, 0x78, 0xee, 0xc8, 0x41, 0x25, 0xb2, 0x57, 0x72, 0x2b, 0xc3, 0xfb, 0xf2, 0x41, 0x38, 0xbb,
	0x7f, 0x04, 0xdd, 0x15, 0xb6, 0x2d, 0xfb, 0x1d, 0xef, 0xcb, 0x5e, 0xac, 0x69, 0x5f, 0x46, 0xce,
	0xa2, 0xac, 0x9a, 0x5a, 0x01, 0x86, 0xef, 0xe0, 0xef, 0xb5, 0xad, 0xda, 0x0a, 0x1a, 0x93, 0xea,
	0x9f, 0x38, 0xdb, 0xae, 0x44, 0x21, 0x47, 0x91, 0xdb, 0x04, 0x75, 0xbb, 0x92, 0x12, 0xda, 0x14,
	0x6b, 0x2b, 0xfe, 0xb3, 0x14, 0x27, 0x3f, 0x3c, 0x38, 0xe6, 0x32, 0xf6, 0x0d, 0x26, 0x1c, 0x13,
	0xe3, 0xa7, 0x32, 0x62, 0x4a, 0x68, 0x5f, 0xa7, 0xc8, 0xc5, 0x9d, 0xe0, 0xee, 0x38, 0x7c, 0x96,
	0x0a, 0x3b, 0x29, 0xf7, 0xa1, 0xf3, 0x8d, 0x8c, 0x50, 0xb1, 0x84, 0xe3, 0x09, 0x59, 0xf9, 0xa0,
	0xb9, 0x3e, 0xbe, 0xbd, 0x9f, 0x0b, 0xb3, 0xc8, 0x6e, 0x7d, 0x2e, 0xe3, 0x71, 0x99, 0x2c, 0x46,
	0xbd, 0x18, 0xaf, 0x24, 0x1c, 0x6b, 0x99, 0x29, 0x8e, 0xe3, 0xb9, 0x1c, 0xb3, 0x54, 0x8c, 0xf3,
	0x83, 0x71, 0xf1, 0x0d, 0x5d, 0xa6, 0xbe, 0xdd, 0x70, 0x8f, 0xe9, 0xf0, 0x77, 0x00, 0x00, 0x00,
	0xff, 0xff, 0x5b, 0x34, 0xf6, 0x08, 0x5d, 0x05, 0x00, 0x00,
}
