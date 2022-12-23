// Code generated by protoc-gen-go. DO NOT EDIT.
// source: client.proto

package service_manage // import "github.com/polarismesh/specification/source/go/api/v1/service_manage"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import model "github.com/polarismesh/specification/source/go/api/v1/model"
import wrapperspb "google.golang.org/protobuf/types/known/wrapperspb"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Client_ClientType int32

const (
	Client_UNKNOWN Client_ClientType = 0
	Client_SDK     Client_ClientType = 1
	Client_AGENT   Client_ClientType = 2
)

var Client_ClientType_name = map[int32]string{
	0: "UNKNOWN",
	1: "SDK",
	2: "AGENT",
}
var Client_ClientType_value = map[string]int32{
	"UNKNOWN": 0,
	"SDK":     1,
	"AGENT":   2,
}

func (x Client_ClientType) String() string {
	return proto.EnumName(Client_ClientType_name, int32(x))
}
func (Client_ClientType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_client_ac96b32637bf3687, []int{0, 0}
}

type Client struct {
	Host                 *wrapperspb.StringValue `protobuf:"bytes,1,opt,name=host,proto3" json:"host,omitempty"`
	Type                 Client_ClientType       `protobuf:"varint,2,opt,name=type,proto3,enum=polaris.v1.Client_ClientType" json:"type,omitempty"`
	Version              *wrapperspb.StringValue `protobuf:"bytes,3,opt,name=version,proto3" json:"version,omitempty"`
	Location             *model.Location         `protobuf:"bytes,4,opt,name=location,proto3" json:"location,omitempty"`
	Id                   *wrapperspb.StringValue `protobuf:"bytes,5,opt,name=id,proto3" json:"id,omitempty"`
	Stat                 []*StatInfo             `protobuf:"bytes,6,rep,name=stat,proto3" json:"stat,omitempty"`
	Ctime                *wrapperspb.StringValue `protobuf:"bytes,7,opt,name=ctime,proto3" json:"ctime,omitempty"`
	Mtime                *wrapperspb.StringValue `protobuf:"bytes,8,opt,name=mtime,proto3" json:"mtime,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                `json:"-"`
	XXX_unrecognized     []byte                  `json:"-"`
	XXX_sizecache        int32                   `json:"-"`
}

func (m *Client) Reset()         { *m = Client{} }
func (m *Client) String() string { return proto.CompactTextString(m) }
func (*Client) ProtoMessage()    {}
func (*Client) Descriptor() ([]byte, []int) {
	return fileDescriptor_client_ac96b32637bf3687, []int{0}
}
func (m *Client) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Client.Unmarshal(m, b)
}
func (m *Client) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Client.Marshal(b, m, deterministic)
}
func (dst *Client) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Client.Merge(dst, src)
}
func (m *Client) XXX_Size() int {
	return xxx_messageInfo_Client.Size(m)
}
func (m *Client) XXX_DiscardUnknown() {
	xxx_messageInfo_Client.DiscardUnknown(m)
}

var xxx_messageInfo_Client proto.InternalMessageInfo

func (m *Client) GetHost() *wrapperspb.StringValue {
	if m != nil {
		return m.Host
	}
	return nil
}

func (m *Client) GetType() Client_ClientType {
	if m != nil {
		return m.Type
	}
	return Client_UNKNOWN
}

func (m *Client) GetVersion() *wrapperspb.StringValue {
	if m != nil {
		return m.Version
	}
	return nil
}

func (m *Client) GetLocation() *model.Location {
	if m != nil {
		return m.Location
	}
	return nil
}

func (m *Client) GetId() *wrapperspb.StringValue {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *Client) GetStat() []*StatInfo {
	if m != nil {
		return m.Stat
	}
	return nil
}

func (m *Client) GetCtime() *wrapperspb.StringValue {
	if m != nil {
		return m.Ctime
	}
	return nil
}

func (m *Client) GetMtime() *wrapperspb.StringValue {
	if m != nil {
		return m.Mtime
	}
	return nil
}

type StatInfo struct {
	Target               *wrapperspb.StringValue `protobuf:"bytes,1,opt,name=target,proto3" json:"target,omitempty"`
	Port                 *wrapperspb.UInt32Value `protobuf:"bytes,2,opt,name=port,proto3" json:"port,omitempty"`
	Path                 *wrapperspb.StringValue `protobuf:"bytes,3,opt,name=path,proto3" json:"path,omitempty"`
	Protocol             *wrapperspb.StringValue `protobuf:"bytes,4,opt,name=protocol,proto3" json:"protocol,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                `json:"-"`
	XXX_unrecognized     []byte                  `json:"-"`
	XXX_sizecache        int32                   `json:"-"`
}

func (m *StatInfo) Reset()         { *m = StatInfo{} }
func (m *StatInfo) String() string { return proto.CompactTextString(m) }
func (*StatInfo) ProtoMessage()    {}
func (*StatInfo) Descriptor() ([]byte, []int) {
	return fileDescriptor_client_ac96b32637bf3687, []int{1}
}
func (m *StatInfo) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_StatInfo.Unmarshal(m, b)
}
func (m *StatInfo) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_StatInfo.Marshal(b, m, deterministic)
}
func (dst *StatInfo) XXX_Merge(src proto.Message) {
	xxx_messageInfo_StatInfo.Merge(dst, src)
}
func (m *StatInfo) XXX_Size() int {
	return xxx_messageInfo_StatInfo.Size(m)
}
func (m *StatInfo) XXX_DiscardUnknown() {
	xxx_messageInfo_StatInfo.DiscardUnknown(m)
}

var xxx_messageInfo_StatInfo proto.InternalMessageInfo

func (m *StatInfo) GetTarget() *wrapperspb.StringValue {
	if m != nil {
		return m.Target
	}
	return nil
}

func (m *StatInfo) GetPort() *wrapperspb.UInt32Value {
	if m != nil {
		return m.Port
	}
	return nil
}

func (m *StatInfo) GetPath() *wrapperspb.StringValue {
	if m != nil {
		return m.Path
	}
	return nil
}

func (m *StatInfo) GetProtocol() *wrapperspb.StringValue {
	if m != nil {
		return m.Protocol
	}
	return nil
}

func init() {
	proto.RegisterType((*Client)(nil), "polaris.v1.Client")
	proto.RegisterType((*StatInfo)(nil), "polaris.v1.StatInfo")
	proto.RegisterEnum("polaris.v1.Client_ClientType", Client_ClientType_name, Client_ClientType_value)
}

func init() { proto.RegisterFile("client.proto", fileDescriptor_client_ac96b32637bf3687) }

var fileDescriptor_client_ac96b32637bf3687 = []byte{
	// 442 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x92, 0xdf, 0x8a, 0x13, 0x31,
	0x14, 0xc6, 0x9d, 0xfe, 0xf7, 0x54, 0xa4, 0x04, 0x2f, 0x86, 0x45, 0xa5, 0xf4, 0xaa, 0x17, 0x9a,
	0x6c, 0xbb, 0xa2, 0xde, 0xba, 0xae, 0xc8, 0xb2, 0x52, 0xa5, 0xdd, 0x55, 0xf0, 0x46, 0xd2, 0xf4,
	0x74, 0x1a, 0x98, 0x99, 0x84, 0xe4, 0x74, 0x64, 0xdf, 0xc1, 0xe7, 0xf2, 0x31, 0x7c, 0x16, 0x99,
	0xcc, 0x74, 0x57, 0x45, 0x96, 0xb9, 0x1a, 0x86, 0xfc, 0xbe, 0x5f, 0x0e, 0xf9, 0x0e, 0x3c, 0x50,
	0xa9, 0xc6, 0x9c, 0xb8, 0x75, 0x86, 0x0c, 0x03, 0x6b, 0x52, 0xe9, 0xb4, 0xe7, 0xc5, 0xec, 0xe8,
	0x69, 0x62, 0x4c, 0x92, 0xa2, 0x08, 0x27, 0xeb, 0xfd, 0x56, 0x7c, 0x77, 0xd2, 0x5a, 0x74, 0xbe,
	0x62, 0x8f, 0x86, 0x99, 0xd9, 0x60, 0x5a, 0xfd, 0x4c, 0x7e, 0xb6, 0xa1, 0xf7, 0x36, 0x98, 0xd8,
	0x31, 0x74, 0x76, 0xc6, 0x53, 0x1c, 0x8d, 0xa3, 0xe9, 0x70, 0xfe, 0x98, 0x57, 0x1a, 0x7e, 0xd0,
	0xf0, 0x15, 0x39, 0x9d, 0x27, 0x9f, 0x65, 0xba, 0xc7, 0x65, 0x20, 0xd9, 0x0c, 0x3a, 0x74, 0x6d,
	0x31, 0x6e, 0x8d, 0xa3, 0xe9, 0xc3, 0xf9, 0x13, 0x7e, 0x3b, 0x04, 0xaf, 0x9c, 0xf5, 0xe7, 0xf2,
	0xda, 0xe2, 0x32, 0xa0, 0xec, 0x25, 0xf4, 0x0b, 0x74, 0x5e, 0x9b, 0x3c, 0x6e, 0x37, 0xb8, 0xe7,
	0x00, 0xb3, 0x63, 0x18, 0xa4, 0x46, 0x49, 0x2a, 0x83, 0x9d, 0x10, 0x7c, 0xf4, 0xe7, 0x75, 0x1f,
	0xea, 0xb3, 0xe5, 0x0d, 0xc5, 0x9e, 0x41, 0x4b, 0x6f, 0xe2, 0x6e, 0x83, 0x4b, 0x5a, 0x7a, 0xc3,
	0xa6, 0xd0, 0xf1, 0x24, 0x29, 0xee, 0x8d, 0xdb, 0xff, 0xba, 0x57, 0x24, 0xe9, 0x3c, 0xdf, 0x9a,
	0x65, 0x20, 0xd8, 0x1c, 0xba, 0x8a, 0x74, 0x86, 0x71, 0xbf, 0x81, 0xba, 0x42, 0xcb, 0x4c, 0x16,
	0x32, 0x83, 0x26, 0x99, 0x80, 0x4e, 0x9e, 0x03, 0xdc, 0xbe, 0x1e, 0x1b, 0x42, 0xff, 0x6a, 0x71,
	0xb1, 0xf8, 0xf8, 0x65, 0x31, 0xba, 0xc7, 0xfa, 0xd0, 0x5e, 0x9d, 0x5d, 0x8c, 0x22, 0x76, 0x1f,
	0xba, 0x6f, 0xde, 0xbf, 0x5b, 0x5c, 0x8e, 0x5a, 0x93, 0x5f, 0x11, 0x0c, 0x0e, 0x93, 0xb2, 0x17,
	0xd0, 0x23, 0xe9, 0x12, 0x6c, 0x56, 0x66, 0xcd, 0x96, 0x0b, 0x60, 0x8d, 0xa3, 0x50, 0xe7, 0xff,
	0x32, 0x57, 0xe7, 0x39, 0x9d, 0xcc, 0xeb, 0x05, 0x28, 0xc9, 0x90, 0x90, 0xb4, 0x6b, 0x54, 0x65,
	0x20, 0xd9, 0x6b, 0x18, 0x84, 0x53, 0x65, 0xd2, 0xba, 0xc7, 0xbb, 0x53, 0x37, 0xf4, 0xe9, 0x8f,
	0x08, 0x5e, 0x29, 0x93, 0x71, 0xc2, 0x5c, 0x85, 0xc5, 0xaf, 0x1b, 0xf2, 0x16, 0x95, 0xde, 0xea,
	0xaa, 0x75, 0x2e, 0xad, 0x2e, 0x3b, 0xf3, 0xe8, 0x0a, 0xad, 0x90, 0x67, 0x32, 0x97, 0x09, 0x9e,
	0x0e, 0xab, 0x97, 0xfc, 0x54, 0xba, 0xbe, 0x9e, 0x25, 0x9a, 0x76, 0xfb, 0x35, 0x57, 0x26, 0x13,
	0xb5, 0x24, 0x43, 0xbf, 0x13, 0x7f, 0x89, 0x84, 0x37, 0x7b, 0xa7, 0x50, 0x24, 0x46, 0x48, 0xab,
	0x45, 0x31, 0x13, 0xb5, 0xf2, 0x5b, 0xa5, 0x5c, 0xf7, 0xc2, 0x60, 0x27, 0xbf, 0x03, 0x00, 0x00,
	0xff, 0xff, 0x15, 0xe2, 0x11, 0x26, 0x88, 0x03, 0x00, 0x00,
}